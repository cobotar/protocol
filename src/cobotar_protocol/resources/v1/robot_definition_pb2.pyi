from buf.validate import validate_pb2 as _validate_pb2
from capability.v1 import capability_profile_pb2 as _capability_profile_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RobotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_TYPE_UNSPECIFIED: _ClassVar[RobotType]
    ROBOT_TYPE_UR3E: _ClassVar[RobotType]
    ROBOT_TYPE_UR5E: _ClassVar[RobotType]
    ROBOT_TYPE_UR10E: _ClassVar[RobotType]
    ROBOT_TYPE_KUKA_IIWA: _ClassVar[RobotType]

class RobotDriverType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_DRIVER_TYPE_UNSPECIFIED: _ClassVar[RobotDriverType]
    ROBOT_DRIVER_TYPE_UR: _ClassVar[RobotDriverType]
    ROBOT_DRIVER_TYPE_GENERIC: _ClassVar[RobotDriverType]
ROBOT_TYPE_UNSPECIFIED: RobotType
ROBOT_TYPE_UR3E: RobotType
ROBOT_TYPE_UR5E: RobotType
ROBOT_TYPE_UR10E: RobotType
ROBOT_TYPE_KUKA_IIWA: RobotType
ROBOT_DRIVER_TYPE_UNSPECIFIED: RobotDriverType
ROBOT_DRIVER_TYPE_UR: RobotDriverType
ROBOT_DRIVER_TYPE_GENERIC: RobotDriverType

class RobotDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "driver_type", "model_id", "coupler_model_id", "supported_tool_definition_ids", "default_tool_definition_id", "tool_slots", "capability_profile", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DRIVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    COUPLER_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_TOOL_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TOOL_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_SLOTS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: RobotType
    driver_type: RobotDriverType
    model_id: str
    coupler_model_id: str
    supported_tool_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    default_tool_definition_id: str
    tool_slots: int
    capability_profile: _capability_profile_pb2.CapabilityProfile
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[RobotType, str]] = ..., driver_type: _Optional[_Union[RobotDriverType, str]] = ..., model_id: _Optional[str] = ..., coupler_model_id: _Optional[str] = ..., supported_tool_definition_ids: _Optional[_Iterable[str]] = ..., default_tool_definition_id: _Optional[str] = ..., tool_slots: _Optional[int] = ..., capability_profile: _Optional[_Union[_capability_profile_pb2.CapabilityProfile, _Mapping]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class RobotDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[RobotDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[RobotDefinition, _Mapping]]] = ...) -> None: ...
