import datetime

from assembly.v1 import actor_pb2 as _actor_pb2
from assembly.v1 import common_pb2 as _common_pb2
from assembly.v1 import variant_pb2 as _variant_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessRunState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESS_RUN_STATE_UNSPECIFIED: _ClassVar[ProcessRunState]
    PROCESS_RUN_STATE_WAITING: _ClassVar[ProcessRunState]
    PROCESS_RUN_STATE_IN_PROGRESS: _ClassVar[ProcessRunState]
    PROCESS_RUN_STATE_COMPLETED: _ClassVar[ProcessRunState]
    PROCESS_RUN_STATE_ABORTED: _ClassVar[ProcessRunState]

class SequenceRunState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEQUENCE_RUN_STATE_UNSPECIFIED: _ClassVar[SequenceRunState]
    SEQUENCE_RUN_STATE_MISSING_PRECONDITION: _ClassVar[SequenceRunState]
    SEQUENCE_RUN_STATE_WAITING: _ClassVar[SequenceRunState]
    SEQUENCE_RUN_STATE_IN_PROGRESS: _ClassVar[SequenceRunState]
    SEQUENCE_RUN_STATE_COMPLETED: _ClassVar[SequenceRunState]
    SEQUENCE_RUN_STATE_ABORTED: _ClassVar[SequenceRunState]

class TaskRunState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_RUN_STATE_UNSPECIFIED: _ClassVar[TaskRunState]
    TASK_RUN_STATE_MISSING_PRECONDITION: _ClassVar[TaskRunState]
    TASK_RUN_STATE_WAITING: _ClassVar[TaskRunState]
    TASK_RUN_STATE_IN_PROGRESS: _ClassVar[TaskRunState]
    TASK_RUN_STATE_COMPLETED: _ClassVar[TaskRunState]
    TASK_RUN_STATE_ERROR: _ClassVar[TaskRunState]
    TASK_RUN_STATE_ABORTED: _ClassVar[TaskRunState]
PROCESS_RUN_STATE_UNSPECIFIED: ProcessRunState
PROCESS_RUN_STATE_WAITING: ProcessRunState
PROCESS_RUN_STATE_IN_PROGRESS: ProcessRunState
PROCESS_RUN_STATE_COMPLETED: ProcessRunState
PROCESS_RUN_STATE_ABORTED: ProcessRunState
SEQUENCE_RUN_STATE_UNSPECIFIED: SequenceRunState
SEQUENCE_RUN_STATE_MISSING_PRECONDITION: SequenceRunState
SEQUENCE_RUN_STATE_WAITING: SequenceRunState
SEQUENCE_RUN_STATE_IN_PROGRESS: SequenceRunState
SEQUENCE_RUN_STATE_COMPLETED: SequenceRunState
SEQUENCE_RUN_STATE_ABORTED: SequenceRunState
TASK_RUN_STATE_UNSPECIFIED: TaskRunState
TASK_RUN_STATE_MISSING_PRECONDITION: TaskRunState
TASK_RUN_STATE_WAITING: TaskRunState
TASK_RUN_STATE_IN_PROGRESS: TaskRunState
TASK_RUN_STATE_COMPLETED: TaskRunState
TASK_RUN_STATE_ERROR: TaskRunState
TASK_RUN_STATE_ABORTED: TaskRunState

class RunParameter(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ProcessRun(_message.Message):
    __slots__ = ("id", "recipe_id", "order_id", "station_id", "cell_id", "frame", "root_sequence_run_id", "sequences", "tasks", "state", "initiated_at", "ended_at", "assignments", "custom", "variant_configuration", "parameters")
    ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_SEQUENCE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INITIATED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    VARIANT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    recipe_id: str
    order_id: str
    station_id: str
    cell_id: str
    frame: _pose_pb2.LocalizedPose
    root_sequence_run_id: str
    sequences: _containers.RepeatedCompositeFieldContainer[SequenceRun]
    tasks: _containers.RepeatedCompositeFieldContainer[TaskRun]
    state: ProcessRunState
    initiated_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    assignments: _containers.RepeatedCompositeFieldContainer[_actor_pb2.ActorAssignment]
    custom: _common_pb2.CustomProperties
    variant_configuration: _variant_pb2.VariantConfiguration
    parameters: _containers.RepeatedCompositeFieldContainer[RunParameter]
    def __init__(self, id: _Optional[str] = ..., recipe_id: _Optional[str] = ..., order_id: _Optional[str] = ..., station_id: _Optional[str] = ..., cell_id: _Optional[str] = ..., frame: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., root_sequence_run_id: _Optional[str] = ..., sequences: _Optional[_Iterable[_Union[SequenceRun, _Mapping]]] = ..., tasks: _Optional[_Iterable[_Union[TaskRun, _Mapping]]] = ..., state: _Optional[_Union[ProcessRunState, str]] = ..., initiated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., assignments: _Optional[_Iterable[_Union[_actor_pb2.ActorAssignment, _Mapping]]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ..., variant_configuration: _Optional[_Union[_variant_pb2.VariantConfiguration, _Mapping]] = ..., parameters: _Optional[_Iterable[_Union[RunParameter, _Mapping]]] = ...) -> None: ...

class SequenceRun(_message.Message):
    __slots__ = ("id", "sequence_definition_id", "parent_sequence_run_id", "child_sequence_run_ids", "child_task_run_ids", "state", "completed_tasks", "can_bulk_complete", "assigned_actors")
    ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SEQUENCE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_SEQUENCE_RUN_IDS_FIELD_NUMBER: _ClassVar[int]
    CHILD_TASK_RUN_IDS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_TASKS_FIELD_NUMBER: _ClassVar[int]
    CAN_BULK_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ACTORS_FIELD_NUMBER: _ClassVar[int]
    id: str
    sequence_definition_id: str
    parent_sequence_run_id: str
    child_sequence_run_ids: _containers.RepeatedScalarFieldContainer[str]
    child_task_run_ids: _containers.RepeatedScalarFieldContainer[str]
    state: SequenceRunState
    completed_tasks: int
    can_bulk_complete: bool
    assigned_actors: _containers.RepeatedCompositeFieldContainer[_actor_pb2.ActorRef]
    def __init__(self, id: _Optional[str] = ..., sequence_definition_id: _Optional[str] = ..., parent_sequence_run_id: _Optional[str] = ..., child_sequence_run_ids: _Optional[_Iterable[str]] = ..., child_task_run_ids: _Optional[_Iterable[str]] = ..., state: _Optional[_Union[SequenceRunState, str]] = ..., completed_tasks: _Optional[int] = ..., can_bulk_complete: bool = ..., assigned_actors: _Optional[_Iterable[_Union[_actor_pb2.ActorRef, _Mapping]]] = ...) -> None: ...

class TaskRun(_message.Message):
    __slots__ = ("id", "task_definition_id", "parent_sequence_run_id", "state", "candidate_actors", "assigned_actor", "can_do", "can_undo", "workable_horizon", "estimated_duration", "started_at", "completed_at", "error_code", "error_message", "evidence", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
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
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    task_definition_id: str
    parent_sequence_run_id: str
    state: TaskRunState
    candidate_actors: _containers.RepeatedCompositeFieldContainer[_actor_pb2.ActorRef]
    assigned_actor: _actor_pb2.ActorRef
    can_do: bool
    can_undo: bool
    workable_horizon: int
    estimated_duration: _common_pb2.EstimatedDuration
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    error_code: str
    error_message: str
    evidence: _containers.RepeatedCompositeFieldContainer[ExecutionEvidence]
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., task_definition_id: _Optional[str] = ..., parent_sequence_run_id: _Optional[str] = ..., state: _Optional[_Union[TaskRunState, str]] = ..., candidate_actors: _Optional[_Iterable[_Union[_actor_pb2.ActorRef, _Mapping]]] = ..., assigned_actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ..., can_do: bool = ..., can_undo: bool = ..., workable_horizon: _Optional[int] = ..., estimated_duration: _Optional[_Union[_common_pb2.EstimatedDuration, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., evidence: _Optional[_Iterable[_Union[ExecutionEvidence, _Mapping]]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

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
