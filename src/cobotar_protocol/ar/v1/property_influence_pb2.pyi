from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssistanceScalingAxis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSISTANCE_SCALING_AXIS_UNSPECIFIED: _ClassVar[AssistanceScalingAxis]
    ASSISTANCE_SCALING_AXIS_PRESENTATION: _ClassVar[AssistanceScalingAxis]
    ASSISTANCE_SCALING_AXIS_SEMANTIC_DETAIL: _ClassVar[AssistanceScalingAxis]
    ASSISTANCE_SCALING_AXIS_SCOPE: _ClassVar[AssistanceScalingAxis]

class PropertyInfluenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROPERTY_INFLUENCE_TYPE_UNSPECIFIED: _ClassVar[PropertyInfluenceType]
    PROPERTY_INFLUENCE_TYPE_MODULATES: _ClassVar[PropertyInfluenceType]
    PROPERTY_INFLUENCE_TYPE_ENABLES: _ClassVar[PropertyInfluenceType]
    PROPERTY_INFLUENCE_TYPE_SELECTS: _ClassVar[PropertyInfluenceType]
ASSISTANCE_SCALING_AXIS_UNSPECIFIED: AssistanceScalingAxis
ASSISTANCE_SCALING_AXIS_PRESENTATION: AssistanceScalingAxis
ASSISTANCE_SCALING_AXIS_SEMANTIC_DETAIL: AssistanceScalingAxis
ASSISTANCE_SCALING_AXIS_SCOPE: AssistanceScalingAxis
PROPERTY_INFLUENCE_TYPE_UNSPECIFIED: PropertyInfluenceType
PROPERTY_INFLUENCE_TYPE_MODULATES: PropertyInfluenceType
PROPERTY_INFLUENCE_TYPE_ENABLES: PropertyInfluenceType
PROPERTY_INFLUENCE_TYPE_SELECTS: PropertyInfluenceType

class PropertyInfluence(_message.Message):
    __slots__ = ("property_key", "axis", "influence")
    PROPERTY_KEY_FIELD_NUMBER: _ClassVar[int]
    AXIS_FIELD_NUMBER: _ClassVar[int]
    INFLUENCE_FIELD_NUMBER: _ClassVar[int]
    property_key: str
    axis: AssistanceScalingAxis
    influence: PropertyInfluenceType
    def __init__(self, property_key: _Optional[str] = ..., axis: _Optional[_Union[AssistanceScalingAxis, str]] = ..., influence: _Optional[_Union[PropertyInfluenceType, str]] = ...) -> None: ...
