# CobotAR-Protocol
A collection of protobuf messages for the CobotAR-project

Current version: 0.14.1

## Documentation
Find it here: [documentation/README.md](documentation/README.md)

## New version
1. Make changes
2. `make publish bump={patch,minor,major}`



## NATS subject convention
### CRUD
* add: `<kind>-add`
* update: `<kind>-update`
* delete: `<kind>-delete`
* get: `<kind>-get`
* getAll: `<kind>s`

### Events
 Subject shape: `<kind>.<domain>.<type>.<scope..>`
where:
* kind: `{command | event | plan | telemetry}`
* domain: `{robot | task | asset | ...}`
* type: event type as lower_snake_case string token (`start_stop`, `started`, `task_completed`, etc.) 
* scope optional identifiers for routing (`robotId`, `taskId`, `assetId`, `lineId`, etc.). Generally following this:
  ```
  <kind>.<domain>.<type>.<site>.<workcell>.<entityId>[.<planId>]
  ```

Examples:
```
command.robot.start_stop.workcellA.robot-1
plan.robot.path.workcellA.robot-1.plan-P123
telemetry.robot.state.workcellA.robot-1
event.robot.started.workcellA.robot-1
event.plan.cancelled.workcellA.plan-P123
```
