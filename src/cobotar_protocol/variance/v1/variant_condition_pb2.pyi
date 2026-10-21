from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AxisCondition(_message.Message):
    __slots__ = ("axis_id", "option_ids")
    AXIS_ID_FIELD_NUMBER: _ClassVar[int]
    OPTION_IDS_FIELD_NUMBER: _ClassVar[int]
    axis_id: str
    option_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, axis_id: _Optional[str] = ..., option_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class VariantCondition(_message.Message):
    __slots__ = ("all_of",)
    ALL_OF_FIELD_NUMBER: _ClassVar[int]
    all_of: _containers.RepeatedCompositeFieldContainer[AxisCondition]
    def __init__(self, all_of: _Optional[_Iterable[_Union[AxisCondition, _Mapping]]] = ...) -> None: ...
