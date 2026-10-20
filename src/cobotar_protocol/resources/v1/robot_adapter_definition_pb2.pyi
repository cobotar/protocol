from buf.validate import validate_pb2 as _validate_pb2
from resources.v1 import robot_definition_pb2 as _robot_definition_pb2
from robot.v1 import robot_adapter_pb2 as _robot_adapter_pb2
from robot.v1 import robot_io_catalog_pb2 as _robot_io_catalog_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RobotAdapterDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "adapter_type", "supported_robot_types", "commands", "telemetry", "plans", "configurable_io_register_kinds")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ROBOT_TYPES_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    PLANS_FIELD_NUMBER: _ClassVar[int]
    CONFIGURABLE_IO_REGISTER_KINDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    adapter_type: str
    supported_robot_types: _containers.RepeatedScalarFieldContainer[_robot_definition_pb2.RobotType]
    commands: _containers.RepeatedCompositeFieldContainer[_robot_adapter_pb2.RobotAdapterCommandCapability]
    telemetry: _containers.RepeatedCompositeFieldContainer[_robot_adapter_pb2.RobotAdapterTelemetryCapability]
    plans: _containers.RepeatedCompositeFieldContainer[_robot_adapter_pb2.RobotAdapterPlanCapability]
    configurable_io_register_kinds: _containers.RepeatedScalarFieldContainer[_robot_io_catalog_pb2.RobotIORegisterKind]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., adapter_type: _Optional[str] = ..., supported_robot_types: _Optional[_Iterable[_Union[_robot_definition_pb2.RobotType, str]]] = ..., commands: _Optional[_Iterable[_Union[_robot_adapter_pb2.RobotAdapterCommandCapability, _Mapping]]] = ..., telemetry: _Optional[_Iterable[_Union[_robot_adapter_pb2.RobotAdapterTelemetryCapability, _Mapping]]] = ..., plans: _Optional[_Iterable[_Union[_robot_adapter_pb2.RobotAdapterPlanCapability, _Mapping]]] = ..., configurable_io_register_kinds: _Optional[_Iterable[_Union[_robot_io_catalog_pb2.RobotIORegisterKind, str]]] = ...) -> None: ...

class RobotAdapterDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[RobotAdapterDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[RobotAdapterDefinition, _Mapping]]] = ...) -> None: ...
