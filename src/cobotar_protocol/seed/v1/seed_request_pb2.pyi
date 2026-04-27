from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SaveSeedEntity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAVE_SEED_ENTITY_UNSPECIFIED: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_LINES: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_CELLS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_STATIONS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_WORKERS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_ROBOT_DEFINITIONS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_ROBOT_INSTANCES: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_SKILLS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_ACTOR_SKILLS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_DEVICES: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_MODELS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_ASSET_DEFINITIONS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_ASSET_INSTANCES: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_CONTAINER_DEFINITIONS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_CONTAINER_INSTANCES: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_TOOL_DEFINITIONS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_TOOL_INSTANCES: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_MARKERS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_PART_DEFINITIONS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_PART_INSTANCES: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_PRODUCTS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_RECIPES: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_SEQUENCES: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_TASKS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_PROCESSES: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_SEQUENCE_RUNS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_TASK_RUNS: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_FEEDBACK: _ClassVar[SaveSeedEntity]
    SAVE_SEED_ENTITY_ACTIONS: _ClassVar[SaveSeedEntity]
SAVE_SEED_ENTITY_UNSPECIFIED: SaveSeedEntity
SAVE_SEED_ENTITY_LINES: SaveSeedEntity
SAVE_SEED_ENTITY_CELLS: SaveSeedEntity
SAVE_SEED_ENTITY_STATIONS: SaveSeedEntity
SAVE_SEED_ENTITY_WORKERS: SaveSeedEntity
SAVE_SEED_ENTITY_ROBOT_DEFINITIONS: SaveSeedEntity
SAVE_SEED_ENTITY_ROBOT_INSTANCES: SaveSeedEntity
SAVE_SEED_ENTITY_SKILLS: SaveSeedEntity
SAVE_SEED_ENTITY_ACTOR_SKILLS: SaveSeedEntity
SAVE_SEED_ENTITY_DEVICES: SaveSeedEntity
SAVE_SEED_ENTITY_MODELS: SaveSeedEntity
SAVE_SEED_ENTITY_ASSET_DEFINITIONS: SaveSeedEntity
SAVE_SEED_ENTITY_ASSET_INSTANCES: SaveSeedEntity
SAVE_SEED_ENTITY_CONTAINER_DEFINITIONS: SaveSeedEntity
SAVE_SEED_ENTITY_CONTAINER_INSTANCES: SaveSeedEntity
SAVE_SEED_ENTITY_TOOL_DEFINITIONS: SaveSeedEntity
SAVE_SEED_ENTITY_TOOL_INSTANCES: SaveSeedEntity
SAVE_SEED_ENTITY_MARKERS: SaveSeedEntity
SAVE_SEED_ENTITY_PART_DEFINITIONS: SaveSeedEntity
SAVE_SEED_ENTITY_PART_INSTANCES: SaveSeedEntity
SAVE_SEED_ENTITY_PRODUCTS: SaveSeedEntity
SAVE_SEED_ENTITY_RECIPES: SaveSeedEntity
SAVE_SEED_ENTITY_SEQUENCES: SaveSeedEntity
SAVE_SEED_ENTITY_TASKS: SaveSeedEntity
SAVE_SEED_ENTITY_PROCESSES: SaveSeedEntity
SAVE_SEED_ENTITY_SEQUENCE_RUNS: SaveSeedEntity
SAVE_SEED_ENTITY_TASK_RUNS: SaveSeedEntity
SAVE_SEED_ENTITY_FEEDBACK: SaveSeedEntity
SAVE_SEED_ENTITY_ACTIONS: SaveSeedEntity

class SaveSeedRequest(_message.Message):
    __slots__ = ("name", "icon", "description", "include", "exclude")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    name: str
    icon: str
    description: str
    include: _containers.RepeatedScalarFieldContainer[SaveSeedEntity]
    exclude: _containers.RepeatedScalarFieldContainer[SaveSeedEntity]
    def __init__(self, name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., include: _Optional[_Iterable[_Union[SaveSeedEntity, str]]] = ..., exclude: _Optional[_Iterable[_Union[SaveSeedEntity, str]]] = ...) -> None: ...

class LoadSeedRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
