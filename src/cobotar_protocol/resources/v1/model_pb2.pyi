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

class ModelOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_ORIGIN_UNSPECIFIED: _ClassVar[ModelOrigin]
    MODEL_ORIGIN_BUILT_IN: _ClassVar[ModelOrigin]
    MODEL_ORIGIN_UPLOADED: _ClassVar[ModelOrigin]
    MODEL_ORIGIN_EXTERNAL: _ClassVar[ModelOrigin]

class ModelFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_FORMAT_UNSPECIFIED: _ClassVar[ModelFormat]
    MODEL_FORMAT_GLB: _ClassVar[ModelFormat]
    MODEL_FORMAT_GLTF: _ClassVar[ModelFormat]
    MODEL_FORMAT_OBJ: _ClassVar[ModelFormat]
    MODEL_FORMAT_STEP: _ClassVar[ModelFormat]
    MODEL_FORMAT_STL: _ClassVar[ModelFormat]
    MODEL_FORMAT_USDZ: _ClassVar[ModelFormat]

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
MODEL_ORIGIN_UNSPECIFIED: ModelOrigin
MODEL_ORIGIN_BUILT_IN: ModelOrigin
MODEL_ORIGIN_UPLOADED: ModelOrigin
MODEL_ORIGIN_EXTERNAL: ModelOrigin
MODEL_FORMAT_UNSPECIFIED: ModelFormat
MODEL_FORMAT_GLB: ModelFormat
MODEL_FORMAT_GLTF: ModelFormat
MODEL_FORMAT_OBJ: ModelFormat
MODEL_FORMAT_STEP: ModelFormat
MODEL_FORMAT_STL: ModelFormat
MODEL_FORMAT_USDZ: ModelFormat
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
    __slots__ = ("backend", "bucket", "object_key", "uri", "filename", "content_type", "size_bytes", "sha256")
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    backend: ModelStorageBackend
    bucket: str
    object_key: str
    uri: str
    filename: str
    content_type: str
    size_bytes: int
    sha256: str
    def __init__(self, backend: _Optional[_Union[ModelStorageBackend, str]] = ..., bucket: _Optional[str] = ..., object_key: _Optional[str] = ..., uri: _Optional[str] = ..., filename: _Optional[str] = ..., content_type: _Optional[str] = ..., size_bytes: _Optional[int] = ..., sha256: _Optional[str] = ...) -> None: ...

class ModelArtifact(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "group", "origin", "format", "asset", "thumbnail", "version", "unit", "up_axis", "forward_axis", "external_references")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    UP_AXIS_FIELD_NUMBER: _ClassVar[int]
    FORWARD_AXIS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    group: ModelGroup
    origin: ModelOrigin
    format: ModelFormat
    asset: StoredAssetRef
    thumbnail: StoredAssetRef
    version: str
    unit: ModelUnit
    up_axis: ModelAxis
    forward_axis: ModelAxis
    external_references: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., group: _Optional[_Union[ModelGroup, str]] = ..., origin: _Optional[_Union[ModelOrigin, str]] = ..., format: _Optional[_Union[ModelFormat, str]] = ..., asset: _Optional[_Union[StoredAssetRef, _Mapping]] = ..., thumbnail: _Optional[_Union[StoredAssetRef, _Mapping]] = ..., version: _Optional[str] = ..., unit: _Optional[_Union[ModelUnit, str]] = ..., up_axis: _Optional[_Union[ModelAxis, str]] = ..., forward_axis: _Optional[_Union[ModelAxis, str]] = ..., external_references: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ...) -> None: ...

class ModelArtifacts(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ModelArtifact]
    def __init__(self, items: _Optional[_Iterable[_Union[ModelArtifact, _Mapping]]] = ...) -> None: ...
