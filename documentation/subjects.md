# NATS subject catalog

This file is generated from `subjects/catalog.yaml`. Do not edit it directly.

Catalog conformance: **staged** ([cobotar/protocol#11](https://github.com/cobotar/protocol/issues/11)).

- **planned** reserves a contract while its message types or implementations may still be incomplete.
- **active** has complete catalog metadata and is the current contract; **deprecated** remains supported until retirement.
- **retired** reserves the old ID and pattern but generates no helper.
- **staged** permits incremental cross-repository rollout, does not assert that every component has migrated, and requires a tracking issue.
- **enforced** declares that every listed component is expected to conform to the catalog entry.

## Entity names and route families

`EntityName` is generated from these stable subject tokens:

`action`, `action_definition`, `actor_availability`, `actor_skill`, `ar_config`, `ar_config_binding`, `asset_adapter_definition`, `asset_adapter_info`, `asset_definition`, `asset_instance`, `cell`, `container_definition`, `container_instance`, `device`, `execution_evidence`, `feedback`, `feedback_definition`, `function`, `function_definition`, `line`, `marker`, `model`, `part_definition`, `part_family`, `part_instance`, `presentation_strategy`, `process_recipe`, `process_run`, `process_run_definitions`, `product`, `property_definition`, `property_instance`, `robot_adapter_definition`, `robot_adapter_info`, `robot_definition`, `robot_instance`, `sequence_definition`, `sequence_run`, `skill`, `station`, `task_definition`, `task_run`, `tool_definition`, `tool_instance`, `validity_policy`, `worker`, `zone`.

Route families expand into concrete, message-aware catalog entries. Generic helpers validate their entity argument against the named set; concrete helpers remain available for consumers that prefer them.

| Family | Entity set | Pattern |
|---|---|---|
| `edit.entity.add` | `creatable` | `edit.{entity}.add` |
| `edit.entity.clone` | `cloneable` | `edit.{entity}.clone` |
| `edit.entity.remove` | `mutable` | `edit.{entity}.remove` |
| `edit.entity.update` | `mutable` | `edit.{entity}.update` |
| `event.entity.added` | `evented` | `event.{entity}.added.{entity_id}` |
| `event.entity.removed` | `evented` | `event.{entity}.removed.{entity_id}` |
| `event.entity.updated` | `evented` | `event.{entity}.updated.{entity_id}` |
| `get.entity.all` | `readable` | `get.{entity}.all` |
| `get.entity.one` | `readable` | `get.{entity}.one` |
| `get.entity.some` | `readable` | `get.{entity}.some` |

## Concrete routes

| ID | Pattern | Family | Lifecycle | Conformance | Messages | Publishers | Consumers |
|---|---|---|---|---|---|---|---|
| `command.action.request_ownership` | `command.action.request_ownership` | — | active | staged | ar.v1.RequestActionOwnership → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `command.actor_availability.clear_override` | `command.actor_availability.clear_override` | — | active | staged | runtime.v1.ActorAvailabilityOverrideClearRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `command.actor_availability.override` | `command.actor_availability.override` | — | active | staged | runtime.v1.ActorAvailabilityOverrideRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `command.actor_availability.report` | `command.actor_availability.report` | — | active | staged | runtime.v1.ActorAvailabilityReportRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `command.feedback.request_ownership` | `command.feedback.request_ownership` | — | active | staged | ar.v1.RequestFeedbackOwnership → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `command.popup.hide` | `command.popup.hide.{robot_instance_id}` | — | active | staged | robot.v1.RobotHidePopupRequest → service.v1.Response / service.v1.Response | web_cobotar | robot_adapter |
| `command.popup.show` | `command.popup.show.{robot_instance_id}` | — | active | staged | robot.v1.RobotShowPopupRequest → service.v1.Response / service.v1.Response | web_cobotar | robot_adapter |
| `command.process_run.abort` | `command.process_run.abort` | — | active | staged | runtime.v1.ProcessAbortRequest → service.v1.Response / service.v1.Response | web_cobotar, holo_cobotar | authoring |
| `command.process_run.load_request` | `command.process_run.load_request` | — | active | staged | runtime.v1.ProcessLoadRequest → runtime.v1.ProcessLoadResult / service.v1.Response | web_cobotar | authoring |
| `command.robot.visibility` | `command.robot.visibility.{robot_instance_id}` | — | active | staged | robot.v1.RobotVisibilityMessage | web_cobotar | holo_cobotar |
| `command.robot_instance.acknowledge` | `command.robot_instance.acknowledge.{robot_instance_id}` | — | active | staged | robot.v1.AcknowledgeRobot → service.v1.Response / service.v1.Response | web_cobotar, holo_cobotar | robot_adapter |
| `command.robot_instance.free_drive` | `command.robot_instance.free_drive.{robot_instance_id}` | — | active | staged | robot.v1.RobotFreeDriveRequest → service.v1.Response / service.v1.Response | web_cobotar, holo_cobotar | robot_adapter |
| `command.robot_instance.set_io` | `command.robot_instance.set_io.{robot_instance_id}` | — | active | staged | robot.v1.RobotIOCommand → service.v1.Response / service.v1.Response | web_cobotar, holo_cobotar | robot_adapter |
| `command.robot_instance.state_change` | `command.robot_instance.state_change.{robot_instance_id}` | — | active | staged | robot.v1.ProgramStateRequest → service.v1.Response / service.v1.Response | web_cobotar, holo_cobotar | robot_adapter |
| `command.sequence_run.complete` | `command.sequence_run.complete` | — | active | staged | runtime.v1.SequenceCompleteRequest → service.v1.Response / service.v1.Response | holo_cobotar | authoring |
| `command.sequence_run.reassign` | `command.sequence_run.reassign` | — | active | staged | runtime.v1.SequenceReassignRequest → service.v1.Response / service.v1.Response | web_cobotar, holo_cobotar | authoring |
| `command.storage.clear` | `command.storage.clear` | — | active | staged | service.v1.StorageClearRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `command.storage.collect_garbage` | `command.storage.collect_garbage` | — | active | staged | service.v1.StorageCollectGarbageRequest → service.v1.StorageCollectGarbageResult / service.v1.Response | web_cobotar | authoring |
| `command.storage.dump` | `command.storage.dump` | — | active | staged | service.v1.StorageDumpRequest → service.v1.StorageDumpResult / service.v1.Response | web_cobotar | authoring |
| `command.storage.load` | `command.storage.load` | — | active | staged | service.v1.StorageLoadRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `command.task_run.progress` | `command.task_run.progress` | — | active | staged | runtime.v1.TaskProgressUpdate → service.v1.Response / service.v1.Response | robot_adapter, web_cobotar, holo_cobotar | authoring |
| `command.task_run.reassign` | `command.task_run.reassign` | — | active | staged | runtime.v1.TaskReassignRequest → service.v1.Response / service.v1.Response | web_cobotar, holo_cobotar | authoring |
| `command.task_run.state_change` | `command.task_run.state_change.{task_run_id}` | — | active | staged | runtime.v1.TaskStateChangeRequest → service.v1.Response / service.v1.Response | robot_adapter, web_cobotar, holo_cobotar | authoring |
| `edit.ar_config.add.ar_input_slot` | `edit.ar_config.add.ar_input_slot` | — | active | staged | ar.v1.ARInputSlotAddMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config.remove.ar_input_slot` | `edit.ar_config.remove.ar_input_slot` | — | active | staged | ar.v1.ARInputSlotDeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config.reset.presentation_binding` | `edit.ar_config.reset.presentation_binding` | — | active | staged | ar.v1.PresentationBindingReset → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config.update.ar_input_slot` | `edit.ar_config.update.ar_input_slot` | — | active | staged | ar.v1.ARInputSlotUpdateMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config.update.presentation_binding` | `edit.ar_config.update.presentation_binding` | — | active | staged | ar.v1.PresentationBindingUpdate → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.container_definition.import` | `edit.container_definition.import` | — | planned | staged | resources.v1.ImportContainer → resources.v1.ImportContainerResult / service.v1.Response | fusion360_exporter | authoring |
| `edit.part_instance.add_many` | `edit.part_instance.add_many` | — | active | staged | product.v1.BulkCreatePartInstancesRequest → product.v1.PartInstances / service.v1.Response | web_cobotar | authoring |
| `edit.process_recipe.add.root` | `edit.process_recipe.add.root` | — | active | staged | process.v1.AddRootSequenceRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.process_recipe.add.sequence` | `edit.process_recipe.add.sequence` | — | active | staged | process.v1.AddChildSequenceRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.process_recipe.add.task` | `edit.process_recipe.add.task` | — | active | staged | process.v1.AddChildTaskRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.process_recipe.remove.sequence` | `edit.process_recipe.remove.sequence` | — | active | staged | process.v1.RemoveSequenceRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.process_recipe.remove.task` | `edit.process_recipe.remove.task` | — | active | staged | process.v1.RemoveTaskRequest → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.product.import` | `edit.product.import` | — | active | staged | product.v1.ImportProduct → product.v1.ImportProductResult / service.v1.Response | fusion360_exporter | authoring |
| `edit.property_instance.update_value` | `edit.property_instance.update_value` | — | active | staged | common.v1.PropertyInstanceUpdate → service.v1.Response / service.v1.Response | web_cobotar, holo_cobotar | authoring |
| `event.device.heartbeat` | `event.device.heartbeat.{device_id}` | — | active | staged | resources.v1.DeviceHeartbeat | holo_cobotar | authoring |
| `event.log.error` | `event.log.error.{service}` | — | active | staged | common.v1.LogRecord | authoring, robot_adapter, holo_cobotar | web_cobotar |
| `event.log.full` | `event.log.full.{service}` | — | active | staged | common.v1.LogRecord | authoring, robot_adapter, holo_cobotar | web_cobotar |
| `event.process_run_definitions.added` | `event.process_run_definitions.added.{process_run_id}` | — | active | staged | runtime.v1.ProcessRunDefinitions | authoring | web_cobotar, holo_cobotar |
| `event.server.heartbeat.backend` | `event.server.heartbeat.backend` | — | active | staged | service.v1.ServerHeartbeat | authoring | web_cobotar, holo_cobotar |
| `event.server.heartbeat.robot_adapter` | `event.server.heartbeat.robot_adapter.{robot_instance_id}` | — | active | staged | service.v1.ServerHeartbeat | robot_adapter | authoring, web_cobotar |
| `event.server.restarted.backend` | `event.server.restarted.backend` | — | active | staged | service.v1.ServerInfo | authoring | web_cobotar, holo_cobotar |
| `event.task_run.progress` | `event.task_run.progress.{task_run_id}` | — | active | staged | runtime.v1.TaskProgressUpdate | authoring | web_cobotar, holo_cobotar |
| `generate.process_recipe.draft` | `generate.process_recipe.draft` | — | active | staged | process.v1.DraftProcessRecipeGenerateRequest → process.v1.DraftProcessRecipeGenerateResult / service.v1.Response | web_cobotar | authoring |
| `generate.process_recipe.draft.disassembly` | `generate.process_recipe.draft.disassembly` | — | active | staged | process.v1.DraftDisassemblyProcessRecipeGenerateRequest → process.v1.DraftProcessRecipeGenerateResult / service.v1.Response | web_cobotar | authoring |
| `generate.process_recipe.draft.kitting` | `generate.process_recipe.draft.kitting` | — | active | staged | process.v1.DraftKittingProcessRecipeGenerateRequest → process.v1.DraftProcessRecipeGenerateResult / service.v1.Response | web_cobotar | authoring |
| `get.actor_availability.actor` | `get.actor_availability.actor` | — | active | staged | common.v1.ActorRef → runtime.v1.ActorAvailability / service.v1.Response | web_cobotar | authoring |
| `get.actor_skill.field.actor_id` | `get.actor_skill.field.actor_id` | — | active | staged | common.v1.GetByFieldMessage → capability.v1.ActorSkills / service.v1.Response | web_cobotar | authoring |
| `get.actor_skill.field.skill_id` | `get.actor_skill.field.skill_id` | — | active | staged | common.v1.GetByFieldMessage → capability.v1.ActorSkills / service.v1.Response | web_cobotar | authoring |
| `get.ar_config.info` | `get.ar_config.info` | — | active | staged | (empty) → ar.v1.ARConfigInfoMessages / service.v1.Response | web_cobotar, holo_cobotar | authoring |
| `get.ar_config_binding.candidates` | `get.ar_config_binding.candidates` | — | active | staged | ar.v1.ARBindingCandidatesRequest → ar.v1.ARBindingCandidatesResponse / service.v1.Response | web_cobotar | authoring |
| `get.asset_adapter.info` | `get.asset_adapter.info.{asset_instance_id}` | — | active | staged | (empty) → resources.v1.AssetAdapterInfoMessage / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_instance.field.definition_id` | `get.asset_instance.field.definition_id` | — | active | staged | common.v1.GetByFieldMessage → resources.v1.AssetInstances / service.v1.Response | web_cobotar | authoring |
| `get.backend.info` | `get.backend.info` | — | active | staged | (empty) → service.v1.ServerInfo / service.v1.Response | web_cobotar, holo_cobotar | authoring |
| `get.container_instance.field.cell_id` | `get.container_instance.field.cell_id` | — | active | staged | common.v1.GetByFieldMessage → resources.v1.ContainerInstances / service.v1.Response | web_cobotar | authoring |
| `get.container_instance.field.definition_id` | `get.container_instance.field.definition_id` | — | active | staged | common.v1.GetByFieldMessage → resources.v1.ContainerInstances / service.v1.Response | web_cobotar | authoring |
| `get.container_instance.field.line_id` | `get.container_instance.field.line_id` | — | active | staged | common.v1.GetByFieldMessage → resources.v1.ContainerInstances / service.v1.Response | web_cobotar | authoring |
| `get.container_instance.field.station_id` | `get.container_instance.field.station_id` | — | active | staged | common.v1.GetByFieldMessage → resources.v1.ContainerInstances / service.v1.Response | web_cobotar | authoring |
| `get.execution_evidence.field.task_run_id` | `get.execution_evidence.field.task_run_id` | — | active | staged | common.v1.GetByFieldMessage → runtime.v1.ExecutionEvidences / service.v1.Response | web_cobotar | authoring |
| `get.part_instance.field.cell_id` | `get.part_instance.field.cell_id` | — | active | staged | common.v1.GetByFieldMessage → product.v1.PartInstances / service.v1.Response | web_cobotar | authoring |
| `get.part_instance.field.definition_id` | `get.part_instance.field.definition_id` | — | active | staged | common.v1.GetByFieldMessage → product.v1.PartInstances / service.v1.Response | web_cobotar | authoring |
| `get.part_instance.field.line_id` | `get.part_instance.field.line_id` | — | active | staged | common.v1.GetByFieldMessage → product.v1.PartInstances / service.v1.Response | web_cobotar | authoring |
| `get.part_instance.field.station_id` | `get.part_instance.field.station_id` | — | active | staged | common.v1.GetByFieldMessage → product.v1.PartInstances / service.v1.Response | web_cobotar | authoring |
| `get.process_run_definitions.one` | `get.process_run_definitions.one` | — | active | staged | runtime.v1.ProcessRunDefinitionsRequest → runtime.v1.ProcessRunDefinitions / service.v1.Response | robot_adapter, web_cobotar, holo_cobotar | authoring |
| `get.robot_adapter.info` | `get.robot_adapter.info.{robot_instance_id}` | — | active | staged | (empty) → robot.v1.RobotAdapterInfoMessage / service.v1.Response | authoring, web_cobotar, holo_cobotar | robot_adapter |
| `get.robot_instance.controller_status` | `get.robot_instance.controller_status.{robot_instance_id}` | — | active | staged | (empty) → robot.v1.RobotControllerStatusMessage / service.v1.Response | web_cobotar, holo_cobotar | robot_adapter |
| `get.robot_instance.field.definition_id` | `get.robot_instance.field.definition_id` | — | active | staged | common.v1.GetByFieldMessage → resources.v1.RobotInstances / service.v1.Response | web_cobotar | authoring |
| `get.robot_instance.io` | `get.robot_instance.io.{robot_instance_id}` | — | active | staged | (empty) → robot.v1.RobotIOState / service.v1.Response | web_cobotar | robot_adapter |
| `get.storage.info` | `get.storage.info` | — | active | staged | (empty) → service.v1.StorageInfo / service.v1.Response | web_cobotar | authoring |
| `get.tool_instance.field.definition_id` | `get.tool_instance.field.definition_id` | — | active | staged | common.v1.GetByFieldMessage → resources.v1.ToolInstances / service.v1.Response | web_cobotar | authoring |
| `plan.robot.path` | `plan.robot.path.{robot_instance_id}.{plan_id}` | — | active | staged | robot.v1.PathMessage | robot_adapter | web_cobotar, holo_cobotar |
| `report.asset_adapter.info` | `report.asset_adapter.info.{asset_instance_id}` | — | active | staged | resources.v1.AssetAdapterInfoMessage | asset_adapter | authoring |
| `report.robot_adapter.info` | `report.robot_adapter.info.{robot_instance_id}` | — | active | staged | robot.v1.RobotAdapterInfoMessage | robot_adapter | authoring |
| `telemetry.robot.controller_status` | `telemetry.robot.controller_status.{robot_instance_id}` | — | active | staged | robot.v1.RobotControllerStatusMessage | robot_adapter | web_cobotar, holo_cobotar |
| `telemetry.robot.end_effector` | `telemetry.robot.end_effector.{robot_instance_id}` | — | planned | staged | robot.v1.EndEffectorStateMessage | robot_adapter | holo_cobotar |
| `telemetry.robot.force_torque` | `telemetry.robot.force_torque.{robot_instance_id}` | — | active | staged | geometry.v1.Wrench | robot_adapter | web_cobotar |
| `telemetry.robot.io` | `telemetry.robot.io.{robot_instance_id}` | — | active | staged | robot.v1.RobotIOState | robot_adapter | web_cobotar |
| `telemetry.robot.joint_angles` | `telemetry.robot.joint_angles.{robot_instance_id}` | — | active | staged | robot.v1.JointStateMessage | robot_adapter | web_cobotar, holo_cobotar |
| `telemetry.robot.state` | `telemetry.robot.state.{robot_instance_id}` | — | active | staged | robot.v1.RobotStateMessage | robot_adapter | web_cobotar, holo_cobotar |
| `telemetry.robot.tcp` | `telemetry.robot.tcp.{robot_instance_id}` | — | active | staged | robot.v1.TcpMessage | robot_adapter | web_cobotar, holo_cobotar |
| `edit.action.add` | `edit.action.add` | `edit.entity.add` | active | staged | ar.v1.ActionAddMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.action.clone` | `edit.action.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.action.remove` | `edit.action.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.action.update` | `edit.action.update` | `edit.entity.update` | active | staged | ar.v1.ActionUpdateMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.actor_skill.add` | `edit.actor_skill.add` | `edit.entity.add` | active | staged | capability.v1.ActorSkill → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.actor_skill.clone` | `edit.actor_skill.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.actor_skill.remove` | `edit.actor_skill.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.actor_skill.update` | `edit.actor_skill.update` | `edit.entity.update` | active | staged | capability.v1.ActorSkill → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config.add` | `edit.ar_config.add` | `edit.entity.add` | active | staged | ar.v1.ARConfigAddMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config.clone` | `edit.ar_config.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config.remove` | `edit.ar_config.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config.update` | `edit.ar_config.update` | `edit.entity.update` | active | staged | ar.v1.ARConfigUpdateMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config_binding.add` | `edit.ar_config_binding.add` | `edit.entity.add` | active | staged | ar.v1.ARConfigBindingMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config_binding.clone` | `edit.ar_config_binding.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config_binding.remove` | `edit.ar_config_binding.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.ar_config_binding.update` | `edit.ar_config_binding.update` | `edit.entity.update` | active | staged | ar.v1.ARConfigBindingMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.asset_definition.add` | `edit.asset_definition.add` | `edit.entity.add` | active | staged | resources.v1.AssetDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.asset_definition.clone` | `edit.asset_definition.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.asset_definition.remove` | `edit.asset_definition.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.asset_definition.update` | `edit.asset_definition.update` | `edit.entity.update` | active | staged | resources.v1.AssetDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.asset_instance.add` | `edit.asset_instance.add` | `edit.entity.add` | active | staged | resources.v1.AssetInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.asset_instance.clone` | `edit.asset_instance.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.asset_instance.remove` | `edit.asset_instance.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.asset_instance.update` | `edit.asset_instance.update` | `edit.entity.update` | active | staged | resources.v1.AssetInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.cell.add` | `edit.cell.add` | `edit.entity.add` | active | staged | resources.v1.CellDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.cell.clone` | `edit.cell.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.cell.remove` | `edit.cell.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.cell.update` | `edit.cell.update` | `edit.entity.update` | active | staged | resources.v1.CellDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.container_definition.add` | `edit.container_definition.add` | `edit.entity.add` | active | staged | resources.v1.ContainerDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.container_definition.clone` | `edit.container_definition.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.container_definition.remove` | `edit.container_definition.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.container_definition.update` | `edit.container_definition.update` | `edit.entity.update` | active | staged | resources.v1.ContainerDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.container_instance.add` | `edit.container_instance.add` | `edit.entity.add` | active | staged | resources.v1.ContainerInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.container_instance.clone` | `edit.container_instance.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.container_instance.remove` | `edit.container_instance.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.container_instance.update` | `edit.container_instance.update` | `edit.entity.update` | active | staged | resources.v1.ContainerInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.device.add` | `edit.device.add` | `edit.entity.add` | active | staged | resources.v1.DeviceMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.device.clone` | `edit.device.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.device.remove` | `edit.device.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.device.update` | `edit.device.update` | `edit.entity.update` | active | staged | resources.v1.DeviceMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.execution_evidence.add` | `edit.execution_evidence.add` | `edit.entity.add` | active | staged | runtime.v1.ExecutionEvidence → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.feedback.add` | `edit.feedback.add` | `edit.entity.add` | active | staged | ar.v1.FeedbackAddMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.feedback.clone` | `edit.feedback.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.feedback.remove` | `edit.feedback.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.feedback.update` | `edit.feedback.update` | `edit.entity.update` | active | staged | ar.v1.FeedbackUpdateMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.function.add` | `edit.function.add` | `edit.entity.add` | active | staged | ar.v1.FunctionAddMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.function.clone` | `edit.function.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.function.remove` | `edit.function.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.function.update` | `edit.function.update` | `edit.entity.update` | active | staged | ar.v1.FunctionUpdateMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.line.add` | `edit.line.add` | `edit.entity.add` | active | staged | resources.v1.LineDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.line.clone` | `edit.line.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.line.remove` | `edit.line.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.line.update` | `edit.line.update` | `edit.entity.update` | active | staged | resources.v1.LineDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.marker.add` | `edit.marker.add` | `edit.entity.add` | active | staged | resources.v1.MarkerInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.marker.clone` | `edit.marker.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.marker.remove` | `edit.marker.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.marker.update` | `edit.marker.update` | `edit.entity.update` | active | staged | resources.v1.MarkerInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.model.add` | `edit.model.add` | `edit.entity.add` | active | staged | resources.v1.CreateModelArtifact → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.model.clone` | `edit.model.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.model.remove` | `edit.model.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.model.update` | `edit.model.update` | `edit.entity.update` | active | staged | resources.v1.ModelArtifact → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.part_definition.add` | `edit.part_definition.add` | `edit.entity.add` | active | staged | product.v1.PartDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.part_definition.clone` | `edit.part_definition.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.part_definition.remove` | `edit.part_definition.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.part_definition.update` | `edit.part_definition.update` | `edit.entity.update` | active | staged | product.v1.PartDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.part_family.add` | `edit.part_family.add` | `edit.entity.add` | active | staged | product.v1.PartFamily → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.part_family.remove` | `edit.part_family.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.part_family.update` | `edit.part_family.update` | `edit.entity.update` | active | staged | product.v1.PartFamily → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.part_instance.add` | `edit.part_instance.add` | `edit.entity.add` | active | staged | product.v1.PartInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.part_instance.clone` | `edit.part_instance.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.part_instance.remove` | `edit.part_instance.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.part_instance.update` | `edit.part_instance.update` | `edit.entity.update` | active | staged | product.v1.PartInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.presentation_strategy.add` | `edit.presentation_strategy.add` | `edit.entity.add` | active | staged | ar.v1.PresentationStrategyAdd → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.presentation_strategy.clone` | `edit.presentation_strategy.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.presentation_strategy.remove` | `edit.presentation_strategy.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.presentation_strategy.update` | `edit.presentation_strategy.update` | `edit.entity.update` | active | staged | ar.v1.PresentationStrategy → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.process_recipe.add` | `edit.process_recipe.add` | `edit.entity.add` | active | staged | process.v1.CreateProcessRecipe → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.process_recipe.clone` | `edit.process_recipe.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.process_recipe.remove` | `edit.process_recipe.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.process_recipe.update` | `edit.process_recipe.update` | `edit.entity.update` | active | staged | process.v1.ProcessRecipe → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.product.add` | `edit.product.add` | `edit.entity.add` | active | staged | product.v1.ProductDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.product.clone` | `edit.product.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.product.remove` | `edit.product.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.product.update` | `edit.product.update` | `edit.entity.update` | active | staged | product.v1.ProductDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.property_definition.add` | `edit.property_definition.add` | `edit.entity.add` | active | staged | common.v1.CreatePropertyMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.property_definition.clone` | `edit.property_definition.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.property_definition.remove` | `edit.property_definition.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.property_definition.update` | `edit.property_definition.update` | `edit.entity.update` | active | staged | common.v1.PropertyDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.property_instance.add` | `edit.property_instance.add` | `edit.entity.add` | active | staged | common.v1.PropertyInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.property_instance.clone` | `edit.property_instance.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.property_instance.remove` | `edit.property_instance.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.property_instance.update` | `edit.property_instance.update` | `edit.entity.update` | active | staged | common.v1.PropertyInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.robot_definition.add` | `edit.robot_definition.add` | `edit.entity.add` | active | staged | resources.v1.RobotDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.robot_definition.clone` | `edit.robot_definition.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.robot_definition.remove` | `edit.robot_definition.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.robot_definition.update` | `edit.robot_definition.update` | `edit.entity.update` | active | staged | resources.v1.RobotDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.robot_instance.add` | `edit.robot_instance.add` | `edit.entity.add` | active | staged | resources.v1.RobotInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.robot_instance.clone` | `edit.robot_instance.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.robot_instance.remove` | `edit.robot_instance.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.robot_instance.update` | `edit.robot_instance.update` | `edit.entity.update` | active | staged | resources.v1.RobotInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.sequence_definition.add` | `edit.sequence_definition.add` | `edit.entity.add` | active | staged | process.v1.SequenceDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.sequence_definition.clone` | `edit.sequence_definition.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.sequence_definition.remove` | `edit.sequence_definition.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.sequence_definition.update` | `edit.sequence_definition.update` | `edit.entity.update` | active | staged | process.v1.UpdateSequenceDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.skill.add` | `edit.skill.add` | `edit.entity.add` | active | staged | capability.v1.SkillDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.skill.clone` | `edit.skill.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.skill.remove` | `edit.skill.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.skill.update` | `edit.skill.update` | `edit.entity.update` | active | staged | capability.v1.SkillDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.station.add` | `edit.station.add` | `edit.entity.add` | active | staged | resources.v1.StationDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.station.clone` | `edit.station.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.station.remove` | `edit.station.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.station.update` | `edit.station.update` | `edit.entity.update` | active | staged | resources.v1.StationDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.task_definition.add` | `edit.task_definition.add` | `edit.entity.add` | active | staged | process.v1.TaskDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.task_definition.clone` | `edit.task_definition.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.task_definition.remove` | `edit.task_definition.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.task_definition.update` | `edit.task_definition.update` | `edit.entity.update` | active | staged | process.v1.UpdateTaskDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.tool_definition.add` | `edit.tool_definition.add` | `edit.entity.add` | active | staged | resources.v1.ToolDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.tool_definition.clone` | `edit.tool_definition.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.tool_definition.remove` | `edit.tool_definition.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.tool_definition.update` | `edit.tool_definition.update` | `edit.entity.update` | active | staged | resources.v1.ToolDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.tool_instance.add` | `edit.tool_instance.add` | `edit.entity.add` | active | staged | resources.v1.ToolInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.tool_instance.clone` | `edit.tool_instance.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.tool_instance.remove` | `edit.tool_instance.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.tool_instance.update` | `edit.tool_instance.update` | `edit.entity.update` | active | staged | resources.v1.ToolInstance → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.validity_policy.add` | `edit.validity_policy.add` | `edit.entity.add` | active | staged | capability.v1.ValidityPolicy → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.validity_policy.clone` | `edit.validity_policy.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.validity_policy.remove` | `edit.validity_policy.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.validity_policy.update` | `edit.validity_policy.update` | `edit.entity.update` | active | staged | capability.v1.ValidityPolicy → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.worker.add` | `edit.worker.add` | `edit.entity.add` | active | staged | resources.v1.WorkerDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.worker.clone` | `edit.worker.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.worker.remove` | `edit.worker.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.worker.update` | `edit.worker.update` | `edit.entity.update` | active | staged | resources.v1.WorkerDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.zone.add` | `edit.zone.add` | `edit.entity.add` | active | staged | geometry.v1.ZoneDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.zone.clone` | `edit.zone.clone` | `edit.entity.clone` | active | staged | common.v1.CloneMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.zone.remove` | `edit.zone.remove` | `edit.entity.remove` | active | staged | common.v1.DeleteMessage → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `edit.zone.update` | `edit.zone.update` | `edit.entity.update` | active | staged | geometry.v1.ZoneDefinition → service.v1.Response / service.v1.Response | web_cobotar | authoring |
| `event.action.added` | `event.action.added.{entity_id}` | `event.entity.added` | active | staged | ar.v1.ActionMessage | authoring | web_cobotar, holo_cobotar |
| `event.action.removed` | `event.action.removed.{entity_id}` | `event.entity.removed` | active | staged | ar.v1.ActionMessage | authoring | web_cobotar, holo_cobotar |
| `event.action.updated` | `event.action.updated.{entity_id}` | `event.entity.updated` | active | staged | ar.v1.ActionMessage | authoring | web_cobotar, holo_cobotar |
| `event.action_definition.added` | `event.action_definition.added.{entity_id}` | `event.entity.added` | active | staged | ar.v1.ActionDefinition | authoring | web_cobotar, holo_cobotar |
| `event.action_definition.removed` | `event.action_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | ar.v1.ActionDefinition | authoring | web_cobotar, holo_cobotar |
| `event.action_definition.updated` | `event.action_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | ar.v1.ActionDefinition | authoring | web_cobotar, holo_cobotar |
| `event.actor_availability.added` | `event.actor_availability.added.{entity_id}` | `event.entity.added` | active | staged | runtime.v1.ActorAvailability | authoring | web_cobotar, holo_cobotar |
| `event.actor_availability.removed` | `event.actor_availability.removed.{entity_id}` | `event.entity.removed` | active | staged | runtime.v1.ActorAvailability | authoring | web_cobotar, holo_cobotar |
| `event.actor_availability.updated` | `event.actor_availability.updated.{entity_id}` | `event.entity.updated` | active | staged | runtime.v1.ActorAvailability | authoring | web_cobotar, holo_cobotar |
| `event.actor_skill.added` | `event.actor_skill.added.{entity_id}` | `event.entity.added` | active | staged | capability.v1.ActorSkill | authoring | web_cobotar, holo_cobotar |
| `event.actor_skill.removed` | `event.actor_skill.removed.{entity_id}` | `event.entity.removed` | active | staged | capability.v1.ActorSkill | authoring | web_cobotar, holo_cobotar |
| `event.actor_skill.updated` | `event.actor_skill.updated.{entity_id}` | `event.entity.updated` | active | staged | capability.v1.ActorSkill | authoring | web_cobotar, holo_cobotar |
| `event.ar_config.added` | `event.ar_config.added.{entity_id}` | `event.entity.added` | active | staged | ar.v1.ARConfigMessage | authoring | web_cobotar, holo_cobotar |
| `event.ar_config.removed` | `event.ar_config.removed.{entity_id}` | `event.entity.removed` | active | staged | ar.v1.ARConfigMessage | authoring | web_cobotar, holo_cobotar |
| `event.ar_config.updated` | `event.ar_config.updated.{entity_id}` | `event.entity.updated` | active | staged | ar.v1.ARConfigMessage | authoring | web_cobotar, holo_cobotar |
| `event.ar_config_binding.added` | `event.ar_config_binding.added.{entity_id}` | `event.entity.added` | active | staged | ar.v1.ARConfigBindingMessage | authoring | web_cobotar, holo_cobotar |
| `event.ar_config_binding.removed` | `event.ar_config_binding.removed.{entity_id}` | `event.entity.removed` | active | staged | ar.v1.ARConfigBindingMessage | authoring | web_cobotar, holo_cobotar |
| `event.ar_config_binding.updated` | `event.ar_config_binding.updated.{entity_id}` | `event.entity.updated` | active | staged | ar.v1.ARConfigBindingMessage | authoring | web_cobotar, holo_cobotar |
| `event.asset_adapter_definition.added` | `event.asset_adapter_definition.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.AssetAdapterDefinition | authoring | web_cobotar, holo_cobotar |
| `event.asset_adapter_definition.removed` | `event.asset_adapter_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.AssetAdapterDefinition | authoring | web_cobotar, holo_cobotar |
| `event.asset_adapter_definition.updated` | `event.asset_adapter_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.AssetAdapterDefinition | authoring | web_cobotar, holo_cobotar |
| `event.asset_adapter_info.added` | `event.asset_adapter_info.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.AssetAdapterInfoMessage | authoring | web_cobotar, holo_cobotar |
| `event.asset_adapter_info.removed` | `event.asset_adapter_info.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.AssetAdapterInfoMessage | authoring | web_cobotar, holo_cobotar |
| `event.asset_adapter_info.updated` | `event.asset_adapter_info.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.AssetAdapterInfoMessage | authoring | web_cobotar, holo_cobotar |
| `event.asset_definition.added` | `event.asset_definition.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.AssetDefinition | authoring | web_cobotar, holo_cobotar |
| `event.asset_definition.removed` | `event.asset_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.AssetDefinition | authoring | web_cobotar, holo_cobotar |
| `event.asset_definition.updated` | `event.asset_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.AssetDefinition | authoring | web_cobotar, holo_cobotar |
| `event.asset_instance.added` | `event.asset_instance.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.AssetInstance | authoring | web_cobotar, holo_cobotar |
| `event.asset_instance.removed` | `event.asset_instance.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.AssetInstance | authoring | web_cobotar, holo_cobotar |
| `event.asset_instance.updated` | `event.asset_instance.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.AssetInstance | authoring | web_cobotar, holo_cobotar |
| `event.cell.added` | `event.cell.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.CellDefinition | authoring | web_cobotar, holo_cobotar |
| `event.cell.removed` | `event.cell.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.CellDefinition | authoring | web_cobotar, holo_cobotar |
| `event.cell.updated` | `event.cell.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.CellDefinition | authoring | web_cobotar, holo_cobotar |
| `event.container_definition.added` | `event.container_definition.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.ContainerDefinition | authoring | web_cobotar, holo_cobotar |
| `event.container_definition.removed` | `event.container_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.ContainerDefinition | authoring | web_cobotar, holo_cobotar |
| `event.container_definition.updated` | `event.container_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.ContainerDefinition | authoring | web_cobotar, holo_cobotar |
| `event.container_instance.added` | `event.container_instance.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.ContainerInstance | authoring | web_cobotar, holo_cobotar |
| `event.container_instance.removed` | `event.container_instance.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.ContainerInstance | authoring | web_cobotar, holo_cobotar |
| `event.container_instance.updated` | `event.container_instance.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.ContainerInstance | authoring | web_cobotar, holo_cobotar |
| `event.device.added` | `event.device.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.DeviceMessage | authoring | web_cobotar, holo_cobotar |
| `event.device.removed` | `event.device.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.DeviceMessage | authoring | web_cobotar, holo_cobotar |
| `event.device.updated` | `event.device.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.DeviceMessage | authoring | web_cobotar, holo_cobotar |
| `event.execution_evidence.added` | `event.execution_evidence.added.{entity_id}` | `event.entity.added` | active | staged | runtime.v1.ExecutionEvidence | authoring | web_cobotar, holo_cobotar |
| `event.execution_evidence.removed` | `event.execution_evidence.removed.{entity_id}` | `event.entity.removed` | active | staged | runtime.v1.ExecutionEvidence | authoring | web_cobotar, holo_cobotar |
| `event.execution_evidence.updated` | `event.execution_evidence.updated.{entity_id}` | `event.entity.updated` | active | staged | runtime.v1.ExecutionEvidence | authoring | web_cobotar, holo_cobotar |
| `event.feedback.added` | `event.feedback.added.{entity_id}` | `event.entity.added` | active | staged | ar.v1.FeedbackMessage | authoring | web_cobotar, holo_cobotar |
| `event.feedback.removed` | `event.feedback.removed.{entity_id}` | `event.entity.removed` | active | staged | ar.v1.FeedbackMessage | authoring | web_cobotar, holo_cobotar |
| `event.feedback.updated` | `event.feedback.updated.{entity_id}` | `event.entity.updated` | active | staged | ar.v1.FeedbackMessage | authoring | web_cobotar, holo_cobotar |
| `event.feedback_definition.added` | `event.feedback_definition.added.{entity_id}` | `event.entity.added` | active | staged | ar.v1.FeedbackDefinition | authoring | web_cobotar, holo_cobotar |
| `event.feedback_definition.removed` | `event.feedback_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | ar.v1.FeedbackDefinition | authoring | web_cobotar, holo_cobotar |
| `event.feedback_definition.updated` | `event.feedback_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | ar.v1.FeedbackDefinition | authoring | web_cobotar, holo_cobotar |
| `event.function.added` | `event.function.added.{entity_id}` | `event.entity.added` | active | staged | ar.v1.FunctionMessage | authoring | web_cobotar, holo_cobotar |
| `event.function.removed` | `event.function.removed.{entity_id}` | `event.entity.removed` | active | staged | ar.v1.FunctionMessage | authoring | web_cobotar, holo_cobotar |
| `event.function.updated` | `event.function.updated.{entity_id}` | `event.entity.updated` | active | staged | ar.v1.FunctionMessage | authoring | web_cobotar, holo_cobotar |
| `event.function_definition.added` | `event.function_definition.added.{entity_id}` | `event.entity.added` | active | staged | ar.v1.FunctionDefinition | authoring | web_cobotar, holo_cobotar |
| `event.function_definition.removed` | `event.function_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | ar.v1.FunctionDefinition | authoring | web_cobotar, holo_cobotar |
| `event.function_definition.updated` | `event.function_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | ar.v1.FunctionDefinition | authoring | web_cobotar, holo_cobotar |
| `event.line.added` | `event.line.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.LineDefinition | authoring | web_cobotar, holo_cobotar |
| `event.line.removed` | `event.line.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.LineDefinition | authoring | web_cobotar, holo_cobotar |
| `event.line.updated` | `event.line.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.LineDefinition | authoring | web_cobotar, holo_cobotar |
| `event.marker.added` | `event.marker.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.MarkerInstance | authoring | web_cobotar, holo_cobotar |
| `event.marker.removed` | `event.marker.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.MarkerInstance | authoring | web_cobotar, holo_cobotar |
| `event.marker.updated` | `event.marker.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.MarkerInstance | authoring | web_cobotar, holo_cobotar |
| `event.model.added` | `event.model.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.ModelArtifact | authoring | web_cobotar, holo_cobotar |
| `event.model.removed` | `event.model.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.ModelArtifact | authoring | web_cobotar, holo_cobotar |
| `event.model.updated` | `event.model.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.ModelArtifact | authoring | web_cobotar, holo_cobotar |
| `event.part_definition.added` | `event.part_definition.added.{entity_id}` | `event.entity.added` | active | staged | product.v1.PartDefinition | authoring | web_cobotar, holo_cobotar |
| `event.part_definition.removed` | `event.part_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | product.v1.PartDefinition | authoring | web_cobotar, holo_cobotar |
| `event.part_definition.updated` | `event.part_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | product.v1.PartDefinition | authoring | web_cobotar, holo_cobotar |
| `event.part_family.added` | `event.part_family.added.{entity_id}` | `event.entity.added` | active | staged | product.v1.PartFamily | authoring | web_cobotar |
| `event.part_family.removed` | `event.part_family.removed.{entity_id}` | `event.entity.removed` | active | staged | product.v1.PartFamily | authoring | web_cobotar |
| `event.part_family.updated` | `event.part_family.updated.{entity_id}` | `event.entity.updated` | active | staged | product.v1.PartFamily | authoring | web_cobotar |
| `event.part_instance.added` | `event.part_instance.added.{entity_id}` | `event.entity.added` | active | staged | product.v1.PartInstance | authoring | web_cobotar, holo_cobotar |
| `event.part_instance.removed` | `event.part_instance.removed.{entity_id}` | `event.entity.removed` | active | staged | product.v1.PartInstance | authoring | web_cobotar, holo_cobotar |
| `event.part_instance.updated` | `event.part_instance.updated.{entity_id}` | `event.entity.updated` | active | staged | product.v1.PartInstance | authoring | web_cobotar, holo_cobotar |
| `event.presentation_strategy.added` | `event.presentation_strategy.added.{entity_id}` | `event.entity.added` | active | staged | ar.v1.PresentationStrategy | authoring | web_cobotar, holo_cobotar |
| `event.presentation_strategy.removed` | `event.presentation_strategy.removed.{entity_id}` | `event.entity.removed` | active | staged | ar.v1.PresentationStrategy | authoring | web_cobotar, holo_cobotar |
| `event.presentation_strategy.updated` | `event.presentation_strategy.updated.{entity_id}` | `event.entity.updated` | active | staged | ar.v1.PresentationStrategy | authoring | web_cobotar, holo_cobotar |
| `event.process_recipe.added` | `event.process_recipe.added.{entity_id}` | `event.entity.added` | active | staged | process.v1.ProcessRecipe | authoring | web_cobotar, holo_cobotar |
| `event.process_recipe.removed` | `event.process_recipe.removed.{entity_id}` | `event.entity.removed` | active | staged | process.v1.ProcessRecipe | authoring | web_cobotar, holo_cobotar |
| `event.process_recipe.updated` | `event.process_recipe.updated.{entity_id}` | `event.entity.updated` | active | staged | process.v1.ProcessRecipe | authoring | web_cobotar, holo_cobotar |
| `event.process_run.added` | `event.process_run.added.{entity_id}` | `event.entity.added` | active | staged | runtime.v1.ProcessRun | authoring | web_cobotar, holo_cobotar |
| `event.process_run.removed` | `event.process_run.removed.{entity_id}` | `event.entity.removed` | active | staged | runtime.v1.ProcessRun | authoring | web_cobotar, holo_cobotar |
| `event.process_run.updated` | `event.process_run.updated.{entity_id}` | `event.entity.updated` | active | staged | runtime.v1.ProcessRun | authoring | web_cobotar, holo_cobotar |
| `event.product.added` | `event.product.added.{entity_id}` | `event.entity.added` | active | staged | product.v1.ProductDefinition | authoring | web_cobotar, holo_cobotar |
| `event.product.removed` | `event.product.removed.{entity_id}` | `event.entity.removed` | active | staged | product.v1.ProductDefinition | authoring | web_cobotar, holo_cobotar |
| `event.product.updated` | `event.product.updated.{entity_id}` | `event.entity.updated` | active | staged | product.v1.ProductDefinition | authoring | web_cobotar, holo_cobotar |
| `event.property_definition.added` | `event.property_definition.added.{entity_id}` | `event.entity.added` | active | staged | common.v1.PropertyDefinition | authoring | web_cobotar, holo_cobotar |
| `event.property_definition.removed` | `event.property_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | common.v1.PropertyDefinition | authoring | web_cobotar, holo_cobotar |
| `event.property_definition.updated` | `event.property_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | common.v1.PropertyDefinition | authoring | web_cobotar, holo_cobotar |
| `event.property_instance.added` | `event.property_instance.added.{entity_id}` | `event.entity.added` | active | staged | common.v1.PropertyInstance | authoring | web_cobotar, holo_cobotar |
| `event.property_instance.removed` | `event.property_instance.removed.{entity_id}` | `event.entity.removed` | active | staged | common.v1.PropertyInstance | authoring | web_cobotar, holo_cobotar |
| `event.property_instance.updated` | `event.property_instance.updated.{entity_id}` | `event.entity.updated` | active | staged | common.v1.PropertyInstance | authoring | web_cobotar, holo_cobotar |
| `event.robot_adapter_definition.added` | `event.robot_adapter_definition.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.RobotAdapterDefinition | authoring | web_cobotar, holo_cobotar |
| `event.robot_adapter_definition.removed` | `event.robot_adapter_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.RobotAdapterDefinition | authoring | web_cobotar, holo_cobotar |
| `event.robot_adapter_definition.updated` | `event.robot_adapter_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.RobotAdapterDefinition | authoring | web_cobotar, holo_cobotar |
| `event.robot_adapter_info.added` | `event.robot_adapter_info.added.{entity_id}` | `event.entity.added` | active | staged | robot.v1.RobotAdapterInfoMessage | authoring | web_cobotar, holo_cobotar |
| `event.robot_adapter_info.removed` | `event.robot_adapter_info.removed.{entity_id}` | `event.entity.removed` | active | staged | robot.v1.RobotAdapterInfoMessage | authoring | web_cobotar, holo_cobotar |
| `event.robot_adapter_info.updated` | `event.robot_adapter_info.updated.{entity_id}` | `event.entity.updated` | active | staged | robot.v1.RobotAdapterInfoMessage | authoring | web_cobotar, holo_cobotar |
| `event.robot_definition.added` | `event.robot_definition.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.RobotDefinition | authoring | web_cobotar, holo_cobotar |
| `event.robot_definition.removed` | `event.robot_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.RobotDefinition | authoring | web_cobotar, holo_cobotar |
| `event.robot_definition.updated` | `event.robot_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.RobotDefinition | authoring | web_cobotar, holo_cobotar |
| `event.robot_instance.added` | `event.robot_instance.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.RobotInstance | authoring | web_cobotar, holo_cobotar |
| `event.robot_instance.removed` | `event.robot_instance.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.RobotInstance | authoring | web_cobotar, holo_cobotar |
| `event.robot_instance.updated` | `event.robot_instance.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.RobotInstance | authoring | web_cobotar, holo_cobotar |
| `event.sequence_definition.added` | `event.sequence_definition.added.{entity_id}` | `event.entity.added` | active | staged | process.v1.SequenceDefinition | authoring | web_cobotar, holo_cobotar |
| `event.sequence_definition.removed` | `event.sequence_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | process.v1.SequenceDefinition | authoring | web_cobotar, holo_cobotar |
| `event.sequence_definition.updated` | `event.sequence_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | process.v1.SequenceDefinition | authoring | web_cobotar, holo_cobotar |
| `event.sequence_run.added` | `event.sequence_run.added.{entity_id}` | `event.entity.added` | active | staged | runtime.v1.SequenceRun | authoring | web_cobotar, holo_cobotar |
| `event.sequence_run.removed` | `event.sequence_run.removed.{entity_id}` | `event.entity.removed` | active | staged | runtime.v1.SequenceRun | authoring | web_cobotar, holo_cobotar |
| `event.sequence_run.updated` | `event.sequence_run.updated.{entity_id}` | `event.entity.updated` | active | staged | runtime.v1.SequenceRun | authoring | web_cobotar, holo_cobotar |
| `event.skill.added` | `event.skill.added.{entity_id}` | `event.entity.added` | active | staged | capability.v1.SkillDefinition | authoring | web_cobotar, holo_cobotar |
| `event.skill.removed` | `event.skill.removed.{entity_id}` | `event.entity.removed` | active | staged | capability.v1.SkillDefinition | authoring | web_cobotar, holo_cobotar |
| `event.skill.updated` | `event.skill.updated.{entity_id}` | `event.entity.updated` | active | staged | capability.v1.SkillDefinition | authoring | web_cobotar, holo_cobotar |
| `event.station.added` | `event.station.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.StationDefinition | authoring | web_cobotar, holo_cobotar |
| `event.station.removed` | `event.station.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.StationDefinition | authoring | web_cobotar, holo_cobotar |
| `event.station.updated` | `event.station.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.StationDefinition | authoring | web_cobotar, holo_cobotar |
| `event.task_definition.added` | `event.task_definition.added.{entity_id}` | `event.entity.added` | active | staged | process.v1.TaskDefinition | authoring | web_cobotar, holo_cobotar |
| `event.task_definition.removed` | `event.task_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | process.v1.TaskDefinition | authoring | web_cobotar, holo_cobotar |
| `event.task_definition.updated` | `event.task_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | process.v1.TaskDefinition | authoring | web_cobotar, holo_cobotar |
| `event.task_run.added` | `event.task_run.added.{entity_id}` | `event.entity.added` | active | staged | runtime.v1.TaskRun | authoring | web_cobotar, holo_cobotar |
| `event.task_run.removed` | `event.task_run.removed.{entity_id}` | `event.entity.removed` | active | staged | runtime.v1.TaskRun | authoring | web_cobotar, holo_cobotar |
| `event.task_run.updated` | `event.task_run.updated.{entity_id}` | `event.entity.updated` | active | staged | runtime.v1.TaskRun | authoring | web_cobotar, holo_cobotar |
| `event.tool_definition.added` | `event.tool_definition.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.ToolDefinition | authoring | web_cobotar, holo_cobotar |
| `event.tool_definition.removed` | `event.tool_definition.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.ToolDefinition | authoring | web_cobotar, holo_cobotar |
| `event.tool_definition.updated` | `event.tool_definition.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.ToolDefinition | authoring | web_cobotar, holo_cobotar |
| `event.tool_instance.added` | `event.tool_instance.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.ToolInstance | authoring | web_cobotar, holo_cobotar |
| `event.tool_instance.removed` | `event.tool_instance.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.ToolInstance | authoring | web_cobotar, holo_cobotar |
| `event.tool_instance.updated` | `event.tool_instance.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.ToolInstance | authoring | web_cobotar, holo_cobotar |
| `event.validity_policy.added` | `event.validity_policy.added.{entity_id}` | `event.entity.added` | active | staged | capability.v1.ValidityPolicy | authoring | web_cobotar, holo_cobotar |
| `event.validity_policy.removed` | `event.validity_policy.removed.{entity_id}` | `event.entity.removed` | active | staged | capability.v1.ValidityPolicy | authoring | web_cobotar, holo_cobotar |
| `event.validity_policy.updated` | `event.validity_policy.updated.{entity_id}` | `event.entity.updated` | active | staged | capability.v1.ValidityPolicy | authoring | web_cobotar, holo_cobotar |
| `event.worker.added` | `event.worker.added.{entity_id}` | `event.entity.added` | active | staged | resources.v1.WorkerDefinition | authoring | web_cobotar, holo_cobotar |
| `event.worker.removed` | `event.worker.removed.{entity_id}` | `event.entity.removed` | active | staged | resources.v1.WorkerDefinition | authoring | web_cobotar, holo_cobotar |
| `event.worker.updated` | `event.worker.updated.{entity_id}` | `event.entity.updated` | active | staged | resources.v1.WorkerDefinition | authoring | web_cobotar, holo_cobotar |
| `event.zone.added` | `event.zone.added.{entity_id}` | `event.entity.added` | active | staged | geometry.v1.ZoneDefinition | authoring | web_cobotar, holo_cobotar |
| `event.zone.removed` | `event.zone.removed.{entity_id}` | `event.entity.removed` | active | staged | geometry.v1.ZoneDefinition | authoring | web_cobotar, holo_cobotar |
| `event.zone.updated` | `event.zone.updated.{entity_id}` | `event.entity.updated` | active | staged | geometry.v1.ZoneDefinition | authoring | web_cobotar, holo_cobotar |
| `get.action.all` | `get.action.all` | `get.entity.all` | active | staged | (empty) → ar.v1.ActionMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.action.one` | `get.action.one` | `get.entity.one` | active | staged | common.v1.GetMessage → ar.v1.ActionMessage / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.action.some` | `get.action.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → ar.v1.ActionMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.action_definition.all` | `get.action_definition.all` | `get.entity.all` | active | staged | (empty) → ar.v1.ActionDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.action_definition.one` | `get.action_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → ar.v1.ActionDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.action_definition.some` | `get.action_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → ar.v1.ActionDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.actor_availability.all` | `get.actor_availability.all` | `get.entity.all` | active | staged | (empty) → runtime.v1.ActorAvailabilities / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.actor_availability.one` | `get.actor_availability.one` | `get.entity.one` | active | staged | common.v1.GetMessage → runtime.v1.ActorAvailability / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.actor_availability.some` | `get.actor_availability.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → runtime.v1.ActorAvailabilities / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.actor_skill.all` | `get.actor_skill.all` | `get.entity.all` | active | staged | (empty) → capability.v1.ActorSkills / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.actor_skill.one` | `get.actor_skill.one` | `get.entity.one` | active | staged | common.v1.GetMessage → capability.v1.ActorSkill / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.actor_skill.some` | `get.actor_skill.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → capability.v1.ActorSkills / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.ar_config.all` | `get.ar_config.all` | `get.entity.all` | active | staged | (empty) → ar.v1.ARConfigMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.ar_config.one` | `get.ar_config.one` | `get.entity.one` | active | staged | common.v1.GetMessage → ar.v1.ARConfigMessage / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.ar_config.some` | `get.ar_config.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → ar.v1.ARConfigMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.ar_config_binding.all` | `get.ar_config_binding.all` | `get.entity.all` | active | staged | (empty) → ar.v1.ARConfigBindingMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.ar_config_binding.one` | `get.ar_config_binding.one` | `get.entity.one` | active | staged | common.v1.GetMessage → ar.v1.ARConfigBindingMessage / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.ar_config_binding.some` | `get.ar_config_binding.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → ar.v1.ARConfigBindingMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_adapter_definition.all` | `get.asset_adapter_definition.all` | `get.entity.all` | active | staged | (empty) → resources.v1.AssetAdapterDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_adapter_definition.one` | `get.asset_adapter_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.AssetAdapterDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_adapter_definition.some` | `get.asset_adapter_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.AssetAdapterDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_definition.all` | `get.asset_definition.all` | `get.entity.all` | active | staged | (empty) → resources.v1.AssetDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_definition.one` | `get.asset_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.AssetDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_definition.some` | `get.asset_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.AssetDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_instance.all` | `get.asset_instance.all` | `get.entity.all` | active | staged | (empty) → resources.v1.AssetInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_instance.one` | `get.asset_instance.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.AssetInstance / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.asset_instance.some` | `get.asset_instance.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.AssetInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.cell.all` | `get.cell.all` | `get.entity.all` | active | staged | (empty) → resources.v1.CellDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.cell.one` | `get.cell.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.CellDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.cell.some` | `get.cell.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.CellDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.container_definition.all` | `get.container_definition.all` | `get.entity.all` | active | staged | (empty) → resources.v1.ContainerDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar, robot_adapter | authoring |
| `get.container_definition.one` | `get.container_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.ContainerDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.container_definition.some` | `get.container_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.ContainerDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.container_instance.all` | `get.container_instance.all` | `get.entity.all` | active | staged | (empty) → resources.v1.ContainerInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar, robot_adapter | authoring |
| `get.container_instance.one` | `get.container_instance.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.ContainerInstance / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.container_instance.some` | `get.container_instance.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.ContainerInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.device.all` | `get.device.all` | `get.entity.all` | active | staged | (empty) → resources.v1.DeviceMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.device.one` | `get.device.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.DeviceMessage / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.device.some` | `get.device.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.DeviceMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.execution_evidence.all` | `get.execution_evidence.all` | `get.entity.all` | active | staged | (empty) → runtime.v1.ExecutionEvidences / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.execution_evidence.one` | `get.execution_evidence.one` | `get.entity.one` | active | staged | common.v1.GetMessage → runtime.v1.ExecutionEvidence / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.execution_evidence.some` | `get.execution_evidence.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → runtime.v1.ExecutionEvidences / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.feedback.all` | `get.feedback.all` | `get.entity.all` | active | staged | (empty) → ar.v1.FeedbackMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.feedback.one` | `get.feedback.one` | `get.entity.one` | active | staged | common.v1.GetMessage → ar.v1.FeedbackMessage / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.feedback.some` | `get.feedback.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → ar.v1.FeedbackMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.feedback_definition.all` | `get.feedback_definition.all` | `get.entity.all` | active | staged | (empty) → ar.v1.FeedbackDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.feedback_definition.one` | `get.feedback_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → ar.v1.FeedbackDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.feedback_definition.some` | `get.feedback_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → ar.v1.FeedbackDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.function.all` | `get.function.all` | `get.entity.all` | active | staged | (empty) → ar.v1.FunctionMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.function.one` | `get.function.one` | `get.entity.one` | active | staged | common.v1.GetMessage → ar.v1.FunctionMessage / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.function.some` | `get.function.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → ar.v1.FunctionMessages / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.function_definition.all` | `get.function_definition.all` | `get.entity.all` | active | staged | (empty) → ar.v1.FunctionDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.function_definition.one` | `get.function_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → ar.v1.FunctionDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.function_definition.some` | `get.function_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → ar.v1.FunctionDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.line.all` | `get.line.all` | `get.entity.all` | active | staged | (empty) → resources.v1.LineDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.line.one` | `get.line.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.LineDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.line.some` | `get.line.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.LineDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.marker.all` | `get.marker.all` | `get.entity.all` | active | staged | (empty) → resources.v1.MarkerInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.marker.one` | `get.marker.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.MarkerInstance / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.marker.some` | `get.marker.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.MarkerInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.model.all` | `get.model.all` | `get.entity.all` | active | staged | (empty) → resources.v1.ModelArtifacts / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.model.one` | `get.model.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.ModelArtifact / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.model.some` | `get.model.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.ModelArtifacts / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.part_definition.all` | `get.part_definition.all` | `get.entity.all` | active | staged | (empty) → product.v1.PartDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.part_definition.one` | `get.part_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → product.v1.PartDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar, robot_adapter | authoring |
| `get.part_definition.some` | `get.part_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → product.v1.PartDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.part_family.all` | `get.part_family.all` | `get.entity.all` | active | staged | (empty) → product.v1.PartFamilies / service.v1.Response | authoring, web_cobotar | authoring |
| `get.part_family.one` | `get.part_family.one` | `get.entity.one` | active | staged | common.v1.GetMessage → product.v1.PartFamily / service.v1.Response | authoring, web_cobotar | authoring |
| `get.part_family.some` | `get.part_family.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → product.v1.PartFamilies / service.v1.Response | authoring, web_cobotar | authoring |
| `get.part_instance.all` | `get.part_instance.all` | `get.entity.all` | active | staged | (empty) → product.v1.PartInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.part_instance.one` | `get.part_instance.one` | `get.entity.one` | active | staged | common.v1.GetMessage → product.v1.PartInstance / service.v1.Response | authoring, web_cobotar, holo_cobotar, robot_adapter | authoring |
| `get.part_instance.some` | `get.part_instance.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → product.v1.PartInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.presentation_strategy.all` | `get.presentation_strategy.all` | `get.entity.all` | active | staged | (empty) → ar.v1.PresentationStrategies / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.presentation_strategy.one` | `get.presentation_strategy.one` | `get.entity.one` | active | staged | common.v1.GetMessage → ar.v1.PresentationStrategy / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.presentation_strategy.some` | `get.presentation_strategy.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → ar.v1.PresentationStrategies / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.process_recipe.all` | `get.process_recipe.all` | `get.entity.all` | active | staged | (empty) → process.v1.ProcessRecipes / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.process_recipe.one` | `get.process_recipe.one` | `get.entity.one` | active | staged | common.v1.GetMessage → process.v1.ProcessRecipe / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.process_recipe.some` | `get.process_recipe.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → process.v1.ProcessRecipes / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.process_run.all` | `get.process_run.all` | `get.entity.all` | active | staged | (empty) → runtime.v1.ProcessRuns / service.v1.Response | authoring, web_cobotar, holo_cobotar, robot_adapter | authoring |
| `get.process_run.one` | `get.process_run.one` | `get.entity.one` | active | staged | common.v1.GetMessage → runtime.v1.ProcessRun / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.process_run.some` | `get.process_run.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → runtime.v1.ProcessRuns / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.product.all` | `get.product.all` | `get.entity.all` | active | staged | (empty) → product.v1.ProductDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.product.one` | `get.product.one` | `get.entity.one` | active | staged | common.v1.GetMessage → product.v1.ProductDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.product.some` | `get.product.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → product.v1.ProductDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.property_definition.all` | `get.property_definition.all` | `get.entity.all` | active | staged | (empty) → common.v1.PropertyDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.property_definition.one` | `get.property_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → common.v1.PropertyDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.property_definition.some` | `get.property_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → common.v1.PropertyDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.property_instance.all` | `get.property_instance.all` | `get.entity.all` | active | staged | (empty) → common.v1.PropertyInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.property_instance.one` | `get.property_instance.one` | `get.entity.one` | active | staged | common.v1.GetMessage → common.v1.PropertyInstance / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.property_instance.some` | `get.property_instance.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → common.v1.PropertyInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_adapter_definition.all` | `get.robot_adapter_definition.all` | `get.entity.all` | active | staged | (empty) → resources.v1.RobotAdapterDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_adapter_definition.one` | `get.robot_adapter_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.RobotAdapterDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_adapter_definition.some` | `get.robot_adapter_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.RobotAdapterDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_definition.all` | `get.robot_definition.all` | `get.entity.all` | active | staged | (empty) → resources.v1.RobotDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_definition.one` | `get.robot_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.RobotDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_definition.some` | `get.robot_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.RobotDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_instance.all` | `get.robot_instance.all` | `get.entity.all` | active | staged | (empty) → resources.v1.RobotInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_instance.one` | `get.robot_instance.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.RobotInstance / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.robot_instance.some` | `get.robot_instance.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.RobotInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.sequence_definition.all` | `get.sequence_definition.all` | `get.entity.all` | active | staged | (empty) → process.v1.SequenceDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.sequence_definition.one` | `get.sequence_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → process.v1.SequenceDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.sequence_definition.some` | `get.sequence_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → process.v1.SequenceDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.sequence_run.all` | `get.sequence_run.all` | `get.entity.all` | active | staged | (empty) → runtime.v1.SequenceRuns / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.sequence_run.one` | `get.sequence_run.one` | `get.entity.one` | active | staged | common.v1.GetMessage → runtime.v1.SequenceRun / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.sequence_run.some` | `get.sequence_run.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → runtime.v1.SequenceRuns / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.skill.all` | `get.skill.all` | `get.entity.all` | active | staged | (empty) → capability.v1.SkillDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.skill.one` | `get.skill.one` | `get.entity.one` | active | staged | common.v1.GetMessage → capability.v1.SkillDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.skill.some` | `get.skill.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → capability.v1.SkillDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.station.all` | `get.station.all` | `get.entity.all` | active | staged | (empty) → resources.v1.StationDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.station.one` | `get.station.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.StationDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.station.some` | `get.station.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.StationDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.task_definition.all` | `get.task_definition.all` | `get.entity.all` | active | staged | (empty) → process.v1.TaskDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.task_definition.one` | `get.task_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → process.v1.TaskDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.task_definition.some` | `get.task_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → process.v1.TaskDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.task_run.all` | `get.task_run.all` | `get.entity.all` | active | staged | (empty) → runtime.v1.TaskRuns / service.v1.Response | authoring, web_cobotar, holo_cobotar, robot_adapter | authoring |
| `get.task_run.one` | `get.task_run.one` | `get.entity.one` | active | staged | common.v1.GetMessage → runtime.v1.TaskRun / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.task_run.some` | `get.task_run.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → runtime.v1.TaskRuns / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.tool_definition.all` | `get.tool_definition.all` | `get.entity.all` | active | staged | (empty) → resources.v1.ToolDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.tool_definition.one` | `get.tool_definition.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.ToolDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.tool_definition.some` | `get.tool_definition.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.ToolDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.tool_instance.all` | `get.tool_instance.all` | `get.entity.all` | active | staged | (empty) → resources.v1.ToolInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.tool_instance.one` | `get.tool_instance.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.ToolInstance / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.tool_instance.some` | `get.tool_instance.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.ToolInstances / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.validity_policy.all` | `get.validity_policy.all` | `get.entity.all` | active | staged | (empty) → capability.v1.ValidityPolicies / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.validity_policy.one` | `get.validity_policy.one` | `get.entity.one` | active | staged | common.v1.GetMessage → capability.v1.ValidityPolicy / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.validity_policy.some` | `get.validity_policy.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → capability.v1.ValidityPolicies / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.worker.all` | `get.worker.all` | `get.entity.all` | active | staged | (empty) → resources.v1.WorkerDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.worker.one` | `get.worker.one` | `get.entity.one` | active | staged | common.v1.GetMessage → resources.v1.WorkerDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.worker.some` | `get.worker.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → resources.v1.WorkerDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.zone.all` | `get.zone.all` | `get.entity.all` | active | staged | (empty) → geometry.v1.ZoneDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.zone.one` | `get.zone.one` | `get.entity.one` | active | staged | common.v1.GetMessage → geometry.v1.ZoneDefinition / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |
| `get.zone.some` | `get.zone.some` | `get.entity.some` | active | staged | common.v1.GetByIdMessage → geometry.v1.ZoneDefinitions / service.v1.Response | authoring, web_cobotar, holo_cobotar | authoring |

For request/reply routes, publishers are requesters and consumers are responders. These lists describe intended ownership; staged conformance does not claim that every implementation has landed.

## Naming rules

- Literal tokens and entity names use lower_snake_case.
- Route families use the literal `entity` segment in their ID and `{entity}` in their pattern; generated concrete routes substitute one declared `EntityName`.
- Parameters occupy exactly one NATS token and reject `.`, `*`, `>`, whitespace, and empty values.
- Concrete publishers and requesters never use wildcards. Generated `Subscribe…Any` and named partial-subscription helpers introduce wildcards explicitly.
- Entity and routing identifiers follow the operation token unless a catalog entry documents a different order.
- Planned and staged helpers are experimental; their presence does not guarantee runtime availability.
