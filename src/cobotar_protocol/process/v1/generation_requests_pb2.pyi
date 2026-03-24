from process.v1 import process_recipe_pb2 as _process_recipe_pb2
from variance.v1 import variant_configuration_pb2 as _variant_configuration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DraftProcessRecipeGenerateRequest(_message.Message):
    __slots__ = ("product_definition_id", "recipe_id", "recipe_name", "recipe_description", "variant_configuration", "insert_align_before_fasten_group", "group_fasteners_threshold", "group_repeated_parts_threshold", "generate_verify_tasks", "prefer_move_tasks_when_possible")
    PRODUCT_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VARIANT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    INSERT_ALIGN_BEFORE_FASTEN_GROUP_FIELD_NUMBER: _ClassVar[int]
    GROUP_FASTENERS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    GROUP_REPEATED_PARTS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    GENERATE_VERIFY_TASKS_FIELD_NUMBER: _ClassVar[int]
    PREFER_MOVE_TASKS_WHEN_POSSIBLE_FIELD_NUMBER: _ClassVar[int]
    product_definition_id: str
    recipe_id: str
    recipe_name: str
    recipe_description: str
    variant_configuration: _variant_configuration_pb2.VariantConfiguration
    insert_align_before_fasten_group: bool
    group_fasteners_threshold: int
    group_repeated_parts_threshold: int
    generate_verify_tasks: bool
    prefer_move_tasks_when_possible: bool
    def __init__(self, product_definition_id: _Optional[str] = ..., recipe_id: _Optional[str] = ..., recipe_name: _Optional[str] = ..., recipe_description: _Optional[str] = ..., variant_configuration: _Optional[_Union[_variant_configuration_pb2.VariantConfiguration, _Mapping]] = ..., insert_align_before_fasten_group: bool = ..., group_fasteners_threshold: _Optional[int] = ..., group_repeated_parts_threshold: _Optional[int] = ..., generate_verify_tasks: bool = ..., prefer_move_tasks_when_possible: bool = ...) -> None: ...

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
    __slots__ = ("recipe", "issues")
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    recipe: _process_recipe_pb2.ProcessRecipe
    issues: _containers.RepeatedCompositeFieldContainer[DraftProcessRecipeGenerateIssue]
    def __init__(self, recipe: _Optional[_Union[_process_recipe_pb2.ProcessRecipe, _Mapping]] = ..., issues: _Optional[_Iterable[_Union[DraftProcessRecipeGenerateIssue, _Mapping]]] = ...) -> None: ...
