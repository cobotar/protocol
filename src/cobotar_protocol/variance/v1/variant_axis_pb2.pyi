from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from variance.v1 import variant_condition_pb2 as _variant_condition_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VariantOption(_message.Message):
    __slots__ = ("id", "name", "icon", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class VariantAxis(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "options", "derivation")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DERIVATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    options: _containers.RepeatedCompositeFieldContainer[VariantOption]
    derivation: VariantDerivation
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., options: _Optional[_Iterable[_Union[VariantOption, _Mapping]]] = ..., derivation: _Optional[_Union[VariantDerivation, _Mapping]] = ...) -> None: ...

class VariantDerivation(_message.Message):
    __slots__ = ("options",)
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedCompositeFieldContainer[DerivedVariantOption]
    def __init__(self, options: _Optional[_Iterable[_Union[DerivedVariantOption, _Mapping]]] = ...) -> None: ...

class DerivedVariantOption(_message.Message):
    __slots__ = ("option_id", "when")
    OPTION_ID_FIELD_NUMBER: _ClassVar[int]
    WHEN_FIELD_NUMBER: _ClassVar[int]
    option_id: str
    when: _variant_condition_pb2.VariantCondition
    def __init__(self, option_id: _Optional[str] = ..., when: _Optional[_Union[_variant_condition_pb2.VariantCondition, _Mapping]] = ...) -> None: ...
