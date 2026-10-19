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
