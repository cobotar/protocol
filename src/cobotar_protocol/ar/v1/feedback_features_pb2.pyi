from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FeedbackFeature(_message.Message):
    __slots__ = ("key", "description", "property_keys")
    KEY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_KEYS_FIELD_NUMBER: _ClassVar[int]
    key: str
    description: str
    property_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., description: _Optional[str] = ..., property_keys: _Optional[_Iterable[str]] = ...) -> None: ...
