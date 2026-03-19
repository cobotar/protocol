from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConstraintOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSTRAINT_OPERATOR_UNSPECIFIED: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_EQ: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_NEQ: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_GT: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_GTE: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_LT: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_LTE: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_IN: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_NOT_IN: _ClassVar[ConstraintOperator]
CONSTRAINT_OPERATOR_UNSPECIFIED: ConstraintOperator
CONSTRAINT_OPERATOR_EQ: ConstraintOperator
CONSTRAINT_OPERATOR_NEQ: ConstraintOperator
CONSTRAINT_OPERATOR_GT: ConstraintOperator
CONSTRAINT_OPERATOR_GTE: ConstraintOperator
CONSTRAINT_OPERATOR_LT: ConstraintOperator
CONSTRAINT_OPERATOR_LTE: ConstraintOperator
CONSTRAINT_OPERATOR_IN: ConstraintOperator
CONSTRAINT_OPERATOR_NOT_IN: ConstraintOperator

class KeyValueConstraint(_message.Message):
    __slots__ = ("key", "op", "value", "values")
    KEY_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    op: ConstraintOperator
    value: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., op: _Optional[_Union[ConstraintOperator, str]] = ..., value: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
