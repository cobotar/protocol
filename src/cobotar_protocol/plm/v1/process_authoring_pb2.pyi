from geometry.v1 import pose_pb2 as _pose_pb2
from plm.v1 import process_pb2 as _process_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoredProcessMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "fixture_offset", "root_sequence_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FIXTURE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ROOT_SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: _process_pb2.ProcessType
    fixture_offset: _pose_pb2.Pose
    root_sequence_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_process_pb2.ProcessType, str]] = ..., fixture_offset: _Optional[_Union[_pose_pb2.Pose, _Mapping]] = ..., root_sequence_id: _Optional[str] = ...) -> None: ...

class StoredProcessMessages(_message.Message):
    __slots__ = ("processes",)
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    processes: _containers.RepeatedCompositeFieldContainer[StoredProcessMessage]
    def __init__(self, processes: _Optional[_Iterable[_Union[StoredProcessMessage, _Mapping]]] = ...) -> None: ...

class NewProcessMessage(_message.Message):
    __slots__ = ("name", "icon", "description", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    icon: str
    description: str
    type: _process_pb2.ProcessType
    def __init__(self, name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_process_pb2.ProcessType, str]] = ...) -> None: ...

class UpdateProcessMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "fixture_offset", "root_sequence_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FIXTURE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ROOT_SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: _process_pb2.ProcessType
    fixture_offset: _pose_pb2.Pose
    root_sequence_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_process_pb2.ProcessType, str]] = ..., fixture_offset: _Optional[_Union[_pose_pb2.Pose, _Mapping]] = ..., root_sequence_id: _Optional[str] = ...) -> None: ...
