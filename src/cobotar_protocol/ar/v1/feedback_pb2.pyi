from ar.v1 import provenance_pb2 as _provenance_pb2
from buf.validate import validate_pb2 as _validate_pb2
from geometry.v1 import anchor_pb2 as _anchor_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeedbackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEEDBACK_TYPE_UNSPECIFIED: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_TARGET_GHOST: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_TARGET_HIGHLIGHT: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_SNAP_GUIDES: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_CONTACT_SURFACE_HIGHLIGHT: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_TOLERANCE_ZONE: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_EXPLODED_VIEW: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_PART_HIGHLIGHT: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_TOOL_HIGHLIGHT: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_CONSUMABLE_INDICATOR: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_INSTRUCTION: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_CHECKLIST: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_PROGRESS_PANEL: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_DEPENDENCY_GRAPH: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_TIME_ESTIMATE: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_RULER: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_POSE_VALIDATOR: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_VISION_CONFIRMATION: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_TORQUE_CONFIRMATION: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_ROBOT_PATH: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_ROBOT_WAYPOINTS: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_ROBOT_SILHOUETTE: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_ROBOT_INTENT_CONE: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_ROBOT_OCCUPANCY_VOLUME: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_ROBOT_STATUS: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_ROBOT_LIGHT: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_HANDOVER_ZONE: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_SYNCHRONIZATION_BARRIER: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_SHARED_TASK_INDICATOR: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_ROBOT_ATTENTION: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_MESSAGE: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_ICON: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_HIGHLIGHT: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_ZONE: _ClassVar[FeedbackType]
    FEEDBACK_TYPE_PLAY_SOUND: _ClassVar[FeedbackType]
FEEDBACK_TYPE_UNSPECIFIED: FeedbackType
FEEDBACK_TYPE_TARGET_GHOST: FeedbackType
FEEDBACK_TYPE_TARGET_HIGHLIGHT: FeedbackType
FEEDBACK_TYPE_SNAP_GUIDES: FeedbackType
FEEDBACK_TYPE_CONTACT_SURFACE_HIGHLIGHT: FeedbackType
FEEDBACK_TYPE_TOLERANCE_ZONE: FeedbackType
FEEDBACK_TYPE_EXPLODED_VIEW: FeedbackType
FEEDBACK_TYPE_PART_HIGHLIGHT: FeedbackType
FEEDBACK_TYPE_TOOL_HIGHLIGHT: FeedbackType
FEEDBACK_TYPE_CONSUMABLE_INDICATOR: FeedbackType
FEEDBACK_TYPE_INSTRUCTION: FeedbackType
FEEDBACK_TYPE_CHECKLIST: FeedbackType
FEEDBACK_TYPE_PROGRESS_PANEL: FeedbackType
FEEDBACK_TYPE_DEPENDENCY_GRAPH: FeedbackType
FEEDBACK_TYPE_TIME_ESTIMATE: FeedbackType
FEEDBACK_TYPE_RULER: FeedbackType
FEEDBACK_TYPE_POSE_VALIDATOR: FeedbackType
FEEDBACK_TYPE_VISION_CONFIRMATION: FeedbackType
FEEDBACK_TYPE_TORQUE_CONFIRMATION: FeedbackType
FEEDBACK_TYPE_ROBOT_PATH: FeedbackType
FEEDBACK_TYPE_ROBOT_WAYPOINTS: FeedbackType
FEEDBACK_TYPE_ROBOT_SILHOUETTE: FeedbackType
FEEDBACK_TYPE_ROBOT_INTENT_CONE: FeedbackType
FEEDBACK_TYPE_ROBOT_OCCUPANCY_VOLUME: FeedbackType
FEEDBACK_TYPE_ROBOT_STATUS: FeedbackType
FEEDBACK_TYPE_ROBOT_LIGHT: FeedbackType
FEEDBACK_TYPE_HANDOVER_ZONE: FeedbackType
FEEDBACK_TYPE_SYNCHRONIZATION_BARRIER: FeedbackType
FEEDBACK_TYPE_SHARED_TASK_INDICATOR: FeedbackType
FEEDBACK_TYPE_ROBOT_ATTENTION: FeedbackType
FEEDBACK_TYPE_MESSAGE: FeedbackType
FEEDBACK_TYPE_ICON: FeedbackType
FEEDBACK_TYPE_HIGHLIGHT: FeedbackType
FEEDBACK_TYPE_ZONE: FeedbackType
FEEDBACK_TYPE_PLAY_SOUND: FeedbackType

class FeedbackMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "config_id", "provenance")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: FeedbackType
    config_id: str
    provenance: _provenance_pb2.ARContentProvenance
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[FeedbackType, str]] = ..., config_id: _Optional[str] = ..., provenance: _Optional[_Union[_provenance_pb2.ARContentProvenance, _Mapping]] = ...) -> None: ...

class FeedbackMessages(_message.Message):
    __slots__ = ("feedbacks",)
    FEEDBACKS_FIELD_NUMBER: _ClassVar[int]
    feedbacks: _containers.RepeatedCompositeFieldContainer[FeedbackMessage]
    def __init__(self, feedbacks: _Optional[_Iterable[_Union[FeedbackMessage, _Mapping]]] = ...) -> None: ...

class FeedbackAddMessage(_message.Message):
    __slots__ = ("config_id", "name", "icon", "description", "type", "robot_property_id", "anchor", "link_default_properties")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROBOT_PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    LINK_DEFAULT_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    config_id: str
    name: str
    icon: str
    description: str
    type: FeedbackType
    robot_property_id: str
    anchor: _anchor_pb2.Anchor
    link_default_properties: bool
    def __init__(self, config_id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[FeedbackType, str]] = ..., robot_property_id: _Optional[str] = ..., anchor: _Optional[_Union[_anchor_pb2.Anchor, _Mapping]] = ..., link_default_properties: bool = ...) -> None: ...

class FeedbackUpdateMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "participation")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARTICIPATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    participation: _provenance_pb2.AdaptiveParticipation
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., participation: _Optional[_Union[_provenance_pb2.AdaptiveParticipation, str]] = ...) -> None: ...

class RequestFeedbackOwnership(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
