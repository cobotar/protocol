from buf.validate import validate_pb2 as _validate_pb2
from robot.v1 import robot_io_catalog_pb2 as _robot_io_catalog_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RobotAdapterCommandType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_ADAPTER_COMMAND_TYPE_UNSPECIFIED: _ClassVar[RobotAdapterCommandType]
    ROBOT_ADAPTER_COMMAND_TYPE_PROGRAM_PLAY: _ClassVar[RobotAdapterCommandType]
    ROBOT_ADAPTER_COMMAND_TYPE_PROGRAM_PAUSE: _ClassVar[RobotAdapterCommandType]
    ROBOT_ADAPTER_COMMAND_TYPE_PROGRAM_STOP: _ClassVar[RobotAdapterCommandType]
    ROBOT_ADAPTER_COMMAND_TYPE_ACKNOWLEDGE: _ClassVar[RobotAdapterCommandType]
    ROBOT_ADAPTER_COMMAND_TYPE_SHOW_POPUP: _ClassVar[RobotAdapterCommandType]
    ROBOT_ADAPTER_COMMAND_TYPE_HIDE_POPUP: _ClassVar[RobotAdapterCommandType]
    ROBOT_ADAPTER_COMMAND_TYPE_LOAD_PROGRAM: _ClassVar[RobotAdapterCommandType]
    ROBOT_ADAPTER_COMMAND_TYPE_LOAD_INSTALLATION: _ClassVar[RobotAdapterCommandType]
    ROBOT_ADAPTER_COMMAND_TYPE_POWER_ON: _ClassVar[RobotAdapterCommandType]
    ROBOT_ADAPTER_COMMAND_TYPE_POWER_OFF: _ClassVar[RobotAdapterCommandType]
    ROBOT_ADAPTER_COMMAND_TYPE_BRAKE_RELEASE: _ClassVar[RobotAdapterCommandType]

class RobotAdapterTelemetryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_ADAPTER_TELEMETRY_TYPE_UNSPECIFIED: _ClassVar[RobotAdapterTelemetryType]
    ROBOT_ADAPTER_TELEMETRY_TYPE_ROBOT_STATE: _ClassVar[RobotAdapterTelemetryType]
    ROBOT_ADAPTER_TELEMETRY_TYPE_JOINT_STATE: _ClassVar[RobotAdapterTelemetryType]
    ROBOT_ADAPTER_TELEMETRY_TYPE_TCP_POSE: _ClassVar[RobotAdapterTelemetryType]
    ROBOT_ADAPTER_TELEMETRY_TYPE_TCP_WRENCH: _ClassVar[RobotAdapterTelemetryType]
    ROBOT_ADAPTER_TELEMETRY_TYPE_IO_STATE: _ClassVar[RobotAdapterTelemetryType]
ROBOT_ADAPTER_COMMAND_TYPE_UNSPECIFIED: RobotAdapterCommandType
ROBOT_ADAPTER_COMMAND_TYPE_PROGRAM_PLAY: RobotAdapterCommandType
ROBOT_ADAPTER_COMMAND_TYPE_PROGRAM_PAUSE: RobotAdapterCommandType
ROBOT_ADAPTER_COMMAND_TYPE_PROGRAM_STOP: RobotAdapterCommandType
ROBOT_ADAPTER_COMMAND_TYPE_ACKNOWLEDGE: RobotAdapterCommandType
ROBOT_ADAPTER_COMMAND_TYPE_SHOW_POPUP: RobotAdapterCommandType
ROBOT_ADAPTER_COMMAND_TYPE_HIDE_POPUP: RobotAdapterCommandType
ROBOT_ADAPTER_COMMAND_TYPE_LOAD_PROGRAM: RobotAdapterCommandType
ROBOT_ADAPTER_COMMAND_TYPE_LOAD_INSTALLATION: RobotAdapterCommandType
ROBOT_ADAPTER_COMMAND_TYPE_POWER_ON: RobotAdapterCommandType
ROBOT_ADAPTER_COMMAND_TYPE_POWER_OFF: RobotAdapterCommandType
ROBOT_ADAPTER_COMMAND_TYPE_BRAKE_RELEASE: RobotAdapterCommandType
ROBOT_ADAPTER_TELEMETRY_TYPE_UNSPECIFIED: RobotAdapterTelemetryType
ROBOT_ADAPTER_TELEMETRY_TYPE_ROBOT_STATE: RobotAdapterTelemetryType
ROBOT_ADAPTER_TELEMETRY_TYPE_JOINT_STATE: RobotAdapterTelemetryType
ROBOT_ADAPTER_TELEMETRY_TYPE_TCP_POSE: RobotAdapterTelemetryType
ROBOT_ADAPTER_TELEMETRY_TYPE_TCP_WRENCH: RobotAdapterTelemetryType
ROBOT_ADAPTER_TELEMETRY_TYPE_IO_STATE: RobotAdapterTelemetryType

class RobotAdapterCommandCapability(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: RobotAdapterCommandType
    def __init__(self, type: _Optional[_Union[RobotAdapterCommandType, str]] = ...) -> None: ...

class RobotAdapterTelemetryCapability(_message.Message):
    __slots__ = ("type", "frequency_hz")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_HZ_FIELD_NUMBER: _ClassVar[int]
    type: RobotAdapterTelemetryType
    frequency_hz: float
    def __init__(self, type: _Optional[_Union[RobotAdapterTelemetryType, str]] = ..., frequency_hz: _Optional[float] = ...) -> None: ...

class RobotAdapterCapabilities(_message.Message):
    __slots__ = ("commands", "telemetry", "io_signals")
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    IO_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[RobotAdapterCommandCapability]
    telemetry: _containers.RepeatedCompositeFieldContainer[RobotAdapterTelemetryCapability]
    io_signals: _robot_io_catalog_pb2.RobotIOSignalCatalog
    def __init__(self, commands: _Optional[_Iterable[_Union[RobotAdapterCommandCapability, _Mapping]]] = ..., telemetry: _Optional[_Iterable[_Union[RobotAdapterTelemetryCapability, _Mapping]]] = ..., io_signals: _Optional[_Union[_robot_io_catalog_pb2.RobotIOSignalCatalog, _Mapping]] = ...) -> None: ...

class RobotControllerIdentity(_message.Message):
    __slots__ = ("manufacturer", "model", "serial_number", "controller_software_version")
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    manufacturer: str
    model: str
    serial_number: str
    controller_software_version: str
    def __init__(self, manufacturer: _Optional[str] = ..., model: _Optional[str] = ..., serial_number: _Optional[str] = ..., controller_software_version: _Optional[str] = ...) -> None: ...

class RobotAdapterInfoMessage(_message.Message):
    __slots__ = ("robot_id", "robot_type", "identifier", "adapter_type", "adapter_version", "controller", "capabilities", "capabilities_revision")
    ROBOT_ID_FIELD_NUMBER: _ClassVar[int]
    ROBOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_REVISION_FIELD_NUMBER: _ClassVar[int]
    robot_id: str
    robot_type: str
    identifier: str
    adapter_type: str
    adapter_version: str
    controller: RobotControllerIdentity
    capabilities: RobotAdapterCapabilities
    capabilities_revision: str
    def __init__(self, robot_id: _Optional[str] = ..., robot_type: _Optional[str] = ..., identifier: _Optional[str] = ..., adapter_type: _Optional[str] = ..., adapter_version: _Optional[str] = ..., controller: _Optional[_Union[RobotControllerIdentity, _Mapping]] = ..., capabilities: _Optional[_Union[RobotAdapterCapabilities, _Mapping]] = ..., capabilities_revision: _Optional[str] = ...) -> None: ...
