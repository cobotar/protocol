from common.v1 import actor_pb2 as _actor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskStateRequest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_STATE_REQUEST_UNSPECIFIED: _ClassVar[TaskStateRequest]
    TASK_STATE_REQUEST_IN_PROGRESS: _ClassVar[TaskStateRequest]
    TASK_STATE_REQUEST_DONE: _ClassVar[TaskStateRequest]
    TASK_STATE_REQUEST_UNDO: _ClassVar[TaskStateRequest]
    TASK_STATE_REQUEST_ERROR: _ClassVar[TaskStateRequest]
    TASK_STATE_REQUEST_ABORT: _ClassVar[TaskStateRequest]
TASK_STATE_REQUEST_UNSPECIFIED: TaskStateRequest
TASK_STATE_REQUEST_IN_PROGRESS: TaskStateRequest
TASK_STATE_REQUEST_DONE: TaskStateRequest
TASK_STATE_REQUEST_UNDO: TaskStateRequest
TASK_STATE_REQUEST_ERROR: TaskStateRequest
TASK_STATE_REQUEST_ABORT: TaskStateRequest

class ProcessAbortRequest(_message.Message):
    __slots__ = ("process_run_id", "reason")
    PROCESS_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    process_run_id: str
    reason: str
    def __init__(self, process_run_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class TaskStateChangeRequest(_message.Message):
    __slots__ = ("task_run_id", "state")
    TASK_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    task_run_id: str
    state: TaskStateRequest
    def __init__(self, task_run_id: _Optional[str] = ..., state: _Optional[_Union[TaskStateRequest, str]] = ...) -> None: ...

class TaskReassignRequest(_message.Message):
    __slots__ = ("task_run_id", "actor")
    TASK_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    task_run_id: str
    actor: _actor_pb2.ActorRef
    def __init__(self, task_run_id: _Optional[str] = ..., actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ...) -> None: ...

class TaskProgressUpdate(_message.Message):
    __slots__ = ("task_run_id", "actor", "message", "elapsed_time", "estimated_time_left")
    TASK_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_TIME_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TIME_LEFT_FIELD_NUMBER: _ClassVar[int]
    task_run_id: str
    actor: _actor_pb2.ActorRef
    message: str
    elapsed_time: int
    estimated_time_left: int
    def __init__(self, task_run_id: _Optional[str] = ..., actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ..., message: _Optional[str] = ..., elapsed_time: _Optional[int] = ..., estimated_time_left: _Optional[int] = ...) -> None: ...
