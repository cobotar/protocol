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
