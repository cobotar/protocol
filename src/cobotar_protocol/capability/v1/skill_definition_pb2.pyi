from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import enums_pb2 as _enums_pb2
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

class ToolRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOOL_ROLE_UNSPECIFIED: _ClassVar[ToolRole]
    TOOL_ROLE_GRIP_WORKPIECE: _ClassVar[ToolRole]
    TOOL_ROLE_POSITION_COMPONENT: _ClassVar[ToolRole]
    TOOL_ROLE_ALIGN_COMPONENT: _ClassVar[ToolRole]
    TOOL_ROLE_APPLY_TORQUE: _ClassVar[ToolRole]
    TOOL_ROLE_APPLY_LINEAR_FORCE: _ClassVar[ToolRole]
    TOOL_ROLE_MEASURE_DIMENSION: _ClassVar[ToolRole]
    TOOL_ROLE_DETECT_PRESENCE: _ClassVar[ToolRole]
    TOOL_ROLE_DISPENSE_MATERIAL: _ClassVar[ToolRole]
    TOOL_ROLE_EXECUTE_MOTION: _ClassVar[ToolRole]
    TOOL_ROLE_SAFETY_INTERACTION: _ClassVar[ToolRole]
    TOOL_ROLE_HANDLE_ESD: _ClassVar[ToolRole]
    TOOL_ROLE_VISUAL_INSPECTION: _ClassVar[ToolRole]
    TOOL_ROLE_WIPE_CLEAN: _ClassVar[ToolRole]
SKILL_DOMAIN_UNSPECIFIED: SkillDomain
SKILL_DOMAIN_HANDLING: SkillDomain
SKILL_DOMAIN_ASSEMBLY: SkillDomain
SKILL_DOMAIN_FASTENING: SkillDomain
SKILL_DOMAIN_INSPECTION: SkillDomain
SKILL_DOMAIN_ELECTRICAL: SkillDomain
SKILL_DOMAIN_COLLABORATION: SkillDomain
SKILL_DOMAIN_SAFETY: SkillDomain
SKILL_DOMAIN_ROBOT_OPERATION: SkillDomain
TOOL_ROLE_UNSPECIFIED: ToolRole
TOOL_ROLE_GRIP_WORKPIECE: ToolRole
TOOL_ROLE_POSITION_COMPONENT: ToolRole
TOOL_ROLE_ALIGN_COMPONENT: ToolRole
TOOL_ROLE_APPLY_TORQUE: ToolRole
TOOL_ROLE_APPLY_LINEAR_FORCE: ToolRole
TOOL_ROLE_MEASURE_DIMENSION: ToolRole
TOOL_ROLE_DETECT_PRESENCE: ToolRole
TOOL_ROLE_DISPENSE_MATERIAL: ToolRole
TOOL_ROLE_EXECUTE_MOTION: ToolRole
TOOL_ROLE_SAFETY_INTERACTION: ToolRole
TOOL_ROLE_HANDLE_ESD: ToolRole
TOOL_ROLE_VISUAL_INSPECTION: ToolRole
TOOL_ROLE_WIPE_CLEAN: ToolRole

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
    tool_roles: _containers.RepeatedScalarFieldContainer[ToolRole]
    safety_relevance: _enums_pb2.SafetyRelevance
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., domain: _Optional[_Union[SkillDomain, str]] = ..., tool_roles: _Optional[_Iterable[_Union[ToolRole, str]]] = ..., safety_relevance: _Optional[_Union[_enums_pb2.SafetyRelevance, str]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...
