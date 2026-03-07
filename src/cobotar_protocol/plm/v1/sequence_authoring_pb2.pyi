from geometry.v1 import pose_pb2 as _pose_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEQUENCE_TYPE_UNSPECIFIED: _ClassVar[SequenceType]
    SEQUENCE_TYPE_ALL_OF_CHILDREN: _ClassVar[SequenceType]
    SEQUENCE_TYPE_ONE_OF_CHILDREN: _ClassVar[SequenceType]
SEQUENCE_TYPE_UNSPECIFIED: SequenceType
SEQUENCE_TYPE_ALL_OF_CHILDREN: SequenceType
SEQUENCE_TYPE_ONE_OF_CHILDREN: SequenceType

class StoredSequenceMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "sequence_number", "offset", "sequence_ids", "task_ids", "can_bulk_complete")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_IDS_FIELD_NUMBER: _ClassVar[int]
    TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    CAN_BULK_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    sequence_number: int
    offset: _pose_pb2.Pose
    sequence_ids: _containers.RepeatedScalarFieldContainer[str]
    task_ids: _containers.RepeatedScalarFieldContainer[str]
    can_bulk_complete: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., sequence_number: _Optional[int] = ..., offset: _Optional[_Union[_pose_pb2.Pose, _Mapping]] = ..., sequence_ids: _Optional[_Iterable[str]] = ..., task_ids: _Optional[_Iterable[str]] = ..., can_bulk_complete: bool = ...) -> None: ...

class StoredSequenceMessages(_message.Message):
    __slots__ = ("sequences",)
    SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    sequences: _containers.RepeatedCompositeFieldContainer[StoredSequenceMessage]
    def __init__(self, sequences: _Optional[_Iterable[_Union[StoredSequenceMessage, _Mapping]]] = ...) -> None: ...

class NewSequenceMessage(_message.Message):
    __slots__ = ("name", "icon", "description", "sequence_number")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    name: str
    icon: str
    description: str
    sequence_number: int
    def __init__(self, name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., sequence_number: _Optional[int] = ...) -> None: ...

class UpdateSequenceMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "sequence_number", "offset", "sequence_ids", "task_ids", "can_bulk_complete")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_IDS_FIELD_NUMBER: _ClassVar[int]
    TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    CAN_BULK_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    sequence_number: int
    offset: _pose_pb2.Pose
    sequence_ids: _containers.RepeatedScalarFieldContainer[str]
    task_ids: _containers.RepeatedScalarFieldContainer[str]
    can_bulk_complete: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., sequence_number: _Optional[int] = ..., offset: _Optional[_Union[_pose_pb2.Pose, _Mapping]] = ..., sequence_ids: _Optional[_Iterable[str]] = ..., task_ids: _Optional[_Iterable[str]] = ..., can_bulk_complete: bool = ...) -> None: ...
