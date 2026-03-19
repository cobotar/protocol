from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalReference(_message.Message):
    __slots__ = ("system", "external_id", "url")
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    system: str
    external_id: str
    url: str
    def __init__(self, system: _Optional[str] = ..., external_id: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
