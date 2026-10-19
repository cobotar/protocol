package subjectgen

import (
	"fmt"
	"regexp"
	"sort"
	"strings"
)

var (
	idPattern           = regexp.MustCompile(`^[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)+$`)
	literalTokenPattern = regexp.MustCompile(`^[a-z][a-z0-9_]*$`)
	parameterPattern    = regexp.MustCompile(`^\{([a-z][a-z0-9_]*)\}$`)
)

func Validate(catalog *Catalog, messageTypes map[string]struct{}) error {
	if catalog.Version != 1 {
		return fmt.Errorf("catalog version must be 1")
	}
	if err := validateConformance("catalog", catalog.Conformance); err != nil {
		return err
	}

	components := make(map[string]struct{}, len(catalog.Components))
	for _, component := range catalog.Components {
		if !literalTokenPattern.MatchString(component) {
			return fmt.Errorf("component %q must be a lower_snake_case subject token", component)
		}
		if _, duplicate := components[component]; duplicate {
			return fmt.Errorf("component %q is duplicated", component)
		}
		components[component] = struct{}{}
	}
	if len(components) == 0 {
		return fmt.Errorf("catalog must declare at least one component")
	}

	ids := make(map[string]struct{}, len(catalog.Routes))
	patterns := make(map[string]string, len(catalog.Routes))
	names := make(map[string]string, len(catalog.Routes))
	for index := range catalog.Routes {
		route := &catalog.Routes[index]
		if err := validateRoute(route, components, messageTypes); err != nil {
			return fmt.Errorf("route %q: %w", route.ID, err)
		}
		if _, duplicate := ids[route.ID]; duplicate {
			return fmt.Errorf("route ID %q is duplicated", route.ID)
		}
		ids[route.ID] = struct{}{}
		if previous, duplicate := patterns[route.Pattern]; duplicate {
			return fmt.Errorf("routes %q and %q use the same pattern %q", previous, route.ID, route.Pattern)
		}
		patterns[route.Pattern] = route.ID
		generatedName := pascalName(route.ID)
		if previous, duplicate := names[generatedName]; duplicate {
			return fmt.Errorf("routes %q and %q generate the same helper name %q", previous, route.ID, generatedName)
		}
		names[generatedName] = route.ID
	}
	for _, route := range catalog.Routes {
		if route.Lifecycle == "deprecated" {
			if _, ok := ids[route.Replacement]; !ok {
				return fmt.Errorf("route %q replacement %q does not exist", route.ID, route.Replacement)
			}
		}
	}

	sort.Slice(catalog.Routes, func(i, j int) bool { return catalog.Routes[i].ID < catalog.Routes[j].ID })
	return nil
}

func validateRoute(route *Route, components, messageTypes map[string]struct{}) error {
	if !idPattern.MatchString(route.ID) {
		return fmt.Errorf("ID must contain at least two lower_snake_case segments")
	}
	switch route.Lifecycle {
	case "planned", "active", "deprecated", "retired":
	default:
		return fmt.Errorf("unknown lifecycle %q", route.Lifecycle)
	}
	if err := validateConformance("route", route.Conformance); err != nil {
		return err
	}
	if route.Lifecycle == "planned" && route.Conformance.Mode != "staged" {
		return fmt.Errorf("planned routes must use staged conformance")
	}
	if route.Lifecycle == "retired" && route.Conformance.Mode == "enforced" {
		return fmt.Errorf("retired routes cannot use enforced conformance")
	}
	if route.Lifecycle == "deprecated" && route.Replacement == "" {
		return fmt.Errorf("deprecated routes must name a replacement")
	}

	parameters, err := validatePattern(route.Pattern)
	if err != nil {
		return err
	}
	route.parameterList = parameters
	used := make(map[string]struct{}, len(parameters))
	for _, name := range parameters {
		used[name] = struct{}{}
		parameter, ok := route.Parameters[name]
		if !ok {
			return fmt.Errorf("pattern parameter %q is not declared", name)
		}
		if parameter.Type != "subject_token" {
			return fmt.Errorf("parameter %q has unsupported type %q", name, parameter.Type)
		}
	}
	for name := range route.Parameters {
		if _, ok := used[name]; !ok {
			return fmt.Errorf("parameter %q is declared but not used", name)
		}
	}
	if err := validateSubscriptions(route, used); err != nil {
		return err
	}

	if route.Lifecycle != "retired" {
		if len(route.Publishers) == 0 {
			return fmt.Errorf("must declare at least one intended publisher")
		}
		if len(route.Consumers) == 0 {
			return fmt.Errorf("must declare at least one intended consumer")
		}
	}
	if err := validateComponentList("publisher", route.Publishers, components); err != nil {
		return err
	}
	if err := validateComponentList("consumer", route.Consumers, components); err != nil {
		return err
	}

	switch route.Interaction {
	case "publish":
		if route.Payload == "" && route.Lifecycle != "planned" && route.Lifecycle != "retired" {
			return fmt.Errorf("publish route must declare a payload")
		}
		if route.Request != "" || route.Replies.Success != "" || route.Replies.Failure != "" {
			return fmt.Errorf("publish route cannot declare request or reply types")
		}
	case "request_reply":
		if route.Request != "" && route.EmptyRequest {
			return fmt.Errorf("request/reply route cannot declare both request and empty_request")
		}
		if route.Lifecycle != "planned" && route.Lifecycle != "retired" && ((route.Request == "" && !route.EmptyRequest) || route.Replies.Success == "" || route.Replies.Failure == "") {
			return fmt.Errorf("request/reply route must declare request, success reply, and failure reply")
		}
		if route.Payload != "" {
			return fmt.Errorf("request/reply route cannot declare a payload")
		}
	default:
		if route.Lifecycle != "retired" {
			return fmt.Errorf("unknown interaction %q", route.Interaction)
		}
	}

	for label, messageType := range map[string]string{
		"payload": route.Payload, "request": route.Request,
		"success reply": route.Replies.Success, "failure reply": route.Replies.Failure,
	} {
		if messageType == "" {
			continue
		}
		if _, ok := messageTypes[messageType]; !ok {
			return fmt.Errorf("%s type %q does not exist", label, messageType)
		}
	}
	return nil
}

func validateComponentList(role string, values []string, components map[string]struct{}) error {
	seen := make(map[string]struct{}, len(values))
	for _, component := range values {
		if _, ok := components[component]; !ok {
			return fmt.Errorf("references unknown %s component %q", role, component)
		}
		if _, duplicate := seen[component]; duplicate {
			return fmt.Errorf("%s component %q is duplicated", role, component)
		}
		seen[component] = struct{}{}
	}
	return nil
}

func validateSubscriptions(route *Route, routeParameters map[string]struct{}) error {
	names := make(map[string]struct{}, len(route.Subscriptions))
	for _, subscription := range route.Subscriptions {
		if !literalTokenPattern.MatchString(subscription.Name) {
			return fmt.Errorf("subscription name %q must be lower_snake_case", subscription.Name)
		}
		if _, duplicate := names[subscription.Name]; duplicate {
			return fmt.Errorf("subscription name %q is duplicated", subscription.Name)
		}
		names[subscription.Name] = struct{}{}
		if len(subscription.Parameters) == 0 {
			return fmt.Errorf("subscription %q must keep at least one concrete parameter; use the generated Any helper otherwise", subscription.Name)
		}
		parameters := make(map[string]struct{}, len(subscription.Parameters))
		for _, parameter := range subscription.Parameters {
			if _, ok := routeParameters[parameter]; !ok {
				return fmt.Errorf("subscription %q references unknown parameter %q", subscription.Name, parameter)
			}
			if _, duplicate := parameters[parameter]; duplicate {
				return fmt.Errorf("subscription %q repeats parameter %q", subscription.Name, parameter)
			}
			parameters[parameter] = struct{}{}
		}
		if len(parameters) == len(routeParameters) {
			return fmt.Errorf("subscription %q has no wildcard parameters", subscription.Name)
		}
	}
	return nil
}

func validateConformance(owner string, conformance Conformance) error {
	switch conformance.Mode {
	case "staged":
		if strings.TrimSpace(conformance.TrackingIssue) == "" {
			return fmt.Errorf("%s staged conformance requires tracking_issue", owner)
		}
	case "enforced":
		if conformance.TrackingIssue != "" {
			return fmt.Errorf("%s enforced conformance must not have tracking_issue", owner)
		}
	default:
		return fmt.Errorf("%s has unknown conformance mode %q", owner, conformance.Mode)
	}
	return nil
}

func validatePattern(pattern string) ([]string, error) {
	if pattern == "" {
		return nil, fmt.Errorf("pattern is empty")
	}
	var parameters []string
	seen := make(map[string]struct{})
	for _, token := range strings.Split(pattern, ".") {
		if literalTokenPattern.MatchString(token) {
			continue
		}
		match := parameterPattern.FindStringSubmatch(token)
		if match == nil {
			return nil, fmt.Errorf("pattern token %q is neither lower_snake_case nor a parameter", token)
		}
		if _, duplicate := seen[match[1]]; duplicate {
			return nil, fmt.Errorf("pattern parameter %q is repeated", match[1])
		}
		seen[match[1]] = struct{}{}
		parameters = append(parameters, match[1])
	}
	if len(strings.Split(pattern, ".")) < 3 {
		return nil, fmt.Errorf("pattern must contain at least three tokens")
	}
	return parameters, nil
}
