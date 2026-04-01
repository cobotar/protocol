from buf.validate import validate_pb2 as _validate_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToolPlacement(_message.Message):
    __slots__ = ("tool_instance_id", "pose", "comment")
    TOOL_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    tool_instance_id: str
    pose: _pose_pb2.LocalizedPose
    comment: str
    def __init__(self, tool_instance_id: _Optional[str] = ..., pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., comment: _Optional[str] = ...) -> None: ...

class AssetPlacement(_message.Message):
    __slots__ = ("asset_instance_id", "pose", "comment")
    ASSET_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    asset_instance_id: str
    pose: _pose_pb2.LocalizedPose
    comment: str
    def __init__(self, asset_instance_id: _Optional[str] = ..., pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., comment: _Optional[str] = ...) -> None: ...

class RobotPlacement(_message.Message):
    __slots__ = ("robot_instance_id", "pose", "comment")
    ROBOT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    robot_instance_id: str
    pose: _pose_pb2.LocalizedPose
    comment: str
    def __init__(self, robot_instance_id: _Optional[str] = ..., pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., comment: _Optional[str] = ...) -> None: ...

class MarkerPlacement(_message.Message):
    __slots__ = ("marker_instance_id", "pose", "comment")
    MARKER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    marker_instance_id: str
    pose: _pose_pb2.LocalizedPose
    comment: str
    def __init__(self, marker_instance_id: _Optional[str] = ..., pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., comment: _Optional[str] = ...) -> None: ...
