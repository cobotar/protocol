from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import key_value_constraint_pb2 as _key_value_constraint_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from geometry.v1 import vector3_pb2 as _vector3_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContainerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTAINER_TYPE_UNSPECIFIED: _ClassVar[ContainerType]
    CONTAINER_TYPE_STORAGE: _ClassVar[ContainerType]
    CONTAINER_TYPE_KIT: _ClassVar[ContainerType]
    CONTAINER_TYPE_TRAY: _ClassVar[ContainerType]
    CONTAINER_TYPE_FIXTURE: _ClassVar[ContainerType]

class ContainerSlotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTAINER_SLOT_TYPE_UNSPECIFIED: _ClassVar[ContainerSlotType]
    CONTAINER_SLOT_TYPE_STORAGE_BIN: _ClassVar[ContainerSlotType]
    CONTAINER_SLOT_TYPE_KIT_SLOT: _ClassVar[ContainerSlotType]
    CONTAINER_SLOT_TYPE_TRAY_CELL: _ClassVar[ContainerSlotType]
    CONTAINER_SLOT_TYPE_FIXTURE_SLOT: _ClassVar[ContainerSlotType]
CONTAINER_TYPE_UNSPECIFIED: ContainerType
CONTAINER_TYPE_STORAGE: ContainerType
CONTAINER_TYPE_KIT: ContainerType
CONTAINER_TYPE_TRAY: ContainerType
CONTAINER_TYPE_FIXTURE: ContainerType
CONTAINER_SLOT_TYPE_UNSPECIFIED: ContainerSlotType
CONTAINER_SLOT_TYPE_STORAGE_BIN: ContainerSlotType
CONTAINER_SLOT_TYPE_KIT_SLOT: ContainerSlotType
CONTAINER_SLOT_TYPE_TRAY_CELL: ContainerSlotType
CONTAINER_SLOT_TYPE_FIXTURE_SLOT: ContainerSlotType

class ContainerSlotRef(_message.Message):
    __slots__ = ("container_instance_id", "slot_id", "type")
    CONTAINER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    container_instance_id: str
    slot_id: str
    type: ContainerSlotType
    def __init__(self, container_instance_id: _Optional[str] = ..., slot_id: _Optional[str] = ..., type: _Optional[_Union[ContainerSlotType, str]] = ...) -> None: ...

class ContainerSlotDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "pose", "size", "type", "supported_product_definition_ids", "supported_root_part_definition_ids", "supported_part_definition_ids", "constraints", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PRODUCT_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ROOT_PART_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PART_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    pose: _pose_pb2.Pose
    size: _vector3_pb2.Vector3
    type: ContainerSlotType
    supported_product_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    supported_root_part_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    supported_part_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    constraints: _containers.RepeatedCompositeFieldContainer[_key_value_constraint_pb2.KeyValueConstraint]
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., pose: _Optional[_Union[_pose_pb2.Pose, _Mapping]] = ..., size: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., type: _Optional[_Union[ContainerSlotType, str]] = ..., supported_product_definition_ids: _Optional[_Iterable[str]] = ..., supported_root_part_definition_ids: _Optional[_Iterable[str]] = ..., supported_part_definition_ids: _Optional[_Iterable[str]] = ..., constraints: _Optional[_Iterable[_Union[_key_value_constraint_pb2.KeyValueConstraint, _Mapping]]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class ContainerDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "model_id", "slots", "constraints", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: ContainerType
    model_id: str
    slots: _containers.RepeatedCompositeFieldContainer[ContainerSlotDefinition]
    constraints: _containers.RepeatedCompositeFieldContainer[_key_value_constraint_pb2.KeyValueConstraint]
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[ContainerType, str]] = ..., model_id: _Optional[str] = ..., slots: _Optional[_Iterable[_Union[ContainerSlotDefinition, _Mapping]]] = ..., constraints: _Optional[_Iterable[_Union[_key_value_constraint_pb2.KeyValueConstraint, _Mapping]]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class ContainerDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ContainerDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[ContainerDefinition, _Mapping]]] = ...) -> None: ...
