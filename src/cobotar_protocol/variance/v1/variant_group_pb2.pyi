from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from variance.v1 import variant_condition_pb2 as _variant_condition_pb2
from variance.v1 import variant_configuration_pb2 as _variant_configuration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VariantGroup(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "axis_ids", "excluded", "allowed")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AXIS_IDS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    axis_ids: _containers.RepeatedScalarFieldContainer[str]
    excluded: _containers.RepeatedCompositeFieldContainer[_variant_condition_pb2.VariantCondition]
    allowed: _containers.RepeatedCompositeFieldContainer[_variant_configuration_pb2.VariantConfiguration]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., axis_ids: _Optional[_Iterable[str]] = ..., excluded: _Optional[_Iterable[_Union[_variant_condition_pb2.VariantCondition, _Mapping]]] = ..., allowed: _Optional[_Iterable[_Union[_variant_configuration_pb2.VariantConfiguration, _Mapping]]] = ...) -> None: ...
