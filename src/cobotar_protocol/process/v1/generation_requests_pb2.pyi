from buf.validate import validate_pb2 as _validate_pb2
from process.v1 import process_recipe_pb2 as _process_recipe_pb2
from process.v1 import sequence_definition_pb2 as _sequence_definition_pb2
from process.v1 import task_definition_pb2 as _task_definition_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from variance.v1 import variant_configuration_pb2 as _variant_configuration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DraftProcessRecipeGenerateRequest(_message.Message):
    __slots__ = ("product_definition_id", "recipe_id", "recipe_name", "recipe_icon", "recipe_description", "variant_configuration", "insert_align_before_fasten_group", "group_fasteners_threshold", "group_repeated_parts_threshold", "generate_verify_tasks", "prefer_move_tasks_when_possible", "include_optional_nodes", "generate_apply_tasks", "root_node_id", "assemble_subassemblies_as_units_when_possible", "generate_inspect_tasks", "source_container_definition_ids", "target_container_definition_ids")
    PRODUCT_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPE_ICON_FIELD_NUMBER: _ClassVar[int]
    RECIPE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VARIANT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    INSERT_ALIGN_BEFORE_FASTEN_GROUP_FIELD_NUMBER: _ClassVar[int]
    GROUP_FASTENERS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    GROUP_REPEATED_PARTS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    GENERATE_VERIFY_TASKS_FIELD_NUMBER: _ClassVar[int]
    PREFER_MOVE_TASKS_WHEN_POSSIBLE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_OPTIONAL_NODES_FIELD_NUMBER: _ClassVar[int]
    GENERATE_APPLY_TASKS_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSEMBLE_SUBASSEMBLIES_AS_UNITS_WHEN_POSSIBLE_FIELD_NUMBER: _ClassVar[int]
    GENERATE_INSPECT_TASKS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTAINER_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CONTAINER_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    product_definition_id: str
    recipe_id: str
    recipe_name: str
    recipe_icon: str
    recipe_description: str
    variant_configuration: _variant_configuration_pb2.VariantConfiguration
    insert_align_before_fasten_group: bool
    group_fasteners_threshold: int
    group_repeated_parts_threshold: int
    generate_verify_tasks: bool
    prefer_move_tasks_when_possible: bool
    include_optional_nodes: bool
    generate_apply_tasks: bool
    root_node_id: str
    assemble_subassemblies_as_units_when_possible: bool
    generate_inspect_tasks: bool
    source_container_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    target_container_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, product_definition_id: _Optional[str] = ..., recipe_id: _Optional[str] = ..., recipe_name: _Optional[str] = ..., recipe_icon: _Optional[str] = ..., recipe_description: _Optional[str] = ..., variant_configuration: _Optional[_Union[_variant_configuration_pb2.VariantConfiguration, _Mapping]] = ..., insert_align_before_fasten_group: bool = ..., group_fasteners_threshold: _Optional[int] = ..., group_repeated_parts_threshold: _Optional[int] = ..., generate_verify_tasks: bool = ..., prefer_move_tasks_when_possible: bool = ..., include_optional_nodes: bool = ..., generate_apply_tasks: bool = ..., root_node_id: _Optional[str] = ..., assemble_subassemblies_as_units_when_possible: bool = ..., generate_inspect_tasks: bool = ..., source_container_definition_ids: _Optional[_Iterable[str]] = ..., target_container_definition_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DraftDisassemblyProcessRecipeGenerateRequest(_message.Message):
    __slots__ = ("product_definition_id", "recipe_id", "recipe_name", "recipe_icon", "recipe_description", "variant_configuration", "insert_hold_before_unfasten_group", "group_fasteners_threshold", "group_repeated_parts_threshold", "generate_verify_tasks", "prefer_move_tasks_when_possible", "include_optional_nodes", "generate_wipe_tasks", "target_container_definition_ids", "root_node_id", "preserve_subassemblies_when_possible", "reverse_child_sequence_order", "generate_inspect_tasks")
    PRODUCT_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPE_ICON_FIELD_NUMBER: _ClassVar[int]
    RECIPE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VARIANT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    INSERT_HOLD_BEFORE_UNFASTEN_GROUP_FIELD_NUMBER: _ClassVar[int]
    GROUP_FASTENERS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    GROUP_REPEATED_PARTS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    GENERATE_VERIFY_TASKS_FIELD_NUMBER: _ClassVar[int]
    PREFER_MOVE_TASKS_WHEN_POSSIBLE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_OPTIONAL_NODES_FIELD_NUMBER: _ClassVar[int]
    GENERATE_WIPE_TASKS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CONTAINER_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_SUBASSEMBLIES_WHEN_POSSIBLE_FIELD_NUMBER: _ClassVar[int]
    REVERSE_CHILD_SEQUENCE_ORDER_FIELD_NUMBER: _ClassVar[int]
    GENERATE_INSPECT_TASKS_FIELD_NUMBER: _ClassVar[int]
    product_definition_id: str
    recipe_id: str
    recipe_name: str
    recipe_icon: str
    recipe_description: str
    variant_configuration: _variant_configuration_pb2.VariantConfiguration
    insert_hold_before_unfasten_group: bool
    group_fasteners_threshold: int
    group_repeated_parts_threshold: int
    generate_verify_tasks: bool
    prefer_move_tasks_when_possible: bool
    include_optional_nodes: bool
    generate_wipe_tasks: bool
    target_container_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    root_node_id: str
    preserve_subassemblies_when_possible: bool
    reverse_child_sequence_order: bool
    generate_inspect_tasks: bool
    def __init__(self, product_definition_id: _Optional[str] = ..., recipe_id: _Optional[str] = ..., recipe_name: _Optional[str] = ..., recipe_icon: _Optional[str] = ..., recipe_description: _Optional[str] = ..., variant_configuration: _Optional[_Union[_variant_configuration_pb2.VariantConfiguration, _Mapping]] = ..., insert_hold_before_unfasten_group: bool = ..., group_fasteners_threshold: _Optional[int] = ..., group_repeated_parts_threshold: _Optional[int] = ..., generate_verify_tasks: bool = ..., prefer_move_tasks_when_possible: bool = ..., include_optional_nodes: bool = ..., generate_wipe_tasks: bool = ..., target_container_definition_ids: _Optional[_Iterable[str]] = ..., root_node_id: _Optional[str] = ..., preserve_subassemblies_when_possible: bool = ..., reverse_child_sequence_order: bool = ..., generate_inspect_tasks: bool = ...) -> None: ...

class DraftProcessRecipeGenerateIssue(_message.Message):
    __slots__ = ("message", "node_id", "part_definition_id")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PART_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    message: str
    node_id: str
    part_definition_id: str
    def __init__(self, message: _Optional[str] = ..., node_id: _Optional[str] = ..., part_definition_id: _Optional[str] = ...) -> None: ...

class DraftProcessRecipeGenerateResult(_message.Message):
    __slots__ = ("recipe", "sequences", "tasks", "issues")
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    recipe: _process_recipe_pb2.ProcessRecipe
    sequences: _containers.RepeatedCompositeFieldContainer[_sequence_definition_pb2.SequenceDefinition]
    tasks: _containers.RepeatedCompositeFieldContainer[_task_definition_pb2.TaskDefinition]
    issues: _containers.RepeatedCompositeFieldContainer[DraftProcessRecipeGenerateIssue]
    def __init__(self, recipe: _Optional[_Union[_process_recipe_pb2.ProcessRecipe, _Mapping]] = ..., sequences: _Optional[_Iterable[_Union[_sequence_definition_pb2.SequenceDefinition, _Mapping]]] = ..., tasks: _Optional[_Iterable[_Union[_task_definition_pb2.TaskDefinition, _Mapping]]] = ..., issues: _Optional[_Iterable[_Union[DraftProcessRecipeGenerateIssue, _Mapping]]] = ...) -> None: ...
