from ar.v1 import action_pb2 as _action_pb2
from ar.v1 import feedback_pb2 as _feedback_pb2
from capability.v1 import actor_skill_pb2 as _actor_skill_pb2
from capability.v1 import skill_definition_pb2 as _skill_definition_pb2
from process.v1 import process_recipe_pb2 as _process_recipe_pb2
from process.v1 import sequence_definition_pb2 as _sequence_definition_pb2
from process.v1 import task_definition_pb2 as _task_definition_pb2
from product.v1 import part_definition_pb2 as _part_definition_pb2
from product.v1 import part_instance_pb2 as _part_instance_pb2
from product.v1 import product_definition_pb2 as _product_definition_pb2
from resources.v1 import asset_definition_pb2 as _asset_definition_pb2
from resources.v1 import asset_instance_pb2 as _asset_instance_pb2
from resources.v1 import cell_definition_pb2 as _cell_definition_pb2
from resources.v1 import container_definition_pb2 as _container_definition_pb2
from resources.v1 import container_instance_pb2 as _container_instance_pb2
from resources.v1 import device_pb2 as _device_pb2
from resources.v1 import line_definition_pb2 as _line_definition_pb2
from resources.v1 import marker_instance_pb2 as _marker_instance_pb2
from resources.v1 import model_pb2 as _model_pb2
from resources.v1 import robot_definition_pb2 as _robot_definition_pb2
from resources.v1 import robot_instance_pb2 as _robot_instance_pb2
from resources.v1 import station_definition_pb2 as _station_definition_pb2
from resources.v1 import tool_definition_pb2 as _tool_definition_pb2
from resources.v1 import tool_instance_pb2 as _tool_instance_pb2
from resources.v1 import worker_definition_pb2 as _worker_definition_pb2
from runtime.v1 import process_run_pb2 as _process_run_pb2
from runtime.v1 import sequence_run_pb2 as _sequence_run_pb2
from runtime.v1 import task_run_pb2 as _task_run_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Seed(_message.Message):
    __slots__ = ("lines", "cells", "stations", "workers", "robot_definitions", "robot_instances", "skills", "actor_skills", "devices", "models", "asset_definitions", "asset_instances", "container_definitions", "container_instances", "tool_definitions", "tool_instances", "markers", "part_definitions", "part_instances", "products", "recipes", "sequences", "tasks", "processes", "sequence_runs", "task_runs", "feedback", "actions")
    LINES_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    STATIONS_FIELD_NUMBER: _ClassVar[int]
    WORKERS_FIELD_NUMBER: _ClassVar[int]
    ROBOT_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    ROBOT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    ACTOR_SKILLS_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    ASSET_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    ASSET_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    TOOL_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    TOOL_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MARKERS_FIELD_NUMBER: _ClassVar[int]
    PART_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    PART_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_RUNS_FIELD_NUMBER: _ClassVar[int]
    TASK_RUNS_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    lines: _containers.RepeatedCompositeFieldContainer[_line_definition_pb2.LineDefinition]
    cells: _containers.RepeatedCompositeFieldContainer[_cell_definition_pb2.CellDefinition]
    stations: _containers.RepeatedCompositeFieldContainer[_station_definition_pb2.StationDefinition]
    workers: _containers.RepeatedCompositeFieldContainer[_worker_definition_pb2.WorkerDefinition]
    robot_definitions: _containers.RepeatedCompositeFieldContainer[_robot_definition_pb2.RobotDefinition]
    robot_instances: _containers.RepeatedCompositeFieldContainer[_robot_instance_pb2.RobotInstance]
    skills: _containers.RepeatedCompositeFieldContainer[_skill_definition_pb2.SkillDefinition]
    actor_skills: _containers.RepeatedCompositeFieldContainer[_actor_skill_pb2.ActorSkill]
    devices: _containers.RepeatedCompositeFieldContainer[_device_pb2.DeviceMessage]
    models: _containers.RepeatedCompositeFieldContainer[_model_pb2.ModelArtifact]
    asset_definitions: _containers.RepeatedCompositeFieldContainer[_asset_definition_pb2.AssetDefinition]
    asset_instances: _containers.RepeatedCompositeFieldContainer[_asset_instance_pb2.AssetInstance]
    container_definitions: _containers.RepeatedCompositeFieldContainer[_container_definition_pb2.ContainerDefinition]
    container_instances: _containers.RepeatedCompositeFieldContainer[_container_instance_pb2.ContainerInstance]
    tool_definitions: _containers.RepeatedCompositeFieldContainer[_tool_definition_pb2.ToolDefinition]
    tool_instances: _containers.RepeatedCompositeFieldContainer[_tool_instance_pb2.ToolInstance]
    markers: _containers.RepeatedCompositeFieldContainer[_marker_instance_pb2.MarkerInstance]
    part_definitions: _containers.RepeatedCompositeFieldContainer[_part_definition_pb2.PartDefinition]
    part_instances: _containers.RepeatedCompositeFieldContainer[_part_instance_pb2.PartInstance]
    products: _containers.RepeatedCompositeFieldContainer[_product_definition_pb2.ProductDefinition]
    recipes: _containers.RepeatedCompositeFieldContainer[_process_recipe_pb2.ProcessRecipe]
    sequences: _containers.RepeatedCompositeFieldContainer[_sequence_definition_pb2.SequenceDefinition]
    tasks: _containers.RepeatedCompositeFieldContainer[_task_definition_pb2.TaskDefinition]
    processes: _containers.RepeatedCompositeFieldContainer[_process_run_pb2.ProcessRun]
    sequence_runs: _containers.RepeatedCompositeFieldContainer[_sequence_run_pb2.SequenceRun]
    task_runs: _containers.RepeatedCompositeFieldContainer[_task_run_pb2.TaskRun]
    feedback: _containers.RepeatedCompositeFieldContainer[_feedback_pb2.FeedbackMessage]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.ActionMessage]
    def __init__(self, lines: _Optional[_Iterable[_Union[_line_definition_pb2.LineDefinition, _Mapping]]] = ..., cells: _Optional[_Iterable[_Union[_cell_definition_pb2.CellDefinition, _Mapping]]] = ..., stations: _Optional[_Iterable[_Union[_station_definition_pb2.StationDefinition, _Mapping]]] = ..., workers: _Optional[_Iterable[_Union[_worker_definition_pb2.WorkerDefinition, _Mapping]]] = ..., robot_definitions: _Optional[_Iterable[_Union[_robot_definition_pb2.RobotDefinition, _Mapping]]] = ..., robot_instances: _Optional[_Iterable[_Union[_robot_instance_pb2.RobotInstance, _Mapping]]] = ..., skills: _Optional[_Iterable[_Union[_skill_definition_pb2.SkillDefinition, _Mapping]]] = ..., actor_skills: _Optional[_Iterable[_Union[_actor_skill_pb2.ActorSkill, _Mapping]]] = ..., devices: _Optional[_Iterable[_Union[_device_pb2.DeviceMessage, _Mapping]]] = ..., models: _Optional[_Iterable[_Union[_model_pb2.ModelArtifact, _Mapping]]] = ..., asset_definitions: _Optional[_Iterable[_Union[_asset_definition_pb2.AssetDefinition, _Mapping]]] = ..., asset_instances: _Optional[_Iterable[_Union[_asset_instance_pb2.AssetInstance, _Mapping]]] = ..., container_definitions: _Optional[_Iterable[_Union[_container_definition_pb2.ContainerDefinition, _Mapping]]] = ..., container_instances: _Optional[_Iterable[_Union[_container_instance_pb2.ContainerInstance, _Mapping]]] = ..., tool_definitions: _Optional[_Iterable[_Union[_tool_definition_pb2.ToolDefinition, _Mapping]]] = ..., tool_instances: _Optional[_Iterable[_Union[_tool_instance_pb2.ToolInstance, _Mapping]]] = ..., markers: _Optional[_Iterable[_Union[_marker_instance_pb2.MarkerInstance, _Mapping]]] = ..., part_definitions: _Optional[_Iterable[_Union[_part_definition_pb2.PartDefinition, _Mapping]]] = ..., part_instances: _Optional[_Iterable[_Union[_part_instance_pb2.PartInstance, _Mapping]]] = ..., products: _Optional[_Iterable[_Union[_product_definition_pb2.ProductDefinition, _Mapping]]] = ..., recipes: _Optional[_Iterable[_Union[_process_recipe_pb2.ProcessRecipe, _Mapping]]] = ..., sequences: _Optional[_Iterable[_Union[_sequence_definition_pb2.SequenceDefinition, _Mapping]]] = ..., tasks: _Optional[_Iterable[_Union[_task_definition_pb2.TaskDefinition, _Mapping]]] = ..., processes: _Optional[_Iterable[_Union[_process_run_pb2.ProcessRun, _Mapping]]] = ..., sequence_runs: _Optional[_Iterable[_Union[_sequence_run_pb2.SequenceRun, _Mapping]]] = ..., task_runs: _Optional[_Iterable[_Union[_task_run_pb2.TaskRun, _Mapping]]] = ..., feedback: _Optional[_Iterable[_Union[_feedback_pb2.FeedbackMessage, _Mapping]]] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.ActionMessage, _Mapping]]] = ...) -> None: ...
