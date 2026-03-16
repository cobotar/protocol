from assembly.v1 import common_pb2 as _common_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StationDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "tool_instance_ids", "container_instance_ids", "robot_instance_ids", "asset_instance_ids", "frame", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TOOL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    ROBOT_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    ASSET_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    tool_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    container_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    robot_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    asset_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    frame: _pose_pb2.LocalizedPose
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., tool_instance_ids: _Optional[_Iterable[str]] = ..., container_instance_ids: _Optional[_Iterable[str]] = ..., robot_instance_ids: _Optional[_Iterable[str]] = ..., asset_instance_ids: _Optional[_Iterable[str]] = ..., frame: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class CellDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "station_ids", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    STATION_IDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    station_ids: _containers.RepeatedScalarFieldContainer[str]
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., station_ids: _Optional[_Iterable[str]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...
