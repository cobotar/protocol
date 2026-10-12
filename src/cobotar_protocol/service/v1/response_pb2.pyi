from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MUTATION_STATUS_UNSPECIFIED: _ClassVar[MutationStatus]
    MUTATION_STATUS_CREATED: _ClassVar[MutationStatus]
    MUTATION_STATUS_UPDATED: _ClassVar[MutationStatus]
    MUTATION_STATUS_UNCHANGED: _ClassVar[MutationStatus]
    MUTATION_STATUS_DELETED: _ClassVar[MutationStatus]
MUTATION_STATUS_UNSPECIFIED: MutationStatus
MUTATION_STATUS_CREATED: MutationStatus
MUTATION_STATUS_UPDATED: MutationStatus
MUTATION_STATUS_UNCHANGED: MutationStatus
MUTATION_STATUS_DELETED: MutationStatus

class ValidationViolation(_message.Message):
    __slots__ = ("field_path", "message", "rule_id")
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    field_path: str
    message: str
    rule_id: str
    def __init__(self, field_path: _Optional[str] = ..., message: _Optional[str] = ..., rule_id: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("success", "message", "main_modified_id", "status", "validation_violations")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAIN_MODIFIED_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    main_modified_id: str
    status: MutationStatus
    validation_violations: _containers.RepeatedCompositeFieldContainer[ValidationViolation]
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., main_modified_id: _Optional[str] = ..., status: _Optional[_Union[MutationStatus, str]] = ..., validation_violations: _Optional[_Iterable[_Union[ValidationViolation, _Mapping]]] = ...) -> None: ...
