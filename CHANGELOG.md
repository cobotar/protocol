# Changelog

## Unreleased

### Added

- Free drive and robot plans as robot adapter capabilities (cobotar/protocol#24): `robot.v1.RobotAdapterCommandType` `FREE_DRIVE_START` and `FREE_DRIVE_STOP`; `robot.v1.RobotAdapterPlanType` (path, waypoints, joint angles) with `RobotAdapterPlanCapability` and `resources.v1.RobotAdapterDefinition.plans`; `resources.v1.ResourcePlanRequirement` as `ResourceRequirement.plan`, which only robot resource requirements may use; `common.v1.SignalSemantic.SIGNAL_SEMANTIC_ROBOT_FREE_DRIVE` for the output that puts the robot in free drive; and `robot.v1.RobotFreeDriveRequest` on the new route `command.robot_instance.free_drive.{robot_instance_id}`, which robot adapters serve.
- `ar.v1.ARResourceBindingStatus.AR_RESOURCE_BINDING_STATUS_OFFLINE`: the adapter of a bound resource isn't running, so every requirement on the slot is listed as unmet with the consumers that need it. Authoring reports it while it doesn't hear the adapter's heartbeats, without storing it (cobotar/Authoring#69).
- Subject catalog routes for every subject Authoring serves, publishes, requests or subscribes to: the run, task, availability and ownership commands, AR config input slots and presentation bindings, process recipe structure edits, field lookups, process recipe draft generation, `get.ar_config.info`, `get.process_run_definitions.one`, `get.backend.info`, the robot adapter's commands and requests, robot telemetry, task progress, device and server heartbeats, server restarts and log records (cobotar/Authoring#64).
- The adapter info subjects (cobotar/protocol#23): adapters announce their info on `report.robot_adapter.info.{robot_instance_id}` and `report.asset_adapter.info.{asset_instance_id}`, and Authoring reports changes as added, updated and removed events of the new `robot_adapter_info` and `asset_adapter_info` entities. The new `robot_adapter` and `asset_adapter` components stand for the adapters of robot instances (such as the UR adapter) and of asset instances, so the routes they serve, request and publish say so.
- `ARBindingCandidatesRequest` and `ARBindingCandidatesResponse`, plus `get.ar_config_binding.candidates`, for evaluating which resources satisfy an AR config slot without creating or changing a binding (cobotar/protocol#26).
- Entity-aware NATS route families, a generated `EntityName` API, and concrete CRUD/event subject contracts with per-entity protobuf metadata for Go, C#, TypeScript, and Python (cobotar/protocol#11).
- `ar.v1.FunctionType.FUNCTION_TYPE_ROBOT_ANCHOR` and `FUNCTION_TYPE_ROBOT_STATE`, which output a robot frame's anchor and the robot's state, replacing the anchor, state and colour properties that a robot input slot used to generate; and `ar.v1.FunctionAddMessage.robot_property_id`, so a robot function is linked to a slot when it is created, like feedback and actions (cobotar/Authoring#51).
- `common.v1.SignalSemantic.SIGNAL_SEMANTIC_ROBOT_ACKNOWLEDGE` for the robot input that an adapter pulses for the `ACKNOWLEDGE` command, so whether a connected robot can acknowledge shows in its signal catalog (cobotar/protocol#22).
- Resource capability requirements for feedback, action and function definitions; explicit AR input-slot constraints; and per-resource binding status with unmet requirements and affected consumers (cobotar/protocol#16).
- `resources.v1.AssetAdapterDefinition` and `resources.v1.AssetAdapterInfoMessage`, describing static asset commands, telemetry and standard signals separately from instance-specific identity and effective signals (cobotar/protocol#15).
- A shared `common.v1.SignalCatalog` for typed, readable and writable robot and asset signals, plus standard signal semantics for cameras, stack lights, conveyors, sensors, HMIs and part feeders (cobotar/protocol#15).
- `resources.v1.RobotAdapterDefinition`, describing the static commands, telemetry, supported robot types and configurable I/O register kinds supplied by an adapter implementation (cobotar/protocol#14).
- A staged, descriptor-validated NATS subject catalog and generated subject helpers for Go, C#, TypeScript, and Python. Planned routes remain available for incremental implementation without being treated as enforced runtime contracts (cobotar/protocol#11).
- `runtime.v1.ProcessRunDefinitions`: the recipe, sequence, task and part definitions a process run was loaded with, so every client shows and uses the same definitions as the backend while the run is active, whatever happens to the definitions afterwards. `source` says whether it holds the pinned definitions or, once the retention period after the run has passed, the latest ones. AR content isn't pinned and stays live. Published as an added event when a run is loaded (cobotar/protocol#18, part of cobotar/protocol#17).
- `runtime.v1.ProcessRunDefinitionsRequest` to fetch a run's definitions by process run ID.
- Predefined string rules and stricter field validation for execution evidence and evidence facts.

### Changed

- `plan.robot.path.{robot_instance_id}.{plan_id}` is published by robot adapters, not by Authoring.
- `edit.property_instance.update-value` is now `edit.property_instance.update_value`, since subject tokens are lower_snake_case.
- The reserved `edit.{entity}.reset.{child}` route is replaced by `edit.ar_config.reset.presentation_binding`, which takes an `ar.v1.PresentationBindingReset`.
- `get.ar_config_binding.candidates` and `get.asset_adapter.info` are active, since Authoring serves them.
- `resources.v1.ResourceSignalRequirement` now accepts an unspecified data type when `signal_id` or `signal_id_property_key` selects the concrete signal, allowing the selected signal to satisfy the requirement regardless of its type (cobotar/protocol#25).
- `resources.v1.AssetDefinition` now selects an asset adapter definition. `AssetDriverType`, `driver_type` and the robot-specific signal catalog messages have been removed; robot adapter info now uses the shared signal catalog (cobotar/protocol#15).
- `resources.v1.RobotDefinition` now selects a robot adapter definition, and `robot.v1.RobotAdapterInfoMessage` references that definition while reporting the connected controller identity, adapter version and configured I/O catalog. The former `RobotDriverType`, `driver_type`, legacy adapter identity fields and embedded `RobotAdapterCapabilities` have been removed (cobotar/protocol#14).
- `max_concurrent_processes` on lines, cells and stations is documented to count only active runs.
