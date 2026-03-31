from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import key_value_constraint_pb2 as _key_value_constraint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALIDATION_MODE_UNSPECIFIED: _ClassVar[ValidationMode]
    VALIDATION_MODE_PRESENCE_CHECK: _ClassVar[ValidationMode]
    VALIDATION_MODE_POSE_CHECK: _ClassVar[ValidationMode]
    VALIDATION_MODE_FASTENER_CHECK: _ClassVar[ValidationMode]
    VALIDATION_MODE_LABEL_CHECK: _ClassVar[ValidationMode]
    VALIDATION_MODE_SURFACE_CHECK: _ClassVar[ValidationMode]

class AssetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_TYPE_UNSPECIFIED: _ClassVar[AssetType]
    ASSET_TYPE_CAMERA: _ClassVar[AssetType]
    ASSET_TYPE_LIGHT: _ClassVar[AssetType]
    ASSET_TYPE_CONVEYOR: _ClassVar[AssetType]
    ASSET_TYPE_SENSOR: _ClassVar[AssetType]
    ASSET_TYPE_HMI: _ClassVar[AssetType]
    ASSET_TYPE_PART_FEEDER: _ClassVar[AssetType]

class AssetDriverType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_DRIVER_TYPE_UNSPECIFIED: _ClassVar[AssetDriverType]
    ASSET_DRIVER_TYPE_DEFAULT: _ClassVar[AssetDriverType]
VALIDATION_MODE_UNSPECIFIED: ValidationMode
VALIDATION_MODE_PRESENCE_CHECK: ValidationMode
VALIDATION_MODE_POSE_CHECK: ValidationMode
VALIDATION_MODE_FASTENER_CHECK: ValidationMode
VALIDATION_MODE_LABEL_CHECK: ValidationMode
VALIDATION_MODE_SURFACE_CHECK: ValidationMode
ASSET_TYPE_UNSPECIFIED: AssetType
ASSET_TYPE_CAMERA: AssetType
ASSET_TYPE_LIGHT: AssetType
ASSET_TYPE_CONVEYOR: AssetType
ASSET_TYPE_SENSOR: AssetType
ASSET_TYPE_HMI: AssetType
ASSET_TYPE_PART_FEEDER: AssetType
ASSET_DRIVER_TYPE_UNSPECIFIED: AssetDriverType
ASSET_DRIVER_TYPE_DEFAULT: AssetDriverType

class VisionCapability(_message.Message):
    __slots__ = ("supported_validation_modes", "supported_part_definition_ids", "supported_task_type_ids", "constraints")
    SUPPORTED_VALIDATION_MODES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PART_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_TASK_TYPE_IDS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    supported_validation_modes: _containers.RepeatedScalarFieldContainer[ValidationMode]
    supported_part_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    supported_task_type_ids: _containers.RepeatedScalarFieldContainer[str]
    constraints: _containers.RepeatedCompositeFieldContainer[_key_value_constraint_pb2.KeyValueConstraint]
    def __init__(self, supported_validation_modes: _Optional[_Iterable[_Union[ValidationMode, str]]] = ..., supported_part_definition_ids: _Optional[_Iterable[str]] = ..., supported_task_type_ids: _Optional[_Iterable[str]] = ..., constraints: _Optional[_Iterable[_Union[_key_value_constraint_pb2.KeyValueConstraint, _Mapping]]] = ...) -> None: ...

class AssetDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "driver_type", "model_id", "vision", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DRIVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    VISION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: AssetType
    driver_type: AssetDriverType
    model_id: str
    vision: VisionCapability
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[AssetType, str]] = ..., driver_type: _Optional[_Union[AssetDriverType, str]] = ..., model_id: _Optional[str] = ..., vision: _Optional[_Union[VisionCapability, _Mapping]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class AssetDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AssetDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[AssetDefinition, _Mapping]]] = ...) -> None: ...
