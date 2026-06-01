from robot.v1 import program_state_pb2 as _program_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProgramStateRequest(_message.Message):
    __slots__ = ("robot_id", "state")
    ROBOT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    robot_id: str
    state: _program_state_pb2.ProgramState
    def __init__(self, robot_id: _Optional[str] = ..., state: _Optional[_Union[_program_state_pb2.ProgramState, str]] = ...) -> None: ...

class AcknowledgeRobot(_message.Message):
    __slots__ = ("robot_id",)
    ROBOT_ID_FIELD_NUMBER: _ClassVar[int]
    robot_id: str
    def __init__(self, robot_id: _Optional[str] = ...) -> None: ...
