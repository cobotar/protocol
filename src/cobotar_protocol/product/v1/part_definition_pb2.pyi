from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import external_references_pb2 as _external_references_pb2
from common.v1 import key_value_constraint_pb2 as _key_value_constraint_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
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
    PART_TYPE_PCB: _ClassVar[PartType]
    PART_TYPE_ELECTRONIC_COMPONENT: _ClassVar[PartType]
    PART_TYPE_ELECTRICAL_COMPONENT: _ClassVar[PartType]
    PART_TYPE_CABLE: _ClassVar[PartType]
    PART_TYPE_DISPENSED_MATERIAL: _ClassVar[PartType]

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
    MATERIAL_CATEGORY_ELECTRONICS_SUBSTRATE: _ClassVar[MaterialCategory]
    MATERIAL_CATEGORY_CHEMICAL: _ClassVar[MaterialCategory]
    MATERIAL_CATEGORY_OTHER: _ClassVar[MaterialCategory]
PART_TYPE_UNSPECIFIED: PartType
PART_TYPE_COMPONENT: PartType
PART_TYPE_FASTENER: PartType
PART_TYPE_SUBASSEMBLY: PartType
PART_TYPE_CONSUMABLE: PartType
PART_TYPE_LABEL: PartType
PART_TYPE_PACKAGING: PartType
PART_TYPE_PCB: PartType
PART_TYPE_ELECTRONIC_COMPONENT: PartType
PART_TYPE_ELECTRICAL_COMPONENT: PartType
PART_TYPE_CABLE: PartType
PART_TYPE_DISPENSED_MATERIAL: PartType
MATERIAL_CATEGORY_UNSPECIFIED: MaterialCategory
MATERIAL_CATEGORY_METAL: MaterialCategory
MATERIAL_CATEGORY_POLYMER: MaterialCategory
MATERIAL_CATEGORY_ELASTOMER: MaterialCategory
MATERIAL_CATEGORY_COMPOSITE: MaterialCategory
MATERIAL_CATEGORY_CERAMIC: MaterialCategory
MATERIAL_CATEGORY_GLASS: MaterialCategory
MATERIAL_CATEGORY_WOOD: MaterialCategory
MATERIAL_CATEGORY_FOAM: MaterialCategory
MATERIAL_CATEGORY_ELECTRONICS_SUBSTRATE: MaterialCategory
MATERIAL_CATEGORY_CHEMICAL: MaterialCategory
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
    constraints: _containers.RepeatedCompositeFieldContainer[_key_value_constraint_pb2.KeyValueConstraint]
    def __init__(self, fragile: bool = ..., esd_sensitive: bool = ..., requires_two_hand_lift: bool = ..., requires_fixture_support: bool = ..., max_grip_force_n: _Optional[float] = ..., max_torque_nm: _Optional[float] = ..., constraints: _Optional[_Iterable[_Union[_key_value_constraint_pb2.KeyValueConstraint, _Mapping]]] = ...) -> None: ...

class PartDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "subtype", "weight_g", "dimensions", "material", "default_model_id", "handling", "external_references", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
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
    subtype: str
    weight_g: int
    dimensions: Dimensions
    material: MaterialSpec
    default_model_id: str
    handling: PartHandlingProfile
    external_references: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[PartType, str]] = ..., subtype: _Optional[str] = ..., weight_g: _Optional[int] = ..., dimensions: _Optional[_Union[Dimensions, _Mapping]] = ..., material: _Optional[_Union[MaterialSpec, _Mapping]] = ..., default_model_id: _Optional[str] = ..., handling: _Optional[_Union[PartHandlingProfile, _Mapping]] = ..., external_references: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class PartDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PartDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[PartDefinition, _Mapping]]] = ...) -> None: ...
