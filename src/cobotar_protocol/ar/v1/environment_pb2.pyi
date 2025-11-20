from ar.v1 import marker_pb2 as _marker_pb2
from ar.v1 import property_pb2 as _property_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentLocation(_message.Message):
    __slots__ = ("id", "location")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    location: _pose_pb2.LocalizedPose
    def __init__(self, id: _Optional[str] = ..., location: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ...) -> None: ...

class PartLocation(_message.Message):
    __slots__ = ("id", "location")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    location: _pose_pb2.LocalizedPose
    def __init__(self, id: _Optional[str] = ..., location: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ...) -> None: ...

class ToolLocation(_message.Message):
    __slots__ = ("id", "location")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    location: _pose_pb2.LocalizedPose
    def __init__(self, id: _Optional[str] = ..., location: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ...) -> None: ...

class Environment(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "markers", "agents", "parts", "tools", "properties")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARKERS_FIELD_NUMBER: _ClassVar[int]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    markers: _containers.RepeatedCompositeFieldContainer[_marker_pb2.MarkerMessage]
    agents: _containers.RepeatedCompositeFieldContainer[AgentLocation]
    parts: _containers.RepeatedCompositeFieldContainer[PartLocation]
    tools: _containers.RepeatedCompositeFieldContainer[ToolLocation]
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.Property]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., markers: _Optional[_Iterable[_Union[_marker_pb2.MarkerMessage, _Mapping]]] = ..., agents: _Optional[_Iterable[_Union[AgentLocation, _Mapping]]] = ..., parts: _Optional[_Iterable[_Union[PartLocation, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[ToolLocation, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.Property, _Mapping]]] = ...) -> None: ...
