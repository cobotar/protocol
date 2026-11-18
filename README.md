# CobotAR-Protocol
A collection of protobuf messages for the CobotAR-project

Current version: 2.3.6

## Documentation
Find it here: [documentation/README.md](documentation/README.md)

## New version
1. Make changes
2. `make publish bump={patch,minor,major}`

## Python

The generated Python modules are imported below the `cobotar_protocol`
namespace. Install the package with Buf's generated SDK index enabled, since
the generated Protovalidate messages are hosted there:

```shell
python3 -m pip install \
  --extra-index-url https://buf.build/gen/python \
  cobotar-protocol
```

Consumers only add the package's parent directory to `sys.path`; do not add
the inner `cobotar_protocol/` directory.



## NATS subjects

NATS subjects are defined in [`subjects/catalog.yaml`](subjects/catalog.yaml). The
catalog records each subject pattern, protobuf payload or request/reply types,
lifecycle, conformance state, intended publishers, and consumers. Generated Go,
C#, TypeScript, and Python helpers reject invalid concrete subject tokens and
provide explicit wildcard builders for subscriptions. Entity route families
generate both concrete message-aware routes and generic helpers whose entity
argument uses the shared generated `EntityName` contract.

See the generated [subject catalog and naming rules](documentation/subjects.md).
Run `go run ./cmd/subjectgen check` to validate the catalog and verify that all
generated outputs are current.


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
    product: {
      node_id: "node-screw-1"
      part_definition_id: "part_definition-m4x12"
      local_target: {
        // In mm in the product's frame, relative to the sequence that lists the task
        // (see "Process-local poses").
        anchor: { reference: "<parent>", frame: "origin" }
        position: { x: 12, y: 30, z: 4 }
      }
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


## Process-local poses
How the pose of a sequence or a task target in a process recipe resolves to a place in the station
(cobotar/protocol#50). The protos say the same in `SequenceDefinition.local_target`,
`ProductTarget.local_target` and `ProcessRun.frame`.

```
environment (station or cell)
  -> optional container instance -> optional slot      ProcessRun.frame
  -> process-run origin, `<process>`                   where the product's root frame sits
  -> root sequence -> child sequences                  SequenceDefinition.local_target
  -> task target                                       ProductTarget.local_target
```

**The process-run origin** is `ProcessRun.frame`:
- omitted: the origin of the run's station, or else its cell (a run without a fixture);
- anchored to `<environment>`/`origin`, or without an anchor: a pose relative to that origin, in the units and axes of
  station and cell placements;
- anchored to a container instance, with frame `origin` or one of its slot IDs: a pose relative to the container or
  the slot, in mm in the frame of the container's model. A slot is where the product it holds sits, so the pose is
  usually the identity.

**Below the origin**, a `LocalTarget` is a pose in the frame its anchor names, in mm in the frame of the recipe's
product (the frame in which the root node's `AssemblyNode.local_pose` is given; mm, right-handed with +Z up without a
product). Clients convert to their own units and axes once, at the origin, with the axes the product's model declares.
The anchors, always with frame `origin`:

| Anchor reference | Frame |
|---|---|
| `<process>` | The process-run origin. |
| `<parent>` | The immediate containing sequence: a sequence's parent, or the sequence that lists a task in `child_task_ids`. Not for the root sequence. |
| a sequence definition ID | That sequence, which has to be an ancestor on the direct line to the root. |
| none (or no `local_target`) | `<parent>`, and `<process>` for the root sequence. |

An omitted position is the anchor's origin, and an omitted orientation is the identity. A present orientation has to
be a unit quaternion (its squared length within 0.001 of 1, rule `local_target.orientation.unit`): an all-zero
quaternion isn't the identity, it's refused. Every other anchor is invalid, including the frame-only product-node
anchors (`{ reference: "", frame: "<node id>" }`) that recipe
generation used to write: they have no defined meaning, and validation refuses them.

**Assembly node poses** (`AssemblyNode.local_pose`) are always relative to the node's parent, and the root node's to
the product's frame. A node's frame is its parent's composed with its pose, for GROUP nodes too. A producer whose CAD
system gives poses in the product's frame converts them before export; there is no flag for other bases. So a target
copied from a node's pose is relative to the frame of the node's parent: a generator anchors it to the sequence whose
frame is that frame (with `<parent>` when the sequence tree follows the node tree), or composes the node poses up to
the anchor it names, e.g. `<process>` for poses in the product's frame.

**Parent-relative tree**, e.g. generated from a product whose node poses are relative to their parent node:

```yaml
sequences:
  - id: sequence_definition-housing          # root
    local_target: { anchor: { reference: "<process>", frame: origin } }
  - id: sequence_definition-motor            # subassembly, 40 mm above the housing's frame
    parent_sequence_id: sequence_definition-housing
    local_target: { anchor: { reference: "<parent>", frame: origin }, position: { z: 40 } }
tasks:
  - id: task_definition-fasten-motor-screw   # listed by sequence_definition-motor
    target:
      product:
        node_id: node-motor-screw-1
        local_target: { position: { x: 12, y: 0, z: 5 } }   # no anchor: <parent>, the motor sequence
```

**Common-origin tree**, e.g. every pose in the product's root frame:

```yaml
sequences:
  - id: sequence_definition-housing          # root, no local_target: the process-run origin
  - id: sequence_definition-motor
    parent_sequence_id: sequence_definition-housing
tasks:
  - id: task_definition-fasten-motor-screw
    target:
      product:
        node_id: node-motor-screw-1
        local_target:
          anchor: { reference: "<process>", frame: origin }  # or sequence_definition-housing, an ancestor
          position: { x: 12, y: 0, z: 45 }
```

**Validation.** The protos refuse what one definition shows: an anchor other than the ones above
(`sequence_definition.local_target.process_anchor`, `product_target.local_target.process_anchor`), a root sequence
anchored to anything but `<process>` (`sequence_definition.local_target.root_anchor`), and a run frame anchored to
anything but `<environment>` or a container instance (`process_run.frame.anchor`). The backend checks the recipe's
tree, with these rule IDs in `ValidationViolation.rule_id`:

| Rule ID | Refused |
|---|---|
| `process_pose.anchor_not_ancestor` | A sequence ID that isn't an ancestor on the direct line: a sibling, a descendant, a sequence of another branch or recipe. |
| `process_pose.sequence_cycle` | Parent sequences that form a cycle. |
| `process_pose.parent_mismatch` | A `parent_sequence_id` the parent's `child_sequence_ids` don't agree with, or a sequence without a parent that isn't the recipe's root. |
| `process_pose.task_owner_missing` | A task no sequence lists, so `<parent>` has no meaning. |
| `process_pose.task_owner_ambiguous` | A task several sequences list. |

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
