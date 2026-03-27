import datetime

from buf.validate import validate_pb2 as _validate_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from runtime.v1 import actor_assignment_pb2 as _actor_assignment_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from variance.v1 import variant_configuration_pb2 as _variant_configuration_pb2
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
PROCESS_RUN_STATE_UNSPECIFIED: ProcessRunState
PROCESS_RUN_STATE_WAITING: ProcessRunState
PROCESS_RUN_STATE_IN_PROGRESS: ProcessRunState
PROCESS_RUN_STATE_COMPLETED: ProcessRunState
PROCESS_RUN_STATE_ABORTED: ProcessRunState

class RunParameter(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ProcessRun(_message.Message):
    __slots__ = ("id", "name", "icon", "process_recipe_id", "order_id", "station_id", "cell_id", "frame", "root_sequence_run_id", "sequence_run_ids", "task_run_ids", "state", "initiated_at", "ended_at", "assignments", "variant_configuration", "parameters")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    PROCESS_RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_SEQUENCE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_RUN_IDS_FIELD_NUMBER: _ClassVar[int]
    TASK_RUN_IDS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INITIATED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    VARIANT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    process_recipe_id: str
    order_id: str
    station_id: str
    cell_id: str
    frame: _pose_pb2.LocalizedPose
    root_sequence_run_id: str
    sequence_run_ids: _containers.RepeatedScalarFieldContainer[str]
    task_run_ids: _containers.RepeatedScalarFieldContainer[str]
    state: ProcessRunState
    initiated_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    assignments: _containers.RepeatedCompositeFieldContainer[_actor_assignment_pb2.ActorAssignment]
    variant_configuration: _variant_configuration_pb2.VariantConfiguration
    parameters: _containers.RepeatedCompositeFieldContainer[RunParameter]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., process_recipe_id: _Optional[str] = ..., order_id: _Optional[str] = ..., station_id: _Optional[str] = ..., cell_id: _Optional[str] = ..., frame: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., root_sequence_run_id: _Optional[str] = ..., sequence_run_ids: _Optional[_Iterable[str]] = ..., task_run_ids: _Optional[_Iterable[str]] = ..., state: _Optional[_Union[ProcessRunState, str]] = ..., initiated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., assignments: _Optional[_Iterable[_Union[_actor_assignment_pb2.ActorAssignment, _Mapping]]] = ..., variant_configuration: _Optional[_Union[_variant_configuration_pb2.VariantConfiguration, _Mapping]] = ..., parameters: _Optional[_Iterable[_Union[RunParameter, _Mapping]]] = ...) -> None: ...

class ProcessRuns(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ProcessRun]
    def __init__(self, items: _Optional[_Iterable[_Union[ProcessRun, _Mapping]]] = ...) -> None: ...
