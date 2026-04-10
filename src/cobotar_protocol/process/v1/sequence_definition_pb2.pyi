from buf.validate import validate_pb2 as _validate_pb2
from geometry.v1 import local_target_pb2 as _local_target_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequenceOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEQUENCE_OPERATOR_UNSPECIFIED: _ClassVar[SequenceOperator]
    SEQUENCE_OPERATOR_ORDERED: _ClassVar[SequenceOperator]
    SEQUENCE_OPERATOR_PARALLEL: _ClassVar[SequenceOperator]
    SEQUENCE_OPERATOR_EXCLUSIVE: _ClassVar[SequenceOperator]
    SEQUENCE_OPERATOR_INCLUSIVE: _ClassVar[SequenceOperator]
SEQUENCE_OPERATOR_UNSPECIFIED: SequenceOperator
SEQUENCE_OPERATOR_ORDERED: SequenceOperator
SEQUENCE_OPERATOR_PARALLEL: SequenceOperator
SEQUENCE_OPERATOR_EXCLUSIVE: SequenceOperator
SEQUENCE_OPERATOR_INCLUSIVE: SequenceOperator

class SequenceDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "sequence_number", "parent_sequence_id", "operator", "child_sequence_ids", "child_task_ids", "local_target", "optional", "can_bulk_complete")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PARENT_SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    CHILD_SEQUENCE_IDS_FIELD_NUMBER: _ClassVar[int]
    CHILD_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    CAN_BULK_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    sequence_number: int
    parent_sequence_id: str
    operator: SequenceOperator
    child_sequence_ids: _containers.RepeatedScalarFieldContainer[str]
    child_task_ids: _containers.RepeatedScalarFieldContainer[str]
    local_target: _local_target_pb2.LocalTarget
    optional: bool
    can_bulk_complete: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., sequence_number: _Optional[int] = ..., parent_sequence_id: _Optional[str] = ..., operator: _Optional[_Union[SequenceOperator, str]] = ..., child_sequence_ids: _Optional[_Iterable[str]] = ..., child_task_ids: _Optional[_Iterable[str]] = ..., local_target: _Optional[_Union[_local_target_pb2.LocalTarget, _Mapping]] = ..., optional: bool = ..., can_bulk_complete: bool = ...) -> None: ...

class SequenceDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SequenceDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[SequenceDefinition, _Mapping]]] = ...) -> None: ...
