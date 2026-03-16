from assembly.v1 import common_pb2 as _common_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from geometry.v1 import vector3_pb2 as _vector3_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PART_TYPE_UNSPECIFIED: _ClassVar[PartType]
    PART_TYPE_COMPONENT: _ClassVar[PartType]
    PART_TYPE_FASTENER: _ClassVar[PartType]
    PART_TYPE_SUBASSEMBLY: _ClassVar[PartType]
    PART_TYPE_CONSUMABLE: _ClassVar[PartType]
    PART_TYPE_LABEL: _ClassVar[PartType]
    PART_TYPE_PACKAGING: _ClassVar[PartType]

class NodeKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_KIND_UNSPECIFIED: _ClassVar[NodeKind]
    NODE_KIND_GROUP: _ClassVar[NodeKind]
    NODE_KIND_PART_OCCURRENCE: _ClassVar[NodeKind]
    NODE_KIND_SUBASSEMBLY_OCCURRENCE: _ClassVar[NodeKind]
    NODE_KIND_PATTERN: _ClassVar[NodeKind]

class JoinMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOIN_METHOD_UNSPECIFIED: _ClassVar[JoinMethod]
    JOIN_METHOD_NONE: _ClassVar[JoinMethod]
    JOIN_METHOD_FASTEN: _ClassVar[JoinMethod]
    JOIN_METHOD_PRESS_FIT: _ClassVar[JoinMethod]
    JOIN_METHOD_SNAP_FIT: _ClassVar[JoinMethod]
    JOIN_METHOD_ADHESIVE: _ClassVar[JoinMethod]
    JOIN_METHOD_WELD: _ClassVar[JoinMethod]
    JOIN_METHOD_PLACE: _ClassVar[JoinMethod]

class MaterialCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MATERIAL_CATEGORY_UNSPECIFIED: _ClassVar[MaterialCategory]
    MATERIAL_CATEGORY_METAL: _ClassVar[MaterialCategory]
    MATERIAL_CATEGORY_POLYMER: _ClassVar[MaterialCategory]
    MATERIAL_CATEGORY_ELASTOMER: _ClassVar[MaterialCategory]
    MATERIAL_CATEGORY_COMPOSITE: _ClassVar[MaterialCategory]
    MATERIAL_CATEGORY_CERAMIC: _ClassVar[MaterialCategory]
    MATERIAL_CATEGORY_GLASS: _ClassVar[MaterialCategory]
    MATERIAL_CATEGORY_WOOD: _ClassVar[MaterialCategory]
    MATERIAL_CATEGORY_FOAM: _ClassVar[MaterialCategory]
    MATERIAL_CATEGORY_OTHER: _ClassVar[MaterialCategory]
PART_TYPE_UNSPECIFIED: PartType
PART_TYPE_COMPONENT: PartType
PART_TYPE_FASTENER: PartType
PART_TYPE_SUBASSEMBLY: PartType
PART_TYPE_CONSUMABLE: PartType
PART_TYPE_LABEL: PartType
PART_TYPE_PACKAGING: PartType
NODE_KIND_UNSPECIFIED: NodeKind
NODE_KIND_GROUP: NodeKind
NODE_KIND_PART_OCCURRENCE: NodeKind
NODE_KIND_SUBASSEMBLY_OCCURRENCE: NodeKind
NODE_KIND_PATTERN: NodeKind
JOIN_METHOD_UNSPECIFIED: JoinMethod
JOIN_METHOD_NONE: JoinMethod
JOIN_METHOD_FASTEN: JoinMethod
JOIN_METHOD_PRESS_FIT: JoinMethod
JOIN_METHOD_SNAP_FIT: JoinMethod
JOIN_METHOD_ADHESIVE: JoinMethod
JOIN_METHOD_WELD: JoinMethod
JOIN_METHOD_PLACE: JoinMethod
MATERIAL_CATEGORY_UNSPECIFIED: MaterialCategory
MATERIAL_CATEGORY_METAL: MaterialCategory
MATERIAL_CATEGORY_POLYMER: MaterialCategory
MATERIAL_CATEGORY_ELASTOMER: MaterialCategory
MATERIAL_CATEGORY_COMPOSITE: MaterialCategory
MATERIAL_CATEGORY_CERAMIC: MaterialCategory
MATERIAL_CATEGORY_GLASS: MaterialCategory
MATERIAL_CATEGORY_WOOD: MaterialCategory
MATERIAL_CATEGORY_FOAM: MaterialCategory
MATERIAL_CATEGORY_OTHER: MaterialCategory

class Dimensions(_message.Message):
    __slots__ = ("x_mm", "y_mm", "z_mm")
    X_MM_FIELD_NUMBER: _ClassVar[int]
    Y_MM_FIELD_NUMBER: _ClassVar[int]
    Z_MM_FIELD_NUMBER: _ClassVar[int]
    x_mm: float
    y_mm: float
    z_mm: float
    def __init__(self, x_mm: _Optional[float] = ..., y_mm: _Optional[float] = ..., z_mm: _Optional[float] = ...) -> None: ...

class MaterialSpec(_message.Message):
    __slots__ = ("category", "name", "grade")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    category: MaterialCategory
    name: str
    grade: str
    def __init__(self, category: _Optional[_Union[MaterialCategory, str]] = ..., name: _Optional[str] = ..., grade: _Optional[str] = ...) -> None: ...

class PartHandlingProfile(_message.Message):
    __slots__ = ("fragile", "esd_sensitive", "requires_two_hand_lift", "requires_fixture_support", "max_grip_force_n", "max_torque_nm", "constraints")
    FRAGILE_FIELD_NUMBER: _ClassVar[int]
    ESD_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_TWO_HAND_LIFT_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_FIXTURE_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    MAX_GRIP_FORCE_N_FIELD_NUMBER: _ClassVar[int]
    MAX_TORQUE_NM_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    fragile: bool
    esd_sensitive: bool
    requires_two_hand_lift: bool
    requires_fixture_support: bool
    max_grip_force_n: float
    max_torque_nm: float
    constraints: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValueConstraint]
    def __init__(self, fragile: bool = ..., esd_sensitive: bool = ..., requires_two_hand_lift: bool = ..., requires_fixture_support: bool = ..., max_grip_force_n: _Optional[float] = ..., max_torque_nm: _Optional[float] = ..., constraints: _Optional[_Iterable[_Union[_common_pb2.KeyValueConstraint, _Mapping]]] = ...) -> None: ...

class PartDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "weight_g", "dimensions", "material", "default_model_id", "handling", "external_references", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_G_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    HANDLING_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: PartType
    weight_g: int
    dimensions: Dimensions
    material: MaterialSpec
    default_model_id: str
    handling: PartHandlingProfile
    external_references: _containers.RepeatedCompositeFieldContainer[_common_pb2.ExternalReference]
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[PartType, str]] = ..., weight_g: _Optional[int] = ..., dimensions: _Optional[_Union[Dimensions, _Mapping]] = ..., material: _Optional[_Union[MaterialSpec, _Mapping]] = ..., default_model_id: _Optional[str] = ..., handling: _Optional[_Union[PartHandlingProfile, _Mapping]] = ..., external_references: _Optional[_Iterable[_Union[_common_pb2.ExternalReference, _Mapping]]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class ProductDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "root_node_id", "nodes", "external_references", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    root_node_id: str
    nodes: _containers.RepeatedCompositeFieldContainer[AssemblyNode]
    external_references: _containers.RepeatedCompositeFieldContainer[_common_pb2.ExternalReference]
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., root_node_id: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[AssemblyNode, _Mapping]]] = ..., external_references: _Optional[_Iterable[_Union[_common_pb2.ExternalReference, _Mapping]]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class VariantCondition(_message.Message):
    __slots__ = ("dimension", "values")
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    dimension: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dimension: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class AssemblyNode(_message.Message):
    __slots__ = ("id", "name", "parent_node_id", "kind", "part_definition_id", "override_model_id", "local_pose", "child_node_ids", "sequence_hint", "cad_occurrence_path", "join_method_hint", "insertion_axis_hint", "preferred_approach_hint", "optional", "applicability", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    PART_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_POSE_FIELD_NUMBER: _ClassVar[int]
    CHILD_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_HINT_FIELD_NUMBER: _ClassVar[int]
    CAD_OCCURRENCE_PATH_FIELD_NUMBER: _ClassVar[int]
    JOIN_METHOD_HINT_FIELD_NUMBER: _ClassVar[int]
    INSERTION_AXIS_HINT_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_APPROACH_HINT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    APPLICABILITY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    parent_node_id: str
    kind: NodeKind
    part_definition_id: str
    override_model_id: str
    local_pose: _pose_pb2.Pose
    child_node_ids: _containers.RepeatedScalarFieldContainer[str]
    sequence_hint: int
    cad_occurrence_path: str
    join_method_hint: JoinMethod
    insertion_axis_hint: _vector3_pb2.Vector3
    preferred_approach_hint: _vector3_pb2.Vector3
    optional: bool
    applicability: _containers.RepeatedCompositeFieldContainer[VariantCondition]
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., parent_node_id: _Optional[str] = ..., kind: _Optional[_Union[NodeKind, str]] = ..., part_definition_id: _Optional[str] = ..., override_model_id: _Optional[str] = ..., local_pose: _Optional[_Union[_pose_pb2.Pose, _Mapping]] = ..., child_node_ids: _Optional[_Iterable[str]] = ..., sequence_hint: _Optional[int] = ..., cad_occurrence_path: _Optional[str] = ..., join_method_hint: _Optional[_Union[JoinMethod, str]] = ..., insertion_axis_hint: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., preferred_approach_hint: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., optional: bool = ..., applicability: _Optional[_Iterable[_Union[VariantCondition, _Mapping]]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class PartDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PartDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[PartDefinition, _Mapping]]] = ...) -> None: ...

class ProductDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ProductDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[ProductDefinition, _Mapping]]] = ...) -> None: ...
