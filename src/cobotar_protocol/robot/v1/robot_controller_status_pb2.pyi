import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from robot.v1 import program_state_pb2 as _program_state_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RobotControlAuthority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_CONTROL_AUTHORITY_UNSPECIFIED: _ClassVar[RobotControlAuthority]
    ROBOT_CONTROL_AUTHORITY_LOCAL: _ClassVar[RobotControlAuthority]
    ROBOT_CONTROL_AUTHORITY_REMOTE: _ClassVar[RobotControlAuthority]

class RobotOperationalMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_OPERATIONAL_MODE_UNSPECIFIED: _ClassVar[RobotOperationalMode]
    ROBOT_OPERATIONAL_MODE_NONE: _ClassVar[RobotOperationalMode]
    ROBOT_OPERATIONAL_MODE_MANUAL: _ClassVar[RobotOperationalMode]
    ROBOT_OPERATIONAL_MODE_AUTOMATIC: _ClassVar[RobotOperationalMode]

class RobotSafetyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_SAFETY_STATUS_UNSPECIFIED: _ClassVar[RobotSafetyStatus]
    ROBOT_SAFETY_STATUS_NORMAL: _ClassVar[RobotSafetyStatus]
    ROBOT_SAFETY_STATUS_REDUCED: _ClassVar[RobotSafetyStatus]
    ROBOT_SAFETY_STATUS_PROTECTIVE_STOP: _ClassVar[RobotSafetyStatus]
    ROBOT_SAFETY_STATUS_RECOVERY: _ClassVar[RobotSafetyStatus]
    ROBOT_SAFETY_STATUS_SAFEGUARD_STOP: _ClassVar[RobotSafetyStatus]
    ROBOT_SAFETY_STATUS_SYSTEM_EMERGENCY_STOP: _ClassVar[RobotSafetyStatus]
    ROBOT_SAFETY_STATUS_ROBOT_EMERGENCY_STOP: _ClassVar[RobotSafetyStatus]
    ROBOT_SAFETY_STATUS_VIOLATION: _ClassVar[RobotSafetyStatus]
    ROBOT_SAFETY_STATUS_FAULT: _ClassVar[RobotSafetyStatus]

class RobotMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_MODE_UNSPECIFIED: _ClassVar[RobotMode]
    ROBOT_MODE_NO_CONTROLLER: _ClassVar[RobotMode]
    ROBOT_MODE_DISCONNECTED: _ClassVar[RobotMode]
    ROBOT_MODE_CONFIRM_SAFETY: _ClassVar[RobotMode]
    ROBOT_MODE_BOOTING: _ClassVar[RobotMode]
    ROBOT_MODE_POWER_OFF: _ClassVar[RobotMode]
    ROBOT_MODE_POWER_ON: _ClassVar[RobotMode]
    ROBOT_MODE_IDLE: _ClassVar[RobotMode]
    ROBOT_MODE_BACKDIVE: _ClassVar[RobotMode]
    ROBOT_MODE_RUNNING: _ClassVar[RobotMode]
ROBOT_CONTROL_AUTHORITY_UNSPECIFIED: RobotControlAuthority
ROBOT_CONTROL_AUTHORITY_LOCAL: RobotControlAuthority
ROBOT_CONTROL_AUTHORITY_REMOTE: RobotControlAuthority
ROBOT_OPERATIONAL_MODE_UNSPECIFIED: RobotOperationalMode
ROBOT_OPERATIONAL_MODE_NONE: RobotOperationalMode
ROBOT_OPERATIONAL_MODE_MANUAL: RobotOperationalMode
ROBOT_OPERATIONAL_MODE_AUTOMATIC: RobotOperationalMode
ROBOT_SAFETY_STATUS_UNSPECIFIED: RobotSafetyStatus
ROBOT_SAFETY_STATUS_NORMAL: RobotSafetyStatus
ROBOT_SAFETY_STATUS_REDUCED: RobotSafetyStatus
ROBOT_SAFETY_STATUS_PROTECTIVE_STOP: RobotSafetyStatus
ROBOT_SAFETY_STATUS_RECOVERY: RobotSafetyStatus
ROBOT_SAFETY_STATUS_SAFEGUARD_STOP: RobotSafetyStatus
ROBOT_SAFETY_STATUS_SYSTEM_EMERGENCY_STOP: RobotSafetyStatus
ROBOT_SAFETY_STATUS_ROBOT_EMERGENCY_STOP: RobotSafetyStatus
ROBOT_SAFETY_STATUS_VIOLATION: RobotSafetyStatus
ROBOT_SAFETY_STATUS_FAULT: RobotSafetyStatus
ROBOT_MODE_UNSPECIFIED: RobotMode
ROBOT_MODE_NO_CONTROLLER: RobotMode
ROBOT_MODE_DISCONNECTED: RobotMode
ROBOT_MODE_CONFIRM_SAFETY: RobotMode
ROBOT_MODE_BOOTING: RobotMode
ROBOT_MODE_POWER_OFF: RobotMode
ROBOT_MODE_POWER_ON: RobotMode
ROBOT_MODE_IDLE: RobotMode
ROBOT_MODE_BACKDIVE: RobotMode
ROBOT_MODE_RUNNING: RobotMode

class RobotControllerStatusMessage(_message.Message):
    __slots__ = ("robot_id", "control_authority", "robot_mode", "safety_status", "operational_mode", "program_state", "loaded_program", "observed_at")
    ROBOT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    ROBOT_MODE_FIELD_NUMBER: _ClassVar[int]
    SAFETY_STATUS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_MODE_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_STATE_FIELD_NUMBER: _ClassVar[int]
    LOADED_PROGRAM_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    robot_id: str
    control_authority: RobotControlAuthority
    robot_mode: RobotMode
    safety_status: RobotSafetyStatus
    operational_mode: RobotOperationalMode
    program_state: _program_state_pb2.ProgramState
    loaded_program: str
    observed_at: _timestamp_pb2.Timestamp
    def __init__(self, robot_id: _Optional[str] = ..., control_authority: _Optional[_Union[RobotControlAuthority, str]] = ..., robot_mode: _Optional[_Union[RobotMode, str]] = ..., safety_status: _Optional[_Union[RobotSafetyStatus, str]] = ..., operational_mode: _Optional[_Union[RobotOperationalMode, str]] = ..., program_state: _Optional[_Union[_program_state_pb2.ProgramState, str]] = ..., loaded_program: _Optional[str] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
