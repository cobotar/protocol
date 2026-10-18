import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from process.v1 import process_recipe_pb2 as _process_recipe_pb2
from process.v1 import sequence_definition_pb2 as _sequence_definition_pb2
from process.v1 import task_definition_pb2 as _task_definition_pb2
from product.v1 import part_definition_pb2 as _part_definition_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessRunDefinitionsSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESS_RUN_DEFINITIONS_SOURCE_UNSPECIFIED: _ClassVar[ProcessRunDefinitionsSource]
    PROCESS_RUN_DEFINITIONS_SOURCE_PINNED: _ClassVar[ProcessRunDefinitionsSource]
    PROCESS_RUN_DEFINITIONS_SOURCE_LATEST: _ClassVar[ProcessRunDefinitionsSource]
PROCESS_RUN_DEFINITIONS_SOURCE_UNSPECIFIED: ProcessRunDefinitionsSource
PROCESS_RUN_DEFINITIONS_SOURCE_PINNED: ProcessRunDefinitionsSource
PROCESS_RUN_DEFINITIONS_SOURCE_LATEST: ProcessRunDefinitionsSource

class ProcessRunDefinitions(_message.Message):
    __slots__ = ("process_run_id", "source", "pinned_at", "recipe", "sequence_definitions", "task_definitions", "part_definitions")
    PROCESS_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PINNED_AT_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    TASK_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    PART_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    process_run_id: str
    source: ProcessRunDefinitionsSource
    pinned_at: _timestamp_pb2.Timestamp
    recipe: _process_recipe_pb2.ProcessRecipe
    sequence_definitions: _containers.RepeatedCompositeFieldContainer[_sequence_definition_pb2.SequenceDefinition]
    task_definitions: _containers.RepeatedCompositeFieldContainer[_task_definition_pb2.TaskDefinition]
    part_definitions: _containers.RepeatedCompositeFieldContainer[_part_definition_pb2.PartDefinition]
    def __init__(self, process_run_id: _Optional[str] = ..., source: _Optional[_Union[ProcessRunDefinitionsSource, str]] = ..., pinned_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., recipe: _Optional[_Union[_process_recipe_pb2.ProcessRecipe, _Mapping]] = ..., sequence_definitions: _Optional[_Iterable[_Union[_sequence_definition_pb2.SequenceDefinition, _Mapping]]] = ..., task_definitions: _Optional[_Iterable[_Union[_task_definition_pb2.TaskDefinition, _Mapping]]] = ..., part_definitions: _Optional[_Iterable[_Union[_part_definition_pb2.PartDefinition, _Mapping]]] = ...) -> None: ...

class ProcessRunDefinitionsRequest(_message.Message):
    __slots__ = ("process_run_id",)
    PROCESS_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    process_run_id: str
    def __init__(self, process_run_id: _Optional[str] = ...) -> None: ...
