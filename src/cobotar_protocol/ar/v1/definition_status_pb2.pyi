from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DefinitionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFINITION_STATUS_UNSPECIFIED: _ClassVar[DefinitionStatus]
    DEFINITION_STATUS_ACTIVE: _ClassVar[DefinitionStatus]
    DEFINITION_STATUS_DEPRECATED: _ClassVar[DefinitionStatus]
    DEFINITION_STATUS_DISABLED: _ClassVar[DefinitionStatus]
DEFINITION_STATUS_UNSPECIFIED: DefinitionStatus
DEFINITION_STATUS_ACTIVE: DefinitionStatus
DEFINITION_STATUS_DEPRECATED: DefinitionStatus
DEFINITION_STATUS_DISABLED: DefinitionStatus
