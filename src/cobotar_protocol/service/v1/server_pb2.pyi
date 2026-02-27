import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerInfo(_message.Message):
    __slots__ = ("service", "instance_id", "epoch", "started_at", "reset_reason", "data_wiped")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    RESET_REASON_FIELD_NUMBER: _ClassVar[int]
    DATA_WIPED_FIELD_NUMBER: _ClassVar[int]
    service: str
    instance_id: str
    epoch: int
    started_at: _timestamp_pb2.Timestamp
    reset_reason: str
    data_wiped: bool
    def __init__(self, service: _Optional[str] = ..., instance_id: _Optional[str] = ..., epoch: _Optional[int] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reset_reason: _Optional[str] = ..., data_wiped: bool = ...) -> None: ...

class ServerHeartbeat(_message.Message):
    __slots__ = ("service", "server_id", "epoch", "unix_ms", "ip")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    service: str
    server_id: str
    epoch: int
    unix_ms: int
    ip: str
    def __init__(self, service: _Optional[str] = ..., server_id: _Optional[str] = ..., epoch: _Optional[int] = ..., unix_ms: _Optional[int] = ..., ip: _Optional[str] = ...) -> None: ...
