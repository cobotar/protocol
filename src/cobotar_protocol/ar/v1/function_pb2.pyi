from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FunctionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FUNCTION_TYPE_UNSPECIFIED: _ClassVar[FunctionType]
    FUNCTION_TYPE_PROXIMITY: _ClassVar[FunctionType]
    FUNCTION_TYPE_STATIONARY: _ClassVar[FunctionType]
    FUNCTION_TYPE_TIMER: _ClassVar[FunctionType]
    FUNCTION_TYPE_PART_FOR_TASK: _ClassVar[FunctionType]
    FUNCTION_TYPE_IS_PART_OF_TYPE: _ClassVar[FunctionType]
    FUNCTION_TYPE_STRING_FORMAT_1: _ClassVar[FunctionType]
    FUNCTION_TYPE_STRING_FORMAT_2: _ClassVar[FunctionType]
    FUNCTION_TYPE_AND: _ClassVar[FunctionType]
    FUNCTION_TYPE_OR: _ClassVar[FunctionType]
    FUNCTION_TYPE_NOT: _ClassVar[FunctionType]
FUNCTION_TYPE_UNSPECIFIED: FunctionType
FUNCTION_TYPE_PROXIMITY: FunctionType
FUNCTION_TYPE_STATIONARY: FunctionType
FUNCTION_TYPE_TIMER: FunctionType
FUNCTION_TYPE_PART_FOR_TASK: FunctionType
FUNCTION_TYPE_IS_PART_OF_TYPE: FunctionType
FUNCTION_TYPE_STRING_FORMAT_1: FunctionType
FUNCTION_TYPE_STRING_FORMAT_2: FunctionType
FUNCTION_TYPE_AND: FunctionType
FUNCTION_TYPE_OR: FunctionType
FUNCTION_TYPE_NOT: FunctionType

class FunctionMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "config_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: FunctionType
    config_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[FunctionType, str]] = ..., config_id: _Optional[str] = ...) -> None: ...

class FunctionMessages(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FunctionMessage]
    def __init__(self, items: _Optional[_Iterable[_Union[FunctionMessage, _Mapping]]] = ...) -> None: ...

class FunctionAddMessage(_message.Message):
    __slots__ = ("config_id", "name", "icon", "description", "type")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    config_id: str
    name: str
    icon: str
    description: str
    type: FunctionType
    def __init__(self, config_id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[FunctionType, str]] = ...) -> None: ...

class FunctionUpdateMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
