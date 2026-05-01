from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigurationLoadMessage(_message.Message):
    __slots__ = ("request_id", "config_id", "instance_id", "binding_id")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BINDING_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    config_id: str
    instance_id: str
    binding_id: str
    def __init__(self, request_id: _Optional[str] = ..., config_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., binding_id: _Optional[str] = ...) -> None: ...
