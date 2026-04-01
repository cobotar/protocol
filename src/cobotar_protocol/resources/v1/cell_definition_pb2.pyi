from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from resources.v1 import placement_pb2 as _placement_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CellStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CELL_STATUS_UNSPECIFIED: _ClassVar[CellStatus]
    CELL_STATUS_OPEN: _ClassVar[CellStatus]
    CELL_STATUS_BUSY: _ClassVar[CellStatus]
    CELL_STATUS_CLOSED: _ClassVar[CellStatus]
    CELL_STATUS_BLOCKED: _ClassVar[CellStatus]
CELL_STATUS_UNSPECIFIED: CellStatus
CELL_STATUS_OPEN: CellStatus
CELL_STATUS_BUSY: CellStatus
CELL_STATUS_CLOSED: CellStatus
CELL_STATUS_BLOCKED: CellStatus

class CellDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "status", "max_concurrent_processes", "allow_queued_process", "station_ids", "tools", "robots", "assets", "markers", "frame", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_PROCESSES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_QUEUED_PROCESS_FIELD_NUMBER: _ClassVar[int]
    STATION_IDS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    ROBOTS_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    MARKERS_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    status: CellStatus
    max_concurrent_processes: int
    allow_queued_process: bool
    station_ids: _containers.RepeatedScalarFieldContainer[str]
    tools: _containers.RepeatedCompositeFieldContainer[_placement_pb2.ToolPlacement]
    robots: _containers.RepeatedCompositeFieldContainer[_placement_pb2.RobotPlacement]
    assets: _containers.RepeatedCompositeFieldContainer[_placement_pb2.AssetPlacement]
    markers: _containers.RepeatedCompositeFieldContainer[_placement_pb2.MarkerPlacement]
    frame: _pose_pb2.LocalizedPose
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., status: _Optional[_Union[CellStatus, str]] = ..., max_concurrent_processes: _Optional[int] = ..., allow_queued_process: bool = ..., station_ids: _Optional[_Iterable[str]] = ..., tools: _Optional[_Iterable[_Union[_placement_pb2.ToolPlacement, _Mapping]]] = ..., robots: _Optional[_Iterable[_Union[_placement_pb2.RobotPlacement, _Mapping]]] = ..., assets: _Optional[_Iterable[_Union[_placement_pb2.AssetPlacement, _Mapping]]] = ..., markers: _Optional[_Iterable[_Union[_placement_pb2.MarkerPlacement, _Mapping]]] = ..., frame: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class CellDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CellDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[CellDefinition, _Mapping]]] = ...) -> None: ...
