package subjectgen

import (
	"strings"
	"testing"
)

func TestValidateAllowsIncompletePlannedRoute(t *testing.T) {
	catalog := testCatalog(Route{
		ID:          "edit.entity.reset",
		Pattern:     "edit.{entity}.reset.{child}",
		Lifecycle:   "planned",
		Conformance: Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
		Interaction: "request_reply",
		Parameters: map[string]Parameter{
			"entity": {Type: "subject_token"},
			"child":  {Type: "subject_token"},
		},
		Publishers: []string{"web_cobotar"},
		Consumers:  []string{"authoring"},
	})

	if err := Validate(catalog, map[string]struct{}{}); err != nil {
		t.Fatalf("Validate() error = %v", err)
	}
	if got := catalog.Routes[0].ParameterList(); strings.Join(got, ",") != "entity,child" {
		t.Fatalf("parameter order = %v, want [entity child]", got)
	}
}

func TestValidateRequiresCompleteActiveRequestReply(t *testing.T) {
	catalog := testCatalog(Route{
		ID:          "command.task_run.progress",
		Pattern:     "command.task_run.progress",
		Lifecycle:   "active",
		Conformance: Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
		Interaction: "request_reply",
		Publishers:  []string{"web_cobotar"},
		Consumers:   []string{"authoring"},
	})

	err := Validate(catalog, map[string]struct{}{})
	if err == nil || !strings.Contains(err.Error(), "must declare request, success reply, and failure reply") {
		t.Fatalf("Validate() error = %v", err)
	}
}

func TestValidateRejectsUnknownMessageType(t *testing.T) {
	catalog := testCatalog(Route{
		ID:          "telemetry.robot.state",
		Pattern:     "telemetry.robot.state.{robot_instance_id}",
		Lifecycle:   "active",
		Conformance: Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
		Interaction: "publish",
		Payload:     "robot.v1.Missing",
		Parameters: map[string]Parameter{
			"robot_instance_id": {Type: "subject_token"},
		},
		Publishers: []string{"authoring"},
		Consumers:  []string{"holo_cobotar"},
	})

	err := Validate(catalog, map[string]struct{}{})
	if err == nil || !strings.Contains(err.Error(), `payload type "robot.v1.Missing" does not exist`) {
		t.Fatalf("Validate() error = %v", err)
	}
}

func TestValidateAcceptsExplicitEmptyRequest(t *testing.T) {
	catalog := testCatalog(Route{
		ID:           "get.storage.info",
		Pattern:      "get.storage.info",
		Lifecycle:    "active",
		Conformance:  Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
		Interaction:  "request_reply",
		EmptyRequest: true,
		Replies: Replies{
			Success: "service.v1.StorageInfo",
			Failure: "service.v1.Response",
		},
		Publishers: []string{"web_cobotar"},
		Consumers:  []string{"authoring"},
	})

	types := map[string]struct{}{
		"service.v1.StorageInfo": {},
		"service.v1.Response":    {},
	}
	if err := Validate(catalog, types); err != nil {
		t.Fatalf("Validate() error = %v", err)
	}
}

func TestValidateRequiresTrackingIssueForStagedRoute(t *testing.T) {
	catalog := testCatalog(Route{
		ID:          "telemetry.robot.state",
		Pattern:     "telemetry.robot.state.{robot_instance_id}",
		Lifecycle:   "planned",
		Conformance: Conformance{Mode: "staged"},
		Interaction: "publish",
		Parameters: map[string]Parameter{
			"robot_instance_id": {Type: "subject_token"},
		},
		Publishers: []string{"authoring"},
		Consumers:  []string{"holo_cobotar"},
	})

	err := Validate(catalog, map[string]struct{}{})
	if err == nil || !strings.Contains(err.Error(), "staged conformance requires tracking_issue") {
		t.Fatalf("Validate() error = %v", err)
	}
}

func TestValidateRejectsUnknownPartialSubscriptionParameter(t *testing.T) {
	catalog := testCatalog(Route{
		ID:          "plan.robot.path",
		Pattern:     "plan.robot.path.{robot_instance_id}.{plan_id}",
		Lifecycle:   "planned",
		Conformance: Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
		Interaction: "publish",
		Parameters: map[string]Parameter{
			"robot_instance_id": {Type: "subject_token"},
			"plan_id":           {Type: "subject_token"},
		},
		Subscriptions: []Subscription{{Name: "for_robot", Parameters: []string{"missing"}}},
		Publishers:    []string{"authoring"},
		Consumers:     []string{"holo_cobotar"},
	})

	err := Validate(catalog, map[string]struct{}{})
	if err == nil || !strings.Contains(err.Error(), `references unknown parameter "missing"`) {
		t.Fatalf("Validate() error = %v", err)
	}
}

func TestValidateRejectsDuplicateComponentOwnership(t *testing.T) {
	catalog := testCatalog(Route{
		ID:          "telemetry.robot.state",
		Pattern:     "telemetry.robot.state",
		Lifecycle:   "planned",
		Conformance: Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
		Interaction: "publish",
		Publishers:  []string{"authoring", "authoring"},
		Consumers:   []string{"holo_cobotar"},
	})

	err := Validate(catalog, map[string]struct{}{})
	if err == nil || !strings.Contains(err.Error(), `publisher component "authoring" is duplicated`) {
		t.Fatalf("Validate() error = %v", err)
	}
}

func TestValidateRejectsMissingDeprecatedReplacement(t *testing.T) {
	catalog := testCatalog(Route{
		ID:          "telemetry.robot.old_state",
		Pattern:     "telemetry.robot.old_state",
		Lifecycle:   "deprecated",
		Conformance: Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
		Interaction: "publish",
		Payload:     "robot.v1.RobotStateMessage",
		Publishers:  []string{"authoring"},
		Consumers:   []string{"holo_cobotar"},
		Replacement: "telemetry.robot.state",
	})

	err := Validate(catalog, map[string]struct{}{"robot.v1.RobotStateMessage": {}})
	if err == nil || !strings.Contains(err.Error(), `replacement "telemetry.robot.state" does not exist`) {
		t.Fatalf("Validate() error = %v", err)
	}
}

func TestGenerateIncludesAllLanguageTargets(t *testing.T) {
	catalog := testCatalog(Route{
		ID:          "telemetry.robot.state",
		Pattern:     "telemetry.robot.state.{robot_instance_id}",
		Lifecycle:   "planned",
		Conformance: Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
		Interaction: "publish",
		Payload:     "robot.v1.RobotStateMessage",
		Parameters: map[string]Parameter{
			"robot_instance_id": {Type: "subject_token"},
		},
		Publishers: []string{"authoring"},
		Consumers:  []string{"holo_cobotar"},
	})
	types := map[string]struct{}{"robot.v1.RobotStateMessage": {}}
	if err := Validate(catalog, types); err != nil {
		t.Fatal(err)
	}
	outputs, err := Generate(catalog)
	if err != nil {
		t.Fatal(err)
	}
	want := map[string]bool{
		"subjects/subjects.gen.go":         false,
		"csharp/Subjects.g.cs":             false,
		"lib/subjects.ts":                  false,
		"src/cobotar_protocol/subjects.py": false,
		"documentation/subjects.md":        false,
	}
	for _, output := range outputs {
		if _, ok := want[output.Path]; ok {
			want[output.Path] = true
		}
	}
	for path, found := range want {
		if !found {
			t.Errorf("missing generated output %s", path)
		}
	}
}

func TestValidateExpandsEntityRouteFamilyWithConcreteMessageTypes(t *testing.T) {
	catalog := testCatalog()
	catalog.Entities = []Entity{
		{Name: "action", Messages: map[string]string{"entity": "ar.v1.ActionMessage", "list": "ar.v1.ActionMessages"}},
		{Name: "feedback", Messages: map[string]string{"entity": "ar.v1.FeedbackMessage", "list": "ar.v1.FeedbackMessages"}},
	}
	catalog.EntitySets = map[string][]string{"readable": {"feedback", "action"}}
	catalog.RouteFamilies = []RouteFamily{{
		Route: Route{
			ID:           "get.entity.all",
			Pattern:      "get.{entity}.all",
			Lifecycle:    "active",
			Conformance:  Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
			Interaction:  "request_reply",
			EmptyRequest: true,
			Replies:      Replies{Success: "$list", Failure: "service.v1.Response"},
			Publishers:   []string{"web_cobotar"},
			Consumers:    []string{"authoring"},
		},
		EntitySet: "readable",
	}}
	types := map[string]struct{}{
		"ar.v1.ActionMessage":    {},
		"ar.v1.ActionMessages":   {},
		"ar.v1.FeedbackMessage":  {},
		"ar.v1.FeedbackMessages": {},
		"service.v1.Response":    {},
	}

	if err := Validate(catalog, types); err != nil {
		t.Fatal(err)
	}
	routes := catalog.AllRoutes()
	if len(routes) != 2 {
		t.Fatalf("expanded routes = %d, want 2", len(routes))
	}
	if routes[0].ID != "get.action.all" || routes[0].Replies.Success != "ar.v1.ActionMessages" {
		t.Fatalf("first expanded route = %#v", routes[0])
	}
	if routes[0].FamilyID() != "get.entity.all" || routes[0].EntityName() != "action" {
		t.Fatalf("first route family metadata = %q/%q", routes[0].FamilyID(), routes[0].EntityName())
	}
}

func TestValidateRejectsMissingEntityMessageRole(t *testing.T) {
	catalog := testCatalog()
	catalog.Entities = []Entity{{Name: "action", Messages: map[string]string{"entity": "ar.v1.ActionMessage"}}}
	catalog.EntitySets = map[string][]string{"readable": {"action"}}
	catalog.RouteFamilies = []RouteFamily{{
		Route: Route{
			ID:           "get.entity.all",
			Pattern:      "get.{entity}.all",
			Lifecycle:    "active",
			Conformance:  Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
			Interaction:  "request_reply",
			EmptyRequest: true,
			Replies:      Replies{Success: "$list", Failure: "service.v1.Response"},
			Publishers:   []string{"web_cobotar"},
			Consumers:    []string{"authoring"},
		},
		EntitySet: "readable",
	}}

	err := Validate(catalog, map[string]struct{}{
		"ar.v1.ActionMessage": {}, "service.v1.Response": {},
	})
	if err == nil || !strings.Contains(err.Error(), `does not declare message role "list"`) {
		t.Fatalf("Validate() error = %v", err)
	}
}

func TestValidateAppliesEntityRouteOverride(t *testing.T) {
	catalog := testCatalog()
	catalog.Components = append(catalog.Components, "fusion360_exporter")
	catalog.Entities = []Entity{{
		Name: "model",
		Messages: map[string]string{
			"create": "resources.v1.ModelArtifact",
		},
	}}
	catalog.EntitySets = map[string][]string{"creatable": {"model"}}
	catalog.RouteFamilies = []RouteFamily{{
		Route: Route{
			ID:          "edit.entity.add",
			Pattern:     "edit.{entity}.add",
			Lifecycle:   "active",
			Conformance: Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
			Interaction: "request_reply",
			Request:     "$create",
			Replies:     Replies{Success: "service.v1.Response", Failure: "service.v1.Response"},
			Publishers:  []string{"web_cobotar"},
			Consumers:   []string{"authoring"},
		},
		EntitySet: "creatable",
		EntityOverrides: map[string]RouteOverride{
			"model": {Publishers: []string{"fusion360_exporter", "web_cobotar"}},
		},
	}}

	if err := Validate(catalog, map[string]struct{}{
		"resources.v1.ModelArtifact": {}, "service.v1.Response": {},
	}); err != nil {
		t.Fatal(err)
	}
	route := catalog.AllRoutes()[0]
	if got := strings.Join(route.Publishers, ","); got != "fusion360_exporter,web_cobotar" {
		t.Fatalf("publishers = %q", got)
	}
}

func TestGenerateIncludesEntityNameAndFamilyHelpers(t *testing.T) {
	catalog := testCatalog()
	catalog.Entities = []Entity{{
		Name: "action",
		Messages: map[string]string{
			"list": "ar.v1.ActionMessages",
		},
	}}
	catalog.EntitySets = map[string][]string{"readable": {"action"}}
	catalog.RouteFamilies = []RouteFamily{{
		Route: Route{
			ID:           "get.entity.all",
			Pattern:      "get.{entity}.all",
			Lifecycle:    "active",
			Conformance:  Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
			Interaction:  "request_reply",
			EmptyRequest: true,
			Replies:      Replies{Success: "$list", Failure: "service.v1.Response"},
			Publishers:   []string{"web_cobotar"},
			Consumers:    []string{"authoring"},
		},
		EntitySet: "readable",
	}}
	if err := Validate(catalog, map[string]struct{}{
		"ar.v1.ActionMessages": {}, "service.v1.Response": {},
	}); err != nil {
		t.Fatal(err)
	}
	outputs, err := Generate(catalog)
	if err != nil {
		t.Fatal(err)
	}
	byPath := make(map[string]string, len(outputs))
	for _, output := range outputs {
		byPath[output.Path] = string(output.Content)
	}
	for path, fragments := range map[string][]string{
		"subjects/subjects.gen.go":         {"type EntityName string", "func GetEntityAll(entity EntityName)"},
		"lib/subjects.ts":                  {"export type EntityName", "export function getEntityAll(entity: EntityName)"},
		"src/cobotar_protocol/subjects.py": {"EntityName = Literal", "def get_entity_all(entity: EntityName)"},
		"csharp/Subjects.g.cs":             {"public enum EntityName", "GetEntityAll(EntityName entity)"},
	} {
		for _, fragment := range fragments {
			if !strings.Contains(byPath[path], fragment) {
				t.Errorf("%s does not contain %q", path, fragment)
			}
		}
	}
}

func testCatalog(routes ...Route) *Catalog {
	return &Catalog{
		Version:     2,
		Conformance: Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
		Components:  []string{"authoring", "web_cobotar", "holo_cobotar"},
		Routes:      routes,
	}
}
