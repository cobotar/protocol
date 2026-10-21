from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import external_references_pb2 as _external_references_pb2
from resources.v1 import model_pb2 as _model_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadedObject(_message.Message):
    __slots__ = ("bucket", "object_key")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object_key: str
    def __init__(self, bucket: _Optional[str] = ..., object_key: _Optional[str] = ...) -> None: ...

class CreateModelArtifact(_message.Message):
    __slots__ = ("name", "icon", "description", "group", "version", "external_references", "asset", "format", "unit", "up_axis", "forward_axis", "sidecars", "thumbnail")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    UP_AXIS_FIELD_NUMBER: _ClassVar[int]
    FORWARD_AXIS_FIELD_NUMBER: _ClassVar[int]
    SIDECARS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    icon: str
    description: str
    group: _model_pb2.ModelGroup
    version: str
    external_references: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    asset: UploadedObject
    format: _model_pb2.ModelAssetFormat
    unit: _model_pb2.ModelUnit
    up_axis: _model_pb2.ModelAxis
    forward_axis: _model_pb2.ModelAxis
    sidecars: _containers.RepeatedCompositeFieldContainer[UploadedObject]
    thumbnail: UploadedObject
    def __init__(self, name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., group: _Optional[_Union[_model_pb2.ModelGroup, str]] = ..., version: _Optional[str] = ..., external_references: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ..., asset: _Optional[_Union[UploadedObject, _Mapping]] = ..., format: _Optional[_Union[_model_pb2.ModelAssetFormat, str]] = ..., unit: _Optional[_Union[_model_pb2.ModelUnit, str]] = ..., up_axis: _Optional[_Union[_model_pb2.ModelAxis, str]] = ..., forward_axis: _Optional[_Union[_model_pb2.ModelAxis, str]] = ..., sidecars: _Optional[_Iterable[_Union[UploadedObject, _Mapping]]] = ..., thumbnail: _Optional[_Union[UploadedObject, _Mapping]] = ...) -> None: ...
