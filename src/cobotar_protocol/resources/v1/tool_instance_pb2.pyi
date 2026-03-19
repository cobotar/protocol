import datetime

from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import enums_pb2 as _enums_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToolInstance(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "tool_definition_id", "serial_number", "station_id", "status", "calibrated", "calibration_valid_until", "pose", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TOOL_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CALIBRATED_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    tool_definition_id: str
    serial_number: str
    station_id: str
    status: _enums_pb2.ResourceStatus
    calibrated: bool
    calibration_valid_until: _timestamp_pb2.Timestamp
    pose: _pose_pb2.LocalizedPose
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., tool_definition_id: _Optional[str] = ..., serial_number: _Optional[str] = ..., station_id: _Optional[str] = ..., status: _Optional[_Union[_enums_pb2.ResourceStatus, str]] = ..., calibrated: bool = ..., calibration_valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class ToolInstances(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ToolInstance]
    def __init__(self, items: _Optional[_Iterable[_Union[ToolInstance, _Mapping]]] = ...) -> None: ...
