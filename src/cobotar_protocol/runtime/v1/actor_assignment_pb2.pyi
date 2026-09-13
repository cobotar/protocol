import datetime

from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import actor_pb2 as _actor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskActorAssignmentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_ACTOR_ASSIGNMENT_STATE_UNSPECIFIED: _ClassVar[TaskActorAssignmentState]
    TASK_ACTOR_ASSIGNMENT_STATE_UNASSIGNED: _ClassVar[TaskActorAssignmentState]
    TASK_ACTOR_ASSIGNMENT_STATE_ASSIGNED: _ClassVar[TaskActorAssignmentState]
    TASK_ACTOR_ASSIGNMENT_STATE_BLOCKED: _ClassVar[TaskActorAssignmentState]

class TaskActorAssignmentReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_ACTOR_ASSIGNMENT_REASON_UNSPECIFIED: _ClassVar[TaskActorAssignmentReason]
    TASK_ACTOR_ASSIGNMENT_REASON_ACTOR_UNAVAILABLE: _ClassVar[TaskActorAssignmentReason]
    TASK_ACTOR_ASSIGNMENT_REASON_NO_CAPABLE_ACTOR_AVAILABLE: _ClassVar[TaskActorAssignmentReason]
    TASK_ACTOR_ASSIGNMENT_REASON_REASSIGNMENT_NOT_ALLOWED: _ClassVar[TaskActorAssignmentReason]
    TASK_ACTOR_ASSIGNMENT_REASON_HANDOVER_REQUIRED: _ClassVar[TaskActorAssignmentReason]
TASK_ACTOR_ASSIGNMENT_STATE_UNSPECIFIED: TaskActorAssignmentState
TASK_ACTOR_ASSIGNMENT_STATE_UNASSIGNED: TaskActorAssignmentState
TASK_ACTOR_ASSIGNMENT_STATE_ASSIGNED: TaskActorAssignmentState
TASK_ACTOR_ASSIGNMENT_STATE_BLOCKED: TaskActorAssignmentState
TASK_ACTOR_ASSIGNMENT_REASON_UNSPECIFIED: TaskActorAssignmentReason
TASK_ACTOR_ASSIGNMENT_REASON_ACTOR_UNAVAILABLE: TaskActorAssignmentReason
TASK_ACTOR_ASSIGNMENT_REASON_NO_CAPABLE_ACTOR_AVAILABLE: TaskActorAssignmentReason
TASK_ACTOR_ASSIGNMENT_REASON_REASSIGNMENT_NOT_ALLOWED: TaskActorAssignmentReason
TASK_ACTOR_ASSIGNMENT_REASON_HANDOVER_REQUIRED: TaskActorAssignmentReason

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

class TaskActorAssignmentStatus(_message.Message):
    __slots__ = ("state", "reason", "affected_actor", "message", "evaluated_at")
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_ACTOR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_AT_FIELD_NUMBER: _ClassVar[int]
    state: TaskActorAssignmentState
    reason: TaskActorAssignmentReason
    affected_actor: _actor_pb2.ActorRef
    message: str
    evaluated_at: _timestamp_pb2.Timestamp
    def __init__(self, state: _Optional[_Union[TaskActorAssignmentState, str]] = ..., reason: _Optional[_Union[TaskActorAssignmentReason, str]] = ..., affected_actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ..., message: _Optional[str] = ..., evaluated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
