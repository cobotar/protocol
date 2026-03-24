from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import enums_pb2 as _enums_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RobotInstance(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "robot_definition_id", "serial_number", "station_id", "mounted_tool_instance_id", "available_tool_instance_ids", "supports_tool_change", "is_simulated", "status", "base_pose", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROBOT_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_TOOL_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_TOOL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_TOOL_CHANGE_FIELD_NUMBER: _ClassVar[int]
    IS_SIMULATED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BASE_POSE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    robot_definition_id: str
    serial_number: str
    station_id: str
    mounted_tool_instance_id: str
    available_tool_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    supports_tool_change: bool
    is_simulated: bool
    status: _enums_pb2.ResourceStatus
    base_pose: _pose_pb2.LocalizedPose
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., robot_definition_id: _Optional[str] = ..., serial_number: _Optional[str] = ..., station_id: _Optional[str] = ..., mounted_tool_instance_id: _Optional[str] = ..., available_tool_instance_ids: _Optional[_Iterable[str]] = ..., supports_tool_change: bool = ..., is_simulated: bool = ..., status: _Optional[_Union[_enums_pb2.ResourceStatus, str]] = ..., base_pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class RobotInstances(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[RobotInstance]
    def __init__(self, items: _Optional[_Iterable[_Union[RobotInstance, _Mapping]]] = ...) -> None: ...
