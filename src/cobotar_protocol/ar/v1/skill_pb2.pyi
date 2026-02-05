from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SkillLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKILL_LEVEL_UNSPECIFIED: _ClassVar[SkillLevel]
    SKILL_LEVEL_NOT_ALLOWED: _ClassVar[SkillLevel]
    SKILL_LEVEL_ASSISTED: _ClassVar[SkillLevel]
    SKILL_LEVEL_QUALIFIED: _ClassVar[SkillLevel]
    SKILL_LEVEL_EXPERT: _ClassVar[SkillLevel]
    SKILL_LEVEL_AUTHORITY: _ClassVar[SkillLevel]
SKILL_LEVEL_UNSPECIFIED: SkillLevel
SKILL_LEVEL_NOT_ALLOWED: SkillLevel
SKILL_LEVEL_ASSISTED: SkillLevel
SKILL_LEVEL_QUALIFIED: SkillLevel
SKILL_LEVEL_EXPERT: SkillLevel
SKILL_LEVEL_AUTHORITY: SkillLevel
