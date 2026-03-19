from capability.v1 import capability_profile_pb2 as _capability_profile_pb2
from capability.v1 import skill_definition_pb2 as _skill_definition_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToolProperty(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOOL_PROPERTY_UNSPECIFIED: _ClassVar[ToolProperty]
    TOOL_PROPERTY_TORQUE_CONTROLLED: _ClassVar[ToolProperty]
    TOOL_PROPERTY_ESD_SAFE: _ClassVar[ToolProperty]
    TOOL_PROPERTY_INSULATED: _ClassVar[ToolProperty]
    TOOL_PROPERTY_COLLABORATIVE_SAFE: _ClassVar[ToolProperty]
    TOOL_PROPERTY_CALIBRATED: _ClassVar[ToolProperty]
    TOOL_PROPERTY_QUICK_CHANGE: _ClassVar[ToolProperty]
TOOL_PROPERTY_UNSPECIFIED: ToolProperty
TOOL_PROPERTY_TORQUE_CONTROLLED: ToolProperty
TOOL_PROPERTY_ESD_SAFE: ToolProperty
TOOL_PROPERTY_INSULATED: ToolProperty
TOOL_PROPERTY_COLLABORATIVE_SAFE: ToolProperty
TOOL_PROPERTY_CALIBRATED: ToolProperty
TOOL_PROPERTY_QUICK_CHANGE: ToolProperty

class ToolRequirement(_message.Message):
    __slots__ = ("role", "required_properties", "minimum_capability", "allowed_tool_definition_ids")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TOOL_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    role: _skill_definition_pb2.ToolRole
    required_properties: _containers.RepeatedScalarFieldContainer[ToolProperty]
    minimum_capability: _capability_profile_pb2.CapabilityProfile
    allowed_tool_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, role: _Optional[_Union[_skill_definition_pb2.ToolRole, str]] = ..., required_properties: _Optional[_Iterable[_Union[ToolProperty, str]]] = ..., minimum_capability: _Optional[_Union[_capability_profile_pb2.CapabilityProfile, _Mapping]] = ..., allowed_tool_definition_ids: _Optional[_Iterable[str]] = ...) -> None: ...
