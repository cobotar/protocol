from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import enums_pb2 as _enums_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContainerInstance(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "container_definition_id", "station_id", "status", "pose", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    container_definition_id: str
    station_id: str
    status: _enums_pb2.ResourceStatus
    pose: _pose_pb2.LocalizedPose
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., container_definition_id: _Optional[str] = ..., station_id: _Optional[str] = ..., status: _Optional[_Union[_enums_pb2.ResourceStatus, str]] = ..., pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class ContainerInstances(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ContainerInstance]
    def __init__(self, items: _Optional[_Iterable[_Union[ContainerInstance, _Mapping]]] = ...) -> None: ...
