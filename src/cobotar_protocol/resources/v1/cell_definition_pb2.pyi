from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
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
    __slots__ = ("id", "name", "description", "icon", "station_ids", "status", "max_concurrent_processes", "allow_queued_process", "tool_instance_ids", "container_instance_ids", "robot_instance_ids", "asset_instance_ids", "marker_instance_ids", "worker_ids", "frame", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    STATION_IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_PROCESSES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_QUEUED_PROCESS_FIELD_NUMBER: _ClassVar[int]
    TOOL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    ROBOT_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    ASSET_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    MARKER_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    WORKER_IDS_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    station_ids: _containers.RepeatedScalarFieldContainer[str]
    status: CellStatus
    max_concurrent_processes: int
    allow_queued_process: bool
    tool_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    container_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    robot_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    asset_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    marker_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    worker_ids: _containers.RepeatedScalarFieldContainer[str]
    frame: _pose_pb2.LocalizedPose
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., station_ids: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[CellStatus, str]] = ..., max_concurrent_processes: _Optional[int] = ..., allow_queued_process: bool = ..., tool_instance_ids: _Optional[_Iterable[str]] = ..., container_instance_ids: _Optional[_Iterable[str]] = ..., robot_instance_ids: _Optional[_Iterable[str]] = ..., asset_instance_ids: _Optional[_Iterable[str]] = ..., marker_instance_ids: _Optional[_Iterable[str]] = ..., worker_ids: _Optional[_Iterable[str]] = ..., frame: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class CellDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CellDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[CellDefinition, _Mapping]]] = ...) -> None: ...
