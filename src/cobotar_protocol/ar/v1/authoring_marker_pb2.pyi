from geometry.v1 import pose_pb2 as _pose_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MarkerNewMessage(_message.Message):
    __slots__ = ("name", "description", "marker_text")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARKER_TEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    marker_text: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., marker_text: _Optional[str] = ...) -> None: ...

class MarkerUpdateMessage(_message.Message):
    __slots__ = ("id", "name", "description", "marker_text", "parent_maker_pose")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARKER_TEXT_FIELD_NUMBER: _ClassVar[int]
    PARENT_MAKER_POSE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    marker_text: str
    parent_maker_pose: _pose_pb2.LocalizedPose
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., marker_text: _Optional[str] = ..., parent_maker_pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ...) -> None: ...

class MarkerDeleteMessage(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
