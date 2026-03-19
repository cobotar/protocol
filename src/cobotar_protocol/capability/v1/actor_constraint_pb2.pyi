from common.v1 import actor_pb2 as _actor_pb2
from common.v1 import enums_pb2 as _enums_pb2
from common.v1 import key_value_constraint_pb2 as _key_value_constraint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActorConstraint(_message.Message):
    __slots__ = ("allowed_actor_kinds", "collaboration_mode", "constraints")
    ALLOWED_ACTOR_KINDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATION_MODE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    allowed_actor_kinds: _containers.RepeatedScalarFieldContainer[_actor_pb2.ActorKind]
    collaboration_mode: _enums_pb2.CollaborationMode
    constraints: _containers.RepeatedCompositeFieldContainer[_key_value_constraint_pb2.KeyValueConstraint]
    def __init__(self, allowed_actor_kinds: _Optional[_Iterable[_Union[_actor_pb2.ActorKind, str]]] = ..., collaboration_mode: _Optional[_Union[_enums_pb2.CollaborationMode, str]] = ..., constraints: _Optional[_Iterable[_Union[_key_value_constraint_pb2.KeyValueConstraint, _Mapping]]] = ...) -> None: ...
