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

class SkillInvalidityReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKILL_INVALIDITY_REASON_CODE_UNSPECIFIED: _ClassVar[SkillInvalidityReason]
    SKILL_INVALIDITY_REASON_CODE_INACTIVITY: _ClassVar[SkillInvalidityReason]
    SKILL_INVALIDITY_REASON_CODE_FAILURE_RATE: _ClassVar[SkillInvalidityReason]
    SKILL_INVALIDITY_REASON_CODE_POLICY_EXPIRED: _ClassVar[SkillInvalidityReason]
    SKILL_INVALIDITY_REASON_CODE_ENGINEERING_CHANGE: _ClassVar[SkillInvalidityReason]

class SkillNextAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKILL_NEXT_ACTION_UNSPECIFIED: _ClassVar[SkillNextAction]
    SKILL_NEXT_ACTION_MICRO_TRAINING: _ClassVar[SkillNextAction]
    SKILL_NEXT_ACTION_REFRESHER_TRAINING: _ClassVar[SkillNextAction]
    SKILL_NEXT_ACTION_RE_CERTIFICATION: _ClassVar[SkillNextAction]
    SKILL_NEXT_ACTION_EXTRA_VALIDATION_REQUIRED: _ClassVar[SkillNextAction]
    SKILL_NEXT_ACTION_SUPERVISOR_APPROVAL_REQUIRED: _ClassVar[SkillNextAction]
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
SKILL_INVALIDITY_REASON_CODE_UNSPECIFIED: SkillInvalidityReason
SKILL_INVALIDITY_REASON_CODE_INACTIVITY: SkillInvalidityReason
SKILL_INVALIDITY_REASON_CODE_FAILURE_RATE: SkillInvalidityReason
SKILL_INVALIDITY_REASON_CODE_POLICY_EXPIRED: SkillInvalidityReason
SKILL_INVALIDITY_REASON_CODE_ENGINEERING_CHANGE: SkillInvalidityReason
SKILL_NEXT_ACTION_UNSPECIFIED: SkillNextAction
SKILL_NEXT_ACTION_MICRO_TRAINING: SkillNextAction
SKILL_NEXT_ACTION_REFRESHER_TRAINING: SkillNextAction
SKILL_NEXT_ACTION_RE_CERTIFICATION: SkillNextAction
SKILL_NEXT_ACTION_EXTRA_VALIDATION_REQUIRED: SkillNextAction
SKILL_NEXT_ACTION_SUPERVISOR_APPROVAL_REQUIRED: SkillNextAction

class SkillEvidenceStats(_message.Message):
    __slots__ = ("success_count", "failure_count", "last_success_at", "last_failure_at", "last_activity_at", "rolling_success_rate")
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESS_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_FAILURE_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_AT_FIELD_NUMBER: _ClassVar[int]
    ROLLING_SUCCESS_RATE_FIELD_NUMBER: _ClassVar[int]
    success_count: int
    failure_count: int
    last_success_at: _timestamp_pb2.Timestamp
    last_failure_at: _timestamp_pb2.Timestamp
    last_activity_at: _timestamp_pb2.Timestamp
    rolling_success_rate: float
    def __init__(self, success_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., last_success_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_failure_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_activity_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rolling_success_rate: _Optional[float] = ...) -> None: ...

class ValidityPolicyRef(_message.Message):
    __slots__ = ("policy_id", "version")
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    policy_id: str
    version: str
    def __init__(self, policy_id: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class ActorSkill(_message.Message):
    __slots__ = ("id", "name", "icon", "actor", "skill_id", "level", "status", "confidence_score", "stats", "last_training_at", "last_certified_at", "valid_until", "validity_policy", "reasons", "next_actions")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    LAST_TRAINING_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_CERTIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_POLICY_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    actor: _actor_pb2.ActorRef
    skill_id: str
    level: SkillLevel
    status: SkillStatus
    confidence_score: float
    stats: SkillEvidenceStats
    last_training_at: _timestamp_pb2.Timestamp
    last_certified_at: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    validity_policy: ValidityPolicyRef
    reasons: _containers.RepeatedScalarFieldContainer[SkillInvalidityReason]
    next_actions: _containers.RepeatedScalarFieldContainer[SkillNextAction]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ..., skill_id: _Optional[str] = ..., level: _Optional[_Union[SkillLevel, str]] = ..., status: _Optional[_Union[SkillStatus, str]] = ..., confidence_score: _Optional[float] = ..., stats: _Optional[_Union[SkillEvidenceStats, _Mapping]] = ..., last_training_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_certified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., validity_policy: _Optional[_Union[ValidityPolicyRef, _Mapping]] = ..., reasons: _Optional[_Iterable[_Union[SkillInvalidityReason, str]]] = ..., next_actions: _Optional[_Iterable[_Union[SkillNextAction, str]]] = ...) -> None: ...

class ActorSkills(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ActorSkill]
    def __init__(self, items: _Optional[_Iterable[_Union[ActorSkill, _Mapping]]] = ...) -> None: ...
