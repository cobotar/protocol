from buf.validate import validate_pb2 as _validate_pb2
from capability.v1 import actor_skill_pb2 as _actor_skill_pb2
from common.v1 import key_value_constraint_pb2 as _key_value_constraint_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillRequirement(_message.Message):
    __slots__ = ("skill_id", "minimum_level", "constraints")
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    minimum_level: _actor_skill_pb2.SkillLevel
    constraints: _containers.RepeatedCompositeFieldContainer[_key_value_constraint_pb2.KeyValueConstraint]
    def __init__(self, skill_id: _Optional[str] = ..., minimum_level: _Optional[_Union[_actor_skill_pb2.SkillLevel, str]] = ..., constraints: _Optional[_Iterable[_Union[_key_value_constraint_pb2.KeyValueConstraint, _Mapping]]] = ...) -> None: ...
