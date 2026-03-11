from assembly.v1 import common_pb2 as _common_pb2
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
    MODEL_GROUP_FIXTURE: _ClassVar[ModelGroup]
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
MODEL_GROUP_UNSPECIFIED: ModelGroup
MODEL_GROUP_PART: ModelGroup
MODEL_GROUP_PRODUCT: ModelGroup
MODEL_GROUP_TOOL: ModelGroup
MODEL_GROUP_ROBOT: ModelGroup
MODEL_GROUP_FIXTURE: ModelGroup
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

class ModelArtifact(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "group", "origin", "format", "filename", "uri", "thumbnail_uri", "version", "unit", "external_references", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URI_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    group: ModelGroup
    origin: ModelOrigin
    format: ModelFormat
    filename: str
    uri: str
    thumbnail_uri: str
    version: str
    unit: str
    external_references: _containers.RepeatedCompositeFieldContainer[_common_pb2.ExternalReference]
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., group: _Optional[_Union[ModelGroup, str]] = ..., origin: _Optional[_Union[ModelOrigin, str]] = ..., format: _Optional[_Union[ModelFormat, str]] = ..., filename: _Optional[str] = ..., uri: _Optional[str] = ..., thumbnail_uri: _Optional[str] = ..., version: _Optional[str] = ..., unit: _Optional[str] = ..., external_references: _Optional[_Iterable[_Union[_common_pb2.ExternalReference, _Mapping]]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class ModelArtifacts(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ModelArtifact]
    def __init__(self, items: _Optional[_Iterable[_Union[ModelArtifact, _Mapping]]] = ...) -> None: ...
