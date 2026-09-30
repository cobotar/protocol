from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PresentationBinding(_message.Message):
    __slots__ = ("role_key", "feedback_id", "action_id")
    ROLE_KEY_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    role_key: str
    feedback_id: str
    action_id: str
    def __init__(self, role_key: _Optional[str] = ..., feedback_id: _Optional[str] = ..., action_id: _Optional[str] = ...) -> None: ...

class PresentationBindingUpdate(_message.Message):
    __slots__ = ("config_id", "binding")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    BINDING_FIELD_NUMBER: _ClassVar[int]
    config_id: str
    binding: PresentationBinding
    def __init__(self, config_id: _Optional[str] = ..., binding: _Optional[_Union[PresentationBinding, _Mapping]] = ...) -> None: ...

class PresentationBindingReset(_message.Message):
    __slots__ = ("config_id", "role_key")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_KEY_FIELD_NUMBER: _ClassVar[int]
    config_id: str
    role_key: str
    def __init__(self, config_id: _Optional[str] = ..., role_key: _Optional[str] = ...) -> None: ...
