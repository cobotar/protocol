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
  
- [ar/v1/environment.proto](#ar_v1_environment-proto)
    - [AssetLocation](#ar-v1-AssetLocation)
    - [EnvironmentMessage](#ar-v1-EnvironmentMessage)
    - [EnvironmentMessages](#ar-v1-EnvironmentMessages)
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
    - [ARPriority](#ar-v1-ARPriority)
    - [MappingMessage](#ar-v1-MappingMessage)
    - [MappingMessages](#ar-v1-MappingMessages)
  
- [ar/v1/marker.proto](#ar_v1_marker-proto)
    - [MarkerMessage](#ar-v1-MarkerMessage)
    - [MarkerMessages](#ar-v1-MarkerMessages)
  
    - [MarkerType](#ar-v1-MarkerType)
  
- [ar/v1/robot.proto](#ar_v1_robot-proto)
    - [RobotMessage](#ar-v1-RobotMessage)
    - [RobotMessages](#ar-v1-RobotMessages)
  
    - [RobotDriverType](#ar-v1-RobotDriverType)
    - [RobotType](#ar-v1-RobotType)
  
- [ar/v1/skill.proto](#ar_v1_skill-proto)
    - [SkillLevel](#ar-v1-SkillLevel)
  
- [ar/v1/worker.proto](#ar_v1_worker-proto)
    - [WorkerMessage](#ar-v1-WorkerMessage)
    - [WorkerMessages](#ar-v1-WorkerMessages)
  
    - [WorkerType](#ar-v1-WorkerType)
  
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
  
- [plm/v1/line.proto](#plm_v1_line-proto)
    - [LineMessage](#plm-v1-LineMessage)
  
    - [LineType](#plm-v1-LineType)
  
- [plm/v1/model.proto](#plm_v1_model-proto)
    - [ModelMessage](#plm-v1-ModelMessage)
    - [ModelMessages](#plm-v1-ModelMessages)
  
    - [ModelGroup](#plm-v1-ModelGroup)
    - [ModelOrigin](#plm-v1-ModelOrigin)
  
- [plm/v1/part.proto](#plm_v1_part-proto)
    - [PartMessage](#plm-v1-PartMessage)
    - [PartMessages](#plm-v1-PartMessages)
  
    - [PartType](#plm-v1-PartType)
  
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
  
- [plm/v1/process.proto](#plm_v1_process-proto)
    - [ProcessMessage](#plm-v1-ProcessMessage)
    - [ProcessUpdatedMessage](#plm-v1-ProcessUpdatedMessage)
    - [ProcessesMessage](#plm-v1-ProcessesMessage)
  
    - [ProcessState](#plm-v1-ProcessState)
    - [ProcessType](#plm-v1-ProcessType)
  
- [plm/v1/process_abort.proto](#plm_v1_process_abort-proto)
    - [ProcessAbortMessage](#plm-v1-ProcessAbortMessage)
  
- [plm/v1/sequence_authoring.proto](#plm_v1_sequence_authoring-proto)
    - [DeleteSequenceMessage](#plm-v1-DeleteSequenceMessage)
    - [NewSequenceMessage](#plm-v1-NewSequenceMessage)
    - [StoredSequenceMessage](#plm-v1-StoredSequenceMessage)
    - [UpdateSequenceMessage](#plm-v1-UpdateSequenceMessage)
  
- [plm/v1/process_authoring.proto](#plm_v1_process_authoring-proto)
    - [DeleteProcessMessage](#plm-v1-DeleteProcessMessage)
    - [NewProcessMessage](#plm-v1-NewProcessMessage)
    - [StoredProcessMessage](#plm-v1-StoredProcessMessage)
    - [StoredProcessesMessage](#plm-v1-StoredProcessesMessage)
    - [UpdateProcessMessage](#plm-v1-UpdateProcessMessage)
  
- [plm/v1/process_load.proto](#plm_v1_process_load-proto)
    - [ProcessLoadMessage](#plm-v1-ProcessLoadMessage)
  
    - [AllocationStrategy](#plm-v1-AllocationStrategy)
  
- [plm/v1/requests.proto](#plm_v1_requests-proto)
    - [ProcessAtLocationMessage](#plm-v1-ProcessAtLocationMessage)
  
- [plm/v1/sequence_complete.proto](#plm_v1_sequence_complete-proto)
    - [SequenceBulkCompleteMessage](#plm-v1-SequenceBulkCompleteMessage)
  
- [plm/v1/sequence_reassign.proto](#plm_v1_sequence_reassign-proto)
    - [SequenceReassignMessage](#plm-v1-SequenceReassignMessage)
  
- [plm/v1/task_authoring.proto](#plm_v1_task_authoring-proto)
    - [DeleteTaskMessage](#plm-v1-DeleteTaskMessage)
    - [NewTaskMessage](#plm-v1-NewTaskMessage)
    - [StoredTaskMessage](#plm-v1-StoredTaskMessage)
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
| model_id_component | bool | .buf.validate.StringRules | 10001 |  |
| name_component | bool | .buf.validate.StringRules | 10000 |  |
| property_id_component | bool | .buf.validate.StringRules | 10003 |  |

 

 



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
| default | [common.v1.Color](#common-v1-Color) |  |  |






<a name="ar-v1-EnumExtras"></a>

### EnumExtras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| placeholder | [string](#string) |  |  |
| filter | [bool](#bool) |  |  |
| grouped | [bool](#bool) |  |  |
| show_icons | [bool](#bool) |  |  |
| max_selected_labels | [uint32](#uint32) |  |  |
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
| min | [double](#double) |  |  |
| max | [double](#double) |  |  |
| step | [double](#double) |  |  |
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






<a name="ar-v1-Vector3Extras"></a>

### Vector3Extras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min | [double](#double) |  |  |
| max | [double](#double) |  |  |
| step | [double](#double) |  |  |
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
| PROPERTY_TYPE_BOOL | 1 |  |
| PROPERTY_TYPE_INT | 2 |  |
| PROPERTY_TYPE_FLOAT | 3 |  |
| PROPERTY_TYPE_DOUBLE | 4 |  |
| PROPERTY_TYPE_STRING | 5 |  |
| PROPERTY_TYPE_VECTOR3 | 6 |  |
| PROPERTY_TYPE_POSE | 7 |  |
| PROPERTY_TYPE_ANCHOR | 8 |  |
| PROPERTY_TYPE_COLOR | 9 |  |
| PROPERTY_TYPE_ROBOT | 10 |  |
| PROPERTY_TYPE_ENUM | 11 |  |
| PROPERTY_TYPE_ENUM_MULTI | 12 |  |
| PROPERTY_TYPE_ICON | 13 |  |


 

 

 



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
| PLAN_TYPE_ROBOT_PATH | 100 |  |
| PLAN_TYPE_ROBOT_JOINT_ANGLES | 101 |  |
| PLAN_TYPE_ROBOT_WAYPOINTS | 102 |  |
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
| TELEMETRY_TYPE_ROBOT_TCP | 100 |  |
| TELEMETRY_TYPE_ROBOT_JOINT_ANGLES | 101 |  |
| TELEMETRY_TYPE_ROBOT_FORCE_TORQUE | 102 |  |
| TELEMETRY_TYPE_ROBOT_STATE | 110 |  |
| TELEMETRY_TYPE_ROBOT_PATH | 120 |  |
| TELEMETRY_TYPE_ROBOT_WAYPOINTS | 121 |  |


 

 

 



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
| type | [EnvironmentType](#ar-v1-EnvironmentType) |  |  |
| markers | [MarkerLocation](#ar-v1-MarkerLocation) | repeated | Markers associated with this environment. |
| robots | [RobotLocation](#ar-v1-RobotLocation) | repeated |  |
| assets | [AssetLocation](#ar-v1-AssetLocation) | repeated |  |
| parts | [PartLocation](#ar-v1-PartLocation) | repeated |  |
| tools | [ToolLocation](#ar-v1-ToolLocation) | repeated |  |
| properties | [Property](#ar-v1-Property) | repeated |  |






<a name="ar-v1-EnvironmentMessages"></a>

### EnvironmentMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| environments | [EnvironmentMessage](#ar-v1-EnvironmentMessage) | repeated |  |






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
| consumers_required | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs the action expects to receive |
| consumers_optional | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs that will enhance the action, but not needed to function |
| required_handlers | [HandlerRequirement](#ar-v1-HandlerRequirement) | repeated | Events that MUST have at least one handler somewhere else in the system. (i.e., if the action emits these, it expects the environment to react) |
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



<a name="ar-v1-ARPriority"></a>

### ARPriority



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ar_config_id | [string](#string) |  |  |
| active_property_id | [string](#string) |  |  |






<a name="ar-v1-MappingMessage"></a>

### MappingMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| environment_ids | [string](#string) | repeated |  |
| ar_config_priorities | [ARPriority](#ar-v1-ARPriority) | repeated |  |






<a name="ar-v1-MappingMessages"></a>

### MappingMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mappings | [MappingMessage](#ar-v1-MappingMessage) | repeated |  |





 

 

 

 



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


 

 

 



<a name="ar_v1_skill-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/skill.proto


 


<a name="ar-v1-SkillLevel"></a>

### SkillLevel


| Name | Number | Description |
| ---- | ------ | ----------- |
| SKILL_LEVEL_UNSPECIFIED | 0 |  |
| SKILL_LEVEL_NOT_ALLOWED | 1 | Human: Untrained, Robot: Not programmed |
| SKILL_LEVEL_ASSISTED | 2 | Human: AR-guided, Robot: Supervised execution |
| SKILL_LEVEL_QUALIFIED | 3 | Human: Certified operator, Robot: validated program |
| SKILL_LEVEL_EXPERT | 4 | Human: Technician, Robot: Optimized &amp; adaptive |
| SKILL_LEVEL_AUTHORITY | 5 | Human: Trainer, Robot: Self-adjusting |


 

 

 



<a name="ar_v1_worker-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/worker.proto



<a name="ar-v1-WorkerMessage"></a>

### WorkerMessage
TODO: Add worker (including skill-matrix)?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [WorkerType](#ar-v1-WorkerType) |  |  |
| permission | [WorkerPermission](#ar-v1-WorkerPermission) |  |  |
| properties | [Property](#ar-v1-Property) | repeated |  |
| disabled | [bool](#bool) |  | If disabled, the worker can&#39;t be selected |






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


 

 

 



<a name="plm_v1_model-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/model.proto



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


 

 

 



<a name="plm_v1_sequence-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/sequence.proto



<a name="plm-v1-SequenceMessage"></a>

### SequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int64](#int64) |  |  |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| parent_id | [string](#string) |  |  |
| sequence_ids | [string](#string) | repeated |  |
| task_ids | [string](#string) | repeated |  |
| assigned_to | [string](#string) | repeated |  |
| state | [SequenceState](#plm-v1-SequenceState) |  |  |
| completed_tasks | [int64](#int64) |  |  |
| can_bulk_complete | [bool](#bool) |  |  |






<a name="plm-v1-SequenceUpdatedMessage"></a>

### SequenceUpdatedMessage
Update published when the state of a sequence have changed


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sequence_id | [string](#string) |  |  |
| assigned_to | [string](#string) | repeated |  |
| state | [SequenceState](#plm-v1-SequenceState) |  |  |
| completed_tasks | [int64](#int64) |  |  |





 


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
| description | [string](#string) |  | TODO: rename to instruction_text |
| sequence_number | [int64](#int64) |  |  |
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
| can_undo | [bool](#bool) |  | TODO: &#39;complete-importance&#39;: could be different levels of &#34;this must be explicitly completed&#34; or tie it together with user level, such that expertise level (expert, intermediate, novice) equal and above intermediate can {bulk, automatic, ... } complete and below must explicitly complete. This should potentially also be tied to the part and this field(s) can then be a custom override for this specific task. |






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


 

 

 



<a name="plm_v1_process-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/process.proto



<a name="plm-v1-ProcessMessage"></a>

### ProcessMessage
TODO: should &#39;running&#39; be called process and &#39;static&#39; recipe?
TODO: Add/assign the agent(s) at runtime, instead of allocating them to the environment. THen there could also be a situation where each agent is asked to take a task during execution.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| instance_id | [string](#string) |  |  |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
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






<a name="plm-v1-ProcessUpdatedMessage"></a>

### ProcessUpdatedMessage
Update published when the state of a process have changed


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| instance_id | [string](#string) |  |  |
| id | [string](#string) |  |  |
| state | [ProcessState](#plm-v1-ProcessState) |  |  |
| ended | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |






<a name="plm-v1-ProcessesMessage"></a>

### ProcessesMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| processes | [ProcessMessage](#plm-v1-ProcessMessage) | repeated |  |





 


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





 

 

 

 



<a name="plm_v1_sequence_authoring-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/sequence_authoring.proto



<a name="plm-v1-DeleteSequenceMessage"></a>

### DeleteSequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sequence_id | [string](#string) |  |  |






<a name="plm-v1-NewSequenceMessage"></a>

### NewSequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| parent_id | [string](#string) |  |  |






<a name="plm-v1-StoredSequenceMessage"></a>

### StoredSequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int64](#int64) |  |  |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| parent_id | [string](#string) |  |  |
| sequence_ids | [string](#string) | repeated |  |
| task_ids | [string](#string) | repeated |  |
| can_bulk_complete | [bool](#bool) |  |  |






<a name="plm-v1-UpdateSequenceMessage"></a>

### UpdateSequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int64](#int64) |  |  |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| parent_id | [string](#string) |  |  |
| sequence_ids | [string](#string) | repeated |  |
| task_ids | [string](#string) | repeated |  |
| can_bulk_complete | [bool](#bool) |  |  |





 

 

 

 



<a name="plm_v1_process_authoring-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/process_authoring.proto



<a name="plm-v1-DeleteProcessMessage"></a>

### DeleteProcessMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| process_id | [string](#string) |  |  |






<a name="plm-v1-NewProcessMessage"></a>

### NewProcessMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#plm-v1-ProcessType) |  |  |






<a name="plm-v1-StoredProcessMessage"></a>

### StoredProcessMessage
TODO: rename to recipe?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#plm-v1-ProcessType) |  |  |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| root_sequence_id | [string](#string) |  |  |
| sequences | [StoredSequenceMessage](#plm-v1-StoredSequenceMessage) | repeated |  |
| tasks | [TaskMessage](#plm-v1-TaskMessage) | repeated | TODO: make &#39;interchanceable&#39;, such that multiple variants can be selected |






<a name="plm-v1-StoredProcessesMessage"></a>

### StoredProcessesMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| processes | [StoredProcessMessage](#plm-v1-StoredProcessMessage) | repeated |  |






<a name="plm-v1-UpdateProcessMessage"></a>

### UpdateProcessMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#plm-v1-ProcessType) |  |  |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
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



<a name="plm-v1-DeleteTaskMessage"></a>

### DeleteTaskMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_id | [string](#string) |  |  |






<a name="plm-v1-NewTaskMessage"></a>

### NewTaskMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int64](#int64) |  |  |
| parent_sequence_id | [string](#string) |  |  |






<a name="plm-v1-StoredTaskMessage"></a>

### StoredTaskMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int64](#int64) |  |  |
| part_id | [string](#string) |  |  |
| model_id | [string](#string) |  |  |
| task_type | [TaskType](#plm-v1-TaskType) |  |  |
| target | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| approach | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| assignment_preference | [TaskAssignmentPreference](#plm-v1-TaskAssignmentPreference) |  |  |






<a name="plm-v1-UpdateTaskMessage"></a>

### UpdateTaskMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int64](#int64) |  |  |
| part_id | [string](#string) |  |  |
| model_id | [string](#string) |  |  |
| task_type | [TaskType](#plm-v1-TaskType) |  |  |
| target | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
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
| elapsed_time | [int64](#int64) |  |  |
| estimated_time_left | [int64](#int64) |  |  |





 

 

 

 



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
| TOOL_TYPE_ELECTRONICS | 120 |  |


 

 

 



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

