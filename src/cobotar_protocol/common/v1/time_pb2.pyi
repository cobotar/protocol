import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeWindow(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EstimatedDuration(_message.Message):
    __slots__ = ("nominal_seconds", "min_seconds", "max_seconds")
    NOMINAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MIN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_SECONDS_FIELD_NUMBER: _ClassVar[int]
    nominal_seconds: int
    min_seconds: int
    max_seconds: int
    def __init__(self, nominal_seconds: _Optional[int] = ..., min_seconds: _Optional[int] = ..., max_seconds: _Optional[int] = ...) -> None: ...
