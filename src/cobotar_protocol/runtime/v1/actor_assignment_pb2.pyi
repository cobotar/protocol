import datetime

from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import actor_pb2 as _actor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActorAssignment(_message.Message):
    __slots__ = ("id", "actor", "process_run_id", "sequence_run_id", "task_run_id", "assigned_at", "released_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    PROCESS_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_AT_FIELD_NUMBER: _ClassVar[int]
    RELEASED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    actor: _actor_pb2.ActorRef
    process_run_id: str
    sequence_run_id: str
    task_run_id: str
    assigned_at: _timestamp_pb2.Timestamp
    released_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ..., process_run_id: _Optional[str] = ..., sequence_run_id: _Optional[str] = ..., task_run_id: _Optional[str] = ..., assigned_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., released_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ActorAssignments(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ActorAssignment]
    def __init__(self, items: _Optional[_Iterable[_Union[ActorAssignment, _Mapping]]] = ...) -> None: ...
