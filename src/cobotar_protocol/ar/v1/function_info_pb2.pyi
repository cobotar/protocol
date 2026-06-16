from ar.v1 import events_pb2 as _events_pb2
from ar.v1 import function_pb2 as _function_pb2
from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FunctionGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FUNCTION_GROUP_UNSPECIFIED: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_GENERAL: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_ROBOT: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_TASK: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_ENVIRONMENT: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_OPERATOR: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_SPATIAL: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_LOGIC: _ClassVar[FunctionGroup]
FUNCTION_GROUP_UNSPECIFIED: FunctionGroup
FUNCTION_GROUP_GENERAL: FunctionGroup
FUNCTION_GROUP_ROBOT: FunctionGroup
FUNCTION_GROUP_TASK: FunctionGroup
FUNCTION_GROUP_ENVIRONMENT: FunctionGroup
FUNCTION_GROUP_OPERATOR: FunctionGroup
FUNCTION_GROUP_SPATIAL: FunctionGroup
FUNCTION_GROUP_LOGIC: FunctionGroup

class FunctionInfoMessage(_message.Message):
    __slots__ = ("name", "icon", "description", "type", "group", "consumers_required", "consumers_optional", "required_handlers", "emits", "disabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    CONSUMERS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CONSUMERS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_HANDLERS_FIELD_NUMBER: _ClassVar[int]
    EMITS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    icon: str
    description: str
    type: _function_pb2.FunctionType
    group: FunctionGroup
    consumers_required: _containers.RepeatedCompositeFieldContainer[_events_pb2.ExchangeType]
    consumers_optional: _containers.RepeatedCompositeFieldContainer[_events_pb2.ExchangeType]
    required_handlers: _containers.RepeatedCompositeFieldContainer[_events_pb2.HandlerRequirement]
    emits: _containers.RepeatedCompositeFieldContainer[_events_pb2.ExchangeType]
    disabled: bool
    def __init__(self, name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_function_pb2.FunctionType, str]] = ..., group: _Optional[_Union[FunctionGroup, str]] = ..., consumers_required: _Optional[_Iterable[_Union[_events_pb2.ExchangeType, _Mapping]]] = ..., consumers_optional: _Optional[_Iterable[_Union[_events_pb2.ExchangeType, _Mapping]]] = ..., required_handlers: _Optional[_Iterable[_Union[_events_pb2.HandlerRequirement, _Mapping]]] = ..., emits: _Optional[_Iterable[_Union[_events_pb2.ExchangeType, _Mapping]]] = ..., disabled: bool = ...) -> None: ...

class FunctionInfoMessages(_message.Message):
    __slots__ = ("infos",)
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[FunctionInfoMessage]
    def __init__(self, infos: _Optional[_Iterable[_Union[FunctionInfoMessage, _Mapping]]] = ...) -> None: ...
