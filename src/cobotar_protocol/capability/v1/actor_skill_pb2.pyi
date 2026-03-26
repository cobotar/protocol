import datetime

from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import actor_pb2 as _actor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKILL_LEVEL_UNSPECIFIED: _ClassVar[SkillLevel]
    SKILL_LEVEL_NOT_ALLOWED: _ClassVar[SkillLevel]
    SKILL_LEVEL_ASSISTED: _ClassVar[SkillLevel]
    SKILL_LEVEL_QUALIFIED: _ClassVar[SkillLevel]
    SKILL_LEVEL_EXPERT: _ClassVar[SkillLevel]
    SKILL_LEVEL_AUTHORITY: _ClassVar[SkillLevel]

class SkillStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKILL_STATUS_UNSPECIFIED: _ClassVar[SkillStatus]
    SKILL_STATUS_ACTIVE: _ClassVar[SkillStatus]
    SKILL_STATUS_RESTRICTED: _ClassVar[SkillStatus]
    SKILL_STATUS_EXPIRED: _ClassVar[SkillStatus]
SKILL_LEVEL_UNSPECIFIED: SkillLevel
SKILL_LEVEL_NOT_ALLOWED: SkillLevel
SKILL_LEVEL_ASSISTED: SkillLevel
SKILL_LEVEL_QUALIFIED: SkillLevel
SKILL_LEVEL_EXPERT: SkillLevel
SKILL_LEVEL_AUTHORITY: SkillLevel
SKILL_STATUS_UNSPECIFIED: SkillStatus
SKILL_STATUS_ACTIVE: SkillStatus
SKILL_STATUS_RESTRICTED: SkillStatus
SKILL_STATUS_EXPIRED: SkillStatus

class ValidityPolicyRef(_message.Message):
    __slots__ = ("policy_id", "version")
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    policy_id: str
    version: str
    def __init__(self, policy_id: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class ActorSkill(_message.Message):
    __slots__ = ("actor", "skill_id", "level", "status", "confidence", "last_evidence_at", "evidence_count", "valid_until", "validity_policy", "reasons", "next_actions")
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    LAST_EVIDENCE_AT_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_POLICY_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actor: _actor_pb2.ActorRef
    skill_id: str
    level: SkillLevel
    status: SkillStatus
    confidence: float
    last_evidence_at: _timestamp_pb2.Timestamp
    evidence_count: int
    valid_until: _timestamp_pb2.Timestamp
    validity_policy: ValidityPolicyRef
    reasons: _containers.RepeatedScalarFieldContainer[str]
    next_actions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ..., skill_id: _Optional[str] = ..., level: _Optional[_Union[SkillLevel, str]] = ..., status: _Optional[_Union[SkillStatus, str]] = ..., confidence: _Optional[float] = ..., last_evidence_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., evidence_count: _Optional[int] = ..., valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., validity_policy: _Optional[_Union[ValidityPolicyRef, _Mapping]] = ..., reasons: _Optional[_Iterable[str]] = ..., next_actions: _Optional[_Iterable[str]] = ...) -> None: ...
