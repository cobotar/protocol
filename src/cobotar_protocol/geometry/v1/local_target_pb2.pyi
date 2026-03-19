from geometry.v1 import pose_pb2 as _pose_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalTarget(_message.Message):
    __slots__ = ("anchor_id", "offset")
    ANCHOR_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    anchor_id: str
    offset: _pose_pb2.Pose
    def __init__(self, anchor_id: _Optional[str] = ..., offset: _Optional[_Union[_pose_pb2.Pose, _Mapping]] = ...) -> None: ...
