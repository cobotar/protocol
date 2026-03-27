import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvidenceFact(_message.Message):
    __slots__ = ("key", "value", "unit")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    unit: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., unit: _Optional[str] = ...) -> None: ...

class ExecutionEvidence(_message.Message):
    __slots__ = ("id", "task_run_id", "source", "recorded_at", "facts", "blob_uri")
    ID_FIELD_NUMBER: _ClassVar[int]
    TASK_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    FACTS_FIELD_NUMBER: _ClassVar[int]
    BLOB_URI_FIELD_NUMBER: _ClassVar[int]
    id: str
    task_run_id: str
    source: str
    recorded_at: _timestamp_pb2.Timestamp
    facts: _containers.RepeatedCompositeFieldContainer[EvidenceFact]
    blob_uri: str
    def __init__(self, id: _Optional[str] = ..., task_run_id: _Optional[str] = ..., source: _Optional[str] = ..., recorded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., facts: _Optional[_Iterable[_Union[EvidenceFact, _Mapping]]] = ..., blob_uri: _Optional[str] = ...) -> None: ...
