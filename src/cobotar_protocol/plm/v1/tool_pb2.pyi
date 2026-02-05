from buf.validate import validate_pb2 as _validate_pb2
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
    TOOL_TYPE_CUTTING: _ClassVar[ToolType]
    TOOL_TYPE_SHAPING: _ClassVar[ToolType]
    TOOL_TYPE_FASTENING: _ClassVar[ToolType]
    TOOL_TYPE_GRIPPING: _ClassVar[ToolType]
    TOOL_TYPE_TURNING: _ClassVar[ToolType]
    TOOL_TYPE_STRIKING: _ClassVar[ToolType]
    TOOL_TYPE_MEASURING: _ClassVar[ToolType]
    TOOL_TYPE_MARKING: _ClassVar[ToolType]
    TOOL_TYPE_FINISHING: _ClassVar[ToolType]
    TOOL_TYPE_ABRASIVE: _ClassVar[ToolType]
    TOOL_TYPE_SAFETY: _ClassVar[ToolType]
    TOOL_TYPE_ELECTRONICS: _ClassVar[ToolType]

class ToolProperty(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOOL_PROPERTY_UNSPECIFIED: _ClassVar[ToolProperty]
    TOOL_PROPERTY_TORQUE_CONTROLLED: _ClassVar[ToolProperty]
    TOOL_PROPERTY_ESD_SAFE: _ClassVar[ToolProperty]
    TOOL_PROPERTY_INSULATED: _ClassVar[ToolProperty]
    TOOL_PROPERTY_COLLABORATIVE: _ClassVar[ToolProperty]

class ToolActor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOOL_ACTOR_UNSPECIFIED: _ClassVar[ToolActor]
    TOOL_ACTOR_HUMAN: _ClassVar[ToolActor]
    TOOL_ACTOR_ROBOT: _ClassVar[ToolActor]
    TOOL_ACTOR_HYBRID: _ClassVar[ToolActor]
TOOL_TYPE_UNSPECIFIED: ToolType
TOOL_TYPE_CUTTING: ToolType
TOOL_TYPE_SHAPING: ToolType
TOOL_TYPE_FASTENING: ToolType
TOOL_TYPE_GRIPPING: ToolType
TOOL_TYPE_TURNING: ToolType
TOOL_TYPE_STRIKING: ToolType
TOOL_TYPE_MEASURING: ToolType
TOOL_TYPE_MARKING: ToolType
TOOL_TYPE_FINISHING: ToolType
TOOL_TYPE_ABRASIVE: ToolType
TOOL_TYPE_SAFETY: ToolType
TOOL_TYPE_ELECTRONICS: ToolType
TOOL_PROPERTY_UNSPECIFIED: ToolProperty
TOOL_PROPERTY_TORQUE_CONTROLLED: ToolProperty
TOOL_PROPERTY_ESD_SAFE: ToolProperty
TOOL_PROPERTY_INSULATED: ToolProperty
TOOL_PROPERTY_COLLABORATIVE: ToolProperty
TOOL_ACTOR_UNSPECIFIED: ToolActor
TOOL_ACTOR_HUMAN: ToolActor
TOOL_ACTOR_ROBOT: ToolActor
TOOL_ACTOR_HYBRID: ToolActor

class ToolMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "actor", "properties", "model_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: ToolType
    actor: ToolActor
    properties: _containers.RepeatedScalarFieldContainer[ToolProperty]
    model_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[ToolType, str]] = ..., actor: _Optional[_Union[ToolActor, str]] = ..., properties: _Optional[_Iterable[_Union[ToolProperty, str]]] = ..., model_id: _Optional[str] = ...) -> None: ...

class ToolMessages(_message.Message):
    __slots__ = ("tools",)
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    tools: _containers.RepeatedCompositeFieldContainer[ToolMessage]
    def __init__(self, tools: _Optional[_Iterable[_Union[ToolMessage, _Mapping]]] = ...) -> None: ...
