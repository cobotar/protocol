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
		"subjects/catalog.json":            false,
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

func testCatalog(routes ...Route) *Catalog {
	return &Catalog{
		Version:     1,
		Conformance: Conformance{Mode: "staged", TrackingIssue: "cobotar/protocol#11"},
		Components:  []string{"authoring", "web_cobotar", "holo_cobotar"},
		Routes:      routes,
	}
}
