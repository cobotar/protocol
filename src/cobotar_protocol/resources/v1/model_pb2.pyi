from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import external_references_pb2 as _external_references_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_GROUP_UNSPECIFIED: _ClassVar[ModelGroup]
    MODEL_GROUP_PART: _ClassVar[ModelGroup]
    MODEL_GROUP_PRODUCT: _ClassVar[ModelGroup]
    MODEL_GROUP_TOOL: _ClassVar[ModelGroup]
    MODEL_GROUP_ROBOT: _ClassVar[ModelGroup]
    MODEL_GROUP_CONTAINER: _ClassVar[ModelGroup]
    MODEL_GROUP_ASSET: _ClassVar[ModelGroup]

class AssetFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_FORMAT_UNSPECIFIED: _ClassVar[AssetFormat]
    ASSET_FORMAT_GLB: _ClassVar[AssetFormat]
    ASSET_FORMAT_GLTF: _ClassVar[AssetFormat]
    ASSET_FORMAT_OBJ: _ClassVar[AssetFormat]
    ASSET_FORMAT_FBX: _ClassVar[AssetFormat]
    ASSET_FORMAT_STL: _ClassVar[AssetFormat]
    ASSET_FORMAT_STEP: _ClassVar[AssetFormat]
    ASSET_FORMAT_IGES: _ClassVar[AssetFormat]
    ASSET_FORMAT_USD: _ClassVar[AssetFormat]
    ASSET_FORMAT_USDZ: _ClassVar[AssetFormat]
    ASSET_FORMAT_PNG: _ClassVar[AssetFormat]
    ASSET_FORMAT_JPEG: _ClassVar[AssetFormat]
    ASSET_FORMAT_WEBP: _ClassVar[AssetFormat]
    ASSET_FORMAT_SVG: _ClassVar[AssetFormat]
    ASSET_FORMAT_MTL: _ClassVar[AssetFormat]
    ASSET_FORMAT_BASIS: _ClassVar[AssetFormat]
    ASSET_FORMAT_KTX2: _ClassVar[AssetFormat]
    ASSET_FORMAT_ZIP: _ClassVar[AssetFormat]

class ModelUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_UNIT_UNSPECIFIED: _ClassVar[ModelUnit]
    MODEL_UNIT_MILLIMETER: _ClassVar[ModelUnit]
    MODEL_UNIT_CENTIMETER: _ClassVar[ModelUnit]
    MODEL_UNIT_METER: _ClassVar[ModelUnit]
    MODEL_UNIT_KILOMETER: _ClassVar[ModelUnit]
    MODEL_UNIT_INCH: _ClassVar[ModelUnit]
    MODEL_UNIT_FOOT: _ClassVar[ModelUnit]
    MODEL_UNIT_YARD: _ClassVar[ModelUnit]
    MODEL_UNIT_MICROMETER: _ClassVar[ModelUnit]

class ModelAxis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_AXIS_UNSPECIFIED: _ClassVar[ModelAxis]
    MODEL_AXIS_POSITIVE_X: _ClassVar[ModelAxis]
    MODEL_AXIS_NEGATIVE_X: _ClassVar[ModelAxis]
    MODEL_AXIS_POSITIVE_Y: _ClassVar[ModelAxis]
    MODEL_AXIS_NEGATIVE_Y: _ClassVar[ModelAxis]
    MODEL_AXIS_POSITIVE_Z: _ClassVar[ModelAxis]
    MODEL_AXIS_NEGATIVE_Z: _ClassVar[ModelAxis]

class ModelStorageBackend(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_STORAGE_BACKEND_UNSPECIFIED: _ClassVar[ModelStorageBackend]
    MODEL_STORAGE_BACKEND_BUILT_IN: _ClassVar[ModelStorageBackend]
    MODEL_STORAGE_BACKEND_NATS_OBJECT_STORE: _ClassVar[ModelStorageBackend]
    MODEL_STORAGE_BACKEND_S3: _ClassVar[ModelStorageBackend]
    MODEL_STORAGE_BACKEND_MINIO: _ClassVar[ModelStorageBackend]
    MODEL_STORAGE_BACKEND_LOCAL_FILE: _ClassVar[ModelStorageBackend]
    MODEL_STORAGE_BACKEND_EXTERNAL_URL: _ClassVar[ModelStorageBackend]
MODEL_GROUP_UNSPECIFIED: ModelGroup
MODEL_GROUP_PART: ModelGroup
MODEL_GROUP_PRODUCT: ModelGroup
MODEL_GROUP_TOOL: ModelGroup
MODEL_GROUP_ROBOT: ModelGroup
MODEL_GROUP_CONTAINER: ModelGroup
MODEL_GROUP_ASSET: ModelGroup
ASSET_FORMAT_UNSPECIFIED: AssetFormat
ASSET_FORMAT_GLB: AssetFormat
ASSET_FORMAT_GLTF: AssetFormat
ASSET_FORMAT_OBJ: AssetFormat
ASSET_FORMAT_FBX: AssetFormat
ASSET_FORMAT_STL: AssetFormat
ASSET_FORMAT_STEP: AssetFormat
ASSET_FORMAT_IGES: AssetFormat
ASSET_FORMAT_USD: AssetFormat
ASSET_FORMAT_USDZ: AssetFormat
ASSET_FORMAT_PNG: AssetFormat
ASSET_FORMAT_JPEG: AssetFormat
ASSET_FORMAT_WEBP: AssetFormat
ASSET_FORMAT_SVG: AssetFormat
ASSET_FORMAT_MTL: AssetFormat
ASSET_FORMAT_BASIS: AssetFormat
ASSET_FORMAT_KTX2: AssetFormat
ASSET_FORMAT_ZIP: AssetFormat
MODEL_UNIT_UNSPECIFIED: ModelUnit
MODEL_UNIT_MILLIMETER: ModelUnit
MODEL_UNIT_CENTIMETER: ModelUnit
MODEL_UNIT_METER: ModelUnit
MODEL_UNIT_KILOMETER: ModelUnit
MODEL_UNIT_INCH: ModelUnit
MODEL_UNIT_FOOT: ModelUnit
MODEL_UNIT_YARD: ModelUnit
MODEL_UNIT_MICROMETER: ModelUnit
MODEL_AXIS_UNSPECIFIED: ModelAxis
MODEL_AXIS_POSITIVE_X: ModelAxis
MODEL_AXIS_NEGATIVE_X: ModelAxis
MODEL_AXIS_POSITIVE_Y: ModelAxis
MODEL_AXIS_NEGATIVE_Y: ModelAxis
MODEL_AXIS_POSITIVE_Z: ModelAxis
MODEL_AXIS_NEGATIVE_Z: ModelAxis
MODEL_STORAGE_BACKEND_UNSPECIFIED: ModelStorageBackend
MODEL_STORAGE_BACKEND_BUILT_IN: ModelStorageBackend
MODEL_STORAGE_BACKEND_NATS_OBJECT_STORE: ModelStorageBackend
MODEL_STORAGE_BACKEND_S3: ModelStorageBackend
MODEL_STORAGE_BACKEND_MINIO: ModelStorageBackend
MODEL_STORAGE_BACKEND_LOCAL_FILE: ModelStorageBackend
MODEL_STORAGE_BACKEND_EXTERNAL_URL: ModelStorageBackend

class StoredAssetRef(_message.Message):
    __slots__ = ("backend", "format", "bucket", "object_key", "uri", "filename", "content_type", "size_bytes", "sha256", "unit", "up_axis", "forward_axis")
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    UP_AXIS_FIELD_NUMBER: _ClassVar[int]
    FORWARD_AXIS_FIELD_NUMBER: _ClassVar[int]
    backend: ModelStorageBackend
    format: AssetFormat
    bucket: str
    object_key: str
    uri: str
    filename: str
    content_type: str
    size_bytes: int
    sha256: str
    unit: ModelUnit
    up_axis: ModelAxis
    forward_axis: ModelAxis
    def __init__(self, backend: _Optional[_Union[ModelStorageBackend, str]] = ..., format: _Optional[_Union[AssetFormat, str]] = ..., bucket: _Optional[str] = ..., object_key: _Optional[str] = ..., uri: _Optional[str] = ..., filename: _Optional[str] = ..., content_type: _Optional[str] = ..., size_bytes: _Optional[int] = ..., sha256: _Optional[str] = ..., unit: _Optional[_Union[ModelUnit, str]] = ..., up_axis: _Optional[_Union[ModelAxis, str]] = ..., forward_axis: _Optional[_Union[ModelAxis, str]] = ...) -> None: ...

class ModelArtifact(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "group", "asset", "thumbnail", "alternatives", "version", "external_references")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    group: ModelGroup
    asset: StoredAssetRef
    thumbnail: StoredAssetRef
    alternatives: _containers.RepeatedCompositeFieldContainer[StoredAssetRef]
    version: str
    external_references: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., group: _Optional[_Union[ModelGroup, str]] = ..., asset: _Optional[_Union[StoredAssetRef, _Mapping]] = ..., thumbnail: _Optional[_Union[StoredAssetRef, _Mapping]] = ..., alternatives: _Optional[_Iterable[_Union[StoredAssetRef, _Mapping]]] = ..., version: _Optional[str] = ..., external_references: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ...) -> None: ...

class ModelArtifacts(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ModelArtifact]
    def __init__(self, items: _Optional[_Iterable[_Union[ModelArtifact, _Mapping]]] = ...) -> None: ...
