from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
ASSET_TYPE_UNSPECIFIED: AssetType
ASSET_TYPE_CAMERA: AssetType
ASSET_TYPE_LIGHT: AssetType
ASSET_TYPE_CONVEYOR: AssetType
ASSET_TYPE_SENSOR: AssetType
ASSET_TYPE_HMI: AssetType
ASSET_TYPE_PART_FEEDER: AssetType
ASSET_DRIVER_TYPE_UNSPECIFIED: AssetDriverType
ASSET_DRIVER_TYPE_DEFAULT: AssetDriverType

class AssetDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "driver_type", "model_id", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DRIVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: AssetType
    driver_type: AssetDriverType
    model_id: str
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[AssetType, str]] = ..., driver_type: _Optional[_Union[AssetDriverType, str]] = ..., model_id: _Optional[str] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class AssetDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AssetDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[AssetDefinition, _Mapping]]] = ...) -> None: ...
