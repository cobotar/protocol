import datetime

from assembly.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkerDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "disabled", "employee_id", "external_references", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    disabled: bool
    employee_id: str
    external_references: _containers.RepeatedCompositeFieldContainer[_common_pb2.ExternalReference]
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., disabled: bool = ..., employee_id: _Optional[str] = ..., external_references: _Optional[_Iterable[_Union[_common_pb2.ExternalReference, _Mapping]]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class ActorRef(_message.Message):
    __slots__ = ("kind", "actor_id")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    kind: _common_pb2.ActorKind
    actor_id: str
    def __init__(self, kind: _Optional[_Union[_common_pb2.ActorKind, str]] = ..., actor_id: _Optional[str] = ...) -> None: ...

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
    actor: ActorRef
    process_run_id: str
    sequence_run_id: str
    task_run_id: str
    assigned_at: _timestamp_pb2.Timestamp
    released_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., actor: _Optional[_Union[ActorRef, _Mapping]] = ..., process_run_id: _Optional[str] = ..., sequence_run_id: _Optional[str] = ..., task_run_id: _Optional[str] = ..., assigned_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., released_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
