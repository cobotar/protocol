from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DisplayText(_message.Message):
    __slots__ = ("title", "description", "operator_instruction")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    operator_instruction: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., operator_instruction: _Optional[str] = ...) -> None: ...
