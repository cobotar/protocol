import datetime

from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import actor_pb2 as _actor_pb2
from common.v1 import key_value_constraint_pb2 as _key_value_constraint_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALIDATION_STATUS_UNSPECIFIED: _ClassVar[ValidationStatus]
    VALIDATION_STATUS_PENDING: _ClassVar[ValidationStatus]
    VALIDATION_STATUS_PASSED: _ClassVar[ValidationStatus]
    VALIDATION_STATUS_FAILED: _ClassVar[ValidationStatus]
    VALIDATION_STATUS_BYPASSED: _ClassVar[ValidationStatus]
VALIDATION_STATUS_UNSPECIFIED: ValidationStatus
VALIDATION_STATUS_PENDING: ValidationStatus
VALIDATION_STATUS_PASSED: ValidationStatus
VALIDATION_STATUS_FAILED: ValidationStatus
VALIDATION_STATUS_BYPASSED: ValidationStatus

class ValidationResult(_message.Message):
    __slots__ = ("id", "task_run_id", "status", "method", "validated_at", "measurements", "validated_by_actor", "comment")
    ID_FIELD_NUMBER: _ClassVar[int]
    TASK_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    VALIDATED_AT_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    VALIDATED_BY_ACTOR_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    task_run_id: str
    status: ValidationStatus
    method: str
    validated_at: _timestamp_pb2.Timestamp
    measurements: _containers.RepeatedCompositeFieldContainer[_key_value_constraint_pb2.KeyValueConstraint]
    validated_by_actor: _actor_pb2.ActorRef
    comment: str
    def __init__(self, id: _Optional[str] = ..., task_run_id: _Optional[str] = ..., status: _Optional[_Union[ValidationStatus, str]] = ..., method: _Optional[str] = ..., validated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., measurements: _Optional[_Iterable[_Union[_key_value_constraint_pb2.KeyValueConstraint, _Mapping]]] = ..., validated_by_actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ..., comment: _Optional[str] = ...) -> None: ...
