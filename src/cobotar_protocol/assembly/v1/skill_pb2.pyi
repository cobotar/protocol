import datetime

from assembly.v1 import actor_pb2 as _actor_pb2
from assembly.v1 import common_pb2 as _common_pb2
from assembly.v1 import resources_pb2 as _resources_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillDomain(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKILL_DOMAIN_UNSPECIFIED: _ClassVar[SkillDomain]
    SKILL_DOMAIN_HANDLING: _ClassVar[SkillDomain]
    SKILL_DOMAIN_ASSEMBLY: _ClassVar[SkillDomain]
    SKILL_DOMAIN_FASTENING: _ClassVar[SkillDomain]
    SKILL_DOMAIN_INSPECTION: _ClassVar[SkillDomain]
    SKILL_DOMAIN_ELECTRICAL: _ClassVar[SkillDomain]
    SKILL_DOMAIN_COLLABORATION: _ClassVar[SkillDomain]
    SKILL_DOMAIN_SAFETY: _ClassVar[SkillDomain]
    SKILL_DOMAIN_ROBOT_OPERATION: _ClassVar[SkillDomain]

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
SKILL_DOMAIN_UNSPECIFIED: SkillDomain
SKILL_DOMAIN_HANDLING: SkillDomain
SKILL_DOMAIN_ASSEMBLY: SkillDomain
SKILL_DOMAIN_FASTENING: SkillDomain
SKILL_DOMAIN_INSPECTION: SkillDomain
SKILL_DOMAIN_ELECTRICAL: SkillDomain
SKILL_DOMAIN_COLLABORATION: SkillDomain
SKILL_DOMAIN_SAFETY: SkillDomain
SKILL_DOMAIN_ROBOT_OPERATION: SkillDomain
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

class SkillDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "domain", "tool_roles", "safety_relevance", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TOOL_ROLES_FIELD_NUMBER: _ClassVar[int]
    SAFETY_RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    domain: SkillDomain
    tool_roles: _containers.RepeatedScalarFieldContainer[_resources_pb2.ToolRole]
    safety_relevance: _common_pb2.SafetyRelevance
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., domain: _Optional[_Union[SkillDomain, str]] = ..., tool_roles: _Optional[_Iterable[_Union[_resources_pb2.ToolRole, str]]] = ..., safety_relevance: _Optional[_Union[_common_pb2.SafetyRelevance, str]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class SkillRequirement(_message.Message):
    __slots__ = ("skill_id", "minimum_level", "constraints")
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    minimum_level: SkillLevel
    constraints: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValueConstraint]
    def __init__(self, skill_id: _Optional[str] = ..., minimum_level: _Optional[_Union[SkillLevel, str]] = ..., constraints: _Optional[_Iterable[_Union[_common_pb2.KeyValueConstraint, _Mapping]]] = ...) -> None: ...

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

class ToolRequirement(_message.Message):
    __slots__ = ("role", "required_properties", "minimum_capability", "allowed_tool_definition_ids")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TOOL_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    role: _resources_pb2.ToolRole
    required_properties: _containers.RepeatedScalarFieldContainer[_resources_pb2.ToolProperty]
    minimum_capability: _resources_pb2.CapabilityProfile
    allowed_tool_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, role: _Optional[_Union[_resources_pb2.ToolRole, str]] = ..., required_properties: _Optional[_Iterable[_Union[_resources_pb2.ToolProperty, str]]] = ..., minimum_capability: _Optional[_Union[_resources_pb2.CapabilityProfile, _Mapping]] = ..., allowed_tool_definition_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ActorConstraint(_message.Message):
    __slots__ = ("allowed_actor_kinds", "collaboration_mode", "constraints")
    ALLOWED_ACTOR_KINDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATION_MODE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    allowed_actor_kinds: _containers.RepeatedScalarFieldContainer[_common_pb2.ActorKind]
    collaboration_mode: _common_pb2.CollaborationMode
    constraints: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValueConstraint]
    def __init__(self, allowed_actor_kinds: _Optional[_Iterable[_Union[_common_pb2.ActorKind, str]]] = ..., collaboration_mode: _Optional[_Union[_common_pb2.CollaborationMode, str]] = ..., constraints: _Optional[_Iterable[_Union[_common_pb2.KeyValueConstraint, _Mapping]]] = ...) -> None: ...
