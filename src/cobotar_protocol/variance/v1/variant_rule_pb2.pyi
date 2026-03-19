from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VariantPredicate(_message.Message):
    __slots__ = ("axis_id", "allowed_option_ids", "excluded_option_ids")
    AXIS_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_OPTION_IDS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_OPTION_IDS_FIELD_NUMBER: _ClassVar[int]
    axis_id: str
    allowed_option_ids: _containers.RepeatedScalarFieldContainer[str]
    excluded_option_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, axis_id: _Optional[str] = ..., allowed_option_ids: _Optional[_Iterable[str]] = ..., excluded_option_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class VariantRule(_message.Message):
    __slots__ = ("all_of",)
    ALL_OF_FIELD_NUMBER: _ClassVar[int]
    all_of: _containers.RepeatedCompositeFieldContainer[VariantPredicate]
    def __init__(self, all_of: _Optional[_Iterable[_Union[VariantPredicate, _Mapping]]] = ...) -> None: ...
