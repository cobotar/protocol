from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LineType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINE_TYPE_UNSPECIFIED: _ClassVar[LineType]

class LineStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINE_STATUS_UNSPECIFIED: _ClassVar[LineStatus]
    LINE_STATUS_OPEN: _ClassVar[LineStatus]
    LINE_STATUS_BUSY: _ClassVar[LineStatus]
    LINE_STATUS_CLOSED: _ClassVar[LineStatus]
    LINE_STATUS_BLOCKED: _ClassVar[LineStatus]
LINE_TYPE_UNSPECIFIED: LineType
LINE_STATUS_UNSPECIFIED: LineStatus
LINE_STATUS_OPEN: LineStatus
LINE_STATUS_BUSY: LineStatus
LINE_STATUS_CLOSED: LineStatus
LINE_STATUS_BLOCKED: LineStatus

class LineDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "type", "status", "max_concurrent_processes", "cell_ids", "station_ids", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_PROCESSES_FIELD_NUMBER: _ClassVar[int]
    CELL_IDS_FIELD_NUMBER: _ClassVar[int]
    STATION_IDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    type: LineType
    status: LineStatus
    max_concurrent_processes: int
    cell_ids: _containers.RepeatedScalarFieldContainer[str]
    station_ids: _containers.RepeatedScalarFieldContainer[str]
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., type: _Optional[_Union[LineType, str]] = ..., status: _Optional[_Union[LineStatus, str]] = ..., max_concurrent_processes: _Optional[int] = ..., cell_ids: _Optional[_Iterable[str]] = ..., station_ids: _Optional[_Iterable[str]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class LineDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[LineDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[LineDefinition, _Mapping]]] = ...) -> None: ...
