from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import enums_pb2 as _enums_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MarkerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MARKER_TYPE_UNSPECIFIED: _ClassVar[MarkerType]
    MARKER_TYPE_QR_CODE: _ClassVar[MarkerType]
MARKER_TYPE_UNSPECIFIED: MarkerType
MARKER_TYPE_QR_CODE: MarkerType

class MarkerInstance(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "marker_text", "type", "confirm_instantiate", "status", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARKER_TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_INSTANTIATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    marker_text: str
    type: MarkerType
    confirm_instantiate: bool
    status: _enums_pb2.ResourceStatus
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., marker_text: _Optional[str] = ..., type: _Optional[_Union[MarkerType, str]] = ..., confirm_instantiate: bool = ..., status: _Optional[_Union[_enums_pb2.ResourceStatus, str]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class MarkerInstances(_message.Message):
    __slots__ = ("markers",)
    MARKERS_FIELD_NUMBER: _ClassVar[int]
    markers: _containers.RepeatedCompositeFieldContainer[MarkerInstance]
    def __init__(self, markers: _Optional[_Iterable[_Union[MarkerInstance, _Mapping]]] = ...) -> None: ...
