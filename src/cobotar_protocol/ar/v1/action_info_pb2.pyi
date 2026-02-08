from ar.v1 import action_pb2 as _action_pb2
from ar.v1 import events_pb2 as _events_pb2
from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_GROUP_UNSPECIFIED: _ClassVar[ActionGroup]
    ACTION_GROUP_GENERAL: _ClassVar[ActionGroup]
    ACTION_GROUP_ROBOT: _ClassVar[ActionGroup]
    ACTION_GROUP_TASK: _ClassVar[ActionGroup]
ACTION_GROUP_UNSPECIFIED: ActionGroup
ACTION_GROUP_GENERAL: ActionGroup
ACTION_GROUP_ROBOT: ActionGroup
ACTION_GROUP_TASK: ActionGroup

class ActionInfoMessage(_message.Message):
    __slots__ = ("name", "icon", "description", "type", "group", "require_agent", "consumers_required", "consumers_optional", "required_handlers", "emits", "disabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_AGENT_FIELD_NUMBER: _ClassVar[int]
    CONSUMERS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CONSUMERS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_HANDLERS_FIELD_NUMBER: _ClassVar[int]
    EMITS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    icon: str
    description: str
    type: _action_pb2.ActionType
    group: ActionGroup
    require_agent: bool
    consumers_required: _containers.RepeatedCompositeFieldContainer[_events_pb2.ExchangeType]
    consumers_optional: _containers.RepeatedCompositeFieldContainer[_events_pb2.ExchangeType]
    required_handlers: _containers.RepeatedCompositeFieldContainer[_events_pb2.HandlerRequirement]
    emits: _containers.RepeatedCompositeFieldContainer[_events_pb2.ExchangeType]
    disabled: bool
    def __init__(self, name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_action_pb2.ActionType, str]] = ..., group: _Optional[_Union[ActionGroup, str]] = ..., require_agent: bool = ..., consumers_required: _Optional[_Iterable[_Union[_events_pb2.ExchangeType, _Mapping]]] = ..., consumers_optional: _Optional[_Iterable[_Union[_events_pb2.ExchangeType, _Mapping]]] = ..., required_handlers: _Optional[_Iterable[_Union[_events_pb2.HandlerRequirement, _Mapping]]] = ..., emits: _Optional[_Iterable[_Union[_events_pb2.ExchangeType, _Mapping]]] = ..., disabled: bool = ...) -> None: ...

class ActionInfoMessages(_message.Message):
    __slots__ = ("infos",)
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[ActionInfoMessage]
    def __init__(self, infos: _Optional[_Iterable[_Union[ActionInfoMessage, _Mapping]]] = ...) -> None: ...
