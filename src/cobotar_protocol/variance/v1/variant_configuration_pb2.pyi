from buf.validate import validate_pb2 as _validate_pb2
from cobotar_protocol.validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VariantSelection(_message.Message):
    __slots__ = ("axis_id", "option_id")
    AXIS_ID_FIELD_NUMBER: _ClassVar[int]
    OPTION_ID_FIELD_NUMBER: _ClassVar[int]
    axis_id: str
    option_id: str
    def __init__(self, axis_id: _Optional[str] = ..., option_id: _Optional[str] = ...) -> None: ...

class VariantConfiguration(_message.Message):
    __slots__ = ("selections",)
    SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    selections: _containers.RepeatedCompositeFieldContainer[VariantSelection]
    def __init__(self, selections: _Optional[_Iterable[_Union[VariantSelection, _Mapping]]] = ...) -> None: ...

class NamedVariantConfiguration(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "configuration")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    configuration: VariantConfiguration
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., configuration: _Optional[_Union[VariantConfiguration, _Mapping]] = ...) -> None: ...

class NamedVariantChoice(_message.Message):
    __slots__ = ("named_variant_configuration_id", "select_at_load")
    NAMED_VARIANT_CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
    SELECT_AT_LOAD_FIELD_NUMBER: _ClassVar[int]
    named_variant_configuration_id: str
    select_at_load: VariantConfiguration
    def __init__(self, named_variant_configuration_id: _Optional[str] = ..., select_at_load: _Optional[_Union[VariantConfiguration, _Mapping]] = ...) -> None: ...
