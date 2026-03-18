from assembly.v1 import common_pb2 as _common_pb2
from assembly.v1 import resources_pb2 as _resources_pb2
from assembly.v1 import skill_pb2 as _skill_pb2
from assembly.v1 import variant_pb2 as _variant_pb2
from geometry.v1 import vector3_pb2 as _vector3_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESS_TYPE_UNSPECIFIED: _ClassVar[ProcessType]
    PROCESS_TYPE_ASSEMBLY: _ClassVar[ProcessType]
    PROCESS_TYPE_DISASSEMBLY: _ClassVar[ProcessType]
    PROCESS_TYPE_INSPECTION: _ClassVar[ProcessType]
    PROCESS_TYPE_CHECKLIST: _ClassVar[ProcessType]
    PROCESS_TYPE_KITTING: _ClassVar[ProcessType]
    PROCESS_TYPE_MAINTENANCE: _ClassVar[ProcessType]

class SequenceOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEQUENCE_OPERATOR_UNSPECIFIED: _ClassVar[SequenceOperator]
    SEQUENCE_OPERATOR_ALL_OF_CHILDREN: _ClassVar[SequenceOperator]
    SEQUENCE_OPERATOR_ONE_OF_CHILDREN: _ClassVar[SequenceOperator]
    SEQUENCE_OPERATOR_ORDERED: _ClassVar[SequenceOperator]

class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_TYPE_UNSPECIFIED: _ClassVar[TaskType]
    TASK_TYPE_INSPECT: _ClassVar[TaskType]
    TASK_TYPE_FASTEN: _ClassVar[TaskType]
    TASK_TYPE_UNFASTEN: _ClassVar[TaskType]
    TASK_TYPE_MOUNT: _ClassVar[TaskType]
    TASK_TYPE_UNMOUNT: _ClassVar[TaskType]
    TASK_TYPE_MOVE: _ClassVar[TaskType]
    TASK_TYPE_REMOVE: _ClassVar[TaskType]
    TASK_TYPE_APPLY: _ClassVar[TaskType]
    TASK_TYPE_WIPE: _ClassVar[TaskType]
    TASK_TYPE_ALIGN: _ClassVar[TaskType]
    TASK_TYPE_INSERT: _ClassVar[TaskType]
    TASK_TYPE_HOLD: _ClassVar[TaskType]
    TASK_TYPE_VERIFY: _ClassVar[TaskType]
    TASK_TYPE_PICK: _ClassVar[TaskType]
    TASK_TYPE_PLACE: _ClassVar[TaskType]
    TASK_TYPE_SCAN: _ClassVar[TaskType]
    TASK_TYPE_WAIT: _ClassVar[TaskType]
    TASK_TYPE_CHECK: _ClassVar[TaskType]
    TASK_TYPE_ACKNOWLEDGE: _ClassVar[TaskType]

class TaskAssignmentPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_ASSIGNMENT_PREFERENCE_UNSPECIFIED: _ClassVar[TaskAssignmentPreference]
    TASK_ASSIGNMENT_PREFERENCE_PREFER_HUMAN: _ClassVar[TaskAssignmentPreference]
    TASK_ASSIGNMENT_PREFERENCE_ONLY_HUMAN: _ClassVar[TaskAssignmentPreference]
    TASK_ASSIGNMENT_PREFERENCE_PREFER_ROBOT: _ClassVar[TaskAssignmentPreference]
    TASK_ASSIGNMENT_PREFERENCE_ONLY_ROBOT: _ClassVar[TaskAssignmentPreference]
    TASK_ASSIGNMENT_PREFERENCE_EITHER: _ClassVar[TaskAssignmentPreference]
PROCESS_TYPE_UNSPECIFIED: ProcessType
PROCESS_TYPE_ASSEMBLY: ProcessType
PROCESS_TYPE_DISASSEMBLY: ProcessType
PROCESS_TYPE_INSPECTION: ProcessType
PROCESS_TYPE_CHECKLIST: ProcessType
PROCESS_TYPE_KITTING: ProcessType
PROCESS_TYPE_MAINTENANCE: ProcessType
SEQUENCE_OPERATOR_UNSPECIFIED: SequenceOperator
SEQUENCE_OPERATOR_ALL_OF_CHILDREN: SequenceOperator
SEQUENCE_OPERATOR_ONE_OF_CHILDREN: SequenceOperator
SEQUENCE_OPERATOR_ORDERED: SequenceOperator
TASK_TYPE_UNSPECIFIED: TaskType
TASK_TYPE_INSPECT: TaskType
TASK_TYPE_FASTEN: TaskType
TASK_TYPE_UNFASTEN: TaskType
TASK_TYPE_MOUNT: TaskType
TASK_TYPE_UNMOUNT: TaskType
TASK_TYPE_MOVE: TaskType
TASK_TYPE_REMOVE: TaskType
TASK_TYPE_APPLY: TaskType
TASK_TYPE_WIPE: TaskType
TASK_TYPE_ALIGN: TaskType
TASK_TYPE_INSERT: TaskType
TASK_TYPE_HOLD: TaskType
TASK_TYPE_VERIFY: TaskType
TASK_TYPE_PICK: TaskType
TASK_TYPE_PLACE: TaskType
TASK_TYPE_SCAN: TaskType
TASK_TYPE_WAIT: TaskType
TASK_TYPE_CHECK: TaskType
TASK_TYPE_ACKNOWLEDGE: TaskType
TASK_ASSIGNMENT_PREFERENCE_UNSPECIFIED: TaskAssignmentPreference
TASK_ASSIGNMENT_PREFERENCE_PREFER_HUMAN: TaskAssignmentPreference
TASK_ASSIGNMENT_PREFERENCE_ONLY_HUMAN: TaskAssignmentPreference
TASK_ASSIGNMENT_PREFERENCE_PREFER_ROBOT: TaskAssignmentPreference
TASK_ASSIGNMENT_PREFERENCE_ONLY_ROBOT: TaskAssignmentPreference
TASK_ASSIGNMENT_PREFERENCE_EITHER: TaskAssignmentPreference

class RecipeApplicability(_message.Message):
    __slots__ = ("include", "exclude")
    INCLUDE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    include: _containers.RepeatedCompositeFieldContainer[_variant_pb2.VariantRule]
    exclude: _containers.RepeatedCompositeFieldContainer[_variant_pb2.VariantRule]
    def __init__(self, include: _Optional[_Iterable[_Union[_variant_pb2.VariantRule, _Mapping]]] = ..., exclude: _Optional[_Iterable[_Union[_variant_pb2.VariantRule, _Mapping]]] = ...) -> None: ...

class ProcessRecipe(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "product_definition_id", "applicability", "root_sequence_id", "sequences", "tasks", "supported_container_definition_ids", "external_references", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICABILITY_FIELD_NUMBER: _ClassVar[int]
    ROOT_SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CONTAINER_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: ProcessType
    product_definition_id: str
    applicability: RecipeApplicability
    root_sequence_id: str
    sequences: _containers.RepeatedCompositeFieldContainer[SequenceDefinition]
    tasks: _containers.RepeatedCompositeFieldContainer[TaskDefinition]
    supported_container_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    external_references: _containers.RepeatedCompositeFieldContainer[_common_pb2.ExternalReference]
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[ProcessType, str]] = ..., product_definition_id: _Optional[str] = ..., applicability: _Optional[_Union[RecipeApplicability, _Mapping]] = ..., root_sequence_id: _Optional[str] = ..., sequences: _Optional[_Iterable[_Union[SequenceDefinition, _Mapping]]] = ..., tasks: _Optional[_Iterable[_Union[TaskDefinition, _Mapping]]] = ..., supported_container_definition_ids: _Optional[_Iterable[str]] = ..., external_references: _Optional[_Iterable[_Union[_common_pb2.ExternalReference, _Mapping]]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class SequenceDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "sequence_number", "parent_sequence_id", "operator", "child_sequence_ids", "child_task_ids", "local_target", "optional", "can_bulk_complete", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PARENT_SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    CHILD_SEQUENCE_IDS_FIELD_NUMBER: _ClassVar[int]
    CHILD_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    CAN_BULK_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    sequence_number: int
    parent_sequence_id: str
    operator: SequenceOperator
    child_sequence_ids: _containers.RepeatedScalarFieldContainer[str]
    child_task_ids: _containers.RepeatedScalarFieldContainer[str]
    local_target: _common_pb2.LocalTarget
    optional: bool
    can_bulk_complete: bool
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., sequence_number: _Optional[int] = ..., parent_sequence_id: _Optional[str] = ..., operator: _Optional[_Union[SequenceOperator, str]] = ..., child_sequence_ids: _Optional[_Iterable[str]] = ..., child_task_ids: _Optional[_Iterable[str]] = ..., local_target: _Optional[_Union[_common_pb2.LocalTarget, _Mapping]] = ..., optional: bool = ..., can_bulk_complete: bool = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class TaskTarget(_message.Message):
    __slots__ = ("target_node_id", "target_part_definition_id", "local_target", "asset_instance_id", "robot_instance_id", "station_id", "container_instance_id", "location")
    TARGET_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PART_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    ASSET_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ROBOT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    target_node_id: str
    target_part_definition_id: str
    local_target: _common_pb2.LocalTarget
    asset_instance_id: str
    robot_instance_id: str
    station_id: str
    container_instance_id: str
    location: _resources_pb2.ContainerSlotRef
    def __init__(self, target_node_id: _Optional[str] = ..., target_part_definition_id: _Optional[str] = ..., local_target: _Optional[_Union[_common_pb2.LocalTarget, _Mapping]] = ..., asset_instance_id: _Optional[str] = ..., robot_instance_id: _Optional[str] = ..., station_id: _Optional[str] = ..., container_instance_id: _Optional[str] = ..., location: _Optional[_Union[_resources_pb2.ContainerSlotRef, _Mapping]] = ...) -> None: ...

class ValidationRequirement(_message.Message):
    __slots__ = ("require_tool_feedback", "require_vision_check", "allow_manual_confirmation", "manual_confirmation_min_level", "constraints")
    REQUIRE_TOOL_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_VISION_CHECK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MANUAL_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CONFIRMATION_MIN_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    require_tool_feedback: bool
    require_vision_check: bool
    allow_manual_confirmation: bool
    manual_confirmation_min_level: _skill_pb2.SkillLevel
    constraints: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValueConstraint]
    def __init__(self, require_tool_feedback: bool = ..., require_vision_check: bool = ..., allow_manual_confirmation: bool = ..., manual_confirmation_min_level: _Optional[_Union[_skill_pb2.SkillLevel, str]] = ..., constraints: _Optional[_Iterable[_Union[_common_pb2.KeyValueConstraint, _Mapping]]] = ...) -> None: ...

class TaskExecutionPolicy(_message.Message):
    __slots__ = ("assignment_preference", "actor_constraint", "can_reassign", "can_do", "can_undo", "estimated_duration")
    ASSIGNMENT_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    CAN_REASSIGN_FIELD_NUMBER: _ClassVar[int]
    CAN_DO_FIELD_NUMBER: _ClassVar[int]
    CAN_UNDO_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DURATION_FIELD_NUMBER: _ClassVar[int]
    assignment_preference: TaskAssignmentPreference
    actor_constraint: _skill_pb2.ActorConstraint
    can_reassign: bool
    can_do: bool
    can_undo: bool
    estimated_duration: _common_pb2.EstimatedDuration
    def __init__(self, assignment_preference: _Optional[_Union[TaskAssignmentPreference, str]] = ..., actor_constraint: _Optional[_Union[_skill_pb2.ActorConstraint, _Mapping]] = ..., can_reassign: bool = ..., can_do: bool = ..., can_undo: bool = ..., estimated_duration: _Optional[_Union[_common_pb2.EstimatedDuration, _Mapping]] = ...) -> None: ...

class TaskOverride(_message.Message):
    __slots__ = ("when", "instruction_text", "target_node_id", "approach")
    WHEN_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    TARGET_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    APPROACH_FIELD_NUMBER: _ClassVar[int]
    when: _containers.RepeatedCompositeFieldContainer[_variant_pb2.VariantRule]
    instruction_text: str
    target_node_id: str
    approach: _vector3_pb2.Vector3
    def __init__(self, when: _Optional[_Iterable[_Union[_variant_pb2.VariantRule, _Mapping]]] = ..., instruction_text: _Optional[str] = ..., target_node_id: _Optional[str] = ..., approach: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ...) -> None: ...

class TaskDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "instruction_text", "sequence_number", "task_type", "target", "approach", "tool_requirements", "skill_requirements", "validation", "execution_policy", "safety_relevance", "source_node_id", "destination_node_id", "source_location", "destination_location", "custom", "applicability", "overrides")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    APPROACH_FIELD_NUMBER: _ClassVar[int]
    TOOL_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    SKILL_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    SAFETY_RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    APPLICABILITY_FIELD_NUMBER: _ClassVar[int]
    OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    instruction_text: str
    sequence_number: int
    task_type: TaskType
    target: TaskTarget
    approach: _vector3_pb2.Vector3
    tool_requirements: _containers.RepeatedCompositeFieldContainer[_skill_pb2.ToolRequirement]
    skill_requirements: _containers.RepeatedCompositeFieldContainer[_skill_pb2.SkillRequirement]
    validation: ValidationRequirement
    execution_policy: TaskExecutionPolicy
    safety_relevance: _common_pb2.SafetyRelevance
    source_node_id: str
    destination_node_id: str
    source_location: _resources_pb2.ContainerSlotRef
    destination_location: _resources_pb2.ContainerSlotRef
    custom: _common_pb2.CustomProperties
    applicability: _containers.RepeatedCompositeFieldContainer[_variant_pb2.VariantRule]
    overrides: _containers.RepeatedCompositeFieldContainer[TaskOverride]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., instruction_text: _Optional[str] = ..., sequence_number: _Optional[int] = ..., task_type: _Optional[_Union[TaskType, str]] = ..., target: _Optional[_Union[TaskTarget, _Mapping]] = ..., approach: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., tool_requirements: _Optional[_Iterable[_Union[_skill_pb2.ToolRequirement, _Mapping]]] = ..., skill_requirements: _Optional[_Iterable[_Union[_skill_pb2.SkillRequirement, _Mapping]]] = ..., validation: _Optional[_Union[ValidationRequirement, _Mapping]] = ..., execution_policy: _Optional[_Union[TaskExecutionPolicy, _Mapping]] = ..., safety_relevance: _Optional[_Union[_common_pb2.SafetyRelevance, str]] = ..., source_node_id: _Optional[str] = ..., destination_node_id: _Optional[str] = ..., source_location: _Optional[_Union[_resources_pb2.ContainerSlotRef, _Mapping]] = ..., destination_location: _Optional[_Union[_resources_pb2.ContainerSlotRef, _Mapping]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ..., applicability: _Optional[_Iterable[_Union[_variant_pb2.VariantRule, _Mapping]]] = ..., overrides: _Optional[_Iterable[_Union[TaskOverride, _Mapping]]] = ...) -> None: ...
