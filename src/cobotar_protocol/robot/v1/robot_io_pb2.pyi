import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RobotIOSignalValue(_message.Message):
    __slots__ = ("signal_id", "bool_value", "int_value", "double_value")
    SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    signal_id: str
    bool_value: bool
    int_value: int
    double_value: float
    def __init__(self, signal_id: _Optional[str] = ..., bool_value: bool = ..., int_value: _Optional[int] = ..., double_value: _Optional[float] = ...) -> None: ...

class RobotIOState(_message.Message):
    __slots__ = ("robot_id", "values", "observed_at")
    ROBOT_ID_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    robot_id: str
    values: _containers.RepeatedCompositeFieldContainer[RobotIOSignalValue]
    observed_at: _timestamp_pb2.Timestamp
    def __init__(self, robot_id: _Optional[str] = ..., values: _Optional[_Iterable[_Union[RobotIOSignalValue, _Mapping]]] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RobotIOCommand(_message.Message):
    __slots__ = ("robot_id", "writes")
    ROBOT_ID_FIELD_NUMBER: _ClassVar[int]
    WRITES_FIELD_NUMBER: _ClassVar[int]
    robot_id: str
    writes: _containers.RepeatedCompositeFieldContainer[RobotIOSignalValue]
    def __init__(self, robot_id: _Optional[str] = ..., writes: _Optional[_Iterable[_Union[RobotIOSignalValue, _Mapping]]] = ...) -> None: ...
