from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VariantOption(_message.Message):
    __slots__ = ("id", "name", "icon")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ...) -> None: ...

class VariantAxis(_message.Message):
    __slots__ = ("id", "name", "icon", "options")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    options: _containers.RepeatedCompositeFieldContainer[VariantOption]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., options: _Optional[_Iterable[_Union[VariantOption, _Mapping]]] = ...) -> None: ...

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
