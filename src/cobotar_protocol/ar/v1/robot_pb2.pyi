from ar.v1 import property_pb2 as _property_pb2
from buf.validate import validate_pb2 as _validate_pb2
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
ROBOT_TYPE_UNSPECIFIED: RobotType
ROBOT_TYPE_UR3E: RobotType
ROBOT_TYPE_UR5E: RobotType
ROBOT_TYPE_UR10E: RobotType
ROBOT_TYPE_KUKA_IIWA: RobotType
ROBOT_DRIVER_TYPE_UNSPECIFIED: RobotDriverType
ROBOT_DRIVER_TYPE_UR: RobotDriverType

class RobotMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "robot_driver_type", "coupler_model_id", "end_effector_model_id", "properties")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROBOT_DRIVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUPLER_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    END_EFFECTOR_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: RobotType
    robot_driver_type: RobotDriverType
    coupler_model_id: str
    end_effector_model_id: str
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.Property]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[RobotType, str]] = ..., robot_driver_type: _Optional[_Union[RobotDriverType, str]] = ..., coupler_model_id: _Optional[str] = ..., end_effector_model_id: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.Property, _Mapping]]] = ...) -> None: ...

class RobotMessages(_message.Message):
    __slots__ = ("robots",)
    ROBOTS_FIELD_NUMBER: _ClassVar[int]
    robots: _containers.RepeatedCompositeFieldContainer[RobotMessage]
    def __init__(self, robots: _Optional[_Iterable[_Union[RobotMessage, _Mapping]]] = ...) -> None: ...
