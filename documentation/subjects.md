# NATS subject catalog

This file is generated from `subjects/catalog.yaml`. Do not edit it directly.

Catalog conformance: **staged** ([cobotar/protocol#11](https://github.com/cobotar/protocol/issues/11)).

- **planned** reserves a contract while its message types or implementations may still be incomplete.
- **active** has complete catalog metadata and is the current contract; **deprecated** remains supported until retirement.
- **retired** reserves the old ID and pattern but generates no helper.
- **staged** permits incremental cross-repository rollout, does not assert that every component has migrated, and requires a tracking issue.
- **enforced** declares that every listed component is expected to conform to the catalog entry.

| ID | Pattern | Lifecycle | Conformance | Messages | Publishers | Consumers |
|---|---|---|---|---|---|---|
| `command.robot.visibility` | `command.robot.visibility.{robot_instance_id}` | active | staged | robot.v1.RobotVisibilityMessage | web_cobotar | holo_cobotar |
| `command.storage.clear` | `command.storage.clear` | planned | staged | service.v1.StorageClearRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `command.storage.dump` | `command.storage.dump` | planned | staged | service.v1.StorageDumpRequest → service.v1.StorageDumpResult / service.v1.Response | web_cobotar | authoring |
| `command.storage.load` | `command.storage.load` | planned | staged | service.v1.StorageLoadRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `command.task_run.progress` | `command.task_run.progress` | active | staged | runtime.v1.TaskProgressUpdate → service.v1.Response / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `edit.entity.reset` | `edit.{entity}.reset.{child}` | planned | staged | (TBD) → (TBD) / (TBD) | web_cobotar | authoring |
| `edit.model.add` | `edit.model.add` | active | staged | resources.v1.ModelArtifact → service.v1.Response / service.v1.Response | fusion360_exporter, web_cobotar | authoring |
| `edit.part_definition.add` | `edit.part_definition.add` | active | staged | product.v1.PartDefinition → service.v1.Response / service.v1.Response | fusion360_exporter, web_cobotar | authoring |
| `edit.product.add` | `edit.product.add` | active | staged | product.v1.ProductDefinition → service.v1.Response / service.v1.Response | fusion360_exporter, web_cobotar | authoring |
| `get.asset_adapter.info` | `get.asset_adapter.info.{asset_instance_id}` | planned | staged | (empty) → resources.v1.AssetAdapterInfoMessage / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_adapter_definition.all` | `get.asset_adapter_definition.all` | planned | staged | (empty) → resources.v1.AssetAdapterDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_adapter_definition.one` | `get.asset_adapter_definition.one` | planned | staged | common.v1.GetMessage → resources.v1.AssetAdapterDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_adapter.info` | `get.robot_adapter.info.{robot_instance_id}` | active | staged | (empty) → robot.v1.RobotAdapterInfoMessage / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_adapter_definition.all` | `get.robot_adapter_definition.all` | planned | staged | (empty) → resources.v1.RobotAdapterDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_adapter_definition.one` | `get.robot_adapter_definition.one` | planned | staged | common.v1.GetMessage → resources.v1.RobotAdapterDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.storage.info` | `get.storage.info` | planned | staged | (empty) → service.v1.StorageInfo / service.v1.Response | web_cobotar | authoring |
| `plan.robot.path` | `plan.robot.path.{robot_instance_id}.{plan_id}` | active | staged | robot.v1.PathMessage | authoring | web_cobotar, holo_cobotar |
| `telemetry.robot.controller_status` | `telemetry.robot.controller_status.{robot_instance_id}` | active | staged | robot.v1.RobotControllerStatusMessage | authoring | web_cobotar, holo_cobotar |
| `telemetry.robot.end_effector` | `telemetry.robot.end_effector.{robot_instance_id}` | planned | staged | robot.v1.EndEffectorStateMessage | authoring | holo_cobotar |

For request/reply routes, publishers are requesters and consumers are responders. These lists describe intended ownership; staged conformance does not claim that every implementation has landed.

## Naming rules

- Literal tokens use lower_snake_case.
- Parameters occupy exactly one NATS token and reject `.`, `*`, `>`, whitespace, and empty values.
- Concrete publishers and requesters never use wildcards. Generated `Subscribe…Any` and named partial-subscription helpers introduce wildcards explicitly.
- Entity and routing identifiers follow the operation token unless a catalog entry documents a different order.
- Planned and staged helpers are experimental; their presence does not guarantee runtime availability.
