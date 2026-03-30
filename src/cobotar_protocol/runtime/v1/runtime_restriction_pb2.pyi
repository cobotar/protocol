from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import actor_pb2 as _actor_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestrictionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTRICTION_TYPE_UNSPECIFIED: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_REQUIRE_AR_GUIDANCE: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_REQUIRE_MANUAL_CONFIRMATION: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_REQUIRE_SUPERVISOR_APPROVAL: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_REQUIRE_SECOND_CHECK: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_REQUIRE_VISION_VALIDATION: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_REQUIRE_TOOL_FEEDBACK: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_REQUIRE_HUMAN_ACTOR: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_REQUIRE_ROBOT_ACTOR: _ClassVar[RestrictionType]
RESTRICTION_TYPE_UNSPECIFIED: RestrictionType
RESTRICTION_TYPE_REQUIRE_AR_GUIDANCE: RestrictionType
RESTRICTION_TYPE_REQUIRE_MANUAL_CONFIRMATION: RestrictionType
RESTRICTION_TYPE_REQUIRE_SUPERVISOR_APPROVAL: RestrictionType
RESTRICTION_TYPE_REQUIRE_SECOND_CHECK: RestrictionType
RESTRICTION_TYPE_REQUIRE_VISION_VALIDATION: RestrictionType
RESTRICTION_TYPE_REQUIRE_TOOL_FEEDBACK: RestrictionType
RESTRICTION_TYPE_REQUIRE_HUMAN_ACTOR: RestrictionType
RESTRICTION_TYPE_REQUIRE_ROBOT_ACTOR: RestrictionType

class RuntimeRestriction(_message.Message):
    __slots__ = ("type", "reason", "source_skill_id", "source_policy_id", "actor")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    type: RestrictionType
    reason: str
    source_skill_id: str
    source_policy_id: str
    actor: _actor_pb2.ActorRef
    def __init__(self, type: _Optional[_Union[RestrictionType, str]] = ..., reason: _Optional[str] = ..., source_skill_id: _Optional[str] = ..., source_policy_id: _Optional[str] = ..., actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ...) -> None: ...
