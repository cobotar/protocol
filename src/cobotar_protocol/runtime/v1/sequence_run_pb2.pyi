from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import actor_pb2 as _actor_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequenceRunState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEQUENCE_RUN_STATE_UNSPECIFIED: _ClassVar[SequenceRunState]
    SEQUENCE_RUN_STATE_MISSING_PRECONDITION: _ClassVar[SequenceRunState]
    SEQUENCE_RUN_STATE_WAITING: _ClassVar[SequenceRunState]
    SEQUENCE_RUN_STATE_IN_PROGRESS: _ClassVar[SequenceRunState]
    SEQUENCE_RUN_STATE_COMPLETED: _ClassVar[SequenceRunState]
    SEQUENCE_RUN_STATE_ABORTED: _ClassVar[SequenceRunState]
SEQUENCE_RUN_STATE_UNSPECIFIED: SequenceRunState
SEQUENCE_RUN_STATE_MISSING_PRECONDITION: SequenceRunState
SEQUENCE_RUN_STATE_WAITING: SequenceRunState
SEQUENCE_RUN_STATE_IN_PROGRESS: SequenceRunState
SEQUENCE_RUN_STATE_COMPLETED: SequenceRunState
SEQUENCE_RUN_STATE_ABORTED: SequenceRunState

class SequenceRun(_message.Message):
    __slots__ = ("id", "name", "icon", "sequence_definition_id", "parent_sequence_run_id", "child_sequence_run_ids", "child_task_run_ids", "state", "completed_tasks", "can_bulk_complete", "assigned_actors")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SEQUENCE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_SEQUENCE_RUN_IDS_FIELD_NUMBER: _ClassVar[int]
    CHILD_TASK_RUN_IDS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_TASKS_FIELD_NUMBER: _ClassVar[int]
    CAN_BULK_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ACTORS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    sequence_definition_id: str
    parent_sequence_run_id: str
    child_sequence_run_ids: _containers.RepeatedScalarFieldContainer[str]
    child_task_run_ids: _containers.RepeatedScalarFieldContainer[str]
    state: SequenceRunState
    completed_tasks: int
    can_bulk_complete: bool
    assigned_actors: _containers.RepeatedCompositeFieldContainer[_actor_pb2.ActorRef]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., sequence_definition_id: _Optional[str] = ..., parent_sequence_run_id: _Optional[str] = ..., child_sequence_run_ids: _Optional[_Iterable[str]] = ..., child_task_run_ids: _Optional[_Iterable[str]] = ..., state: _Optional[_Union[SequenceRunState, str]] = ..., completed_tasks: _Optional[int] = ..., can_bulk_complete: bool = ..., assigned_actors: _Optional[_Iterable[_Union[_actor_pb2.ActorRef, _Mapping]]] = ...) -> None: ...

class SequenceRuns(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SequenceRun]
    def __init__(self, items: _Optional[_Iterable[_Union[SequenceRun, _Mapping]]] = ...) -> None: ...
