# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [ar/v1/permissions.proto](#ar_v1_permissions-proto)
    - [WorkerPermission](#ar-v1-WorkerPermission)
  
- [common/v1/color.proto](#common_v1_color-proto)
    - [Color](#common-v1-Color)
  
- [geometry/v1/anchor.proto](#geometry_v1_anchor-proto)
    - [Anchor](#geometry-v1-Anchor)
  
- [geometry/v1/point.proto](#geometry_v1_point-proto)
    - [Point](#geometry-v1-Point)
  
- [geometry/v1/quad.proto](#geometry_v1_quad-proto)
    - [Quad](#geometry-v1-Quad)
  
- [geometry/v1/pose.proto](#geometry_v1_pose-proto)
    - [LocalizedPose](#geometry-v1-LocalizedPose)
    - [Pose](#geometry-v1-Pose)
  
    - [LocalizedState](#geometry-v1-LocalizedState)
  
- [geometry/v1/vector3.proto](#geometry_v1_vector3-proto)
    - [Vector3](#geometry-v1-Vector3)
  
- [validation/v1/predefined_string_rules.proto](#validation_v1_predefined_string_rules-proto)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
  
- [ar/v1/property.proto](#ar_v1_property-proto)
    - [AnchorExtras](#ar-v1-AnchorExtras)
    - [ColorExtras](#ar-v1-ColorExtras)
    - [EnumExtras](#ar-v1-EnumExtras)
    - [EnumOption](#ar-v1-EnumOption)
    - [NumberExtras](#ar-v1-NumberExtras)
    - [PoseExtras](#ar-v1-PoseExtras)
    - [Property](#ar-v1-Property)
    - [PropertyMessages](#ar-v1-PropertyMessages)
    - [PropertyValueUpdate](#ar-v1-PropertyValueUpdate)
    - [Vector3Extras](#ar-v1-Vector3Extras)
  
    - [PropertyGroup](#ar-v1-PropertyGroup)
    - [PropertyOrigin](#ar-v1-PropertyOrigin)
    - [PropertyType](#ar-v1-PropertyType)
  
- [ar/v1/action.proto](#ar_v1_action-proto)
    - [ActionAddMessage](#ar-v1-ActionAddMessage)
    - [ActionCloneMessage](#ar-v1-ActionCloneMessage)
    - [ActionMessage](#ar-v1-ActionMessage)
    - [ActionMessages](#ar-v1-ActionMessages)
    - [ActionUpdateMessage](#ar-v1-ActionUpdateMessage)
  
    - [ActionType](#ar-v1-ActionType)
  
- [ar/v1/events.proto](#ar_v1_events-proto)
    - [ExchangeSupport](#ar-v1-ExchangeSupport)
    - [ExchangeType](#ar-v1-ExchangeType)
    - [HandlerRequirement](#ar-v1-HandlerRequirement)
    - [SupportedExchangesMessage](#ar-v1-SupportedExchangesMessage)
  
    - [CommandType](#ar-v1-CommandType)
    - [EventType](#ar-v1-EventType)
    - [HandlerCardinality](#ar-v1-HandlerCardinality)
    - [PlanType](#ar-v1-PlanType)
    - [TelemetryType](#ar-v1-TelemetryType)
  
- [ar/v1/action_info.proto](#ar_v1_action_info-proto)
    - [ActionInfoMessage](#ar-v1-ActionInfoMessage)
    - [ActionInfoMessages](#ar-v1-ActionInfoMessages)
  
    - [ActionGroup](#ar-v1-ActionGroup)
  
- [ar/v1/feedback.proto](#ar_v1_feedback-proto)
    - [FeedbackAddMessage](#ar-v1-FeedbackAddMessage)
    - [FeedbackCloneMessage](#ar-v1-FeedbackCloneMessage)
    - [FeedbackMessage](#ar-v1-FeedbackMessage)
    - [FeedbackMessages](#ar-v1-FeedbackMessages)
    - [FeedbackUpdateMessage](#ar-v1-FeedbackUpdateMessage)
  
    - [FeedbackType](#ar-v1-FeedbackType)
  
- [ar/v1/helper.proto](#ar_v1_helper-proto)
    - [HelperAddMessage](#ar-v1-HelperAddMessage)
    - [HelperMessage](#ar-v1-HelperMessage)
    - [HelperMessages](#ar-v1-HelperMessages)
    - [HelperUpdateMessage](#ar-v1-HelperUpdateMessage)
  
    - [HelperType](#ar-v1-HelperType)
  
- [ar/v1/ar_config.proto](#ar_v1_ar_config-proto)
    - [ARConfigInfoMessage](#ar-v1-ARConfigInfoMessage)
    - [ARConfigInfoMessages](#ar-v1-ARConfigInfoMessages)
    - [ARConfigMessage](#ar-v1-ARConfigMessage)
    - [ARConfigMessages](#ar-v1-ARConfigMessages)
  
- [ar/v1/assets.proto](#ar_v1_assets-proto)
    - [AssetMessage](#ar-v1-AssetMessage)
    - [AssetMessages](#ar-v1-AssetMessages)
  
    - [AssetDriverType](#ar-v1-AssetDriverType)
    - [AssetType](#ar-v1-AssetType)
  
- [ar/v1/config_load.proto](#ar_v1_config_load-proto)
    - [ConfigurationLoadMessage](#ar-v1-ConfigurationLoadMessage)
  
- [ar/v1/device.proto](#ar_v1_device-proto)
    - [DeviceHeartbeat](#ar-v1-DeviceHeartbeat)
    - [DeviceMessage](#ar-v1-DeviceMessage)
    - [DeviceMessages](#ar-v1-DeviceMessages)
  
    - [DeviceBatteryStatus](#ar-v1-DeviceBatteryStatus)
    - [DeviceStatus](#ar-v1-DeviceStatus)
    - [DeviceType](#ar-v1-DeviceType)
  
- [ar/v1/environment.proto](#ar_v1_environment-proto)
    - [AssetLocation](#ar-v1-AssetLocation)
    - [EnvironmentMessage](#ar-v1-EnvironmentMessage)
    - [EnvironmentMessages](#ar-v1-EnvironmentMessages)
    - [FixtureLocation](#ar-v1-FixtureLocation)
    - [MarkerLocation](#ar-v1-MarkerLocation)
    - [PartLocation](#ar-v1-PartLocation)
    - [RobotLocation](#ar-v1-RobotLocation)
    - [ToolLocation](#ar-v1-ToolLocation)
  
    - [EnvironmentType](#ar-v1-EnvironmentType)
  
- [ar/v1/feedback_info.proto](#ar_v1_feedback_info-proto)
    - [FeedbackInfoMessage](#ar-v1-FeedbackInfoMessage)
    - [FeedbackInfoMessages](#ar-v1-FeedbackInfoMessages)
  
    - [FeedbackGroup](#ar-v1-FeedbackGroup)
  
- [ar/v1/helper_info.proto](#ar_v1_helper_info-proto)
    - [HelperInfoMessage](#ar-v1-HelperInfoMessage)
    - [HelperInfoMessages](#ar-v1-HelperInfoMessages)
  
    - [HelperGroup](#ar-v1-HelperGroup)
  
- [ar/v1/mapping.proto](#ar_v1_mapping-proto)
    - [AssetMapping](#ar-v1-AssetMapping)
    - [MappingMessage](#ar-v1-MappingMessage)
    - [MappingMessages](#ar-v1-MappingMessages)
    - [RobotMapping](#ar-v1-RobotMapping)
  
- [ar/v1/marker.proto](#ar_v1_marker-proto)
    - [MarkerMessage](#ar-v1-MarkerMessage)
    - [MarkerMessages](#ar-v1-MarkerMessages)
  
    - [MarkerType](#ar-v1-MarkerType)
  
- [ar/v1/robot.proto](#ar_v1_robot-proto)
    - [RobotMessage](#ar-v1-RobotMessage)
    - [RobotMessages](#ar-v1-RobotMessages)
  
    - [RobotDriverType](#ar-v1-RobotDriverType)
    - [RobotType](#ar-v1-RobotType)
  
- [ar/v1/worker.proto](#ar_v1_worker-proto)
    - [WorkerMessage](#ar-v1-WorkerMessage)
    - [WorkerMessages](#ar-v1-WorkerMessages)
  
    - [WorkerType](#ar-v1-WorkerType)
  
- [assembly/v1/common.proto](#assembly_v1_common-proto)
    - [CustomProperties](#assembly-v1-CustomProperties)
    - [DisplayText](#assembly-v1-DisplayText)
    - [EstimatedDuration](#assembly-v1-EstimatedDuration)
    - [ExternalReference](#assembly-v1-ExternalReference)
    - [KeyValueConstraint](#assembly-v1-KeyValueConstraint)
    - [LocalTarget](#assembly-v1-LocalTarget)
    - [NamedRef](#assembly-v1-NamedRef)
    - [Ref](#assembly-v1-Ref)
    - [TimeWindow](#assembly-v1-TimeWindow)
  
    - [ActorKind](#assembly-v1-ActorKind)
    - [CollaborationMode](#assembly-v1-CollaborationMode)
    - [ConstraintOperator](#assembly-v1-ConstraintOperator)
    - [ResourceStatus](#assembly-v1-ResourceStatus)
    - [SafetyRelevance](#assembly-v1-SafetyRelevance)
  
- [assembly/v1/actor.proto](#assembly_v1_actor-proto)
    - [ActorAssignment](#assembly-v1-ActorAssignment)
    - [ActorRef](#assembly-v1-ActorRef)
    - [WorkerDefinition](#assembly-v1-WorkerDefinition)
    - [WorkerDefinitions](#assembly-v1-WorkerDefinitions)
  
- [assembly/v1/execution.proto](#assembly_v1_execution-proto)
    - [EvidenceFact](#assembly-v1-EvidenceFact)
    - [ExecutionEvidence](#assembly-v1-ExecutionEvidence)
    - [ProcessRun](#assembly-v1-ProcessRun)
    - [RunParameter](#assembly-v1-RunParameter)
    - [SequenceRun](#assembly-v1-SequenceRun)
    - [TaskRun](#assembly-v1-TaskRun)
    - [VariantSelection](#assembly-v1-VariantSelection)
  
    - [ProcessRunState](#assembly-v1-ProcessRunState)
    - [SequenceRunState](#assembly-v1-SequenceRunState)
    - [TaskRunState](#assembly-v1-TaskRunState)
  
- [assembly/v1/model.proto](#assembly_v1_model-proto)
    - [ModelArtifact](#assembly-v1-ModelArtifact)
    - [ModelArtifacts](#assembly-v1-ModelArtifacts)
  
    - [ModelFormat](#assembly-v1-ModelFormat)
    - [ModelGroup](#assembly-v1-ModelGroup)
    - [ModelOrigin](#assembly-v1-ModelOrigin)
  
- [assembly/v1/product.proto](#assembly_v1_product-proto)
    - [AssemblyNode](#assembly-v1-AssemblyNode)
    - [Dimensions](#assembly-v1-Dimensions)
    - [MaterialSpec](#assembly-v1-MaterialSpec)
    - [PartDefinition](#assembly-v1-PartDefinition)
    - [PartDefinitions](#assembly-v1-PartDefinitions)
    - [PartHandlingProfile](#assembly-v1-PartHandlingProfile)
    - [ProductDefinition](#assembly-v1-ProductDefinition)
    - [ProductDefinitions](#assembly-v1-ProductDefinitions)
    - [VariantCondition](#assembly-v1-VariantCondition)
  
    - [JoinMethod](#assembly-v1-JoinMethod)
    - [NodeKind](#assembly-v1-NodeKind)
    - [PartType](#assembly-v1-PartType)
  
- [assembly/v1/resources.proto](#assembly_v1_resources-proto)
    - [AssetDefinition](#assembly-v1-AssetDefinition)
    - [AssetDefinitions](#assembly-v1-AssetDefinitions)
    - [AssetInstance](#assembly-v1-AssetInstance)
    - [AssetInstances](#assembly-v1-AssetInstances)
    - [CapabilityProfile](#assembly-v1-CapabilityProfile)
    - [FixtureDefinition](#assembly-v1-FixtureDefinition)
    - [FixtureDefinitions](#assembly-v1-FixtureDefinitions)
    - [FixtureInstance](#assembly-v1-FixtureInstance)
    - [FixtureInstances](#assembly-v1-FixtureInstances)
    - [RobotDefinition](#assembly-v1-RobotDefinition)
    - [RobotDefinitions](#assembly-v1-RobotDefinitions)
    - [RobotInstance](#assembly-v1-RobotInstance)
    - [RobotInstances](#assembly-v1-RobotInstances)
    - [ToolDefinition](#assembly-v1-ToolDefinition)
    - [ToolDefinitions](#assembly-v1-ToolDefinitions)
    - [ToolInstance](#assembly-v1-ToolInstance)
    - [ToolInstances](#assembly-v1-ToolInstances)
  
    - [AssetDriverType](#assembly-v1-AssetDriverType)
    - [AssetType](#assembly-v1-AssetType)
    - [FixtureType](#assembly-v1-FixtureType)
    - [RobotDriverType](#assembly-v1-RobotDriverType)
    - [RobotType](#assembly-v1-RobotType)
    - [ToolProperty](#assembly-v1-ToolProperty)
    - [ToolRole](#assembly-v1-ToolRole)
    - [ToolType](#assembly-v1-ToolType)
  
- [assembly/v1/skill.proto](#assembly_v1_skill-proto)
    - [ActorConstraint](#assembly-v1-ActorConstraint)
    - [ActorSkill](#assembly-v1-ActorSkill)
    - [SkillDefinition](#assembly-v1-SkillDefinition)
    - [SkillRequirement](#assembly-v1-SkillRequirement)
    - [ToolRequirement](#assembly-v1-ToolRequirement)
    - [ValidityPolicyRef](#assembly-v1-ValidityPolicyRef)
  
    - [SkillDomain](#assembly-v1-SkillDomain)
    - [SkillLevel](#assembly-v1-SkillLevel)
    - [SkillStatus](#assembly-v1-SkillStatus)
  
- [assembly/v1/process.proto](#assembly_v1_process-proto)
    - [ProcessRecipe](#assembly-v1-ProcessRecipe)
    - [RecipeApplicability](#assembly-v1-RecipeApplicability)
    - [SequenceDefinition](#assembly-v1-SequenceDefinition)
    - [TaskDefinition](#assembly-v1-TaskDefinition)
    - [TaskExecutionPolicy](#assembly-v1-TaskExecutionPolicy)
    - [TaskTarget](#assembly-v1-TaskTarget)
    - [ValidationRequirement](#assembly-v1-ValidationRequirement)
  
    - [ProcessType](#assembly-v1-ProcessType)
    - [SequenceOperator](#assembly-v1-SequenceOperator)
    - [TaskAssignmentPreference](#assembly-v1-TaskAssignmentPreference)
    - [TaskType](#assembly-v1-TaskType)
  
- [assembly/v1/process_requests.proto](#assembly_v1_process_requests-proto)
    - [ProcessLoadRequest](#assembly-v1-ProcessLoadRequest)
    - [ProcessLoadResult](#assembly-v1-ProcessLoadResult)
    - [ProcessRunIssue](#assembly-v1-ProcessRunIssue)
    - [ProcessRunPrecheckResult](#assembly-v1-ProcessRunPrecheckResult)
    - [TaskFeasibility](#assembly-v1-TaskFeasibility)
  
    - [ProcessLoadFailure](#assembly-v1-ProcessLoadFailure)
    - [ProcessLoadStatus](#assembly-v1-ProcessLoadStatus)
    - [ProcessRunIssueSeverity](#assembly-v1-ProcessRunIssueSeverity)
    - [ProcessRunPrecheckStatus](#assembly-v1-ProcessRunPrecheckStatus)
    - [RequirementImportance](#assembly-v1-RequirementImportance)
  
- [assembly/v1/station.proto](#assembly_v1_station-proto)
    - [CellDefinition](#assembly-v1-CellDefinition)
    - [StationDefinition](#assembly-v1-StationDefinition)
  
- [assembly/v1/validation.proto](#assembly_v1_validation-proto)
    - [ValidationResult](#assembly-v1-ValidationResult)
  
    - [ValidationStatus](#assembly-v1-ValidationStatus)
  
- [common/v1/delete.proto](#common_v1_delete-proto)
    - [DeleteMessage](#common-v1-DeleteMessage)
  
- [common/v1/empty.proto](#common_v1_empty-proto)
    - [EmptyMessage](#common-v1-EmptyMessage)
  
- [common/v1/get.proto](#common_v1_get-proto)
    - [GetByIdMessage](#common-v1-GetByIdMessage)
    - [GetMessage](#common-v1-GetMessage)
  
- [geometry/v1/wrench.proto](#geometry_v1_wrench-proto)
    - [Wrench](#geometry-v1-Wrench)
  
- [plm/v1/capability.proto](#plm_v1_capability-proto)
    - [Capabilities](#plm-v1-Capabilities)
    - [Capability](#plm-v1-Capability)
  
- [plm/v1/fixture.proto](#plm_v1_fixture-proto)
    - [FixtureMessage](#plm-v1-FixtureMessage)
    - [FixtureMessages](#plm-v1-FixtureMessages)
  
    - [FixtureType](#plm-v1-FixtureType)
  
- [plm/v1/line.proto](#plm_v1_line-proto)
    - [LineMessage](#plm-v1-LineMessage)
  
    - [LineType](#plm-v1-LineType)
  
- [plm/v1/model_old.proto](#plm_v1_model_old-proto)
    - [ModelMessage](#plm-v1-ModelMessage)
    - [ModelMessages](#plm-v1-ModelMessages)
  
    - [ModelGroup](#plm-v1-ModelGroup)
    - [ModelOrigin](#plm-v1-ModelOrigin)
  
- [plm/v1/part.proto](#plm_v1_part-proto)
    - [PartMessage](#plm-v1-PartMessage)
    - [PartMessages](#plm-v1-PartMessages)
  
    - [PartType](#plm-v1-PartType)
  
- [plm/v1/process_abort.proto](#plm_v1_process_abort-proto)
    - [ProcessAbortMessage](#plm-v1-ProcessAbortMessage)
  
- [plm/v1/sequence.proto](#plm_v1_sequence-proto)
    - [SequenceMessage](#plm-v1-SequenceMessage)
    - [SequenceUpdatedMessage](#plm-v1-SequenceUpdatedMessage)
  
    - [SequenceState](#plm-v1-SequenceState)
  
- [plm/v1/task.proto](#plm_v1_task-proto)
    - [TaskMessage](#plm-v1-TaskMessage)
    - [TaskUpdatedMessage](#plm-v1-TaskUpdatedMessage)
  
    - [TaskAssignmentPreference](#plm-v1-TaskAssignmentPreference)
    - [TaskState](#plm-v1-TaskState)
    - [TaskType](#plm-v1-TaskType)
  
- [plm/v1/process_old.proto](#plm_v1_process_old-proto)
    - [ProcessMessage](#plm-v1-ProcessMessage)
    - [ProcessMessages](#plm-v1-ProcessMessages)
    - [ProcessUpdatedMessage](#plm-v1-ProcessUpdatedMessage)
  
    - [ProcessState](#plm-v1-ProcessState)
    - [ProcessType](#plm-v1-ProcessType)
  
- [plm/v1/process_authoring.proto](#plm_v1_process_authoring-proto)
    - [NewProcessMessage](#plm-v1-NewProcessMessage)
    - [StoredProcessMessage](#plm-v1-StoredProcessMessage)
    - [StoredProcessMessages](#plm-v1-StoredProcessMessages)
    - [UpdateProcessMessage](#plm-v1-UpdateProcessMessage)
  
- [plm/v1/process_load.proto](#plm_v1_process_load-proto)
    - [ProcessLoadMessage](#plm-v1-ProcessLoadMessage)
  
    - [AllocationStrategy](#plm-v1-AllocationStrategy)
  
- [plm/v1/requests.proto](#plm_v1_requests-proto)
    - [ProcessAtLocationMessage](#plm-v1-ProcessAtLocationMessage)
  
- [plm/v1/sequence_authoring.proto](#plm_v1_sequence_authoring-proto)
    - [NewSequenceMessage](#plm-v1-NewSequenceMessage)
    - [StoredSequenceMessage](#plm-v1-StoredSequenceMessage)
    - [StoredSequenceMessages](#plm-v1-StoredSequenceMessages)
    - [UpdateSequenceMessage](#plm-v1-UpdateSequenceMessage)
  
    - [SequenceType](#plm-v1-SequenceType)
  
- [plm/v1/sequence_complete.proto](#plm_v1_sequence_complete-proto)
    - [SequenceBulkCompleteMessage](#plm-v1-SequenceBulkCompleteMessage)
  
- [plm/v1/sequence_reassign.proto](#plm_v1_sequence_reassign-proto)
    - [SequenceReassignMessage](#plm-v1-SequenceReassignMessage)
  
- [plm/v1/task_authoring.proto](#plm_v1_task_authoring-proto)
    - [NewTaskMessage](#plm-v1-NewTaskMessage)
    - [StoredTaskMessage](#plm-v1-StoredTaskMessage)
    - [StoredTaskMessages](#plm-v1-StoredTaskMessages)
    - [UpdateTaskMessage](#plm-v1-UpdateTaskMessage)
  
- [plm/v1/task_progress.proto](#plm_v1_task_progress-proto)
    - [TaskProgressMessage](#plm-v1-TaskProgressMessage)
  
- [plm/v1/task_reassign.proto](#plm_v1_task_reassign-proto)
    - [TaskReassignMessage](#plm-v1-TaskReassignMessage)
  
- [plm/v1/task_state_change.proto](#plm_v1_task_state_change-proto)
    - [TaskStateChangeMessage](#plm-v1-TaskStateChangeMessage)
  
    - [TaskStateRequest](#plm-v1-TaskStateRequest)
  
- [plm/v1/tasks_list.proto](#plm_v1_tasks_list-proto)
    - [TasksForAgentRequest](#plm-v1-TasksForAgentRequest)
    - [TasksForAgentResponse](#plm-v1-TasksForAgentResponse)
  
- [plm/v1/tool.proto](#plm_v1_tool-proto)
    - [ToolMessage](#plm-v1-ToolMessage)
    - [ToolMessages](#plm-v1-ToolMessages)
  
    - [ToolActor](#plm-v1-ToolActor)
    - [ToolProperty](#plm-v1-ToolProperty)
    - [ToolType](#plm-v1-ToolType)
  
- [robot/v1/end_effector.proto](#robot_v1_end_effector-proto)
    - [EndEffectorStateMessage](#robot-v1-EndEffectorStateMessage)
  
- [robot/v1/jointstate.proto](#robot_v1_jointstate-proto)
    - [JointStateMessage](#robot-v1-JointStateMessage)
  
- [robot/v1/path.proto](#robot_v1_path-proto)
    - [PathMessage](#robot-v1-PathMessage)
  
- [robot/v1/popup.proto](#robot_v1_popup-proto)
    - [RobotHidePopupRequest](#robot-v1-RobotHidePopupRequest)
    - [RobotShowPopupRequest](#robot-v1-RobotShowPopupRequest)
  
- [robot/v1/program_state.proto](#robot_v1_program_state-proto)
    - [ProgramStateMessage](#robot-v1-ProgramStateMessage)
  
    - [ProgramState](#robot-v1-ProgramState)
  
- [robot/v1/program_state_request.proto](#robot_v1_program_state_request-proto)
    - [ProgramStateRequest](#robot-v1-ProgramStateRequest)
  
- [robot/v1/robot_state.proto](#robot_v1_robot_state-proto)
    - [RobotStateMessage](#robot-v1-RobotStateMessage)
  
    - [RobotState](#robot-v1-RobotState)
  
- [robot/v1/robot_visibility.proto](#robot_v1_robot_visibility-proto)
    - [RobotVisibilityMessage](#robot-v1-RobotVisibilityMessage)
  
- [robot/v1/tcp.proto](#robot_v1_tcp-proto)
    - [TcpMessage](#robot-v1-TcpMessage)
  
- [robot/v1/waypoints.proto](#robot_v1_waypoints-proto)
    - [WaypointMessage](#robot-v1-WaypointMessage)
    - [WaypointsMessage](#robot-v1-WaypointsMessage)
  
- [robot/v1/zone.proto](#robot_v1_zone-proto)
    - [ZoneMessage](#robot-v1-ZoneMessage)
  
- [service/v1/ar_client.proto](#service_v1_ar_client-proto)
    - [ARClientMessage](#service-v1-ARClientMessage)
  
    - [ARClientRole](#service-v1-ARClientRole)
  
- [service/v1/response.proto](#service_v1_response-proto)
    - [Response](#service-v1-Response)
  
- [service/v1/robot_adapter.proto](#service_v1_robot_adapter-proto)
    - [RobotAdapterInfoMessage](#service-v1-RobotAdapterInfoMessage)
  
- [service/v1/server.proto](#service_v1_server-proto)
    - [ServerHeartbeat](#service-v1-ServerHeartbeat)
    - [ServerInfo](#service-v1-ServerInfo)
  
- [service/v1/status.proto](#service_v1_status-proto)
    - [ServiceStatus](#service-v1-ServiceStatus)
  
    - [Status](#service-v1-Status)
  
- [Scalar Value Types](#scalar-value-types)



<a name="ar_v1_permissions-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/permissions.proto


 


<a name="ar-v1-WorkerPermission"></a>

### WorkerPermission
TODO: Rename to AREditPermission? - what about &#39;automatic&#39; systems?
Consider the mapping, e.g: unspecified, none = nothing, cosmetic = some, full =
User:
- Unspecified: can&#39;t edit any properties
- Basic: can edit {basic} properties
- Cosmetic: can edit {basic, cosmetic} properties
- Full: can edit all editable properties
- None: &lt;not in use?&gt;
Properties:
- Unspecified: can be edited by all?
- Basic: can be edited by users with some permission to edit
- Cosmetic: can be edited by users with cosmetic&#43;full permission
- Full: can be edited by users with full permission
- None: can&#39;t be edited (e.g. outputs or stuff that requires a delete &#43; create new)

TODO: consider the order. It should be possible to use &lt; or &gt; to determine if things are editable (not possible right now when COSMETIC is &#39;in the middle&#39;)

| Name | Number | Description |
| ---- | ------ | ----------- |
| WORKER_PERMISSION_UNSPECIFIED | 0 |  |
| WORKER_PERMISSION_BASIC | 1 |  |
| WORKER_PERMISSION_COSMETIC | 2 |  |
| WORKER_PERMISSION_FULL | 3 |  |
| WORKER_PERMISSION_NONE | 4 |  |


 

 

 



<a name="common_v1_color-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/color.proto



<a name="common-v1-Color"></a>

### Color
Represents a color. Where (255, 255, 255, 255) is solid white, (255, 0, 0, 128) is half transparent red, and so on.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| red | [uint32](#uint32) |  | Ranging from [0:255] |
| green | [uint32](#uint32) |  | Ranging from [0:255] |
| blue | [uint32](#uint32) |  | Ranging from [0:255] |
| alpha | [uint32](#uint32) |  | Ranging from [0:255] --&gt; [transparent : opaque] |





 

 

 

 



<a name="geometry_v1_anchor-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/anchor.proto



<a name="geometry-v1-Anchor"></a>

### Anchor



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reference | [string](#string) |  | Reference point towards an object or a thing, e.g. the environment, a robot, the user, ... |
| frame | [string](#string) |  | Frame is something in relation to the reference, e.g. wrist, tcp, left-hand, ... |





 

 

 

 



<a name="geometry_v1_point-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/point.proto



<a name="geometry-v1-Point"></a>

### Point



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#double) |  |  |
| y | [double](#double) |  |  |
| z | [double](#double) |  |  |





 

 

 

 



<a name="geometry_v1_quad-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/quad.proto



<a name="geometry-v1-Quad"></a>

### Quad



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#double) |  |  |
| y | [double](#double) |  |  |
| z | [double](#double) |  |  |
| w | [double](#double) |  |  |





 

 

 

 



<a name="geometry_v1_pose-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/pose.proto



<a name="geometry-v1-LocalizedPose"></a>

### LocalizedPose
A localized pose with reference to an anchorId. The state and last updated time of the pose can be specified.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| position | [Point](#geometry-v1-Point) |  |  |
| orientation | [Quad](#geometry-v1-Quad) |  |  |
| anchor | [Anchor](#geometry-v1-Anchor) |  |  |
| state | [LocalizedState](#geometry-v1-LocalizedState) |  |  |
| last_updated | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |






<a name="geometry-v1-Pose"></a>

### Pose
A simple pose consisting of a position and orientation


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [Point](#geometry-v1-Point) |  |  |
| orientation | [Quad](#geometry-v1-Quad) |  |  |





 


<a name="geometry-v1-LocalizedState"></a>

### LocalizedState


| Name | Number | Description |
| ---- | ------ | ----------- |
| LOCALIZED_STATE_UNSPECIFIED | 0 |  |
| LOCALIZED_STATE_FOUND | 1 |  |
| LOCALIZED_STATE_LOST | 2 |  |
| LOCALIZED_STATE_STATIC | 3 |  |


 

 

 



<a name="geometry_v1_vector3-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/vector3.proto



<a name="geometry-v1-Vector3"></a>

### Vector3



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [float](#float) |  |  |
| y | [float](#float) |  |  |
| z | [float](#float) |  |  |





 

 

 

 



<a name="validation_v1_predefined_string_rules-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## validation/v1/predefined_string_rules.proto


 

 


<a name="validation_v1_predefined_string_rules-proto-extensions"></a>

### File-level Extensions
| Extension | Type | Base | Number | Description |
| --------- | ---- | ---- | ------ | ----------- |
| ar_config_id_component | bool | .buf.validate.StringRules | 10002 |  |
| asset_id_component | bool | .buf.validate.StringRules | 10005 |  |
| environment_id_component | bool | .buf.validate.StringRules | 10006 |  |
| fixture_id_component | bool | .buf.validate.StringRules | 10010 |  |
| marker_id_component | bool | .buf.validate.StringRules | 10009 |  |
| model_id_component | bool | .buf.validate.StringRules | 10001 |  |
| name_component | bool | .buf.validate.StringRules | 10000 |  |
| part_id_component | bool | .buf.validate.StringRules | 10007 |  |
| property_id_component | bool | .buf.validate.StringRules | 10003 |  |
| robot_id_component | bool | .buf.validate.StringRules | 10004 |  |
| tool_id_component | bool | .buf.validate.StringRules | 10008 |  |

 

 



<a name="ar_v1_property-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/property.proto



<a name="ar-v1-AnchorExtras"></a>

### AnchorExtras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| only_markers | [bool](#bool) |  |  |






<a name="ar-v1-ColorExtras"></a>

### ColorExtras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| step | [double](#double) |  |  |
| default | [common.v1.Color](#common-v1-Color) |  | TODO: allow user-preference override |






<a name="ar-v1-EnumExtras"></a>

### EnumExtras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| placeholder | [string](#string) |  | Placeholder value shown in UI when no enum is selected |
| filter | [bool](#bool) |  | Show filter input |
| grouped | [bool](#bool) |  | If options should be grouped |
| show_icons | [bool](#bool) |  | If options have icons and these should be shown |
| max_selected_labels | [uint32](#uint32) |  | Only relevant for MultiSelect: limits number of selected labels |
| options | [EnumOption](#ar-v1-EnumOption) | repeated |  |






<a name="ar-v1-EnumOption"></a>

### EnumOption



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [string](#string) |  |  |
| label | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| group | [string](#string) |  |  |
| disabled | [bool](#bool) |  |  |






<a name="ar-v1-NumberExtras"></a>

### NumberExtras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min | [double](#double) | optional |  |
| max | [double](#double) | optional |  |
| step | [double](#double) | optional |  |
| unit | [string](#string) |  | &#34;mm&#34;, &#34;deg&#34;, &#34;N&#34; |
| precision | [uint32](#uint32) |  | Decimal places for display |






<a name="ar-v1-PoseExtras"></a>

### PoseExtras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| anchor_editable | [bool](#bool) |  |  |
| pose_editable | [bool](#bool) |  |  |






<a name="ar-v1-Property"></a>

### Property
Properties are used by various components to define them, such as: feedback, actions, and conditions.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [PropertyType](#ar-v1-PropertyType) |  |  |
| minimum_required_permission | [WorkerPermission](#ar-v1-WorkerPermission) |  |  |
| origin | [PropertyOrigin](#ar-v1-PropertyOrigin) |  |  |
| origins | [PropertyOrigin](#ar-v1-PropertyOrigin) | repeated |  |
| mirror_property_id | [string](#string) |  |  |
| group | [PropertyGroup](#ar-v1-PropertyGroup) |  |  |
| ordering | [int32](#int32) |  |  |
| hide_group | [bool](#bool) |  |  |
| parent_id | [string](#string) |  |  |
| advanced | [bool](#bool) |  | Hide behind &#34;Advanced&#34; toogle |
| scope_id | [string](#string) |  |  |
| disable_mirroring | [bool](#bool) |  | If true, this property is not allowed to be mirrored by other properties |
| bool_value | [bool](#bool) | optional |  |
| int_value | [sint64](#sint64) | optional |  |
| float_value | [float](#float) | optional |  |
| double_value | [double](#double) | optional |  |
| string_value | [string](#string) | optional |  |
| vector3_value | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| pose_value | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| anchor_value | [geometry.v1.Anchor](#geometry-v1-Anchor) |  |  |
| color_value | [common.v1.Color](#common-v1-Color) |  |  |
| robot_id_value | [string](#string) | optional |  |
| enum_value | [string](#string) | optional |  |
| enum_multi_value | [string](#string) | repeated |  |
| icon_value | [string](#string) | optional |  |
| asset_id_value | [string](#string) | optional |  |
| number_extras | [NumberExtras](#ar-v1-NumberExtras) |  |  |
| enum_extras | [EnumExtras](#ar-v1-EnumExtras) |  |  |
| vector3_extras | [Vector3Extras](#ar-v1-Vector3Extras) |  |  |
| color_extras | [ColorExtras](#ar-v1-ColorExtras) |  |  |
| pose_extras | [PoseExtras](#ar-v1-PoseExtras) |  |  |
| anchor_extras | [AnchorExtras](#ar-v1-AnchorExtras) |  |  |






<a name="ar-v1-PropertyMessages"></a>

### PropertyMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| properties | [Property](#ar-v1-Property) | repeated |  |






<a name="ar-v1-PropertyValueUpdate"></a>

### PropertyValueUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| type | [PropertyType](#ar-v1-PropertyType) |  |  |
| origin | [PropertyOrigin](#ar-v1-PropertyOrigin) |  |  |
| mirror_property_id | [string](#string) |  |  |
| bool_value | [bool](#bool) | optional |  |
| int_value | [sint64](#sint64) | optional |  |
| float_value | [float](#float) | optional |  |
| double_value | [double](#double) | optional |  |
| string_value | [string](#string) | optional |  |
| vector3_value | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| pose_value | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| anchor_value | [geometry.v1.Anchor](#geometry-v1-Anchor) |  |  |
| color_value | [common.v1.Color](#common-v1-Color) |  |  |
| robot_id_value | [string](#string) | optional |  |
| enum_value | [string](#string) | optional |  |
| enum_multi_value | [string](#string) | repeated |  |
| icon_value | [string](#string) | optional |  |
| asset_id_value | [string](#string) | optional |  |






<a name="ar-v1-Vector3Extras"></a>

### Vector3Extras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min | [double](#double) | optional |  |
| max | [double](#double) | optional |  |
| step | [double](#double) | optional |  |
| label_x | [string](#string) |  |  |
| label_y | [string](#string) |  |  |
| label_z | [string](#string) |  |  |
| unit | [string](#string) |  |  |





 


<a name="ar-v1-PropertyGroup"></a>

### PropertyGroup


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROPERTY_GROUP_UNSPECIFIED | 0 |  |
| PROPERTY_GROUP_OUTPUT | 1 |  |
| PROPERTY_GROUP_NON_EDITABLE | 2 |  |
| PROPERTY_GROUP_STYLING | 3 |  |
| PROPERTY_GROUP_LOCATION | 4 |  |
| PROPERTY_GROUP_ICON | 5 |  |
| PROPERTY_GROUP_CONFIGURATION | 6 |  |
| PROPERTY_GROUP_HIDDEN | 7 |  |



<a name="ar-v1-PropertyOrigin"></a>

### PropertyOrigin
Specifies where the value of a property originates from.

| Name | Number | Description |
| ---- | ------ | ----------- |
| PROPERTY_ORIGIN_UNSPECIFIED | 0 |  |
| PROPERTY_ORIGIN_FIXED | 1 | The value of the property is fixed and must be changed manually |
| PROPERTY_ORIGIN_MIRROR | 2 | The value of the property mirrors the value of another property |



<a name="ar-v1-PropertyType"></a>

### PropertyType
Used to specify the type of a property

| Name | Number | Description |
| ---- | ------ | ----------- |
| PROPERTY_TYPE_UNSPECIFIED | 0 |  |
| PROPERTY_TYPE_BOOL | 1 | Bool type property (true/false) |
| PROPERTY_TYPE_INT | 2 | Int type property |
| PROPERTY_TYPE_FLOAT | 3 | Float type property |
| PROPERTY_TYPE_DOUBLE | 4 | Double type property |
| PROPERTY_TYPE_STRING | 5 | String type property |
| PROPERTY_TYPE_VECTOR3 | 6 | Vector3 type property - {x, y, z} |
| PROPERTY_TYPE_POSE | 7 | Pose type property - LocalizedPose(id, anchor, position, orientation, state, ...) |
| PROPERTY_TYPE_ANCHOR | 8 | Anchor type property - Anchor(reference, frame) |
| PROPERTY_TYPE_COLOR | 9 | Color type property - Color(r,g,b,a) |
| PROPERTY_TYPE_ROBOT | 10 | Robot type property - robot_id as string |
| PROPERTY_TYPE_ENUM | 11 | Enum type property - string from list of strings (defined in EnumExtras) |
| PROPERTY_TYPE_ENUM_MULTI | 12 | Enum-multi type property - select multiple strings from list of strings (defined in EnumExtras) |
| PROPERTY_TYPE_ICON | 13 | Icon property type - icon-name-something from https://pictogrammers.com/ |
| PROPERTY_TYPE_ASSET | 14 | Asset type property - asset_id as string |


 

 

 



<a name="ar_v1_action-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/action.proto



<a name="ar-v1-ActionAddMessage"></a>

### ActionAddMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| config_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ActionType](#ar-v1-ActionType) |  |  |
| agent_id | [string](#string) |  |  |
| activating_property_id | [string](#string) |  |  |






<a name="ar-v1-ActionCloneMessage"></a>

### ActionCloneMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| original_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |






<a name="ar-v1-ActionMessage"></a>

### ActionMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ActionType](#ar-v1-ActionType) |  |  |
| properties | [Property](#ar-v1-Property) | repeated |  |
| config_id | [string](#string) |  |  |






<a name="ar-v1-ActionMessages"></a>

### ActionMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| actions | [ActionMessage](#ar-v1-ActionMessage) | repeated |  |






<a name="ar-v1-ActionUpdateMessage"></a>

### ActionUpdateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |





 


<a name="ar-v1-ActionType"></a>

### ActionType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ACTION_TYPE_UNSPECIFIED | 0 |  |
| ACTION_TYPE_TASK_COMPLETE | 10 |  |
| ACTION_TYPE_TASK_UNDO | 11 |  |
| ACTION_TYPE_TASK_ASSIGN | 12 |  |
| ACTION_TYPE_TASK_HIGHLIGHT | 13 |  |
| ACTION_TYPE_TASK_HELP | 14 |  |
| ACTION_TYPE_ROBOT_PLAY_PAUSE | 50 |  |
| ACTION_TYPE_ROBOT_ACKNOWLEDGE | 51 |  |
| ACTION_TYPE_ROBOT_FREE_DRIVE | 52 |  |
| ACTION_TYPE_ROBOT_COLLABORATE | 53 |  |


 

 

 



<a name="ar_v1_events-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/events.proto



<a name="ar-v1-ExchangeSupport"></a>

### ExchangeSupport



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| message | [ExchangeType](#ar-v1-ExchangeType) |  |  |
| rationale | [string](#string) |  | optional but super helpful for UI |






<a name="ar-v1-ExchangeType"></a>

### ExchangeType
ExchangeType represent a single &#39;event&#39; or exchange.

Example: robot motion
1) UI produces: { Command: ROBOT_START_STOP }
2) Planner produces: { Plan: ROBOT_PATH }
3) Driver publishes: { Telemetry: ROBOT_TCP }
4) System emits: { Event: ROBOT_STARTED_TASK }


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command | [CommandType](#ar-v1-CommandType) |  | Requested intent (future) |
| event | [EventType](#ar-v1-EventType) |  | Confirmed fact (past) |
| telemetry | [TelemetryType](#ar-v1-TelemetryType) |  | Observed state (now) |
| plan | [PlanType](#ar-v1-PlanType) |  | Planned intent (future) |






<a name="ar-v1-HandlerRequirement"></a>

### HandlerRequirement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| message | [ExchangeType](#ar-v1-ExchangeType) |  |  |
| cardinality | [HandlerCardinality](#ar-v1-HandlerCardinality) |  |  |
| rationale | [string](#string) |  | optional but super helpful for UI |






<a name="ar-v1-SupportedExchangesMessage"></a>

### SupportedExchangesMessage
Supported events is a list of all supported events in the current configuration
TODO: should this be a field of ARConfig?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| exchanges | [ExchangeSupport](#ar-v1-ExchangeSupport) | repeated |  |





 


<a name="ar-v1-CommandType"></a>

### CommandType
Commands are intents, i.e. &#34;please do this&#34;. Example: Start/STOP from UI -&gt; Robot driver

| Name | Number | Description |
| ---- | ------ | ----------- |
| COMMAND_TYPE_UNSPECIFIED | 0 |  |
| COMMAND_TYPE_TASK_COMPLETE | 10 | Workflow/UI intent |
| COMMAND_TYPE_TASK_ASSIGN | 11 |  |
| COMMAND_TYPE_TASK_UNDO | 12 |  |
| COMMAND_TYPE_TASK_HIGHLIGHT | 13 |  |
| COMMAND_TYPE_TASK_HELP | 14 |  |
| COMMAND_TYPE_ROBOT_START_STOP | 100 | Robot control intent |
| COMMAND_TYPE_ROBOT_TOGGLE_FREE_DRIVE | 101 |  |
| COMMAND_TYPE_ROBOT_START_COLLABORATION | 102 |  |
| COMMAND_TYPE_ROBOT_STOP_COLLABORATION | 103 |  |
| COMMAND_TYPE_ROBOT_ACKNOWLEDGE | 104 |  |



<a name="ar-v1-EventType"></a>

### EventType
EventType: events are facts, i.e. &#34;this just happened&#34;.

It is intended for low-frequency events. One example could be WAYPOINT_REACHED contrary to TELEMETRY_ROBOT_TCP
Events must be grounded in actual events and not just because &#34;a prediction said so&#34;.

| Name | Number | Description |
| ---- | ------ | ----------- |
| EVENT_TYPE_UNSPECIFIED | 0 |  |
| EVENT_TYPE_PROCESS_COMPLETE | 10 | Workflow facts |
| EVENT_TYPE_SEQUENCE_COMPLETE | 11 |  |
| EVENT_TYPE_TASK_COMPLETE | 12 |  |
| EVENT_TYPE_ROBOT_WAYPOINT_REACHED | 100 |  |
| EVENT_TYPE_ROBOT_PLAN_STARTED | 130 |  |
| EVENT_TYPE_ROBOT_PLAN_CHANGED | 131 |  |
| EVENT_TYPE_ROBOT_PLAN_ABORTED | 132 |  |
| EVENT_TYPE_ROBOT_PLAN_COMPLETED | 133 |  |
| EVENT_TYPE_ROBOT_WAITING_FOR_ACKNOWLEDGE | 150 |  |
| EVENT_TYPE_ROBOT_WAITING_FOR_HELP | 151 |  |
| EVENT_TYPE_ROBOT_WAITING_TASK_RELEASE | 152 |  |



<a name="ar-v1-HandlerCardinality"></a>

### HandlerCardinality


| Name | Number | Description |
| ---- | ------ | ----------- |
| HANDLER_CARDINALITY_UNSPECIFIED | 0 |  |
| HANDLER_CARDINALITY_AT_LEAST_ONE | 1 |  |
| HANDLER_CARDINALITY_EXACTLY_ONE | 2 |  |
| HANDLER_CARDINALITY_AT_MOST_ONE | 3 |  |



<a name="ar-v1-PlanType"></a>

### PlanType
Plan is planned (or expected) future state.

| Name | Number | Description |
| ---- | ------ | ----------- |
| PLAN_TYPE_UNSPECIFIED | 0 |  |
| PLAN_TYPE_ROBOT_PATH | 100 | Planned path for the robot&#39;s next action(s) |
| PLAN_TYPE_ROBOT_JOINT_ANGLES | 101 | Planned joint angles for the robot&#39;s next action(s) |
| PLAN_TYPE_ROBOT_WAYPOINTS | 102 | Planned waypoints for the robot&#39;s next action(s) |
| PLAN_TYPE_ROBOT_ESTIMATED_COMPLETION | 123 |  |
| PLAN_TYPE_ROBOT_TASK_SEQUENCE | 124 |  |
| PLAN_TYPE_TASK_SEQUENCE | 200 |  |



<a name="ar-v1-TelemetryType"></a>

### TelemetryType
TelemetryType: telemetry is current state, i.e. &#34;here is my state&#34;
It is expected to be high-frequency updates or at least updates every time the state have changed

| Name | Number | Description |
| ---- | ------ | ----------- |
| TELEMETRY_TYPE_UNSPECIFIED | 0 |  |
| TELEMETRY_TYPE_ROBOT_TCP | 100 | Current TCP for the robot |
| TELEMETRY_TYPE_ROBOT_JOINT_ANGLES | 101 | Current joint angles for the robot |
| TELEMETRY_TYPE_ROBOT_FORCE_TORQUE | 102 | Current measured force/torque values |
| TELEMETRY_TYPE_ROBOT_STATE | 110 | Current robot state. Check robot.v1.robot_state.proto for actual values. |


 

 

 



<a name="ar_v1_action_info-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/action_info.proto



<a name="ar-v1-ActionInfoMessage"></a>

### ActionInfoMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ActionType](#ar-v1-ActionType) |  |  |
| group | [ActionGroup](#ar-v1-ActionGroup) |  |  |
| require_agent | [bool](#bool) |  |  |
| consumers_required | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs the action expects to receive |
| consumers_optional | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs that will enhance the action, but not needed to function |
| required_handlers | [HandlerRequirement](#ar-v1-HandlerRequirement) | repeated | Events that MUST have at least one handler somewhere else in the system. (i.e., if the action emits these, it expects the environment to react) |
| emits | [ExchangeType](#ar-v1-ExchangeType) | repeated | Outputs the action publishes |
| disabled | [bool](#bool) |  |  |






<a name="ar-v1-ActionInfoMessages"></a>

### ActionInfoMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| infos | [ActionInfoMessage](#ar-v1-ActionInfoMessage) | repeated |  |





 


<a name="ar-v1-ActionGroup"></a>

### ActionGroup


| Name | Number | Description |
| ---- | ------ | ----------- |
| ACTION_GROUP_UNSPECIFIED | 0 |  |
| ACTION_GROUP_GENERAL | 1 |  |
| ACTION_GROUP_ROBOT | 2 |  |
| ACTION_GROUP_TASK | 3 |  |


 

 

 



<a name="ar_v1_feedback-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/feedback.proto



<a name="ar-v1-FeedbackAddMessage"></a>

### FeedbackAddMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| config_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [FeedbackType](#ar-v1-FeedbackType) |  |  |
| robot_id | [string](#string) |  |  |
| anchor | [geometry.v1.Anchor](#geometry-v1-Anchor) |  |  |






<a name="ar-v1-FeedbackCloneMessage"></a>

### FeedbackCloneMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| original_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |






<a name="ar-v1-FeedbackMessage"></a>

### FeedbackMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [FeedbackType](#ar-v1-FeedbackType) |  |  |
| properties | [Property](#ar-v1-Property) | repeated |  |
| config_id | [string](#string) |  | repeated string property_ids = 6 [ (buf.validate.field).repeated.items.string.(.validation.v1.property_id_component) = true, (buf.validate.field).repeated.unique = true ]; |






<a name="ar-v1-FeedbackMessages"></a>

### FeedbackMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| feedbacks | [FeedbackMessage](#ar-v1-FeedbackMessage) | repeated |  |






<a name="ar-v1-FeedbackUpdateMessage"></a>

### FeedbackUpdateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |





 


<a name="ar-v1-FeedbackType"></a>

### FeedbackType


| Name | Number | Description |
| ---- | ------ | ----------- |
| FEEDBACK_TYPE_UNSPECIFIED | 0 |  |
| FEEDBACK_TYPE_TASK_HIGHLIGHT | 10 |  |
| FEEDBACK_TYPE_TASK_PART_HIGHLIGHT | 11 |  |
| FEEDBACK_TYPE_TASK_TOOL_HIGHLIGHT | 12 |  |
| FEEDBACK_TYPE_TASK_OVERVIEW | 13 | Provides an overview of all current tasks |
| FEEDBACK_TYPE_TASK_INSTRUCTION | 14 | Provide instructions of the current task |
| FEEDBACK_TYPE_TASK_CHECKLIST | 15 | Tailored towards tasks that are more checklist oriented than assembly |
| FEEDBACK_TYPE_ROBOT_PATH | 50 | Show the expected path of the robot |
| FEEDBACK_TYPE_ROBOT_SILHOUETTE | 51 |  |
| FEEDBACK_TYPE_ROBOT_WAYPOINTS | 52 |  |
| FEEDBACK_TYPE_ROBOT_STATUS | 53 |  |
| FEEDBACK_TYPE_ROBOT_LIGHT | 54 |  |
| FEEDBACK_TYPE_MESSAGE | 100 |  |
| FEEDBACK_TYPE_ICON | 101 |  |
| FEEDBACK_TYPE_ZONE | 102 |  |
| FEEDBACK_TYPE_PLAY_SOUND | 103 |  |
| FEEDBACK_TYPE_RULER | 104 |  |
| FEEDBACK_TYPE_HIGHLIGHT | 105 |  |


 

 

 



<a name="ar_v1_helper-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/helper.proto



<a name="ar-v1-HelperAddMessage"></a>

### HelperAddMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| config_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [HelperType](#ar-v1-HelperType) |  |  |






<a name="ar-v1-HelperMessage"></a>

### HelperMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [HelperType](#ar-v1-HelperType) |  |  |
| properties | [Property](#ar-v1-Property) | repeated |  |






<a name="ar-v1-HelperMessages"></a>

### HelperMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| helpers | [HelperMessage](#ar-v1-HelperMessage) | repeated |  |






<a name="ar-v1-HelperUpdateMessage"></a>

### HelperUpdateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |





 


<a name="ar-v1-HelperType"></a>

### HelperType


| Name | Number | Description |
| ---- | ------ | ----------- |
| HELPER_TYPE_UNSPECIFIED | 0 |  |
| HELPER_TYPE_PROXIMITY | 10 |  |
| HELPER_TYPE_STATIONARY | 11 |  |
| HELPER_TYPE_TIMER | 21 |  |
| HELPER_TYPE_AND | 100 |  |
| HELPER_TYPE_OR | 101 |  |
| HELPER_TYPE_NOT | 102 |  |


 

 

 



<a name="ar_v1_ar_config-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/ar_config.proto



<a name="ar-v1-ARConfigInfoMessage"></a>

### ARConfigInfoMessage
Just delete this?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |






<a name="ar-v1-ARConfigInfoMessages"></a>

### ARConfigInfoMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| infos | [ARConfigInfoMessage](#ar-v1-ARConfigInfoMessage) | repeated |  |






<a name="ar-v1-ARConfigMessage"></a>

### ARConfigMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| feedback | [FeedbackMessage](#ar-v1-FeedbackMessage) | repeated | TODO: just a list of Id&#39;s? |
| actions | [ActionMessage](#ar-v1-ActionMessage) | repeated |  |
| helpers | [HelperMessage](#ar-v1-HelperMessage) | repeated |  |
| properties | [Property](#ar-v1-Property) | repeated |  |
| ar_disappear_distance | [int64](#int64) |  | Threshold distance in cm all AR elements should disappear. 0 = ignored |






<a name="ar-v1-ARConfigMessages"></a>

### ARConfigMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| configs | [ARConfigMessage](#ar-v1-ARConfigMessage) | repeated |  |





 

 

 

 



<a name="ar_v1_assets-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/assets.proto



<a name="ar-v1-AssetMessage"></a>

### AssetMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  | Name of the asset |
| icon | [string](#string) |  | Optional icon representing the asset |
| description | [string](#string) |  | Optional description of the asset |
| type | [AssetType](#ar-v1-AssetType) |  |  |
| asset_driver_type | [AssetDriverType](#ar-v1-AssetDriverType) |  |  |
| properties | [Property](#ar-v1-Property) | repeated |  |






<a name="ar-v1-AssetMessages"></a>

### AssetMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| assets | [AssetMessage](#ar-v1-AssetMessage) | repeated |  |





 


<a name="ar-v1-AssetDriverType"></a>

### AssetDriverType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ASSET_DRIVER_TYPE_UNSPECIFIED | 0 |  |
| ASSET_DRIVER_TYPE_DEFAULT | 1 |  |



<a name="ar-v1-AssetType"></a>

### AssetType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ASSET_TYPE_UNSPECIFIED | 0 |  |
| ASSET_TYPE_CAMERA | 1 |  |
| ASSET_TYPE_LIGHT | 2 |  |
| ASSET_TYPE_CONVEYOR | 3 |  |


 

 

 



<a name="ar_v1_config_load-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/config_load.proto



<a name="ar-v1-ConfigurationLoadMessage"></a>

### ConfigurationLoadMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| config_id | [string](#string) |  | Id of the configuration to be loaded |
| instance_id | [string](#string) |  | Instance id of the current loaded configuration - from the requestors perspective - used to avoid reloading a configuration. |





 

 

 

 



<a name="ar_v1_device-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/device.proto



<a name="ar-v1-DeviceHeartbeat"></a>

### DeviceHeartbeat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| device_id | [string](#string) |  |  |
| battery_level | [int32](#int32) |  |  |
| battery_status | [DeviceBatteryStatus](#ar-v1-DeviceBatteryStatus) |  |  |






<a name="ar-v1-DeviceMessage"></a>

### DeviceMessage
DeviceMessage hold basic information about AR-devices, such as a HoloLens2


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [DeviceType](#ar-v1-DeviceType) |  |  |
| device_id | [string](#string) |  |  |
| status | [DeviceStatus](#ar-v1-DeviceStatus) |  |  |
| battery_level | [int32](#int32) |  |  |
| battery_status | [DeviceBatteryStatus](#ar-v1-DeviceBatteryStatus) |  |  |






<a name="ar-v1-DeviceMessages"></a>

### DeviceMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| devices | [DeviceMessage](#ar-v1-DeviceMessage) | repeated |  |





 


<a name="ar-v1-DeviceBatteryStatus"></a>

### DeviceBatteryStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| DEVICE_BATTERY_STATUS_UNSPECIFIED | 0 | The device&#39;s battery status cannot be determined. If battery status is not available on your target platform, SystemInfo.batteryStatus will return this value. |
| DEVICE_BATTERY_STATUS_CHARGING | 1 | Device is plugged in and charging. |
| DEVICE_BATTERY_STATUS_DISCHARGING | 2 | Device is unplugged and discharging. |
| DEVICE_BATTERY_STATUS_NOT_CHARGING | 3 | Device is plugged in, but is not charging. |
| DEVICE_BATTERY_STATUS_FULL | 4 | Device is plugged in and the battery is full. |



<a name="ar-v1-DeviceStatus"></a>

### DeviceStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| DEVICE_STATUS_UNSPECIFIED | 0 |  |
| DEVICE_STATUS_ONLINE | 1 |  |
| DEVICE_STATUS_OFFLINE | 2 |  |



<a name="ar-v1-DeviceType"></a>

### DeviceType


| Name | Number | Description |
| ---- | ------ | ----------- |
| DEVICE_TYPE_UNSPECIFIED | 0 |  |
| DEVICE_TYPE_HOLOLENS2 | 1 |  |
| DEVICE_TYPE_PHONE | 2 |  |
| DEVICE_TYPE_TABLET | 3 |  |
| DEVICE_TYPE_PC | 4 |  |


 

 

 



<a name="ar_v1_environment-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/environment.proto



<a name="ar-v1-AssetLocation"></a>

### AssetLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |






<a name="ar-v1-EnvironmentMessage"></a>

### EnvironmentMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [EnvironmentType](#ar-v1-EnvironmentType) |  | Type of environment |
| markers | [MarkerLocation](#ar-v1-MarkerLocation) | repeated | Markers associated with this environment. |
| robots | [RobotLocation](#ar-v1-RobotLocation) | repeated | Robot located in this environment |
| assets | [AssetLocation](#ar-v1-AssetLocation) | repeated | Assets located in this environment |
| parts | [PartLocation](#ar-v1-PartLocation) | repeated | Parts located in this environment |
| tools | [ToolLocation](#ar-v1-ToolLocation) | repeated | Tools located in this environment |
| fixtures | [FixtureLocation](#ar-v1-FixtureLocation) | repeated | Fixtures located in this environment |






<a name="ar-v1-EnvironmentMessages"></a>

### EnvironmentMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| environments | [EnvironmentMessage](#ar-v1-EnvironmentMessage) | repeated |  |






<a name="ar-v1-FixtureLocation"></a>

### FixtureLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |






<a name="ar-v1-MarkerLocation"></a>

### MarkerLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |






<a name="ar-v1-PartLocation"></a>

### PartLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |






<a name="ar-v1-RobotLocation"></a>

### RobotLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |






<a name="ar-v1-ToolLocation"></a>

### ToolLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |





 


<a name="ar-v1-EnvironmentType"></a>

### EnvironmentType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ENVIRONMENT_TYPE_UNSPECIFIED | 0 |  |
| ENVIRONMENT_TYPE_STORAGE | 1 |  |
| ENVIRONMENT_TYPE_MANUAL_STATION | 2 |  |
| ENVIRONMENT_TYPE_AUTOMATIC_STATION | 3 |  |
| ENVIRONMENT_TYPE_HYBRID_STATION | 4 |  |
| ENVIRONMENT_TYPE_MANUAL_LINE | 5 |  |
| ENVIRONMENT_TYPE_AUTOMATIC_LINE | 6 |  |
| ENVIRONMENT_TYPE_HYBRID_LINE | 7 |  |


 

 

 



<a name="ar_v1_feedback_info-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/feedback_info.proto



<a name="ar-v1-FeedbackInfoMessage"></a>

### FeedbackInfoMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [FeedbackType](#ar-v1-FeedbackType) |  |  |
| group | [FeedbackGroup](#ar-v1-FeedbackGroup) |  |  |
| require_agent | [bool](#bool) |  |  |
| require_frame | [bool](#bool) |  |  |
| consumers_required | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs the feedback expects to receive |
| consumers_optional | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs that will enhance the feedback, but not needed to function |
| required_handlers | [HandlerRequirement](#ar-v1-HandlerRequirement) | repeated | Events that MUST have at least one handler somewhere else in the system. (i.e., if the feedback emits these, it expects the environment to react) |
| emits | [ExchangeType](#ar-v1-ExchangeType) | repeated | Outputs the feedback publishes |
| disabled | [bool](#bool) |  |  |






<a name="ar-v1-FeedbackInfoMessages"></a>

### FeedbackInfoMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| infos | [FeedbackInfoMessage](#ar-v1-FeedbackInfoMessage) | repeated |  |





 


<a name="ar-v1-FeedbackGroup"></a>

### FeedbackGroup


| Name | Number | Description |
| ---- | ------ | ----------- |
| FEEDBACK_GROUP_UNSPECIFIED | 0 |  |
| FEEDBACK_GROUP_GENERAL | 1 |  |
| FEEDBACK_GROUP_ROBOT | 2 |  |
| FEEDBACK_GROUP_TASK | 3 |  |
| FEEDBACK_GROUP_ENVIRONMENT | 4 |  |


 

 

 



<a name="ar_v1_helper_info-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/helper_info.proto



<a name="ar-v1-HelperInfoMessage"></a>

### HelperInfoMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [HelperType](#ar-v1-HelperType) |  |  |
| group | [HelperGroup](#ar-v1-HelperGroup) |  |  |
| require_agent | [bool](#bool) |  |  |
| require_frame | [bool](#bool) |  |  |
| consumers_required | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs the action expects to receive |
| consumers_optional | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs that will enhance the action, but not needed to function |
| required_handlers | [HandlerRequirement](#ar-v1-HandlerRequirement) | repeated | Events that MUST have at least one handler somewhere else in the system. (i.e., if the action emits these, it expects the environment to react) |
| emits | [ExchangeType](#ar-v1-ExchangeType) | repeated | Outputs the feedback publishes |
| disabled | [bool](#bool) |  |  |






<a name="ar-v1-HelperInfoMessages"></a>

### HelperInfoMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| infos | [HelperInfoMessage](#ar-v1-HelperInfoMessage) | repeated |  |





 


<a name="ar-v1-HelperGroup"></a>

### HelperGroup


| Name | Number | Description |
| ---- | ------ | ----------- |
| HELPER_GROUP_UNSPECIFIED | 0 |  |
| HELPER_GROUP_GENERAL | 1 |  |
| HELPER_GROUP_ROBOT | 2 |  |
| HELPER_GROUP_TASK | 3 |  |
| HELPER_GROUP_ENVIRONMENT | 4 |  |
| HELPER_GROUP_OPERATOR | 5 |  |
| HELPER_GROUP_SPATIAL | 6 |  |
| HELPER_GROUP_LOGIC | 7 |  |


 

 

 



<a name="ar_v1_mapping-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/mapping.proto



<a name="ar-v1-AssetMapping"></a>

### AssetMapping



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| asset_id | [string](#string) |  |  |
| property_id | [string](#string) |  |  |






<a name="ar-v1-MappingMessage"></a>

### MappingMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| environment_id | [string](#string) |  |  |
| ar_config_id | [string](#string) |  |  |
| disabled | [bool](#bool) |  |  |
| robot_mapping | [RobotMapping](#ar-v1-RobotMapping) | repeated |  |
| asset_mapping | [AssetMapping](#ar-v1-AssetMapping) | repeated |  |
| standalone | [bool](#bool) |  | Only this AR-config should be shown (winner have highest priority) |
| priority | [int32](#int32) |  | High value configs will be shown first |






<a name="ar-v1-MappingMessages"></a>

### MappingMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mappings | [MappingMessage](#ar-v1-MappingMessage) | repeated |  |






<a name="ar-v1-RobotMapping"></a>

### RobotMapping



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| property_id | [string](#string) |  |  |





 

 

 

 



<a name="ar_v1_marker-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/marker.proto



<a name="ar-v1-MarkerMessage"></a>

### MarkerMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| marker_text | [string](#string) |  | Text on the physical marker (QR-code) |
| type | [MarkerType](#ar-v1-MarkerType) |  |  |
| confirm_instantiate | [bool](#bool) |  | If true, the user must confirm that he/she want to instantiate the environment(s) associated with this marker. |






<a name="ar-v1-MarkerMessages"></a>

### MarkerMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| markers | [MarkerMessage](#ar-v1-MarkerMessage) | repeated |  |





 


<a name="ar-v1-MarkerType"></a>

### MarkerType


| Name | Number | Description |
| ---- | ------ | ----------- |
| MARKER_TYPE_UNSPECIFIED | 0 |  |
| MARKER_TYPE_QR_CODE | 1 |  |


 

 

 



<a name="ar_v1_robot-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/robot.proto



<a name="ar-v1-RobotMessage"></a>

### RobotMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  | Autogenerated id |
| name | [string](#string) |  | Name of the robot |
| icon | [string](#string) |  | Optional icon representing the robot |
| description | [string](#string) |  | Optional description of the robot |
| type | [RobotType](#ar-v1-RobotType) |  | Required type of robot |
| robot_driver_type | [RobotDriverType](#ar-v1-RobotDriverType) |  | Required driver type for robot |
| coupler_model_id | [string](#string) |  | Optional coupler model |
| end_effector_model_id | [string](#string) |  | Optional end-effector model |
| properties | [Property](#ar-v1-Property) | repeated |  |






<a name="ar-v1-RobotMessages"></a>

### RobotMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robots | [RobotMessage](#ar-v1-RobotMessage) | repeated |  |





 


<a name="ar-v1-RobotDriverType"></a>

### RobotDriverType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ROBOT_DRIVER_TYPE_UNSPECIFIED | 0 |  |
| ROBOT_DRIVER_TYPE_UR | 1 |  |



<a name="ar-v1-RobotType"></a>

### RobotType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ROBOT_TYPE_UNSPECIFIED | 0 |  |
| ROBOT_TYPE_UR3E | 10 |  |
| ROBOT_TYPE_UR5E | 11 |  |
| ROBOT_TYPE_UR10E | 12 |  |
| ROBOT_TYPE_KUKA_IIWA | 20 |  |


 

 

 



<a name="ar_v1_worker-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/worker.proto



<a name="ar-v1-WorkerMessage"></a>

### WorkerMessage
TODO: Add worker (including skill-matrix)?
TODO: remove to PLM


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [WorkerType](#ar-v1-WorkerType) |  |  |
| permission | [WorkerPermission](#ar-v1-WorkerPermission) |  | TODO: rename to edit permissions |
| properties | [Property](#ar-v1-Property) | repeated |  |
| disabled | [bool](#bool) |  | If disabled, the worker can&#39;t be selected |
| employee_id | [string](#string) |  |  |






<a name="ar-v1-WorkerMessages"></a>

### WorkerMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| workers | [WorkerMessage](#ar-v1-WorkerMessage) | repeated |  |





 


<a name="ar-v1-WorkerType"></a>

### WorkerType


| Name | Number | Description |
| ---- | ------ | ----------- |
| WORKER_TYPE_UNSPECIFIED | 0 |  |
| WORKER_TYPE_NOVICE | 1 |  |
| WORKER_TYPE_INTERMEDIATE | 2 |  |
| WORKER_TYPE_EXPERT | 3 |  |


 

 

 



<a name="assembly_v1_common-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## assembly/v1/common.proto



<a name="assembly-v1-CustomProperties"></a>

### CustomProperties



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| properties | [ar.v1.Property](#ar-v1-Property) | repeated |  |






<a name="assembly-v1-DisplayText"></a>

### DisplayText



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| title | [string](#string) |  |  |
| description | [string](#string) |  |  |
| operator_instruction | [string](#string) |  |  |






<a name="assembly-v1-EstimatedDuration"></a>

### EstimatedDuration



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| nominal | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| min | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| max | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |






<a name="assembly-v1-ExternalReference"></a>

### ExternalReference



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| system | [string](#string) |  |  |
| external_id | [string](#string) |  |  |
| url | [string](#string) |  |  |






<a name="assembly-v1-KeyValueConstraint"></a>

### KeyValueConstraint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| op | [ConstraintOperator](#assembly-v1-ConstraintOperator) |  |  |
| value | [string](#string) |  |  |
| values | [string](#string) | repeated |  |






<a name="assembly-v1-LocalTarget"></a>

### LocalTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| anchor_id | [string](#string) |  |  |
| offset | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |






<a name="assembly-v1-NamedRef"></a>

### NamedRef



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |






<a name="assembly-v1-Ref"></a>

### Ref



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |






<a name="assembly-v1-TimeWindow"></a>

### TimeWindow



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| end | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |





 


<a name="assembly-v1-ActorKind"></a>

### ActorKind


| Name | Number | Description |
| ---- | ------ | ----------- |
| ACTOR_KIND_UNSPECIFIED | 0 |  |
| ACTOR_KIND_HUMAN | 1 |  |
| ACTOR_KIND_ROBOT | 2 |  |
| ACTOR_KIND_HYBRID | 3 |  |



<a name="assembly-v1-CollaborationMode"></a>

### CollaborationMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| COLLABORATION_MODE_UNSPECIFIED | 0 |  |
| COLLABORATION_MODE_HUMAN_ONLY | 1 |  |
| COLLABORATION_MODE_ROBOT_ONLY | 2 |  |
| COLLABORATION_MODE_SEQUENTIAL_HRC | 3 |  |
| COLLABORATION_MODE_SIMULTANEOUS_HRC | 4 |  |



<a name="assembly-v1-ConstraintOperator"></a>

### ConstraintOperator


| Name | Number | Description |
| ---- | ------ | ----------- |
| CONSTRAINT_OPERATOR_UNSPECIFIED | 0 |  |
| CONSTRAINT_OPERATOR_EQ | 1 |  |
| CONSTRAINT_OPERATOR_NEQ | 2 |  |
| CONSTRAINT_OPERATOR_GT | 3 |  |
| CONSTRAINT_OPERATOR_GTE | 4 |  |
| CONSTRAINT_OPERATOR_LT | 5 |  |
| CONSTRAINT_OPERATOR_LTE | 6 |  |
| CONSTRAINT_OPERATOR_IN | 7 |  |
| CONSTRAINT_OPERATOR_NOT_IN | 8 |  |



<a name="assembly-v1-ResourceStatus"></a>

### ResourceStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| RESOURCE_STATUS_UNSPECIFIED | 0 |  |
| RESOURCE_STATUS_AVAILABLE | 1 |  |
| RESOURCE_STATUS_UNAVAILABLE | 2 |  |
| RESOURCE_STATUS_DISABLED | 3 |  |
| RESOURCE_STATUS_MAINTENANCE | 4 |  |



<a name="assembly-v1-SafetyRelevance"></a>

### SafetyRelevance


| Name | Number | Description |
| ---- | ------ | ----------- |
| SAFETY_RELEVANCE_UNSPECIFIED | 0 |  |
| SAFETY_RELEVANCE_LOW | 1 |  |
| SAFETY_RELEVANCE_MEDIUM | 2 |  |
| SAFETY_RELEVANCE_HIGH | 3 |  |
| SAFETY_RELEVANCE_CRITICAL | 4 |  |


 

 

 



<a name="assembly_v1_actor-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## assembly/v1/actor.proto



<a name="assembly-v1-ActorAssignment"></a>

### ActorAssignment



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| actor | [ActorRef](#assembly-v1-ActorRef) |  |  |
| process_run_id | [string](#string) |  |  |
| sequence_run_id | [string](#string) |  |  |
| task_run_id | [string](#string) |  |  |
| assigned_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| released_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |






<a name="assembly-v1-ActorRef"></a>

### ActorRef



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| kind | [ActorKind](#assembly-v1-ActorKind) |  |  |
| actor_id | [string](#string) |  | worker_definition_id or robot_instance_id |






<a name="assembly-v1-WorkerDefinition"></a>

### WorkerDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| disabled | [bool](#bool) |  | If disabled, the worker can&#39;t be selected |
| employee_id | [string](#string) |  |  |
| external_references | [ExternalReference](#assembly-v1-ExternalReference) | repeated |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-WorkerDefinitions"></a>

### WorkerDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [WorkerDefinition](#assembly-v1-WorkerDefinition) | repeated |  |





 

 

 

 



<a name="assembly_v1_execution-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## assembly/v1/execution.proto



<a name="assembly-v1-EvidenceFact"></a>

### EvidenceFact



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |
| unit | [string](#string) |  |  |






<a name="assembly-v1-ExecutionEvidence"></a>

### ExecutionEvidence



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| task_run_id | [string](#string) |  |  |
| source | [string](#string) |  | tool, vision, operator, robot driver, etc. |
| recorded_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| facts | [EvidenceFact](#assembly-v1-EvidenceFact) | repeated |  |
| blob_uri | [string](#string) |  |  |






<a name="assembly-v1-ProcessRun"></a>

### ProcessRun
ProcessRun is only created when a concrete cell can currently satisfy it.
Is is based upon a ProcessRecipe which defines what must be possible.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| recipe_id | [string](#string) |  |  |
| order_id | [string](#string) |  |  |
| station_id | [string](#string) |  |  |
| cell_id | [string](#string) |  |  |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| root_sequence_run_id | [string](#string) |  |  |
| sequences | [SequenceRun](#assembly-v1-SequenceRun) | repeated |  |
| tasks | [TaskRun](#assembly-v1-TaskRun) | repeated |  |
| state | [ProcessRunState](#assembly-v1-ProcessRunState) |  |  |
| initiated_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| ended_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| assignments | [ActorAssignment](#assembly-v1-ActorAssignment) | repeated |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |
| product_selections | [VariantSelection](#assembly-v1-VariantSelection) | repeated |  |
| parameters | [RunParameter](#assembly-v1-RunParameter) | repeated |  |






<a name="assembly-v1-RunParameter"></a>

### RunParameter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  | &#34;color&#34;, &#34;label_text&#34;, &#34;customer_name&#34; |
| value | [string](#string) |  |  |






<a name="assembly-v1-SequenceRun"></a>

### SequenceRun



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| sequence_definition_id | [string](#string) |  |  |
| parent_sequence_run_id | [string](#string) |  |  |
| child_sequence_run_ids | [string](#string) | repeated |  |
| child_task_run_ids | [string](#string) | repeated |  |
| state | [SequenceRunState](#assembly-v1-SequenceRunState) |  |  |
| completed_tasks | [int32](#int32) |  |  |
| can_bulk_complete | [bool](#bool) |  |  |
| assigned_actors | [ActorRef](#assembly-v1-ActorRef) | repeated |  |






<a name="assembly-v1-TaskRun"></a>

### TaskRun



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| task_definition_id | [string](#string) |  |  |
| parent_sequence_run_id | [string](#string) |  |  |
| state | [TaskRunState](#assembly-v1-TaskRunState) |  |  |
| candidate_actors | [ActorRef](#assembly-v1-ActorRef) | repeated |  |
| assigned_actor | [ActorRef](#assembly-v1-ActorRef) |  |  |
| can_do | [bool](#bool) |  |  |
| can_undo | [bool](#bool) |  |  |
| workable_horizon | [int32](#int32) |  | steps needed to complete before this step is workable. |
| estimated_duration | [EstimatedDuration](#assembly-v1-EstimatedDuration) |  |  |
| started_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| completed_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| error_code | [string](#string) |  |  |
| error_message | [string](#string) |  |  |
| evidence | [ExecutionEvidence](#assembly-v1-ExecutionEvidence) | repeated |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-VariantSelection"></a>

### VariantSelection



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dimension | [string](#string) |  |  |
| value | [string](#string) |  |  |





 


<a name="assembly-v1-ProcessRunState"></a>

### ProcessRunState


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_RUN_STATE_UNSPECIFIED | 0 |  |
| PROCESS_RUN_STATE_WAITING | 1 |  |
| PROCESS_RUN_STATE_IN_PROGRESS | 2 |  |
| PROCESS_RUN_STATE_COMPLETED | 3 |  |
| PROCESS_RUN_STATE_ABORTED | 4 |  |



<a name="assembly-v1-SequenceRunState"></a>

### SequenceRunState


| Name | Number | Description |
| ---- | ------ | ----------- |
| SEQUENCE_RUN_STATE_UNSPECIFIED | 0 |  |
| SEQUENCE_RUN_STATE_MISSING_PRECONDITION | 1 |  |
| SEQUENCE_RUN_STATE_WAITING | 2 |  |
| SEQUENCE_RUN_STATE_IN_PROGRESS | 3 |  |
| SEQUENCE_RUN_STATE_COMPLETED | 4 |  |
| SEQUENCE_RUN_STATE_ABORTED | 5 |  |



<a name="assembly-v1-TaskRunState"></a>

### TaskRunState


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_RUN_STATE_UNSPECIFIED | 0 |  |
| TASK_RUN_STATE_MISSING_PRECONDITION | 1 |  |
| TASK_RUN_STATE_WAITING | 2 |  |
| TASK_RUN_STATE_IN_PROGRESS | 3 |  |
| TASK_RUN_STATE_COMPLETED | 4 |  |
| TASK_RUN_STATE_ERROR | 5 |  |
| TASK_RUN_STATE_ABORTED | 6 |  |


 

 

 



<a name="assembly_v1_model-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## assembly/v1/model.proto



<a name="assembly-v1-ModelArtifact"></a>

### ModelArtifact



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| group | [ModelGroup](#assembly-v1-ModelGroup) |  |  |
| origin | [ModelOrigin](#assembly-v1-ModelOrigin) |  |  |
| format | [ModelFormat](#assembly-v1-ModelFormat) |  |  |
| filename | [string](#string) |  | Filename is required for BUILT_IN models, ignored otherwise |
| uri | [string](#string) |  | Uri is required for uploaded and external models |
| thumbnail_uri | [string](#string) |  |  |
| version | [string](#string) |  |  |
| unit | [string](#string) |  | Unit used for the model geometry coordinates. Typically &#34;mm&#34;, &#34;cm&#34;, &#34;m&#34;, &#34;in&#34;, etc. Used to scale the model correctly when loading. |
| up_axis | [string](#string) |  | &#34;X&#34;, &#34;Y&#34;, &#34;Z&#34; |
| external_references | [ExternalReference](#assembly-v1-ExternalReference) | repeated |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-ModelArtifacts"></a>

### ModelArtifacts



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ModelArtifact](#assembly-v1-ModelArtifact) | repeated |  |





 


<a name="assembly-v1-ModelFormat"></a>

### ModelFormat


| Name | Number | Description |
| ---- | ------ | ----------- |
| MODEL_FORMAT_UNSPECIFIED | 0 |  |
| MODEL_FORMAT_GLB | 1 |  |
| MODEL_FORMAT_GLTF | 2 |  |
| MODEL_FORMAT_OBJ | 3 |  |
| MODEL_FORMAT_STEP | 4 |  |
| MODEL_FORMAT_STL | 5 |  |
| MODEL_FORMAT_USDZ | 6 |  |



<a name="assembly-v1-ModelGroup"></a>

### ModelGroup


| Name | Number | Description |
| ---- | ------ | ----------- |
| MODEL_GROUP_UNSPECIFIED | 0 |  |
| MODEL_GROUP_PART | 1 |  |
| MODEL_GROUP_PRODUCT | 2 |  |
| MODEL_GROUP_TOOL | 3 |  |
| MODEL_GROUP_ROBOT | 4 |  |
| MODEL_GROUP_FIXTURE | 5 |  |
| MODEL_GROUP_ASSET | 6 |  |



<a name="assembly-v1-ModelOrigin"></a>

### ModelOrigin


| Name | Number | Description |
| ---- | ------ | ----------- |
| MODEL_ORIGIN_UNSPECIFIED | 0 |  |
| MODEL_ORIGIN_BUILT_IN | 1 |  |
| MODEL_ORIGIN_UPLOADED | 2 |  |
| MODEL_ORIGIN_EXTERNAL | 3 |  |


 

 

 



<a name="assembly_v1_product-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## assembly/v1/product.proto



<a name="assembly-v1-AssemblyNode"></a>

### AssemblyNode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| parent_node_id | [string](#string) |  | Empty if root, otherwise set to parent AssemblyNode id. |
| name | [string](#string) |  | Name of this assembly node |
| kind | [NodeKind](#assembly-v1-NodeKind) |  |  |
| part_definition_id | [string](#string) |  |  |
| override_model_id | [string](#string) |  |  |
| local_pose | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| child_node_ids | [string](#string) | repeated | Children of this node, their parent_node_id must be set to this.id |
| sequence_hint | [int32](#int32) |  |  |
| cad_occurrence_path | [string](#string) |  | CAD/BOM path if available, e.g. &#34;TopAssembly/DriveUnit:1/CoverSubAsm:1/Screw_M4x12:3&#34; |
| join_method_hint | [JoinMethod](#assembly-v1-JoinMethod) |  |  |
| insertion_axis_hint | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| preferred_approach_hint | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| optional | [bool](#bool) |  |  |
| applicability | [VariantCondition](#assembly-v1-VariantCondition) | repeated |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  | TODO: string or anchor reference_frame = 17; // allow tasks to anchor not just to a part but to features, e.g. insert screw into hole_1 |






<a name="assembly-v1-Dimensions"></a>

### Dimensions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x_mm | [double](#double) |  |  |
| y_mm | [double](#double) |  |  |
| z_mm | [double](#double) |  |  |






<a name="assembly-v1-MaterialSpec"></a>

### MaterialSpec
MaterialSpec is meant to capture the engineering material identity of a part
name → the material family / type
grade → the standardized grade or specification
Examples:
name: aluminium, grade: 6061-T6
name: Steel, grade: S355JR
name: stainless steel, grade: AISI 304
name: ABS, grade: general purpose
name: Polycarbonate, grade: PC-110
name: Nylon, grade: PA6 GF15
name: TPU, grade: 70 Shore A


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  | Material family |
| grade | [string](#string) |  | Standard/Specification |






<a name="assembly-v1-PartDefinition"></a>

### PartDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| type | [PartType](#assembly-v1-PartType) |  |  |
| weight_g | [int64](#int64) |  |  |
| dimensions | [Dimensions](#assembly-v1-Dimensions) |  |  |
| material | [MaterialSpec](#assembly-v1-MaterialSpec) |  |  |
| default_model_id | [string](#string) |  | Can later be extended to: CAD model (STEP), AR model (FBX), and lightweight mesh (OBJ) |
| handling | [PartHandlingProfile](#assembly-v1-PartHandlingProfile) |  |  |
| external_references | [ExternalReference](#assembly-v1-ExternalReference) | repeated |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-PartDefinitions"></a>

### PartDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [PartDefinition](#assembly-v1-PartDefinition) | repeated |  |






<a name="assembly-v1-PartHandlingProfile"></a>

### PartHandlingProfile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fragile | [bool](#bool) |  |  |
| esd_sensitive | [bool](#bool) |  |  |
| requires_two_hand_lift | [bool](#bool) |  |  |
| requires_fixture_support | [bool](#bool) |  | If true, this part cannot realistically be handled/assembled without some fixture support |
| max_grip_force_n | [double](#double) |  |  |
| max_torque_nm | [double](#double) |  |  |
| constraints | [KeyValueConstraint](#assembly-v1-KeyValueConstraint) | repeated |  |






<a name="assembly-v1-ProductDefinition"></a>

### ProductDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| root_node_id | [string](#string) |  |  |
| nodes | [AssemblyNode](#assembly-v1-AssemblyNode) | repeated |  |
| external_references | [ExternalReference](#assembly-v1-ExternalReference) | repeated |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-ProductDefinitions"></a>

### ProductDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ProductDefinition](#assembly-v1-ProductDefinition) | repeated |  |






<a name="assembly-v1-VariantCondition"></a>

### VariantCondition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dimension | [string](#string) |  | e.g. &#34;hinge_side&#34; |
| values | [string](#string) | repeated | e.g. [&#34;left&#34;] |





 


<a name="assembly-v1-JoinMethod"></a>

### JoinMethod


| Name | Number | Description |
| ---- | ------ | ----------- |
| JOIN_METHOD_UNSPECIFIED | 0 |  |
| JOIN_METHOD_NONE | 1 |  |
| JOIN_METHOD_FASTEN | 2 |  |
| JOIN_METHOD_PRESS_FIT | 3 |  |
| JOIN_METHOD_SNAP_FIT | 4 |  |
| JOIN_METHOD_ADHESIVE | 5 |  |
| JOIN_METHOD_WELD | 6 |  |
| JOIN_METHOD_PLACE | 7 |  |



<a name="assembly-v1-NodeKind"></a>

### NodeKind
NodeKind defines what kind of structural element the AssemblyNode is in the assembly hierarchy
NodeKind               Represents                    Physical part?   Has children?
GROUP                  logical grouping              ❌               yes
PART_OCCURRENCE        single physical part instance ✅               usually no
SUBASSEMBLY_OCCURRENCE assembly containing parts     ✅               yes
PATTERN                repeated pattern structure    ❌ (structure)   yes

| Name | Number | Description |
| ---- | ------ | ----------- |
| NODE_KIND_UNSPECIFIED | 0 |  |
| NODE_KIND_GROUP | 1 | A logical group node that does not correspond to a real physical part or subassembly. It exist only to organize the structure. Typical uses: CAD folders, BOM groupings, organizing fasteners, grouping operations, AR guidance grouping. part_definition_id should usually be empty. |
| NODE_KIND_PART_OCCURRENCE | 2 | The most common node type which is a single instance of a physical part used in the product as it references a PartDefinition. part_definition_id = required, child_node-Ids = empty. |
| NODE_KIND_SUBASSEMBLY_OCCURRENCE | 3 | A subassembly occurrence is a part that itself contains other parts. Thus a component that has its own internal structure. A subassembly is a real product structure (e.g. a Door assembly for a car) where group is a logical grouping. It usually appears in the BOM and often references a PartDefinition. |
| NODE_KIND_PATTERN | 4 | A repeated pattern of parts created by CAD pattern features. Examples: bolt circle, linear pattern, hole array, repeated clips, repeated LEDs. Instead of listing every occurrence individually, the CAD may represent them as a pattern. Thus a pattern is a special kind of group? |



<a name="assembly-v1-PartType"></a>

### PartType


| Name | Number | Description |
| ---- | ------ | ----------- |
| PART_TYPE_UNSPECIFIED | 0 |  |
| PART_TYPE_COMPONENT | 1 |  |
| PART_TYPE_FASTENER | 2 |  |
| PART_TYPE_SUBASSEMBLY | 3 |  |
| PART_TYPE_CONSUMABLE | 4 |  |
| PART_TYPE_LABEL | 5 |  |
| PART_TYPE_PACKAGING | 6 |  |


 

 

 



<a name="assembly_v1_resources-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## assembly/v1/resources.proto



<a name="assembly-v1-AssetDefinition"></a>

### AssetDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| type | [AssetType](#assembly-v1-AssetType) |  |  |
| driver_type | [AssetDriverType](#assembly-v1-AssetDriverType) |  |  |
| model_id | [string](#string) |  |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-AssetDefinitions"></a>

### AssetDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [AssetDefinition](#assembly-v1-AssetDefinition) | repeated |  |






<a name="assembly-v1-AssetInstance"></a>

### AssetInstance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| asset_definition_id | [string](#string) |  |  |
| station_id | [string](#string) |  |  |
| status | [ResourceStatus](#assembly-v1-ResourceStatus) |  |  |
| pose | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-AssetInstances"></a>

### AssetInstances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [AssetInstance](#assembly-v1-AssetInstance) | repeated |  |






<a name="assembly-v1-CapabilityProfile"></a>

### CapabilityProfile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min_force_n | [double](#double) |  |  |
| max_force_n | [double](#double) |  |  |
| min_torque_nm | [double](#double) |  |  |
| max_torque_nm | [double](#double) |  |  |
| repeatability_mm | [double](#double) |  |  |
| max_payload_g | [double](#double) |  |  |
| min_grip_width_mm | [double](#double) |  |  |
| max_grip_width_mm | [double](#double) |  |  |
| constraints | [KeyValueConstraint](#assembly-v1-KeyValueConstraint) | repeated |  |






<a name="assembly-v1-FixtureDefinition"></a>

### FixtureDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| type | [FixtureType](#assembly-v1-FixtureType) |  |  |
| supported_product_definition_ids | [string](#string) | repeated | This is a capability/compatibility declaration, e.g. fixture-1 supports product A and B |
| supported_root_part_definition_ids | [string](#string) | repeated | This fixture support products whose root assembly is one of these root parts |
| model_id | [string](#string) |  |  |
| constraints | [KeyValueConstraint](#assembly-v1-KeyValueConstraint) | repeated |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-FixtureDefinitions"></a>

### FixtureDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [FixtureDefinition](#assembly-v1-FixtureDefinition) | repeated |  |






<a name="assembly-v1-FixtureInstance"></a>

### FixtureInstance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| fixture_definition_id | [string](#string) |  |  |
| station_id | [string](#string) |  |  |
| status | [ResourceStatus](#assembly-v1-ResourceStatus) |  |  |
| pose | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-FixtureInstances"></a>

### FixtureInstances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [FixtureInstance](#assembly-v1-FixtureInstance) | repeated |  |






<a name="assembly-v1-RobotDefinition"></a>

### RobotDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| type | [RobotType](#assembly-v1-RobotType) |  |  |
| driver_type | [RobotDriverType](#assembly-v1-RobotDriverType) |  |  |
| coupler_model_id | [string](#string) |  |  |
| end_effector_tool_definition_id | [string](#string) |  |  |
| model_id | [string](#string) |  |  |
| capability_profile | [CapabilityProfile](#assembly-v1-CapabilityProfile) |  |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-RobotDefinitions"></a>

### RobotDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [RobotDefinitions](#assembly-v1-RobotDefinitions) | repeated |  |






<a name="assembly-v1-RobotInstance"></a>

### RobotInstance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| robot_definition_id | [string](#string) |  |  |
| station_id | [string](#string) |  |  |
| status | [ResourceStatus](#assembly-v1-ResourceStatus) |  |  |
| base_pose | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-RobotInstances"></a>

### RobotInstances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [RobotInstance](#assembly-v1-RobotInstance) | repeated |  |






<a name="assembly-v1-ToolDefinition"></a>

### ToolDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| type | [ToolType](#assembly-v1-ToolType) |  |  |
| actor_kind | [ActorKind](#assembly-v1-ActorKind) |  |  |
| roles | [ToolRole](#assembly-v1-ToolRole) | repeated |  |
| properties | [ToolProperty](#assembly-v1-ToolProperty) | repeated |  |
| capability_profile | [CapabilityProfile](#assembly-v1-CapabilityProfile) |  |  |
| model_id | [string](#string) |  |  |
| external_references | [ExternalReference](#assembly-v1-ExternalReference) | repeated |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-ToolDefinitions"></a>

### ToolDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ToolDefinition](#assembly-v1-ToolDefinition) | repeated |  |






<a name="assembly-v1-ToolInstance"></a>

### ToolInstance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| tool_definition_id | [string](#string) |  |  |
| serial_number | [string](#string) |  |  |
| station_id | [string](#string) |  |  |
| status | [ResourceStatus](#assembly-v1-ResourceStatus) |  |  |
| calibrated | [bool](#bool) |  |  |
| calibration_valid_until | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| pose | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-ToolInstances"></a>

### ToolInstances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ToolInstance](#assembly-v1-ToolInstance) | repeated |  |





 


<a name="assembly-v1-AssetDriverType"></a>

### AssetDriverType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ASSET_DRIVER_TYPE_UNSPECIFIED | 0 |  |
| ASSET_DRIVER_TYPE_DEFAULT | 1 |  |



<a name="assembly-v1-AssetType"></a>

### AssetType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ASSET_TYPE_UNSPECIFIED | 0 |  |
| ASSET_TYPE_CAMERA | 1 |  |
| ASSET_TYPE_LIGHT | 2 |  |
| ASSET_TYPE_CONVEYOR | 3 |  |
| ASSET_TYPE_SENSOR | 4 |  |
| ASSET_TYPE_HMI | 5 |  |



<a name="assembly-v1-FixtureType"></a>

### FixtureType


| Name | Number | Description |
| ---- | ------ | ----------- |
| FIXTURE_TYPE_UNSPECIFIED | 0 |  |
| FIXTURE_TYPE_BASE | 1 |  |
| FIXTURE_TYPE_CLAMP | 2 |  |
| FIXTURE_TYPE_JIG | 3 |  |
| FIXTURE_TYPE_PALLET | 4 |  |



<a name="assembly-v1-RobotDriverType"></a>

### RobotDriverType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ROBOT_DRIVER_TYPE_UNSPECIFIED | 0 |  |
| ROBOT_DRIVER_TYPE_UR | 1 |  |
| ROBOT_DRIVER_TYPE_GENERIC | 2 |  |



<a name="assembly-v1-RobotType"></a>

### RobotType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ROBOT_TYPE_UNSPECIFIED | 0 |  |
| ROBOT_TYPE_UR3E | 10 |  |
| ROBOT_TYPE_UR5E | 11 |  |
| ROBOT_TYPE_UR10E | 12 |  |
| ROBOT_TYPE_KUKA_IIWA | 20 |  |



<a name="assembly-v1-ToolProperty"></a>

### ToolProperty


| Name | Number | Description |
| ---- | ------ | ----------- |
| TOOL_PROPERTY_UNSPECIFIED | 0 |  |
| TOOL_PROPERTY_TORQUE_CONTROLLED | 1 |  |
| TOOL_PROPERTY_ESD_SAFE | 2 |  |
| TOOL_PROPERTY_INSULATED | 3 |  |
| TOOL_PROPERTY_COLLABORATIVE_SAFE | 4 |  |
| TOOL_PROPERTY_CALIBRATED | 5 |  |
| TOOL_PROPERTY_QUICK_CHANGE | 6 |  |



<a name="assembly-v1-ToolRole"></a>

### ToolRole


| Name | Number | Description |
| ---- | ------ | ----------- |
| TOOL_ROLE_UNSPECIFIED | 0 |  |
| TOOL_ROLE_GRIP_WORKPIECE | 1 |  |
| TOOL_ROLE_POSITION_COMPONENT | 2 |  |
| TOOL_ROLE_ALIGN_COMPONENT | 3 |  |
| TOOL_ROLE_APPLY_TORQUE | 4 |  |
| TOOL_ROLE_APPLY_LINEAR_FORCE | 5 |  |
| TOOL_ROLE_MEASURE_DIMENSION | 6 |  |
| TOOL_ROLE_DETECT_PRESENCE | 7 |  |
| TOOL_ROLE_DISPENSE_MATERIAL | 8 |  |
| TOOL_ROLE_EXECUTE_MOTION | 9 |  |
| TOOL_ROLE_SAFETY_INTERACTION | 10 |  |
| TOOL_ROLE_HANDLE_ESD | 11 |  |
| TOOL_ROLE_VISUAL_INSPECTION | 12 |  |



<a name="assembly-v1-ToolType"></a>

### ToolType


| Name | Number | Description |
| ---- | ------ | ----------- |
| TOOL_TYPE_UNSPECIFIED | 0 |  |
| TOOL_TYPE_FASTENING | 1 |  |
| TOOL_TYPE_GRIPPING | 2 |  |
| TOOL_TYPE_CUTTING | 3 |  |
| TOOL_TYPE_MEASURING | 4 |  |
| TOOL_TYPE_POSITIONING | 5 |  |
| TOOL_TYPE_DISPENSING | 6 |  |
| TOOL_TYPE_INSPECTION | 7 |  |
| TOOL_TYPE_SAFETY | 8 |  |
| TOOL_TYPE_ELECTRONICS | 9 |  |
| TOOL_TYPE_FIXTURE_ACCESSORY | 10 |  |
| TOOL_TYPE_SHAPING | 11 |  |
| TOOL_TYPE_TURNING | 12 |  |
| TOOL_TYPE_STRIKING | 13 |  |
| TOOL_TYPE_MARKING | 14 |  |
| TOOL_TYPE_FINISHING | 15 |  |
| TOOL_TYPE_ABRASIVE | 16 |  |
| TOOL_TYPE_CLEANING | 17 |  |


 

 

 



<a name="assembly_v1_skill-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## assembly/v1/skill.proto



<a name="assembly-v1-ActorConstraint"></a>

### ActorConstraint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| allowed_actor_kinds | [ActorKind](#assembly-v1-ActorKind) | repeated |  |
| collaboration_mode | [CollaborationMode](#assembly-v1-CollaborationMode) |  |  |
| constraints | [KeyValueConstraint](#assembly-v1-KeyValueConstraint) | repeated |  |






<a name="assembly-v1-ActorSkill"></a>

### ActorSkill



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| actor | [ActorRef](#assembly-v1-ActorRef) |  |  |
| skill_id | [string](#string) |  |  |
| level | [SkillLevel](#assembly-v1-SkillLevel) |  |  |
| status | [SkillStatus](#assembly-v1-SkillStatus) |  |  |
| confidence | [double](#double) |  | [0, 1] |
| last_evidence_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | timestamp |
| evidence_count | [int32](#int32) |  | since last training |
| valid_until | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | (timestamp) or policy-derived |
| validity_policy | [ValidityPolicyRef](#assembly-v1-ValidityPolicyRef) |  | which rule set is used |
| reasons | [string](#string) | repeated | [&#34;inactivity_&gt;30d&#34;] |
| next_actions | [string](#string) | repeated | [&#34;micro_training&#34;, &#34;extra_verification_required&#34;] |






<a name="assembly-v1-SkillDefinition"></a>

### SkillDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| domain | [SkillDomain](#assembly-v1-SkillDomain) |  |  |
| tool_roles | [ToolRole](#assembly-v1-ToolRole) | repeated |  |
| safety_relevance | [SafetyRelevance](#assembly-v1-SafetyRelevance) |  |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-SkillRequirement"></a>

### SkillRequirement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| skill_id | [string](#string) |  |  |
| minimum_level | [SkillLevel](#assembly-v1-SkillLevel) |  |  |
| constraints | [KeyValueConstraint](#assembly-v1-KeyValueConstraint) | repeated |  |






<a name="assembly-v1-ToolRequirement"></a>

### ToolRequirement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| role | [ToolRole](#assembly-v1-ToolRole) |  |  |
| required_properties | [ToolProperty](#assembly-v1-ToolProperty) | repeated |  |
| minimum_capability | [CapabilityProfile](#assembly-v1-CapabilityProfile) |  |  |
| allowed_tool_definition_ids | [string](#string) | repeated |  |






<a name="assembly-v1-ValidityPolicyRef"></a>

### ValidityPolicyRef



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| policy_id | [string](#string) |  |  |
| version | [string](#string) |  |  |





 


<a name="assembly-v1-SkillDomain"></a>

### SkillDomain


| Name | Number | Description |
| ---- | ------ | ----------- |
| SKILL_DOMAIN_UNSPECIFIED | 0 |  |
| SKILL_DOMAIN_HANDLING | 1 |  |
| SKILL_DOMAIN_ASSEMBLY | 2 |  |
| SKILL_DOMAIN_FASTENING | 3 |  |
| SKILL_DOMAIN_INSPECTION | 4 |  |
| SKILL_DOMAIN_ELECTRICAL | 5 |  |
| SKILL_DOMAIN_COLLABORATION | 6 |  |
| SKILL_DOMAIN_SAFETY | 7 |  |
| SKILL_DOMAIN_ROBOT_OPERATION | 8 |  |



<a name="assembly-v1-SkillLevel"></a>

### SkillLevel


| Name | Number | Description |
| ---- | ------ | ----------- |
| SKILL_LEVEL_UNSPECIFIED | 0 |  |
| SKILL_LEVEL_NOT_ALLOWED | 1 | Human: Untrained, Robot: Not programmed |
| SKILL_LEVEL_ASSISTED | 2 | Human: AR-guided, Robot: Supervised execution |
| SKILL_LEVEL_QUALIFIED | 3 | Human: Certified operator, Robot: validated program |
| SKILL_LEVEL_EXPERT | 4 | Human: Technician, Robot: Optimized &amp; adaptive |
| SKILL_LEVEL_AUTHORITY | 5 | Human: Trainer, Robot: Self-adjusting |



<a name="assembly-v1-SkillStatus"></a>

### SkillStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| SKILL_STATUS_UNSPECIFIED | 0 |  |
| SKILL_STATUS_ACTIVE | 1 |  |
| SKILL_STATUS_RESTRICTED | 2 |  |
| SKILL_STATUS_EXPIRED | 3 |  |


 

 

 



<a name="assembly_v1_process-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## assembly/v1/process.proto



<a name="assembly-v1-ProcessRecipe"></a>

### ProcessRecipe
ProcessRecipe describes the following:
- What work must be done
- What kinds of capabilities are required
- What tool roles are required
- What skills are required
- What actor constrains exist
- What validation is needed


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| type | [ProcessType](#assembly-v1-ProcessType) |  |  |
| product_definition_id | [string](#string) |  |  |
| applicability | [RecipeApplicability](#assembly-v1-RecipeApplicability) |  |  |
| root_sequence_id | [string](#string) |  |  |
| sequences | [SequenceDefinition](#assembly-v1-SequenceDefinition) | repeated |  |
| tasks | [TaskDefinition](#assembly-v1-TaskDefinition) | repeated |  |
| supported_fixture_definition_ids | [string](#string) | repeated | Meaning: this recipe is intended to run with these fixtures |
| external_references | [ExternalReference](#assembly-v1-ExternalReference) | repeated |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-RecipeApplicability"></a>

### RecipeApplicability



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| required | [VariantCondition](#assembly-v1-VariantCondition) | repeated |  |
| excluded | [VariantCondition](#assembly-v1-VariantCondition) | repeated |  |






<a name="assembly-v1-SequenceDefinition"></a>

### SequenceDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| parent_sequence_id | [string](#string) |  |  |
| operator | [SequenceOperator](#assembly-v1-SequenceOperator) |  |  |
| child_sequence_ids | [string](#string) | repeated |  |
| child_task_ids | [string](#string) | repeated |  |
| local_target | [LocalTarget](#assembly-v1-LocalTarget) |  |  |
| optional | [bool](#bool) |  |  |
| can_bulk_complete | [bool](#bool) |  |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-TaskDefinition"></a>

### TaskDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| instruction_text | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| task_type | [TaskType](#assembly-v1-TaskType) |  |  |
| target | [TaskTarget](#assembly-v1-TaskTarget) |  |  |
| approach | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| tool_requirements | [ToolRequirement](#assembly-v1-ToolRequirement) | repeated | repeated string precondition_task_ids = 10; repeated string dependant_task_ids = 11; |
| skill_requirements | [SkillRequirement](#assembly-v1-SkillRequirement) | repeated |  |
| validation | [ValidationRequirement](#assembly-v1-ValidationRequirement) |  |  |
| execution_policy | [TaskExecutionPolicy](#assembly-v1-TaskExecutionPolicy) |  |  |
| safety_relevance | [SafetyRelevance](#assembly-v1-SafetyRelevance) |  |  |
| source_node_id | [string](#string) |  | optional: where part comes from for move/mount |
| destination_node_id | [string](#string) |  | optional |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-TaskExecutionPolicy"></a>

### TaskExecutionPolicy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| assignment_preference | [TaskAssignmentPreference](#assembly-v1-TaskAssignmentPreference) |  |  |
| actor_constraint | [ActorConstraint](#assembly-v1-ActorConstraint) |  |  |
| can_reassign | [bool](#bool) |  |  |
| can_do | [bool](#bool) |  |  |
| can_undo | [bool](#bool) |  |  |
| estimated_duration | [EstimatedDuration](#assembly-v1-EstimatedDuration) |  |  |






<a name="assembly-v1-TaskTarget"></a>

### TaskTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_node_id | [string](#string) |  | Assembly node occurrence |
| target_part_definition_id | [string](#string) |  | optional denormalized helper |
| local_target | [LocalTarget](#assembly-v1-LocalTarget) |  |  |






<a name="assembly-v1-ValidationRequirement"></a>

### ValidationRequirement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| require_tool_feedback | [bool](#bool) |  |  |
| require_vision_check | [bool](#bool) |  |  |
| allow_manual_confirmation | [bool](#bool) |  |  |
| manual_confirmation_min_level | [SkillLevel](#assembly-v1-SkillLevel) |  |  |
| constraints | [KeyValueConstraint](#assembly-v1-KeyValueConstraint) | repeated |  |





 


<a name="assembly-v1-ProcessType"></a>

### ProcessType


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_TYPE_UNSPECIFIED | 0 |  |
| PROCESS_TYPE_ASSEMBLY | 1 |  |
| PROCESS_TYPE_DISASSEMBLY | 2 |  |
| PROCESS_TYPE_INSPECTION | 3 |  |
| PROCESS_TYPE_CHECKLIST | 4 |  |



<a name="assembly-v1-SequenceOperator"></a>

### SequenceOperator


| Name | Number | Description |
| ---- | ------ | ----------- |
| SEQUENCE_OPERATOR_UNSPECIFIED | 0 |  |
| SEQUENCE_OPERATOR_ALL_OF_CHILDREN | 1 |  |
| SEQUENCE_OPERATOR_ONE_OF_CHILDREN | 2 |  |
| SEQUENCE_OPERATOR_ORDERED | 3 |  |



<a name="assembly-v1-TaskAssignmentPreference"></a>

### TaskAssignmentPreference


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_ASSIGNMENT_PREFERENCE_UNSPECIFIED | 0 |  |
| TASK_ASSIGNMENT_PREFERENCE_PREFER_HUMAN | 1 |  |
| TASK_ASSIGNMENT_PREFERENCE_ONLY_HUMAN | 2 |  |
| TASK_ASSIGNMENT_PREFERENCE_PREFER_ROBOT | 3 |  |
| TASK_ASSIGNMENT_PREFERENCE_ONLY_ROBOT | 4 | Only use this if it truly must be done by a robot. Otherwise use prefer-robot |
| TASK_ASSIGNMENT_PREFERENCE_EITHER | 5 |  |



<a name="assembly-v1-TaskType"></a>

### TaskType


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_TYPE_UNSPECIFIED | 0 |  |
| TASK_TYPE_INSPECT | 1 |  |
| TASK_TYPE_FASTEN | 2 |  |
| TASK_TYPE_UNFASTEN | 3 |  |
| TASK_TYPE_MOUNT | 4 |  |
| TASK_TYPE_UNMOUNT | 5 |  |
| TASK_TYPE_MOVE | 6 |  |
| TASK_TYPE_REMOVE | 7 |  |
| TASK_TYPE_APPLY | 8 |  |
| TASK_TYPE_WIPE | 9 |  |
| TASK_TYPE_ALIGN | 10 |  |
| TASK_TYPE_INSERT | 11 |  |
| TASK_TYPE_HOLD | 12 |  |
| TASK_TYPE_VERIFY | 13 |  |


 

 

 



<a name="assembly_v1_process_requests-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## assembly/v1/process_requests.proto



<a name="assembly-v1-ProcessLoadRequest"></a>

### ProcessLoadRequest
ProcessLoadRequest is used to go from ProcessRecipe -&gt; ProcessRun
During this process, resources feasibility should be checked, i.e.
   &#34;Can this recipe be instantiated now, on this station/cell/line, with the currently available resources?&#34;

Thus the following must be evaluated:
- available robots (if any task requires or strongly prefers a robot, can that be satisfied?)
- available workers (if tasks requires only-human or need certain skills, can that be satisfied? Either check immediately or defer until operator is assigned. Perhaps assigned based on skills and availability? Check that: assigned worker exist, worker enabled, required skills present and valid)
- available tool instances (all ToolRequirements from all tasks, available ToolInstances is station/cell, tool status, calibration validity, required properties, minimum capability profile)
- valid calibration
- fixture availability/feasibility (recipe supported fixtures, available fixture instances, fixture status, product/recipe compatibility)
- safety mode / collaboration mode (check: recipe task collaboration modes, station/cell safety mode, whether simultaneous HRC is allowed, whether human-only or robot-only is possible right now)
- active faults / disabled resources
- asset / inspection feasibility (if validation required: vision, torque feedback, external QC, sensors --&gt; then verify those assets exist and are available.)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| process_recipe_id | [string](#string) |  |  |
| target_line_id | [string](#string) |  |  |
| dry_run | [bool](#bool) |  | true = precheck only, false = precheck &#43; instantiate |






<a name="assembly-v1-ProcessLoadResult"></a>

### ProcessLoadResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| status | [ProcessLoadStatus](#assembly-v1-ProcessLoadStatus) |  |  |
| precheck | [ProcessRunPrecheckResult](#assembly-v1-ProcessRunPrecheckResult) |  |  |
| process_run | [ProcessRun](#assembly-v1-ProcessRun) |  |  |






<a name="assembly-v1-ProcessRunIssue"></a>

### ProcessRunIssue



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| failure | [ProcessLoadFailure](#assembly-v1-ProcessLoadFailure) |  |  |
| message | [string](#string) |  |  |
| severity | [ProcessRunIssueSeverity](#assembly-v1-ProcessRunIssueSeverity) |  |  |
| process_recipe_id | [string](#string) |  | Scope |
| sequence_definition_id | [string](#string) |  |  |
| task_definition_id | [string](#string) |  |  |
| required_tool_role | [string](#string) |  | Related requirement/resource |
| required_skill_id | [string](#string) |  |  |
| fixture_definition_id | [string](#string) |  |  |
| station_id | [string](#string) |  |  |
| actor_id | [string](#string) |  |  |
| resource_id | [string](#string) |  | tool/robot/fixture/asset instance if known |
| remediation | [string](#string) |  | Optional remediation hint |
| importance | [RequirementImportance](#assembly-v1-RequirementImportance) |  |  |






<a name="assembly-v1-ProcessRunPrecheckResult"></a>

### ProcessRunPrecheckResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ok | [bool](#bool) |  |  |
| issues | [ProcessRunIssue](#assembly-v1-ProcessRunIssue) | repeated |  |
| blocking_issue_count | [int32](#int32) |  | Optional summary counts for UI / fast filtering |
| warning_issue_count | [int32](#int32) |  |  |
| process_recipe_id | [string](#string) |  | What was checked |
| target_line_id | [string](#string) |  |  |
| task_feasibility | [TaskFeasibility](#assembly-v1-TaskFeasibility) | repeated | Optional: useful if precheck computes feasible assignments/resources |
| status | [ProcessRunPrecheckStatus](#assembly-v1-ProcessRunPrecheckStatus) |  | Optional overall status |






<a name="assembly-v1-TaskFeasibility"></a>

### TaskFeasibility



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_definition_id | [string](#string) |  |  |
| feasible | [bool](#bool) |  |  |
| candidate_actor_ids | [string](#string) | repeated |  |
| candidate_tool_instance_ids | [string](#string) | repeated |  |
| candidate_fixture_instance_ids | [string](#string) | repeated |  |
| candidate_asset_instance_ids | [string](#string) | repeated |  |
| issues | [ProcessRunIssue](#assembly-v1-ProcessRunIssue) | repeated |  |





 


<a name="assembly-v1-ProcessLoadFailure"></a>

### ProcessLoadFailure


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_LOAD_FAILURE_UNSPECIFIED | 0 |  |
| PROCESS_LOAD_FAILURE_LINE_NOT_FOUND | 1 | General failures |
| PROCESS_LOAD_FAILURE_PROCESS_RECIPE_NOT_FOUND | 2 |  |
| PROCESS_LOAD_FAILURE_PRODUCT_NOT_SUPPORTED | 3 |  |
| PROCESS_LOAD_FAILURE_RESOURCE_STATE_UNKNOWN | 4 |  |
| PROCESS_LOAD_FAILURE_NO_COMPATIBLE_FIXTURE | 10 | Fixture related failures |
| PROCESS_LOAD_FAILURE_MISSING_TOOL_ROLE | 20 | Tool related failures |
| PROCESS_LOAD_FAILURE_TOOL_NOT_CALIBRATED | 21 |  |
| PROCESS_LOAD_FAILURE_TOOL_CAPABILITY_INSUFFICIENT | 22 |  |
| PROCESS_LOAD_FAILURE_ROBOT_UNAVAILABLE | 30 | Robot related failures |
| PROCESS_LOAD_FAILURE_ROBOT_TOOLING_MISMATCH | 31 |  |
| PROCESS_LOAD_FAILURE_NO_QUALIFIED_OPERATOR | 40 | Agent/operator related failueres |
| PROCESS_LOAD_FAILURE_REQUIRED_SKILL_EXPIRED | 41 |  |
| PROCESS_LOAD_FAILURE_NO_FEASIBLE_ACTOR | 42 |  |
| PROCESS_LOAD_FAILURE_COLLABORATION_MODE_UNSUPPORTED | 50 | Safety / collaboration related failures |
| PROCESS_LOAD_FAILURE_SAFETY_MODE_MISMATCH | 51 |  |
| PROCESS_LOAD_FAILURE_VISION_ASSET_UNAVAILABLE | 60 | Validation related failures |
| PROCESS_LOAD_FAILURE_VALIDATION_SOURCE_MISSING | 61 |  |
| PROCESS_LOAD_FAILURE_NO_FEASIBLE_VALIDATION_METHOD | 62 |  |



<a name="assembly-v1-ProcessLoadStatus"></a>

### ProcessLoadStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_LOAD_STATUS_UNSPECIFIED | 0 |  |
| PROCESS_LOAD_STATUS_PRECHECK_FAILED | 1 |  |
| PROCESS_LOAD_STATUS_READY | 2 | feasible, but not instantiated (dry run) |
| PROCESS_LOAD_STATUS_LOADED | 3 | feasible and instantiated |



<a name="assembly-v1-ProcessRunIssueSeverity"></a>

### ProcessRunIssueSeverity


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_RUN_ISSUE_SEVERITY_UNSPECIFIED | 0 |  |
| PROCESS_RUN_ISSUE_SEVERITY_BLOCKING | 1 | Run cannot start. Some reasons: no compatible fixture, required tool missing, robot required but unavailable, safety mode incompatible, no feasible actor for only-human/only-robot task |
| PROCESS_RUN_ISSUE_SEVERITY_WARNING | 2 | Run may start, but quality/performance may suffer. Examples: preferred robot unavailable (but human can do task), calibration expires soon, only one qualified actor available, vision unavailable but manual confirmation allowed. |



<a name="assembly-v1-ProcessRunPrecheckStatus"></a>

### ProcessRunPrecheckStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_RUN_PRECHECK_STATUS_UNSPECIFIED | 0 |  |
| PROCESS_RUN_PRECHECK_STATUS_OK | 1 | Neither warning nor blocking issues |
| PROCESS_RUN_PRECHECK_STATUS_OK_WITH_WARNINGS | 2 | One or more warning issues, but no blocking |
| PROCESS_RUN_PRECHECK_STATUS_BLOCKED | 3 | One or more blocking issues |



<a name="assembly-v1-RequirementImportance"></a>

### RequirementImportance


| Name | Number | Description |
| ---- | ------ | ----------- |
| REQUIREMENT_IMPORTANCE_UNSPECIFIED | 0 |  |
| REQUIREMENT_IMPORTANCE_REQUIRED | 1 |  |
| REQUIREMENT_IMPORTANCE_PREFERRED | 2 |  |


 

 

 



<a name="assembly_v1_station-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## assembly/v1/station.proto



<a name="assembly-v1-CellDefinition"></a>

### CellDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| station_ids | [string](#string) | repeated |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |






<a name="assembly-v1-StationDefinition"></a>

### StationDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| tool_instance_ids | [string](#string) | repeated |  |
| fixture_instance_ids | [string](#string) | repeated |  |
| robot_instance_ids | [string](#string) | repeated |  |
| asset_instance_ids | [string](#string) | repeated |  |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| custom | [CustomProperties](#assembly-v1-CustomProperties) |  |  |





 

 

 

 



<a name="assembly_v1_validation-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## assembly/v1/validation.proto



<a name="assembly-v1-ValidationResult"></a>

### ValidationResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| task_run_id | [string](#string) |  |  |
| status | [ValidationStatus](#assembly-v1-ValidationStatus) |  |  |
| method | [string](#string) |  | tool_feedback / vision / manual / external_qc |
| validated_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| measurements | [KeyValueConstraint](#assembly-v1-KeyValueConstraint) | repeated |  |
| validated_by_actor_id | [string](#string) |  |  |
| comment | [string](#string) |  |  |





 


<a name="assembly-v1-ValidationStatus"></a>

### ValidationStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| VALIDATION_STATUS_UNSPECIFIED | 0 |  |
| VALIDATION_STATUS_PENDING | 1 |  |
| VALIDATION_STATUS_PASSED | 2 |  |
| VALIDATION_STATUS_FAILED | 3 |  |
| VALIDATION_STATUS_BYPASSED | 4 |  |


 

 

 



<a name="common_v1_delete-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/delete.proto



<a name="common-v1-DeleteMessage"></a>

### DeleteMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  | Id of the entity to be deleted |
| message | [string](#string) |  | Optional message |





 

 

 

 



<a name="common_v1_empty-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/empty.proto



<a name="common-v1-EmptyMessage"></a>

### EmptyMessage






 

 

 

 



<a name="common_v1_get-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/get.proto



<a name="common-v1-GetByIdMessage"></a>

### GetByIdMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ids | [string](#string) | repeated |  |






<a name="common-v1-GetMessage"></a>

### GetMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |





 

 

 

 



<a name="geometry_v1_wrench-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/wrench.proto



<a name="geometry-v1-Wrench"></a>

### Wrench



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| force | [Vector3](#geometry-v1-Vector3) |  |  |
| torque | [Vector3](#geometry-v1-Vector3) |  |  |





 

 

 

 



<a name="plm_v1_capability-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/capability.proto



<a name="plm-v1-Capabilities"></a>

### Capabilities



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| capabilities | [Capability](#plm-v1-Capability) | repeated |  |






<a name="plm-v1-Capability"></a>

### Capability



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| agent_id | [string](#string) |  | Id of the agent (either an operator or robot) |
| part_id | [string](#string) |  | Id of the part that the agent can handle |
| estimated_time | [int64](#int64) |  | Estimated time to complete a task with that part |





 

 

 

 



<a name="plm_v1_fixture-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/fixture.proto



<a name="plm-v1-FixtureMessage"></a>

### FixtureMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [FixtureType](#plm-v1-FixtureType) |  |  |
| accepted_part_ids | [string](#string) | repeated |  |






<a name="plm-v1-FixtureMessages"></a>

### FixtureMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fixtures | [FixtureMessage](#plm-v1-FixtureMessage) | repeated |  |





 


<a name="plm-v1-FixtureType"></a>

### FixtureType


| Name | Number | Description |
| ---- | ------ | ----------- |
| FIXTURE_TYPE_UNSPECIFIED | 0 |  |


 

 

 



<a name="plm_v1_line-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/line.proto



<a name="plm-v1-LineMessage"></a>

### LineMessage
TODO: allow multiple processes to make active at the same time?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [LineType](#plm-v1-LineType) |  | TODO: agents TODO: capabilities |





 


<a name="plm-v1-LineType"></a>

### LineType


| Name | Number | Description |
| ---- | ------ | ----------- |
| LINE_TYPE_UNSPECIFIED | 0 |  |
| LINE_TYPE_SUB_ASSEMBLY | 1 |  |
| LINE_TYPE_FASTENER | 2 |  |
| LINE_TYPE_PLATE | 3 |  |
| LINE_TYPE_LUBRICANT | 4 |  |


 

 

 



<a name="plm_v1_model_old-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/model_old.proto



<a name="plm-v1-ModelMessage"></a>

### ModelMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| group | [ModelGroup](#plm-v1-ModelGroup) |  |  |
| origin | [ModelOrigin](#plm-v1-ModelOrigin) |  |  |
| filename | [string](#string) |  |  |
| url | [string](#string) |  |  |






<a name="plm-v1-ModelMessages"></a>

### ModelMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| models | [ModelMessage](#plm-v1-ModelMessage) | repeated |  |





 


<a name="plm-v1-ModelGroup"></a>

### ModelGroup


| Name | Number | Description |
| ---- | ------ | ----------- |
| MODEL_GROUP_UNSPECIFIED | 0 |  |
| MODEL_GROUP_TOOLS | 1 |  |
| MODEL_GROUP_PARTS | 2 |  |
| MODEL_GROUP_ROBOTS | 3 |  |
| MODEL_GROUP_ASSETS | 4 |  |



<a name="plm-v1-ModelOrigin"></a>

### ModelOrigin


| Name | Number | Description |
| ---- | ------ | ----------- |
| MODEL_ORIGIN_UNSPECIFIED | 0 |  |
| MODEL_ORIGIN_BUILD_IN | 1 |  |
| MODEL_ORIGIN_UPLOADED | 2 |  |
| MODEL_ORIGIN_EXTERNAL | 3 |  |


 

 

 



<a name="plm_v1_part-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/part.proto



<a name="plm-v1-PartMessage"></a>

### PartMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [PartType](#plm-v1-PartType) |  |  |
| weight | [int64](#int64) |  | weight in grams |
| model_id | [string](#string) |  | TODO: add dimensions TODO: add material |
| tool_ids | [string](#string) | repeated |  |






<a name="plm-v1-PartMessages"></a>

### PartMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| parts | [PartMessage](#plm-v1-PartMessage) | repeated |  |





 


<a name="plm-v1-PartType"></a>

### PartType


| Name | Number | Description |
| ---- | ------ | ----------- |
| PART_TYPE_UNSPECIFIED | 0 |  |
| PART_TYPE_SUB_ASSEMBLY | 1 |  |
| PART_TYPE_FASTENER | 2 |  |
| PART_TYPE_PLATE | 3 |  |
| PART_TYPE_LUBRICANT | 4 |  |


 

 

 



<a name="plm_v1_process_abort-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/process_abort.proto



<a name="plm-v1-ProcessAbortMessage"></a>

### ProcessAbortMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| reason | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_sequence-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/sequence.proto



<a name="plm-v1-SequenceMessage"></a>

### SequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| offset | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| parent_id | [string](#string) |  |  |
| sequence_ids | [string](#string) | repeated |  |
| task_ids | [string](#string) | repeated |  |
| assigned_to | [string](#string) | repeated |  |
| state | [SequenceState](#plm-v1-SequenceState) |  |  |
| completed_tasks | [int32](#int32) |  |  |
| can_bulk_complete | [bool](#bool) |  |  |






<a name="plm-v1-SequenceUpdatedMessage"></a>

### SequenceUpdatedMessage
Update published when the state of a sequence have changed


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sequence_id | [string](#string) |  |  |
| assigned_to | [string](#string) | repeated |  |
| state | [SequenceState](#plm-v1-SequenceState) |  |  |
| completed_tasks | [int32](#int32) |  |  |





 


<a name="plm-v1-SequenceState"></a>

### SequenceState


| Name | Number | Description |
| ---- | ------ | ----------- |
| SEQUENCE_STATE_UNSPECIFIED | 0 |  |
| SEQUENCE_STATE_MISSING_PRECONDITION | 1 |  |
| SEQUENCE_STATE_WAITING | 2 |  |
| SEQUENCE_STATE_IN_PROGRESS | 3 |  |
| SEQUENCE_STATE_COMPLETED | 4 |  |


 

 

 



<a name="plm_v1_task-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/task.proto



<a name="plm-v1-TaskMessage"></a>

### TaskMessage
TODO: add required skill?
TODO: add tool_role?
TODO: add validation
TODO: add allowed_actors


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| instruction_text | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| part_id | [string](#string) |  |  |
| model_id | [string](#string) |  |  |
| task_type | [TaskType](#plm-v1-TaskType) |  |  |
| target | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| approach | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| parent_id | [string](#string) |  |  |
| agents_ids | [string](#string) | repeated |  |
| assigned_to | [string](#string) |  |  |
| state | [TaskState](#plm-v1-TaskState) |  |  |
| preconditions | [string](#string) | repeated |  |
| dependants | [string](#string) | repeated |  |
| assignment_preference | [TaskAssignmentPreference](#plm-v1-TaskAssignmentPreference) |  |  |
| can_reassign | [bool](#bool) |  |  |
| can_do | [bool](#bool) |  |  |
| can_undo | [bool](#bool) |  |  |
| horizon | [int32](#int32) |  | TODO: &#39;complete-importance&#39;: could be different levels of &#34;this must be explicitly completed&#34; or tie it together with user level, such that expertise level (expert, intermediate, novice) equal and above intermediate can {bulk, automatic, ... } complete and below must explicitly complete. This should potentially also be tied to the part and this field(s) can then be a custom override for this specific task.

steps needed to complete before this step is workable. Could be use to better calculate what task to do next, especially if paired with time estimate for each task. |
| estimated_completion_time | [int32](#int32) |  | estimated time to complete (in seconds) |






<a name="plm-v1-TaskUpdatedMessage"></a>

### TaskUpdatedMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| assigned_to | [string](#string) |  |  |
| state | [TaskState](#plm-v1-TaskState) |  |  |
| can_reassign | [bool](#bool) |  |  |
| can_do | [bool](#bool) |  |  |
| can_undo | [bool](#bool) |  |  |





 


<a name="plm-v1-TaskAssignmentPreference"></a>

### TaskAssignmentPreference


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_ASSIGNMENT_PREFERENCE_UNSPECIFIED | 0 |  |
| TASK_ASSIGNMENT_PREFERENCE_PREFER_HUMAN | 1 |  |
| TASK_ASSIGNMENT_PREFERENCE_ONLY_HUMAN | 2 |  |
| TASK_ASSIGNMENT_PREFERENCE_PREFER_ROBOT | 3 |  |
| TASK_ASSIGNMENT_PREFERENCE_ONLY_ROBOT | 4 |  |



<a name="plm-v1-TaskState"></a>

### TaskState


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_STATE_UNSPECIFIED | 0 |  |
| TASK_STATE_MISSING_PRECONDITION | 1 |  |
| TASK_STATE_WAITING | 2 |  |
| TASK_STATE_IN_PROGRESS | 3 |  |
| TASK_STATE_COMPLETED | 4 |  |
| TASK_STATE_ERROR | 6 |  |



<a name="plm-v1-TaskType"></a>

### TaskType


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_TYPE_UNSPECIFIED | 0 |  |
| TASK_TYPE_INSPECT | 1 |  |
| TASK_TYPE_FASTEN | 2 |  |
| TASK_TYPE_UNFASTEN | 3 |  |
| TASK_TYPE_MOUNT | 4 |  |
| TASK_TYPE_UNMOUNT | 5 |  |
| TASK_TYPE_MOVE | 6 |  |
| TASK_TYPE_REMOVE | 7 |  |
| TASK_TYPE_APPLY | 8 |  |
| TASK_TYPE_WIPE | 9 |  |


 

 

 



<a name="plm_v1_process_old-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/process_old.proto



<a name="plm-v1-ProcessMessage"></a>

### ProcessMessage
TODO: should &#39;running&#39; be called process and &#39;static&#39; recipe?
TODO: Add/assign the agent(s) at runtime, instead of allocating them to the environment. THen there could also be a situation where each agent is asked to take a task during execution.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| instance_id | [string](#string) |  |  |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#plm-v1-ProcessType) |  |  |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| root_sequence_id | [string](#string) |  |  |
| sequences | [SequenceMessage](#plm-v1-SequenceMessage) | repeated |  |
| tasks | [TaskMessage](#plm-v1-TaskMessage) | repeated |  |
| state | [ProcessState](#plm-v1-ProcessState) |  |  |
| initiated | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| ended | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| order_id | [string](#string) |  |  |
| line_id | [string](#string) |  |  |






<a name="plm-v1-ProcessMessages"></a>

### ProcessMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| processes | [ProcessMessage](#plm-v1-ProcessMessage) | repeated |  |






<a name="plm-v1-ProcessUpdatedMessage"></a>

### ProcessUpdatedMessage
Update published when the state of a process have changed


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| instance_id | [string](#string) |  |  |
| id | [string](#string) |  |  |
| state | [ProcessState](#plm-v1-ProcessState) |  |  |
| ended | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |





 


<a name="plm-v1-ProcessState"></a>

### ProcessState


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_STATE_UNSPECIFIED | 0 |  |
| PROCESS_STATE_WAITING | 1 |  |
| PROCESS_STATE_IN_PROGRESS | 2 |  |
| PROCESS_STATE_COMPLETED | 3 |  |
| PROCESS_STATE_ABORTED | 4 |  |



<a name="plm-v1-ProcessType"></a>

### ProcessType


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_TYPE_UNSPECIFIED | 0 |  |
| PROCESS_TYPE_ASSEMBLY | 1 |  |
| PROCESS_TYPE_DISASSEMBLY | 2 |  |
| PROCESS_TYPE_INSPECTION | 3 | TODO: what should this be? |
| PROCESS_TYPE_CHECKLIST | 4 | TODO: this could be startup procedures, fault fixing, ... |


 

 

 



<a name="plm_v1_process_authoring-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/process_authoring.proto



<a name="plm-v1-NewProcessMessage"></a>

### NewProcessMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#plm-v1-ProcessType) |  |  |






<a name="plm-v1-StoredProcessMessage"></a>

### StoredProcessMessage
TODO: rename to recipe?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#plm-v1-ProcessType) |  |  |
| fixture_offset | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| root_sequence_id | [string](#string) |  | TODO: add calculated customization possibilities (or something like that) Then when loadProcess is called, a list with selected IDS must be selected/send with |






<a name="plm-v1-StoredProcessMessages"></a>

### StoredProcessMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| processes | [StoredProcessMessage](#plm-v1-StoredProcessMessage) | repeated |  |






<a name="plm-v1-UpdateProcessMessage"></a>

### UpdateProcessMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#plm-v1-ProcessType) |  |  |
| fixture_offset | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| root_sequence_id | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_process_load-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/process_load.proto



<a name="plm-v1-ProcessLoadMessage"></a>

### ProcessLoadMessage
TODO: Assign agents at runtime?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| process_id | [string](#string) |  |  |
| line_id | [string](#string) |  |  |
| order_id | [string](#string) |  |  |
| allocation_strategy | [AllocationStrategy](#plm-v1-AllocationStrategy) |  | TODO: list participating actors? |





 


<a name="plm-v1-AllocationStrategy"></a>

### AllocationStrategy


| Name | Number | Description |
| ---- | ------ | ----------- |
| ALLOCATION_STRATEGY_UNSPECIFIED | 0 |  |
| ALLOCATION_STRATEGY_STATIC | 1 |  |


 

 

 



<a name="plm_v1_requests-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/requests.proto



<a name="plm-v1-ProcessAtLocationMessage"></a>

### ProcessAtLocationMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| location_id | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_sequence_authoring-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/sequence_authoring.proto



<a name="plm-v1-NewSequenceMessage"></a>

### NewSequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |






<a name="plm-v1-StoredSequenceMessage"></a>

### StoredSequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| offset | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| sequence_ids | [string](#string) | repeated |  |
| task_ids | [string](#string) | repeated |  |
| can_bulk_complete | [bool](#bool) |  | TODO: if variant (or something) to allow for customizeable products |






<a name="plm-v1-StoredSequenceMessages"></a>

### StoredSequenceMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sequences | [StoredSequenceMessage](#plm-v1-StoredSequenceMessage) | repeated |  |






<a name="plm-v1-UpdateSequenceMessage"></a>

### UpdateSequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| offset | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| sequence_ids | [string](#string) | repeated |  |
| task_ids | [string](#string) | repeated |  |
| can_bulk_complete | [bool](#bool) |  |  |





 


<a name="plm-v1-SequenceType"></a>

### SequenceType


| Name | Number | Description |
| ---- | ------ | ----------- |
| SEQUENCE_TYPE_UNSPECIFIED | 0 |  |
| SEQUENCE_TYPE_ALL_OF_CHILDREN | 1 |  |
| SEQUENCE_TYPE_ONE_OF_CHILDREN | 2 |  |


 

 

 



<a name="plm_v1_sequence_complete-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/sequence_complete.proto



<a name="plm-v1-SequenceBulkCompleteMessage"></a>

### SequenceBulkCompleteMessage
Complete all tasks or or sub-sequences (TODO: should that be possible?)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| sequence_id | [string](#string) |  |  |
| agent_id | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_sequence_reassign-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/sequence_reassign.proto



<a name="plm-v1-SequenceReassignMessage"></a>

### SequenceReassignMessage
Reassign all sub-tasks to the assignee (if possible)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| sequence_id | [string](#string) |  |  |
| assignee | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_task_authoring-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/task_authoring.proto



<a name="plm-v1-NewTaskMessage"></a>

### NewTaskMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| parent_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |






<a name="plm-v1-StoredTaskMessage"></a>

### StoredTaskMessage
TODO: can this be made more generic, e.g. from a different pool of &#39;actions&#39; (screw, mount, ….), instead of creating a new stored step for each actual step.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| instruction_text | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| part_id | [string](#string) |  |  |
| model_id | [string](#string) |  |  |
| task_type | [TaskType](#plm-v1-TaskType) |  |  |
| target | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| approach | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| assignment_preference | [TaskAssignmentPreference](#plm-v1-TaskAssignmentPreference) |  |  |






<a name="plm-v1-StoredTaskMessages"></a>

### StoredTaskMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tasks | [StoredTaskMessage](#plm-v1-StoredTaskMessage) | repeated |  |






<a name="plm-v1-UpdateTaskMessage"></a>

### UpdateTaskMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| instruction_text | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| part_id | [string](#string) |  | TODO: what is the difference between part_id and model_id? doesn&#39;t all parts have a model? |
| model_id | [string](#string) |  |  |
| task_type | [TaskType](#plm-v1-TaskType) |  |  |
| target | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| approach | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| assignment_preference | [TaskAssignmentPreference](#plm-v1-TaskAssignmentPreference) |  |  |





 

 

 

 



<a name="plm_v1_task_progress-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/task_progress.proto



<a name="plm-v1-TaskProgressMessage"></a>

### TaskProgressMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| task_id | [string](#string) |  |  |
| agent_id | [string](#string) |  |  |
| message | [string](#string) |  |  |
| elapsed_time | [int32](#int32) |  | elapsed time in seconds |
| estimated_time_left | [int32](#int32) |  | estimated time left in seconds |





 

 

 

 



<a name="plm_v1_task_reassign-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/task_reassign.proto



<a name="plm-v1-TaskReassignMessage"></a>

### TaskReassignMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| task_id | [string](#string) |  |  |
| assignee | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_task_state_change-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/task_state_change.proto



<a name="plm-v1-TaskStateChangeMessage"></a>

### TaskStateChangeMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| task_id | [string](#string) |  |  |
| state | [TaskStateRequest](#plm-v1-TaskStateRequest) |  |  |





 


<a name="plm-v1-TaskStateRequest"></a>

### TaskStateRequest


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_STATE_REQUEST_UNSPECIFIED | 0 |  |
| TASK_STATE_REQUEST_IN_PROGRESS | 3 |  |
| TASK_STATE_REQUEST_COMPLETED | 4 |  |
| TASK_STATE_REQUEST_UNDO | 5 |  |
| TASK_STATE_REQUEST_ERROR | 6 |  |


 

 

 



<a name="plm_v1_tasks_list-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/tasks_list.proto



<a name="plm-v1-TasksForAgentRequest"></a>

### TasksForAgentRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| agent_id | [string](#string) |  |  |
| state | [TaskState](#plm-v1-TaskState) |  | Filter based on state. 0 (unspecified) returns all |






<a name="plm-v1-TasksForAgentResponse"></a>

### TasksForAgentResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| agent_id | [string](#string) |  |  |
| task_ids | [string](#string) | repeated |  |





 

 

 

 



<a name="plm_v1_tool-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/tool.proto



<a name="plm-v1-ToolMessage"></a>

### ToolMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ToolType](#plm-v1-ToolType) |  |  |
| actor | [ToolActor](#plm-v1-ToolActor) |  |  |
| properties | [ToolProperty](#plm-v1-ToolProperty) | repeated |  |
| model_id | [string](#string) |  |  |






<a name="plm-v1-ToolMessages"></a>

### ToolMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tools | [ToolMessage](#plm-v1-ToolMessage) | repeated |  |





 


<a name="plm-v1-ToolActor"></a>

### ToolActor


| Name | Number | Description |
| ---- | ------ | ----------- |
| TOOL_ACTOR_UNSPECIFIED | 0 |  |
| TOOL_ACTOR_HUMAN | 1 |  |
| TOOL_ACTOR_ROBOT | 2 |  |
| TOOL_ACTOR_HYBRID | 3 |  |



<a name="plm-v1-ToolProperty"></a>

### ToolProperty


| Name | Number | Description |
| ---- | ------ | ----------- |
| TOOL_PROPERTY_UNSPECIFIED | 0 |  |
| TOOL_PROPERTY_TORQUE_CONTROLLED | 1 |  |
| TOOL_PROPERTY_ESD_SAFE | 2 |  |
| TOOL_PROPERTY_INSULATED | 3 |  |
| TOOL_PROPERTY_COLLABORATIVE | 4 |  |



<a name="plm-v1-ToolType"></a>

### ToolType


| Name | Number | Description |
| ---- | ------ | ----------- |
| TOOL_TYPE_UNSPECIFIED | 0 |  |
| TOOL_TYPE_CUTTING | 10 |  |
| TOOL_TYPE_SHAPING | 20 |  |
| TOOL_TYPE_FASTENING | 30 |  |
| TOOL_TYPE_GRIPPING | 40 |  |
| TOOL_TYPE_TURNING | 50 |  |
| TOOL_TYPE_STRIKING | 60 |  |
| TOOL_TYPE_MEASURING | 70 |  |
| TOOL_TYPE_MARKING | 80 |  |
| TOOL_TYPE_FINISHING | 90 |  |
| TOOL_TYPE_ABRASIVE | 100 |  |
| TOOL_TYPE_SAFETY | 110 |  |
| TOOL_TYPE_ELECTRONICS | 120 | TODO: Cleaning, lubricating? |


 

 

 



<a name="robot_v1_end_effector-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/end_effector.proto



<a name="robot-v1-EndEffectorStateMessage"></a>

### EndEffectorStateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| live | [bool](#bool) |  |  |
| state | [string](#string) |  |  |





 

 

 

 



<a name="robot_v1_jointstate-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/jointstate.proto



<a name="robot-v1-JointStateMessage"></a>

### JointStateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| live | [bool](#bool) |  |  |
| position | [double](#double) | repeated |  |
| velocity | [double](#double) | repeated |  |





 

 

 

 



<a name="robot_v1_path-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/path.proto



<a name="robot-v1-PathMessage"></a>

### PathMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| robot_id | [string](#string) |  |  |
| points | [geometry.v1.Point](#geometry-v1-Point) | repeated |  |





 

 

 

 



<a name="robot_v1_popup-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/popup.proto



<a name="robot-v1-RobotHidePopupRequest"></a>

### RobotHidePopupRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| robot_id | [string](#string) |  |  |






<a name="robot-v1-RobotShowPopupRequest"></a>

### RobotShowPopupRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| robot_id | [string](#string) |  |  |
| text | [string](#string) |  |  |





 

 

 

 



<a name="robot_v1_program_state-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/program_state.proto



<a name="robot-v1-ProgramStateMessage"></a>

### ProgramStateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| state_code | [ProgramState](#robot-v1-ProgramState) |  |  |
| state | [string](#string) |  |  |
| program_file | [string](#string) |  |  |





 


<a name="robot-v1-ProgramState"></a>

### ProgramState


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROGRAM_STATE_UNSPECIFIED | 0 |  |
| PROGRAM_STATE_PLAY | 1 |  |
| PROGRAM_STATE_PAUSE | 2 |  |
| PROGRAM_STATE_STOP | 3 |  |


 

 

 



<a name="robot_v1_program_state_request-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/program_state_request.proto



<a name="robot-v1-ProgramStateRequest"></a>

### ProgramStateRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| robot_id | [string](#string) |  |  |
| state | [ProgramState](#robot-v1-ProgramState) |  |  |





 

 

 

 



<a name="robot_v1_robot_state-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/robot_state.proto



<a name="robot-v1-RobotStateMessage"></a>

### RobotStateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| state_code | [RobotState](#robot-v1-RobotState) |  |  |
| state | [string](#string) |  |  |
| target_speed | [double](#double) |  |  |
| actual_speed | [double](#double) |  |  |





 


<a name="robot-v1-RobotState"></a>

### RobotState


| Name | Number | Description |
| ---- | ------ | ----------- |
| ROBOT_STATE_UNSPECIFIED | 0 |  |
| ROBOT_STATE_STOPPING | 1 |  |
| ROBOT_STATE_STOPPED | 2 |  |
| ROBOT_STATE_PLAYING | 3 |  |
| ROBOT_STATE_PAUSING | 4 |  |
| ROBOT_STATE_PAUSED | 5 |  |
| ROBOT_STATE_RESUMING | 6 |  |


 

 

 



<a name="robot_v1_robot_visibility-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/robot_visibility.proto



<a name="robot-v1-RobotVisibilityMessage"></a>

### RobotVisibilityMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| base_visible | [bool](#bool) |  |  |
| upper_arm_visible | [bool](#bool) |  |  |
| forearm_visible | [bool](#bool) |  |  |
| wrist_visible | [bool](#bool) |  |  |
| end_effector_visible | [bool](#bool) |  |  |
| tcp_visible | [bool](#bool) |  |  |





 

 

 

 



<a name="robot_v1_tcp-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/tcp.proto



<a name="robot-v1-TcpMessage"></a>

### TcpMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| position | [geometry.v1.Point](#geometry-v1-Point) |  |  |
| orientation | [geometry.v1.Quad](#geometry-v1-Quad) |  |  |





 

 

 

 



<a name="robot_v1_waypoints-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/waypoints.proto



<a name="robot-v1-WaypointMessage"></a>

### WaypointMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| point | [geometry.v1.Point](#geometry-v1-Point) |  |  |






<a name="robot-v1-WaypointsMessage"></a>

### WaypointsMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| robot_id | [string](#string) |  |  |
| frame_id | [string](#string) |  |  |
| highlight_idx | [int32](#int32) |  |  |
| waypoints | [WaypointMessage](#robot-v1-WaypointMessage) | repeated |  |





 

 

 

 



<a name="robot_v1_zone-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/zone.proto



<a name="robot-v1-ZoneMessage"></a>

### ZoneMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| frame_id | [string](#string) |  |  |
| points | [geometry.v1.Point](#geometry-v1-Point) | repeated |  |





 

 

 

 



<a name="service_v1_ar_client-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## service/v1/ar_client.proto



<a name="service-v1-ARClientMessage"></a>

### ARClientMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| role | [ARClientRole](#service-v1-ARClientRole) |  |  |
| operator_id | [string](#string) |  |  |





 


<a name="service-v1-ARClientRole"></a>

### ARClientRole


| Name | Number | Description |
| ---- | ------ | ----------- |
| AR_CLIENT_ROLE_UNSPECIFIED | 0 |  |
| AR_CLIENT_ROLE_MAIN | 1 |  |
| AR_CLIENT_ROLE_SPECTATOR | 2 |  |


 

 

 



<a name="service_v1_response-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## service/v1/response.proto



<a name="service-v1-Response"></a>

### Response



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| success | [bool](#bool) |  | True if the request was carried out, false if an error occured |
| message | [string](#string) |  | Either a status/response message or an error message if the request wasn&#39;t a success |





 

 

 

 



<a name="service_v1_robot_adapter-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## service/v1/robot_adapter.proto



<a name="service-v1-RobotAdapterInfoMessage"></a>

### RobotAdapterInfoMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| robot_type | [string](#string) |  | TODO: use type enum? |
| identifier | [string](#string) |  |  |





 

 

 

 



<a name="service_v1_server-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## service/v1/server.proto



<a name="service-v1-ServerHeartbeat"></a>

### ServerHeartbeat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| service | [string](#string) |  | e.g. &#34;backend&#34; |
| server_id | [string](#string) |  | stable id (hostname/uuid) |
| epoch | [uint64](#uint64) |  | increments on restart (same concept as your restart storm protection) |
| unix_ms | [int64](#int64) |  | server time |
| ip | [string](#string) |  | ip of server |






<a name="service-v1-ServerInfo"></a>

### ServerInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| service | [string](#string) |  | E.g. &#34;backend&#34; |
| instance_id | [string](#string) |  | random UUID per process start |
| epoch | [uint64](#uint64) |  | Increments each restart (or derived) |
| started_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| reset_reason | [string](#string) |  | e.g. &#34;process_restart&#34;, &#34;db_wiped&#34; |
| data_wiped | [bool](#bool) |  | If true clients should strongly consider refetching data |





 

 

 

 



<a name="service_v1_status-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## service/v1/status.proto



<a name="service-v1-ServiceStatus"></a>

### ServiceStatus



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [string](#string) |  |  |
| ip | [string](#string) |  |  |
| status | [Status](#service-v1-Status) |  |  |





 


<a name="service-v1-Status"></a>

### Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS_UNSPECIFIED | 0 |  |
| STATUS_OFFLINE | 1 |  |
| STATUS_ONLINE | 2 |  |


 

 

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

