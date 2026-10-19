package subjects

import "testing"

func TestParameterizedSubject(t *testing.T) {
	subject, err := PlanRobotPath("robot_instance-1", "plan-1")
	if err != nil {
		t.Fatal(err)
	}
	if subject != "plan.robot.path.robot_instance-1.plan-1" {
		t.Fatalf("subject = %q", subject)
	}
}

func TestParameterizedSubjectRejectsWildcard(t *testing.T) {
	if _, err := TelemetryRobotControllerStatus("*"); err == nil {
		t.Fatal("expected wildcard parameter to be rejected")
	}
}

func TestSubscriptionWildcardIsExplicit(t *testing.T) {
	if got := SubscribeTelemetryRobotControllerStatusAny(); got != "telemetry.robot.controller_status.*" {
		t.Fatalf("wildcard subject = %q", got)
	}
}

func TestPartialWildcardSubscription(t *testing.T) {
	got, err := SubscribePlanRobotPathForRobot("robot_instance-1")
	if err != nil {
		t.Fatal(err)
	}
	if got != "plan.robot.path.robot_instance-1.*" {
		t.Fatalf("partial wildcard subject = %q", got)
	}
}

func TestEntityRouteFamily(t *testing.T) {
	subject, err := GetEntityAll(EntityPartDefinition)
	if err != nil {
		t.Fatal(err)
	}
	if subject != "get.part_definition.all" {
		t.Fatalf("subject = %q", subject)
	}
}

func TestEntityRouteFamilyRejectsUnsupportedEntity(t *testing.T) {
	if _, err := EditEntityAdd(EntityProcessRun); err == nil {
		t.Fatal("expected read-only process_run to be rejected by edit.entity.add")
	}
}

func TestEntityEventPartialSubscription(t *testing.T) {
	subject, err := SubscribeEventEntityUpdatedForEntity(EntityRobotInstance)
	if err != nil {
		t.Fatal(err)
	}
	if subject != "event.robot_instance.updated.*" {
		t.Fatalf("subject = %q", subject)
	}
}

func TestExpandedRouteRetainsConcreteMessageMetadata(t *testing.T) {
	for _, definition := range Catalog {
		if definition.ID != "get.product.all" {
			continue
		}
		if definition.Family != "get.entity.all" || definition.Entity != "product" {
			t.Fatalf("family metadata = %q/%q", definition.Family, definition.Entity)
		}
		if definition.SuccessReply != "product.v1.ProductDefinitions" {
			t.Fatalf("success reply = %q", definition.SuccessReply)
		}
		return
	}
	t.Fatal("get.product.all is missing from Catalog")
}
