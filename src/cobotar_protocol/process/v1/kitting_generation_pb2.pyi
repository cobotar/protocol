from buf.validate import validate_pb2 as _validate_pb2
from process.v1 import generation_requests_pb2 as _generation_requests_pb2
from process.v1 import task_definition_pb2 as _task_definition_pb2
from product.v1 import part_definition_pb2 as _part_definition_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from variance.v1 import variant_configuration_pb2 as _variant_configuration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KittingBomMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KITTING_BOM_MODE_UNSPECIFIED: _ClassVar[KittingBomMode]
    KITTING_BOM_MODE_LEAF_PARTS: _ClassVar[KittingBomMode]
    KITTING_BOM_MODE_SUBASSEMBLIES_AS_ITEMS: _ClassVar[KittingBomMode]

class KittingItemOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KITTING_ITEM_ORDER_UNSPECIFIED: _ClassVar[KittingItemOrder]
    KITTING_ITEM_ORDER_ANY_ORDER: _ClassVar[KittingItemOrder]
    KITTING_ITEM_ORDER_PRODUCT_SEQUENCE: _ClassVar[KittingItemOrder]
    KITTING_ITEM_ORDER_TARGET_SLOT_SEQUENCE: _ClassVar[KittingItemOrder]

class KittingItemValidationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KITTING_ITEM_VALIDATION_MODE_UNSPECIFIED: _ClassVar[KittingItemValidationMode]
    KITTING_ITEM_VALIDATION_MODE_NONE: _ClassVar[KittingItemValidationMode]
    KITTING_ITEM_VALIDATION_MODE_MANUAL: _ClassVar[KittingItemValidationMode]
    KITTING_ITEM_VALIDATION_MODE_SCAN: _ClassVar[KittingItemValidationMode]
    KITTING_ITEM_VALIDATION_MODE_VISION: _ClassVar[KittingItemValidationMode]

class UnresolvedKittingItemPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNRESOLVED_KITTING_ITEM_POLICY_UNSPECIFIED: _ClassVar[UnresolvedKittingItemPolicy]
    UNRESOLVED_KITTING_ITEM_POLICY_WARN: _ClassVar[UnresolvedKittingItemPolicy]
    UNRESOLVED_KITTING_ITEM_POLICY_FAIL: _ClassVar[UnresolvedKittingItemPolicy]
    UNRESOLVED_KITTING_ITEM_POLICY_SKIP: _ClassVar[UnresolvedKittingItemPolicy]

class KittingItemAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KITTING_ITEM_ACTION_UNSPECIFIED: _ClassVar[KittingItemAction]
    KITTING_ITEM_ACTION_INCLUDE: _ClassVar[KittingItemAction]
    KITTING_ITEM_ACTION_EXCLUDE: _ClassVar[KittingItemAction]

class KittingAggregationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KITTING_AGGREGATION_MODE_UNSPECIFIED: _ClassVar[KittingAggregationMode]
    KITTING_AGGREGATION_MODE_PER_OCCURRENCE: _ClassVar[KittingAggregationMode]
    KITTING_AGGREGATION_MODE_BY_PART_AND_ROUTE: _ClassVar[KittingAggregationMode]

class KittingTaskGranularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KITTING_TASK_GRANULARITY_UNSPECIFIED: _ClassVar[KittingTaskGranularity]
    KITTING_TASK_GRANULARITY_ATOMIC_TRANSFER: _ClassVar[KittingTaskGranularity]
    KITTING_TASK_GRANULARITY_PICK_AND_PLACE: _ClassVar[KittingTaskGranularity]
KITTING_BOM_MODE_UNSPECIFIED: KittingBomMode
KITTING_BOM_MODE_LEAF_PARTS: KittingBomMode
KITTING_BOM_MODE_SUBASSEMBLIES_AS_ITEMS: KittingBomMode
KITTING_ITEM_ORDER_UNSPECIFIED: KittingItemOrder
KITTING_ITEM_ORDER_ANY_ORDER: KittingItemOrder
KITTING_ITEM_ORDER_PRODUCT_SEQUENCE: KittingItemOrder
KITTING_ITEM_ORDER_TARGET_SLOT_SEQUENCE: KittingItemOrder
KITTING_ITEM_VALIDATION_MODE_UNSPECIFIED: KittingItemValidationMode
KITTING_ITEM_VALIDATION_MODE_NONE: KittingItemValidationMode
KITTING_ITEM_VALIDATION_MODE_MANUAL: KittingItemValidationMode
KITTING_ITEM_VALIDATION_MODE_SCAN: KittingItemValidationMode
KITTING_ITEM_VALIDATION_MODE_VISION: KittingItemValidationMode
UNRESOLVED_KITTING_ITEM_POLICY_UNSPECIFIED: UnresolvedKittingItemPolicy
UNRESOLVED_KITTING_ITEM_POLICY_WARN: UnresolvedKittingItemPolicy
UNRESOLVED_KITTING_ITEM_POLICY_FAIL: UnresolvedKittingItemPolicy
UNRESOLVED_KITTING_ITEM_POLICY_SKIP: UnresolvedKittingItemPolicy
KITTING_ITEM_ACTION_UNSPECIFIED: KittingItemAction
KITTING_ITEM_ACTION_INCLUDE: KittingItemAction
KITTING_ITEM_ACTION_EXCLUDE: KittingItemAction
KITTING_AGGREGATION_MODE_UNSPECIFIED: KittingAggregationMode
KITTING_AGGREGATION_MODE_PER_OCCURRENCE: KittingAggregationMode
KITTING_AGGREGATION_MODE_BY_PART_AND_ROUTE: KittingAggregationMode
KITTING_TASK_GRANULARITY_UNSPECIFIED: KittingTaskGranularity
KITTING_TASK_GRANULARITY_ATOMIC_TRANSFER: KittingTaskGranularity
KITTING_TASK_GRANULARITY_PICK_AND_PLACE: KittingTaskGranularity

class KittingItemRoutingOverride(_message.Message):
    __slots__ = ("assembly_node_id", "part_definition_id", "action", "source", "destination")
    ASSEMBLY_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PART_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    assembly_node_id: str
    part_definition_id: str
    action: KittingItemAction
    source: _task_definition_pb2.ContainerTarget
    destination: _task_definition_pb2.ContainerTarget
    def __init__(self, assembly_node_id: _Optional[str] = ..., part_definition_id: _Optional[str] = ..., action: _Optional[_Union[KittingItemAction, str]] = ..., source: _Optional[_Union[_task_definition_pb2.ContainerTarget, _Mapping]] = ..., destination: _Optional[_Union[_task_definition_pb2.ContainerTarget, _Mapping]] = ...) -> None: ...

class DraftKittingProcessRecipeGenerateRequest(_message.Message):
    __slots__ = ("product_definition_id", "recipe_id", "recipe_name", "recipe_icon", "recipe_description", "variant_generation_mode", "variant_configuration", "root_node_id", "include_optional_nodes", "bom_mode", "product_units_per_kit", "source_container_definition_ids", "target_kit_container_definition_id", "routing_overrides", "item_order", "item_validation_mode", "generate_final_kit_verification", "unresolved_item_policy", "excluded_part_types", "aggregation_mode", "task_granularity")
    PRODUCT_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPE_ICON_FIELD_NUMBER: _ClassVar[int]
    RECIPE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VARIANT_GENERATION_MODE_FIELD_NUMBER: _ClassVar[int]
    VARIANT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_OPTIONAL_NODES_FIELD_NUMBER: _ClassVar[int]
    BOM_MODE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UNITS_PER_KIT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTAINER_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    TARGET_KIT_CONTAINER_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTING_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    ITEM_ORDER_FIELD_NUMBER: _ClassVar[int]
    ITEM_VALIDATION_MODE_FIELD_NUMBER: _ClassVar[int]
    GENERATE_FINAL_KIT_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    UNRESOLVED_ITEM_POLICY_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PART_TYPES_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_MODE_FIELD_NUMBER: _ClassVar[int]
    TASK_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    product_definition_id: str
    recipe_id: str
    recipe_name: str
    recipe_icon: str
    recipe_description: str
    variant_generation_mode: _generation_requests_pb2.VariantGenerationMode
    variant_configuration: _variant_configuration_pb2.VariantConfiguration
    root_node_id: str
    include_optional_nodes: bool
    bom_mode: KittingBomMode
    product_units_per_kit: int
    source_container_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    target_kit_container_definition_id: str
    routing_overrides: _containers.RepeatedCompositeFieldContainer[KittingItemRoutingOverride]
    item_order: KittingItemOrder
    item_validation_mode: KittingItemValidationMode
    generate_final_kit_verification: bool
    unresolved_item_policy: UnresolvedKittingItemPolicy
    excluded_part_types: _containers.RepeatedScalarFieldContainer[_part_definition_pb2.PartType]
    aggregation_mode: KittingAggregationMode
    task_granularity: KittingTaskGranularity
    def __init__(self, product_definition_id: _Optional[str] = ..., recipe_id: _Optional[str] = ..., recipe_name: _Optional[str] = ..., recipe_icon: _Optional[str] = ..., recipe_description: _Optional[str] = ..., variant_generation_mode: _Optional[_Union[_generation_requests_pb2.VariantGenerationMode, str]] = ..., variant_configuration: _Optional[_Union[_variant_configuration_pb2.VariantConfiguration, _Mapping]] = ..., root_node_id: _Optional[str] = ..., include_optional_nodes: bool = ..., bom_mode: _Optional[_Union[KittingBomMode, str]] = ..., product_units_per_kit: _Optional[int] = ..., source_container_definition_ids: _Optional[_Iterable[str]] = ..., target_kit_container_definition_id: _Optional[str] = ..., routing_overrides: _Optional[_Iterable[_Union[KittingItemRoutingOverride, _Mapping]]] = ..., item_order: _Optional[_Union[KittingItemOrder, str]] = ..., item_validation_mode: _Optional[_Union[KittingItemValidationMode, str]] = ..., generate_final_kit_verification: bool = ..., unresolved_item_policy: _Optional[_Union[UnresolvedKittingItemPolicy, str]] = ..., excluded_part_types: _Optional[_Iterable[_Union[_part_definition_pb2.PartType, str]]] = ..., aggregation_mode: _Optional[_Union[KittingAggregationMode, str]] = ..., task_granularity: _Optional[_Union[KittingTaskGranularity, str]] = ...) -> None: ...
