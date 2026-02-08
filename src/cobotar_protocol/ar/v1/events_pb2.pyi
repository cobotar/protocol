from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMAND_TYPE_UNSPECIFIED: _ClassVar[CommandType]
    COMMAND_TYPE_TASK_COMPLETE: _ClassVar[CommandType]
    COMMAND_TYPE_TASK_ASSIGN: _ClassVar[CommandType]
    COMMAND_TYPE_TASK_UNDO: _ClassVar[CommandType]
    COMMAND_TYPE_TASK_HIGHLIGHT: _ClassVar[CommandType]
    COMMAND_TYPE_TASK_HELP: _ClassVar[CommandType]
    COMMAND_TYPE_ROBOT_START_STOP: _ClassVar[CommandType]
    COMMAND_TYPE_ROBOT_TOGGLE_FREE_DRIVE: _ClassVar[CommandType]
    COMMAND_TYPE_ROBOT_START_COLLABORATION: _ClassVar[CommandType]
    COMMAND_TYPE_ROBOT_STOP_COLLABORATION: _ClassVar[CommandType]

class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_TYPE_UNSPECIFIED: _ClassVar[EventType]
    EVENT_TYPE_PROCESS_COMPLETE: _ClassVar[EventType]
    EVENT_TYPE_ROBOT_STARTING_TASK: _ClassVar[EventType]
    EVENT_TYPE_ROBOT_WAITING_FOR_HELP: _ClassVar[EventType]
    EVENT_TYPE_ROBOT_WAITING_TASK_RELEASE: _ClassVar[EventType]

class TelemetryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TELEMETRY_TYPE_UNSPECIFIED: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_ROBOT_TCP: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_ROBOT_JOINT_ANGLES: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_ROBOT_FORCE_TORQUE: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_ROBOT_STATE: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_ROBOT_PATH: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_ROBOT_WAYPOINTS: _ClassVar[TelemetryType]

class HandlerCardinality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HANDLER_CARDINALITY_UNSPECIFIED: _ClassVar[HandlerCardinality]
    HANDLER_CARDINALITY_AT_LEAST_ONE: _ClassVar[HandlerCardinality]
    HANDLER_CARDINALITY_EXACTLY_ONE: _ClassVar[HandlerCardinality]
    HANDLER_CARDINALITY_AT_MOST_ONE: _ClassVar[HandlerCardinality]
COMMAND_TYPE_UNSPECIFIED: CommandType
COMMAND_TYPE_TASK_COMPLETE: CommandType
COMMAND_TYPE_TASK_ASSIGN: CommandType
COMMAND_TYPE_TASK_UNDO: CommandType
COMMAND_TYPE_TASK_HIGHLIGHT: CommandType
COMMAND_TYPE_TASK_HELP: CommandType
COMMAND_TYPE_ROBOT_START_STOP: CommandType
COMMAND_TYPE_ROBOT_TOGGLE_FREE_DRIVE: CommandType
COMMAND_TYPE_ROBOT_START_COLLABORATION: CommandType
COMMAND_TYPE_ROBOT_STOP_COLLABORATION: CommandType
EVENT_TYPE_UNSPECIFIED: EventType
EVENT_TYPE_PROCESS_COMPLETE: EventType
EVENT_TYPE_ROBOT_STARTING_TASK: EventType
EVENT_TYPE_ROBOT_WAITING_FOR_HELP: EventType
EVENT_TYPE_ROBOT_WAITING_TASK_RELEASE: EventType
TELEMETRY_TYPE_UNSPECIFIED: TelemetryType
TELEMETRY_TYPE_ROBOT_TCP: TelemetryType
TELEMETRY_TYPE_ROBOT_JOINT_ANGLES: TelemetryType
TELEMETRY_TYPE_ROBOT_FORCE_TORQUE: TelemetryType
TELEMETRY_TYPE_ROBOT_STATE: TelemetryType
TELEMETRY_TYPE_ROBOT_PATH: TelemetryType
TELEMETRY_TYPE_ROBOT_WAYPOINTS: TelemetryType
HANDLER_CARDINALITY_UNSPECIFIED: HandlerCardinality
HANDLER_CARDINALITY_AT_LEAST_ONE: HandlerCardinality
HANDLER_CARDINALITY_EXACTLY_ONE: HandlerCardinality
HANDLER_CARDINALITY_AT_MOST_ONE: HandlerCardinality

class ExchangeType(_message.Message):
    __slots__ = ("command", "event", "telemetry")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    command: CommandType
    event: EventType
    telemetry: TelemetryType
    def __init__(self, command: _Optional[_Union[CommandType, str]] = ..., event: _Optional[_Union[EventType, str]] = ..., telemetry: _Optional[_Union[TelemetryType, str]] = ...) -> None: ...

class HandlerRequirement(_message.Message):
    __slots__ = ("message", "cardinality", "rationale")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CARDINALITY_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    message: ExchangeType
    cardinality: HandlerCardinality
    rationale: str
    def __init__(self, message: _Optional[_Union[ExchangeType, _Mapping]] = ..., cardinality: _Optional[_Union[HandlerCardinality, str]] = ..., rationale: _Optional[str] = ...) -> None: ...

class SupportedEventsMessage(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedScalarFieldContainer[EventType]
    def __init__(self, events: _Optional[_Iterable[_Union[EventType, str]]] = ...) -> None: ...
