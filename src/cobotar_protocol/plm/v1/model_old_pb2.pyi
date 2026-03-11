from buf.validate import validate_pb2 as _validate_pb2
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
    MODEL_GROUP_TOOLS: _ClassVar[ModelGroup]
    MODEL_GROUP_PARTS: _ClassVar[ModelGroup]
    MODEL_GROUP_ROBOTS: _ClassVar[ModelGroup]
    MODEL_GROUP_ASSETS: _ClassVar[ModelGroup]

class ModelOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_ORIGIN_UNSPECIFIED: _ClassVar[ModelOrigin]
    MODEL_ORIGIN_BUILD_IN: _ClassVar[ModelOrigin]
    MODEL_ORIGIN_UPLOADED: _ClassVar[ModelOrigin]
    MODEL_ORIGIN_EXTERNAL: _ClassVar[ModelOrigin]
MODEL_GROUP_UNSPECIFIED: ModelGroup
MODEL_GROUP_TOOLS: ModelGroup
MODEL_GROUP_PARTS: ModelGroup
MODEL_GROUP_ROBOTS: ModelGroup
MODEL_GROUP_ASSETS: ModelGroup
MODEL_ORIGIN_UNSPECIFIED: ModelOrigin
MODEL_ORIGIN_BUILD_IN: ModelOrigin
MODEL_ORIGIN_UPLOADED: ModelOrigin
MODEL_ORIGIN_EXTERNAL: ModelOrigin

class ModelMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "group", "origin", "filename", "url")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    group: ModelGroup
    origin: ModelOrigin
    filename: str
    url: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., group: _Optional[_Union[ModelGroup, str]] = ..., origin: _Optional[_Union[ModelOrigin, str]] = ..., filename: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class ModelMessages(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[ModelMessage]
    def __init__(self, models: _Optional[_Iterable[_Union[ModelMessage, _Mapping]]] = ...) -> None: ...
