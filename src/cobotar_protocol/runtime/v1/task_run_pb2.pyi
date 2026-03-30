import datetime

from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import actor_pb2 as _actor_pb2
from common.v1 import time_pb2 as _time_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from resources.v1 import container_definition_pb2 as _container_definition_pb2
from runtime.v1 import execution_evidence_pb2 as _execution_evidence_pb2
from runtime.v1 import process_requests_pb2 as _process_requests_pb2
from runtime.v1 import runtime_restriction_pb2 as _runtime_restriction_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskRunState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_RUN_STATE_UNSPECIFIED: _ClassVar[TaskRunState]
    TASK_RUN_STATE_NOT_READY: _ClassVar[TaskRunState]
    TASK_RUN_STATE_READY: _ClassVar[TaskRunState]
    TASK_RUN_STATE_IN_PROGRESS: _ClassVar[TaskRunState]
    TASK_RUN_STATE_DONE: _ClassVar[TaskRunState]
    TASK_RUN_STATE_ERROR: _ClassVar[TaskRunState]
    TASK_RUN_STATE_ABORTED: _ClassVar[TaskRunState]
TASK_RUN_STATE_UNSPECIFIED: TaskRunState
TASK_RUN_STATE_NOT_READY: TaskRunState
TASK_RUN_STATE_READY: TaskRunState
TASK_RUN_STATE_IN_PROGRESS: TaskRunState
TASK_RUN_STATE_DONE: TaskRunState
TASK_RUN_STATE_ERROR: TaskRunState
TASK_RUN_STATE_ABORTED: TaskRunState

class TaskRuntimeBinding(_message.Message):
    __slots__ = ("asset_instance_id", "robot_instance_id", "station_id", "cell_id", "container_slot")
    ASSET_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ROBOT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_SLOT_FIELD_NUMBER: _ClassVar[int]
    asset_instance_id: str
    robot_instance_id: str
    station_id: str
    cell_id: str
    container_slot: _container_definition_pb2.ContainerSlotRef
    def __init__(self, asset_instance_id: _Optional[str] = ..., robot_instance_id: _Optional[str] = ..., station_id: _Optional[str] = ..., cell_id: _Optional[str] = ..., container_slot: _Optional[_Union[_container_definition_pb2.ContainerSlotRef, _Mapping]] = ...) -> None: ...

class TaskRun(_message.Message):
    __slots__ = ("id", "name", "icon", "task_definition_id", "parent_sequence_run_id", "state", "candidate_actors", "assigned_actor", "can_do", "can_undo", "workable_horizon", "estimated_duration", "started_at", "completed_at", "error_code", "error_message", "evidence", "binding", "restrictions", "candidate_actor_evaluations")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TASK_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SEQUENCE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_ACTORS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ACTOR_FIELD_NUMBER: _ClassVar[int]
    CAN_DO_FIELD_NUMBER: _ClassVar[int]
    CAN_UNDO_FIELD_NUMBER: _ClassVar[int]
    WORKABLE_HORIZON_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DURATION_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    BINDING_FIELD_NUMBER: _ClassVar[int]
    RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_ACTOR_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    task_definition_id: str
    parent_sequence_run_id: str
    state: TaskRunState
    candidate_actors: _containers.RepeatedCompositeFieldContainer[_actor_pb2.ActorRef]
    assigned_actor: _actor_pb2.ActorRef
    can_do: bool
    can_undo: bool
    workable_horizon: int
    estimated_duration: _time_pb2.EstimatedDuration
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    error_code: str
    error_message: str
    evidence: _containers.RepeatedCompositeFieldContainer[_execution_evidence_pb2.ExecutionEvidence]
    binding: TaskRuntimeBinding
    restrictions: _containers.RepeatedCompositeFieldContainer[_runtime_restriction_pb2.RuntimeRestriction]
    candidate_actor_evaluations: _containers.RepeatedCompositeFieldContainer[_process_requests_pb2.CandidateActorEvaluation]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., task_definition_id: _Optional[str] = ..., parent_sequence_run_id: _Optional[str] = ..., state: _Optional[_Union[TaskRunState, str]] = ..., candidate_actors: _Optional[_Iterable[_Union[_actor_pb2.ActorRef, _Mapping]]] = ..., assigned_actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ..., can_do: bool = ..., can_undo: bool = ..., workable_horizon: _Optional[int] = ..., estimated_duration: _Optional[_Union[_time_pb2.EstimatedDuration, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., evidence: _Optional[_Iterable[_Union[_execution_evidence_pb2.ExecutionEvidence, _Mapping]]] = ..., binding: _Optional[_Union[TaskRuntimeBinding, _Mapping]] = ..., restrictions: _Optional[_Iterable[_Union[_runtime_restriction_pb2.RuntimeRestriction, _Mapping]]] = ..., candidate_actor_evaluations: _Optional[_Iterable[_Union[_process_requests_pb2.CandidateActorEvaluation, _Mapping]]] = ...) -> None: ...

class TaskRuns(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TaskRun]
    def __init__(self, items: _Optional[_Iterable[_Union[TaskRun, _Mapping]]] = ...) -> None: ...
