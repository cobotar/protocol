# CobotAR-Protocol
A collection of protobuf messages for the CobotAR-project

Current version: 0.20.0

## Documentation
Find it here: [documentation/README.md](documentation/README.md)

## New version
1. Make changes
2. `make publish bump={patch,minor,major}`



## NATS subject convention
### CRUD
* add: `edit.<domain>.add`
* update: `edit.<domain>.update`
* delete: `edit.<domain>.delete`
* get: `get.<domain>.one`
* getByIds: `get.<domain>.some`
* getAll: `get.<domain>.all`


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


## Conceptual design of Assembly processes
### A. Product definition (What the thing is)
* Parts
* Assemblies / sub-assemblies
* Product BOM / hierarchy
* Part occurrences / instances
* CAD / 3D model references
* Mating / connection hints if you have them

### B. Process template (How the thing is normally assembled)
* Process recipe
* Sequences / sub-sequences
* Tasks / operations / steps
* Preconditions / ordering / alternatives / variants
* Required tool roles, skill requirements, actor constraints
* Operator text

### C. Execution instance (What is happening right now on the floor)
* Running process
* Current state of sequences/tasks
* Assigned human(s)/robot(s)
* Start/end timestamps
* Current station
* Evidence / completion / faults / overrides

### D. Resource library (What can be used to perform the work)
* Humans
* Robots
* Tools
* Fixtures
* Assets
* Stations / cells
* Models

### E. Capability layer (Why a given resource can or cannot do a task)
* Skills
* Capability profiles
* Tool roles
* Constraints
* Validity / training / retraining / calibration / certification

## Distinguish type from instance
Example: Part. In assembly we usually need both:
* Part definition: “M4x12 screw”
* Part occurrence: “the third M4x12 screw in this assembly”

thus distinguishing between the two is important and must be supported and done consistently.


### Minimal TaskDefinition example
```typescript
TaskDefinition {
  id: "task-fasten-cover-screw-1"
  name: "Fasten cover screw 1"
  instruction_text: "Fasten screw 1 to 0.8 Nm"
  task_type: TASK_TYPE_FASTEN
  target: {
    target_node_id: "node-screw-1"
    target_part_definition_id: "part-m4x12"
    local_target: {
      anchor_id: "node-screw-1"
    }
  }
  tool_requirements: [{
    role: TOOL_ROLE_APPLY_TORQUE,
    required_properties: [TOOL_PROPERTY_TORQUE_CONTROLLED],
    minimum_capability: {
      min_torque_nm: 0.72,
      max_torque_nm: 0.88
    }
  }]
  skill_requirements: [{
    skill_id: "SK-APPLY-CONTROLLED-TORQUE",
    minimum_level: SKILL_LEVEL_QUALIFIED
  }]
  validation: {
    require_tool_feedback: true
    allow_manual_confirmation: true
    manual_confirmation_min_level: SKILL_LEVEL_QUALIFIED
  }
  execution_policy: {
    assignment_preference: TASK_ASSIGNMENT_PREFERENCE_EITHER
    actor_constraint: {
      allowed_actor_kinds: [ACTOR_KIND_HUMAN, ACTOR_KIND_ROBOT]
      collaboration_mode: COLLABORATION_MODE_SEQUENTIAL_HRC
    }
  }
}
```


## Variant handling

### Types of variants
#### Bucket A — Structural variants
Affect product tree. Modeled in product.

Examples:
* hinge side
* optional handle
* different fastener family
* extra sensor module

#### Bucket B — Workflow variants
Affect tasks/sequences/skills/tools/validation. Modeled in recipe applicability or recipe branching.

Examples:
* door must be flipped
* adhesive cure step required
* fragile part requires two-person lift
* robot can only assemble one orientation

#### Bucket C — Parametric variants
Do not change workflow structure. Passed at run-time.

Examples:
* color
* language
* customer text
* batch number
* cosmetic finish code

### Handle variants without recipe explosion
For a product family, do this:

* **One ProductDefinition**
  * Contains all structural possibilities.
* **Few ProcessRecipes**

  Only split recipes where the workflow truly differs. For example:
  * recipe-door-standard
  * recipe-door-flipped-fixture
  * recipe-door-adhesive

  Not:
  * red-left-short-handle
  * red-left-long-handle
  * blue-right-short-handle
  * …

* **One ProcessRun per actual order/build**

  Contains:
  * selected product configuration
  * runtime parameters

#### Example

##### Product dimensions
* hinge_side = left | right
* color = red | green | blue
* handle = short | long

##### Recipe
* `recipe-door-standard` is applicable when:
  * handle = short or long
  * color = any
  * hinge_side = left
* `recipe-door-flipped` is applicable when:
  * hinge_side = right

They need to be split into two recipes because `right-hinge` requires a `flip` operation and different fixture.

##### Process run
When a real order starts the selection might look like this:
```typescript
product_selection:
  hinge_side = right
  color = green
  handle = long
```
thus the system chooses the `recipe-door-flipped` recipe and the recipe stays the same regardless of `color`.

