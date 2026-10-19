package subjectgen

import (
	"fmt"
	"sort"
	"strings"
)

func expandRouteFamilies(catalog *Catalog, messageTypes map[string]struct{}) error {
	entities := make(map[string]Entity, len(catalog.Entities))
	for _, entity := range catalog.Entities {
		if !literalTokenPattern.MatchString(entity.Name) {
			return fmt.Errorf("entity %q must be a lower_snake_case subject token", entity.Name)
		}
		if _, duplicate := entities[entity.Name]; duplicate {
			return fmt.Errorf("entity %q is duplicated", entity.Name)
		}
		for role, messageType := range entity.Messages {
			if !literalTokenPattern.MatchString(role) {
				return fmt.Errorf("entity %q message role %q must be lower_snake_case", entity.Name, role)
			}
			if _, ok := messageTypes[messageType]; !ok {
				return fmt.Errorf("entity %q message role %q references unknown type %q", entity.Name, role, messageType)
			}
		}
		entities[entity.Name] = entity
	}

	sets := make(map[string][]Entity, len(catalog.EntitySets))
	for name, members := range catalog.EntitySets {
		if !literalTokenPattern.MatchString(name) {
			return fmt.Errorf("entity set %q must be lower_snake_case", name)
		}
		seen := make(map[string]struct{}, len(members))
		for _, member := range members {
			entity, ok := entities[member]
			if !ok {
				return fmt.Errorf("entity set %q references unknown entity %q", name, member)
			}
			if _, duplicate := seen[member]; duplicate {
				return fmt.Errorf("entity set %q repeats entity %q", name, member)
			}
			seen[member] = struct{}{}
			sets[name] = append(sets[name], entity)
		}
		sort.Slice(sets[name], func(i, j int) bool { return sets[name][i].Name < sets[name][j].Name })
	}

	catalog.expandedRoutes = nil
	for index := range catalog.RouteFamilies {
		family := &catalog.RouteFamilies[index]
		members, ok := sets[family.EntitySet]
		if !ok {
			return fmt.Errorf("route family %q references unknown entity set %q", family.ID, family.EntitySet)
		}
		if len(members) == 0 {
			return fmt.Errorf("route family %q entity set %q is empty", family.ID, family.EntitySet)
		}
		if err := validateRouteFamily(family); err != nil {
			return fmt.Errorf("route family %q: %w", family.ID, err)
		}
		memberNames := make(map[string]struct{}, len(members))
		for _, entity := range members {
			memberNames[entity.Name] = struct{}{}
		}
		for entityName := range family.EntityOverrides {
			if _, ok := memberNames[entityName]; !ok {
				return fmt.Errorf("route family %q override references entity %q outside set %q", family.ID, entityName, family.EntitySet)
			}
		}
		for _, entity := range members {
			route, err := expandRouteFamily(*family, entity)
			if err != nil {
				return fmt.Errorf("route family %q entity %q: %w", family.ID, entity.Name, err)
			}
			catalog.expandedRoutes = append(catalog.expandedRoutes, route)
		}
	}
	return nil
}

func validateRouteFamily(family *RouteFamily) error {
	if !strings.Contains(family.ID, ".entity.") {
		return fmt.Errorf("ID must contain the literal segment entity")
	}
	if strings.Count(family.Pattern, "{entity}") != 1 {
		return fmt.Errorf("pattern must contain {entity} exactly once")
	}
	parameters, err := validatePattern(family.Pattern)
	if err != nil {
		return err
	}
	if len(parameters) == 0 || parameters[0] != "entity" {
		return fmt.Errorf("{entity} must be the first pattern parameter")
	}
	family.parameterList = parameters
	used := make(map[string]struct{}, len(parameters))
	used["entity"] = struct{}{}
	for _, name := range parameters[1:] {
		used[name] = struct{}{}
		parameter, ok := family.Parameters[name]
		if !ok {
			return fmt.Errorf("pattern parameter %q is not declared", name)
		}
		if parameter.Type != "subject_token" {
			return fmt.Errorf("parameter %q has unsupported type %q", name, parameter.Type)
		}
	}
	if _, declared := family.Parameters["entity"]; declared {
		return fmt.Errorf("entity is supplied by entity_set and must not be declared as a parameter")
	}
	for name := range family.Parameters {
		if _, ok := used[name]; !ok {
			return fmt.Errorf("parameter %q is declared but not used", name)
		}
	}
	if err := validateSubscriptions(&family.Route, used); err != nil {
		return err
	}
	return nil
}

func expandRouteFamily(family RouteFamily, entity Entity) (Route, error) {
	route := family.Route
	route.ID = replaceIDSegment(route.ID, "entity", entity.Name)
	route.Pattern = strings.Replace(route.Pattern, "{entity}", entity.Name, 1)
	route.Subscriptions = nil
	route.familyID = family.ID
	route.entityName = entity.Name
	if override, ok := family.EntityOverrides[entity.Name]; ok {
		if override.Lifecycle != "" {
			route.Lifecycle = override.Lifecycle
		}
		if override.Conformance != nil {
			route.Conformance = *override.Conformance
		}
		if override.Publishers != nil {
			route.Publishers = override.Publishers
		}
		if override.Consumers != nil {
			route.Consumers = override.Consumers
		}
	}

	var err error
	if route.Payload, err = resolveMessageRole(route.Payload, entity); err != nil {
		return Route{}, fmt.Errorf("payload: %w", err)
	}
	if route.Request, err = resolveMessageRole(route.Request, entity); err != nil {
		return Route{}, fmt.Errorf("request: %w", err)
	}
	if route.Replies.Success, err = resolveMessageRole(route.Replies.Success, entity); err != nil {
		return Route{}, fmt.Errorf("success reply: %w", err)
	}
	if route.Replies.Failure, err = resolveMessageRole(route.Replies.Failure, entity); err != nil {
		return Route{}, fmt.Errorf("failure reply: %w", err)
	}
	return route, nil
}

func resolveMessageRole(value string, entity Entity) (string, error) {
	if !strings.HasPrefix(value, "$") {
		return value, nil
	}
	role := strings.TrimPrefix(value, "$")
	messageType, ok := entity.Messages[role]
	if !ok {
		return "", fmt.Errorf("entity %q does not declare message role %q", entity.Name, role)
	}
	return messageType, nil
}

func replaceIDSegment(id, old, replacement string) string {
	segments := strings.Split(id, ".")
	for index, segment := range segments {
		if segment == old {
			segments[index] = replacement
		}
	}
	return strings.Join(segments, ".")
}
