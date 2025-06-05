# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [common/v1/color.proto](#common_v1_color-proto)
    - [Color](#common-v1-Color)

- [common/v1/property.proto](#common_v1_property-proto)
    - [Property](#common-v1-Property)

    - [Origin](#common-v1-Origin)
    - [PropertyType](#common-v1-PropertyType)

- [geometry/v1/anchor.proto](#geometry_v1_anchor-proto)
    - [Anchor](#geometry-v1-Anchor)

- [geometry/v1/point.proto](#geometry_v1_point-proto)
    - [Point](#geometry-v1-Point)

- [geometry/v1/quad.proto](#geometry_v1_quad-proto)
    - [Quad](#geometry-v1-Quad)

- [geometry/v1/pose.proto](#geometry_v1_pose-proto)
    - [Pose](#geometry-v1-Pose)

- [geometry/v1/vector3.proto](#geometry_v1_vector3-proto)
    - [Vector3](#geometry-v1-Vector3)

- [geometry/v1/wrench.proto](#geometry_v1_wrench-proto)
    - [Wrench](#geometry-v1-Wrench)

- [robot/v1/end_effector.proto](#robot_v1_end_effector-proto)
    - [EndEffector](#robot-v1-EndEffector)

- [robot/v1/jointstate.proto](#robot_v1_jointstate-proto)
    - [JointState](#robot-v1-JointState)

- [robot/v1/tcp.proto](#robot_v1_tcp-proto)
    - [Tcp](#robot-v1-Tcp)

- [service/v1/status.proto](#service_v1_status-proto)
    - [Info](#service-v1-Info)

    - [Status](#service-v1-Status)

- [tracker/v1/tracker.proto](#tracker_v1_tracker-proto)
    - [Tracker](#tracker-v1-Tracker)

    - [TrackerType](#tracker-v1-TrackerType)

- [Scalar Value Types](#scalar-value-types)



<a name="common_v1_color-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/color.proto



<a name="common-v1-Color"></a>

### Color



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| red | [float](#float) |  |  |
| green | [float](#float) |  |  |
| blue | [float](#float) |  |  |
| alpha | [float](#float) |  |  |















<a name="common_v1_property-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/property.proto



<a name="common-v1-Property"></a>

### Property



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [PropertyType](#common-v1-PropertyType) |  |  |
| value | [string](#string) |  |  |
| extras | [string](#string) |  |  |
| user_editable | [bool](#bool) |  |  |
| origin | [Origin](#common-v1-Origin) |  |  |
| origins | [Origin](#common-v1-Origin) | repeated |  |
| mirror_property_id | [string](#string) |  |  |
| group | [string](#string) |  |  |
| ordering | [int32](#int32) |  |  |
| hide_group | [bool](#bool) |  |  |








<a name="common-v1-Origin"></a>

### Origin


| Name | Number | Description |
| ---- | ------ | ----------- |
| ORIGIN_UNSPECIFIED | 0 |  |
| ORIGIN_FIXED | 1 |  |
| ORIGIN_MIRROR | 2 |  |



<a name="common-v1-PropertyType"></a>

### PropertyType


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROPERTY_TYPE_UNSPECIFIED | 0 |  |
| PROPERTY_TYPE_BOOL | 1 |  |
| PROPERTY_TYPE_INT | 2 |  |
| PROPERTY_TYPE_DOUBLE | 3 |  |
| PROPERTY_TYPE_STRING | 4 |  |
| PROPERTY_TYPE_VECTOR3 | 5 |  |
| PROPERTY_TYPE_POSE | 6 |  |
| PROPERTY_TYPE_ANCHOR | 7 |  |
| PROPERTY_TYPE_COLOR | 8 |  |
| PROPERTY_TYPE_AGENT | 9 |  |
| PROPERTY_TYPE_ENUM | 10 |  |
| PROPERTY_TYPE_ENUM_MULTI | 11 |  |










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



<a name="geometry-v1-Pose"></a>

### Pose



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [Point](#geometry-v1-Point) |  |  |
| orientation | [Quad](#geometry-v1-Quad) |  |  |















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















<a name="robot_v1_end_effector-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/end_effector.proto



<a name="robot-v1-EndEffector"></a>

### EndEffector



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| live | [bool](#bool) |  |  |
| state | [string](#string) |  |  |















<a name="robot_v1_jointstate-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/jointstate.proto



<a name="robot-v1-JointState"></a>

### JointState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| live | [bool](#bool) |  |  |
| position | [double](#double) | repeated |  |
| velocity | [double](#double) | repeated |  |















<a name="robot_v1_tcp-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/tcp.proto



<a name="robot-v1-Tcp"></a>

### Tcp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| position | [geometry.v1.Point](#geometry-v1-Point) |  |  |
| orientation | [geometry.v1.Quad](#geometry-v1-Quad) |  |  |















<a name="service_v1_status-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## service/v1/status.proto



<a name="service-v1-Info"></a>

### Info



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
