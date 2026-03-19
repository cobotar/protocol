from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActorKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTOR_KIND_UNSPECIFIED: _ClassVar[ActorKind]
    ACTOR_KIND_HUMAN: _ClassVar[ActorKind]
    ACTOR_KIND_ROBOT: _ClassVar[ActorKind]
    ACTOR_KIND_HYBRID: _ClassVar[ActorKind]
ACTOR_KIND_UNSPECIFIED: ActorKind
ACTOR_KIND_HUMAN: ActorKind
ACTOR_KIND_ROBOT: ActorKind
ACTOR_KIND_HYBRID: ActorKind

class ActorRef(_message.Message):
    __slots__ = ("kind", "actor_id")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    kind: ActorKind
    actor_id: str
    def __init__(self, kind: _Optional[_Union[ActorKind, str]] = ..., actor_id: _Optional[str] = ...) -> None: ...
