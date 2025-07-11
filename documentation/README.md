# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [common/v1/property.proto](#common_v1_property-proto)
    - [Property](#common-v1-Property)
  
    - [PropertyOrigin](#common-v1-PropertyOrigin)
    - [PropertyType](#common-v1-PropertyType)
  
- [geometry/v1/point.proto](#geometry_v1_point-proto)
    - [Point](#geometry-v1-Point)
  
- [geometry/v1/quad.proto](#geometry_v1_quad-proto)
    - [Quad](#geometry-v1-Quad)
  
- [geometry/v1/pose.proto](#geometry_v1_pose-proto)
    - [LocalizedPose](#geometry-v1-LocalizedPose)
    - [Pose](#geometry-v1-Pose)
  
    - [LocalizedState](#geometry-v1-LocalizedState)
  
- [common/v1/agent.proto](#common_v1_agent-proto)
    - [Agent](#common-v1-Agent)
  
    - [AgentType](#common-v1-AgentType)
    - [EndEffectorType](#common-v1-EndEffectorType)
    - [OperatorPermission](#common-v1-OperatorPermission)
    - [OperatorType](#common-v1-OperatorType)
    - [RobotType](#common-v1-RobotType)
  
- [common/v1/capability.proto](#common_v1_capability-proto)
    - [Capabilities](#common-v1-Capabilities)
    - [Capability](#common-v1-Capability)
  
- [common/v1/color.proto](#common_v1_color-proto)
    - [Color](#common-v1-Color)
  
- [tracker/v1/tracker.proto](#tracker_v1_tracker-proto)
    - [Tracker](#tracker-v1-Tracker)
  
    - [TrackerType](#tracker-v1-TrackerType)
  
- [common/v1/configuration.proto](#common_v1_configuration-proto)
    - [AddConfigurationMessage](#common-v1-AddConfigurationMessage)
    - [ConfigurationMessage](#common-v1-ConfigurationMessage)
    - [LoadConfigurationMessage](#common-v1-LoadConfigurationMessage)
  
- [common/v1/configurations.proto](#common_v1_configurations-proto)
    - [ConfigurationInfoMessage](#common-v1-ConfigurationInfoMessage)
    - [ConfigurationInfoMessages](#common-v1-ConfigurationInfoMessages)
  
- [common/v1/delete.proto](#common_v1_delete-proto)
    - [DeleteMessage](#common-v1-DeleteMessage)
  
- [common/v1/template.proto](#common_v1_template-proto)
    - [TemplateMessage](#common-v1-TemplateMessage)
  
- [common/v1/templates.proto](#common_v1_templates-proto)
    - [TemplateInfoMessage](#common-v1-TemplateInfoMessage)
    - [TemplateInfoMessages](#common-v1-TemplateInfoMessages)
  
- [geometry/v1/anchor.proto](#geometry_v1_anchor-proto)
    - [Anchor](#geometry-v1-Anchor)
  
- [geometry/v1/vector3.proto](#geometry_v1_vector3-proto)
    - [Vector3](#geometry-v1-Vector3)
  
- [geometry/v1/wrench.proto](#geometry_v1_wrench-proto)
    - [Wrench](#geometry-v1-Wrench)
  
- [plm/v1/assembly.proto](#plm_v1_assembly-proto)
    - [LoadProcessMessage](#plm-v1-LoadProcessMessage)
    - [ReassignTaskMessage](#plm-v1-ReassignTaskMessage)
    - [UpdateTaskStateMessage](#plm-v1-UpdateTaskStateMessage)
  
    - [TaskStateRequest](#plm-v1-TaskStateRequest)
  
- [plm/v1/process.proto](#plm_v1_process-proto)
- [plm/v1/task.proto](#plm_v1_task-proto)
    - [TaskState](#plm-v1-TaskState)
  
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



<a name="common_v1_property-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/property.proto



<a name="common-v1-Property"></a>

### Property
Properties are used by various components to define them, such as: feedback, actions, and conditions.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [PropertyType](#common-v1-PropertyType) |  |  |
| value | [string](#string) |  | the current value of the property (JSON encoded) |
| extras | [string](#string) |  | JSON encoded extra values, e.g. {min: -0.1, max: 0.5, step: 0.1} for a double property. |
| user_editable | [bool](#bool) |  | TODO: create different user permissions, this field should then set the &#34;minimum required permission&#34; |
| origin | [PropertyOrigin](#common-v1-PropertyOrigin) |  |  |
| origins | [PropertyOrigin](#common-v1-PropertyOrigin) | repeated |  |
| mirror_property_id | [string](#string) |  |  |
| group | [string](#string) |  |  |
| ordering | [int32](#int32) |  |  |
| hide_group | [bool](#bool) |  |  |





 


<a name="common-v1-PropertyOrigin"></a>

### PropertyOrigin
Specifies where the value of a property originates from.

| Name | Number | Description |
| ---- | ------ | ----------- |
| PROPERTY_ORIGIN_UNSPECIFIED | 0 |  |
| PROPERTY_ORIGIN_FIXED | 1 | The value of the property is fixed and must be changed manually |
| PROPERTY_ORIGIN_MIRROR | 2 | The value of the property mirrors the value of another property |



<a name="common-v1-PropertyType"></a>

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
| PROPERTY_TYPE_AGENT | 10 |  |
| PROPERTY_TYPE_ENUM | 11 |  |
| PROPERTY_TYPE_ENUM_MULTI | 12 |  |


 

 

 



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
| pose | [Pose](#geometry-v1-Pose) |  |  |
| anchor_id | [string](#string) |  |  |
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
| LOCALIZED_STATE_UNKNOWN | 4 |  |


 

 

 



<a name="common_v1_agent-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/agent.proto



<a name="common-v1-Agent"></a>

### Agent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| type | [AgentType](#common-v1-AgentType) |  |  |
| operator_type | [OperatorType](#common-v1-OperatorType) |  |  |
| robot_type | [RobotType](#common-v1-RobotType) |  |  |
| end_effector_type | [EndEffectorType](#common-v1-EndEffectorType) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| properties | [Property](#common-v1-Property) | repeated |  |





 


<a name="common-v1-AgentType"></a>

### AgentType


| Name | Number | Description |
| ---- | ------ | ----------- |
| AGENT_TYPE_UNSPECIFIED | 0 |  |
| AGENT_TYPE_OPERATOR | 1 |  |
| AGENT_TYPE_ROBOT | 2 |  |



<a name="common-v1-EndEffectorType"></a>

### EndEffectorType


| Name | Number | Description |
| ---- | ------ | ----------- |
| END_EFFECTOR_TYPE_UNSPECIFIED | 0 |  |
| END_EFFECTOR_TYPE_EMPTY | 1 |  |
| END_EFFECTOR_TYPE_ROBOTIQ_HAND_E | 10 |  |
| END_EFFECTOR_TYPE_CUSTOM_MOUNT | 20 |  |



<a name="common-v1-OperatorPermission"></a>

### OperatorPermission


| Name | Number | Description |
| ---- | ------ | ----------- |
| OPERATOR_PERMISSION_UNSPECIFIED | 0 |  |
| OPERATOR_PERMISSION_NONE | 1 |  |
| OPERATOR_PERMISSION_COSMETIC | 2 |  |
| OPERATOR_PERMISSION_FULL | 3 |  |



<a name="common-v1-OperatorType"></a>

### OperatorType


| Name | Number | Description |
| ---- | ------ | ----------- |
| OPERATOR_TYPE_UNSPECIFIED | 0 |  |
| OPERATOR_TYPE_NOVICE | 1 |  |
| OPERATOR_TYPE_INTERMEDIATE | 2 |  |
| OPERATOR_TYPE_EXPERT | 3 |  |



<a name="common-v1-RobotType"></a>

### RobotType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ROBOT_TYPE_UNSPECIFIED | 0 |  |
| ROBOT_TYPE_UR3E | 10 |  |
| ROBOT_TYPE_UR5E | 11 |  |
| ROBOT_TYPE_UR10E | 12 |  |
| ROBOT_TYPE_KUKA_IIWA | 20 |  |


 

 

 



<a name="common_v1_capability-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/capability.proto



<a name="common-v1-Capabilities"></a>

### Capabilities



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| capabilities | [Capability](#common-v1-Capability) | repeated |  |






<a name="common-v1-Capability"></a>

### Capability



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| agent_id | [string](#string) |  | Id of the agent (either an operator or robot) |
| part_id | [string](#string) |  | Id of the part that the agent can handle |
| estimated_time | [int64](#int64) |  | Estimated time to complete a task with that part |





 

 

 

 



<a name="common_v1_color-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/color.proto



<a name="common-v1-Color"></a>

### Color
Represents a color. Where (1, 1, 1, 1) is solid white, (1, 0, 0, 0.5) is half transparent red, and so on.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| red | [float](#float) |  | Ranging from [0:1] |
| green | [float](#float) |  | Ranging from [0:1] |
| blue | [float](#float) |  | Ranging from [0:1] |
| alpha | [float](#float) |  | Ranging from [0:1] --&gt; [transparent : opaque] |





 

 

 

 



<a name="tracker_v1_tracker-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## tracker/v1/tracker.proto



<a name="tracker-v1-Tracker"></a>

### Tracker



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| reference | [string](#string) |  |  |
| frame | [string](#string) |  |  |
| type | [TrackerType](#tracker-v1-TrackerType) |  |  |
| marker_text | [string](#string) |  | TODO: add properties |





 


<a name="tracker-v1-TrackerType"></a>

### TrackerType


| Name | Number | Description |
| ---- | ------ | ----------- |
| TRACKER_TYPE_UNSPECIFIED | 0 |  |
| TRACKER_TYPE_QR_CODE | 1 |  |


 

 

 



<a name="common_v1_configuration-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/configuration.proto



<a name="common-v1-AddConfigurationMessage"></a>

### AddConfigurationMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  | Name of the new configuration |
| description | [string](#string) |  | A description of the new configuration |
| template_id | [string](#string) |  | Template id is used to pre-populate a configuration. Leave empty for a new fresh start. |






<a name="common-v1-ConfigurationMessage"></a>

### ConfigurationMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| instance_id | [string](#string) |  |  |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| agents | [Agent](#common-v1-Agent) | repeated |  |
| trackers | [tracker.v1.Tracker](#tracker-v1-Tracker) | repeated |  |
| properties | [Property](#common-v1-Property) | repeated | Feedback Actions |






<a name="common-v1-LoadConfigurationMessage"></a>

### LoadConfigurationMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  | Id of the configuration to be loaded |
| instance_id | [string](#string) |  | Instance id of the current loaded configuration - from the requestors perspective - used to avoid reloading a configuration. |





 

 

 

 



<a name="common_v1_configurations-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/configurations.proto



<a name="common-v1-ConfigurationInfoMessage"></a>

### ConfigurationInfoMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |






<a name="common-v1-ConfigurationInfoMessages"></a>

### ConfigurationInfoMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| configurations | [ConfigurationInfoMessage](#common-v1-ConfigurationInfoMessage) | repeated |  |





 

 

 

 



<a name="common_v1_delete-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/delete.proto



<a name="common-v1-DeleteMessage"></a>

### DeleteMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  | Id of the entity to be deleted |
| message | [string](#string) |  | Optional message |





 

 

 

 



<a name="common_v1_template-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/template.proto



<a name="common-v1-TemplateMessage"></a>

### TemplateMessage
TODO: consider this a bit more?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| agents | [Agent](#common-v1-Agent) | repeated |  |
| trackers | [tracker.v1.Tracker](#tracker-v1-Tracker) | repeated |  |
| properties | [Property](#common-v1-Property) | repeated | Feedback Actions |





 

 

 

 



<a name="common_v1_templates-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/templates.proto



<a name="common-v1-TemplateInfoMessage"></a>

### TemplateInfoMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |






<a name="common-v1-TemplateInfoMessages"></a>

### TemplateInfoMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| templates | [TemplateInfoMessage](#common-v1-TemplateInfoMessage) | repeated |  |





 

 

 

 



<a name="geometry_v1_anchor-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/anchor.proto



<a name="geometry-v1-Anchor"></a>

### Anchor



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reference | [string](#string) |  | Reference point towards an object or a thing, e.g. the environment, a robot, the user, ... |
| frame | [string](#string) |  | Frame is something in relation to the reference, e.g. wrist, tcp, left-hand, ... |





 

 

 

 



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





 

 

 

 



<a name="geometry_v1_wrench-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/wrench.proto



<a name="geometry-v1-Wrench"></a>

### Wrench



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| force | [Vector3](#geometry-v1-Vector3) |  |  |
| torque | [Vector3](#geometry-v1-Vector3) |  |  |





 

 

 

 



<a name="plm_v1_assembly-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/assembly.proto



<a name="plm-v1-LoadProcessMessage"></a>

### LoadProcessMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| process_id | [string](#string) |  |  |
| location_id | [string](#string) |  | TODO: What name should this be? |






<a name="plm-v1-ReassignTaskMessage"></a>

### ReassignTaskMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| task_id | [string](#string) |  |  |
| assignee | [string](#string) |  |  |






<a name="plm-v1-UpdateTaskStateMessage"></a>

### UpdateTaskStateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
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


 

 

 



<a name="plm_v1_process-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/process.proto


 

 

 

 



<a name="plm_v1_task-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/task.proto


 


<a name="plm-v1-TaskState"></a>

### TaskState


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_STATE_UNSPECIFIED | 0 |  |
| TASK_STATE_IN_MISSING_PRECONDITION | 1 |  |
| TASK_STATE_IN_WAITING | 2 |  |
| TASK_STATE_IN_PROGRESS | 3 |  |
| TASK_STATE_COMPLETED | 4 |  |
| TASK_STATE_ERROR | 6 |  |


 

 

 



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
| request_id | [string](#string) |  |  |
| success | [bool](#bool) |  | True if the request was carried out |
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

