from buf.validate import validate_pb2 as _validate_pb2
from capability.v1 import capability_profile_pb2 as _capability_profile_pb2
from capability.v1 import skill_definition_pb2 as _skill_definition_pb2
from capability.v1 import tool_requirement_pb2 as _tool_requirement_pb2
from common.v1 import actor_pb2 as _actor_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import external_references_pb2 as _external_references_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToolType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOOL_TYPE_UNSPECIFIED: _ClassVar[ToolType]
    TOOL_TYPE_FASTENING: _ClassVar[ToolType]
    TOOL_TYPE_GRIPPING: _ClassVar[ToolType]
    TOOL_TYPE_CUTTING: _ClassVar[ToolType]
    TOOL_TYPE_MEASURING: _ClassVar[ToolType]
    TOOL_TYPE_POSITIONING: _ClassVar[ToolType]
    TOOL_TYPE_DISPENSING: _ClassVar[ToolType]
    TOOL_TYPE_INSPECTION: _ClassVar[ToolType]
    TOOL_TYPE_SAFETY: _ClassVar[ToolType]
    TOOL_TYPE_ELECTRONICS: _ClassVar[ToolType]
    TOOL_TYPE_FIXTURE_ACCESSORY: _ClassVar[ToolType]
    TOOL_TYPE_SHAPING: _ClassVar[ToolType]
    TOOL_TYPE_TURNING: _ClassVar[ToolType]
    TOOL_TYPE_STRIKING: _ClassVar[ToolType]
    TOOL_TYPE_MARKING: _ClassVar[ToolType]
    TOOL_TYPE_FINISHING: _ClassVar[ToolType]
    TOOL_TYPE_ABRASIVE: _ClassVar[ToolType]
    TOOL_TYPE_CLEANING: _ClassVar[ToolType]
TOOL_TYPE_UNSPECIFIED: ToolType
TOOL_TYPE_FASTENING: ToolType
TOOL_TYPE_GRIPPING: ToolType
TOOL_TYPE_CUTTING: ToolType
TOOL_TYPE_MEASURING: ToolType
TOOL_TYPE_POSITIONING: ToolType
TOOL_TYPE_DISPENSING: ToolType
TOOL_TYPE_INSPECTION: ToolType
TOOL_TYPE_SAFETY: ToolType
TOOL_TYPE_ELECTRONICS: ToolType
TOOL_TYPE_FIXTURE_ACCESSORY: ToolType
TOOL_TYPE_SHAPING: ToolType
TOOL_TYPE_TURNING: ToolType
TOOL_TYPE_STRIKING: ToolType
TOOL_TYPE_MARKING: ToolType
TOOL_TYPE_FINISHING: ToolType
TOOL_TYPE_ABRASIVE: ToolType
TOOL_TYPE_CLEANING: ToolType

class ToolDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "actor_kind", "roles", "properties", "capability_profile", "model_id", "external_references", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_KIND_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: ToolType
    actor_kind: _actor_pb2.ActorKind
    roles: _containers.RepeatedScalarFieldContainer[_skill_definition_pb2.ToolRole]
    properties: _containers.RepeatedScalarFieldContainer[_tool_requirement_pb2.ToolProperty]
    capability_profile: _capability_profile_pb2.CapabilityProfile
    model_id: str
    external_references: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[ToolType, str]] = ..., actor_kind: _Optional[_Union[_actor_pb2.ActorKind, str]] = ..., roles: _Optional[_Iterable[_Union[_skill_definition_pb2.ToolRole, str]]] = ..., properties: _Optional[_Iterable[_Union[_tool_requirement_pb2.ToolProperty, str]]] = ..., capability_profile: _Optional[_Union[_capability_profile_pb2.CapabilityProfile, _Mapping]] = ..., model_id: _Optional[str] = ..., external_references: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class ToolDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ToolDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[ToolDefinition, _Mapping]]] = ...) -> None: ...
