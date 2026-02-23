from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RobotMapping(_message.Message):
    __slots__ = ("robot_id", "property_id")
    ROBOT_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    robot_id: str
    property_id: str
    def __init__(self, robot_id: _Optional[str] = ..., property_id: _Optional[str] = ...) -> None: ...

class AssetMapping(_message.Message):
    __slots__ = ("asset_id", "property_id")
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    property_id: str
    def __init__(self, asset_id: _Optional[str] = ..., property_id: _Optional[str] = ...) -> None: ...

class MappingMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "environment_id", "ar_config_id", "disabled", "robot_mappings", "asset_mapping", "standalone", "priority")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    AR_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    ROBOT_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    ASSET_MAPPING_FIELD_NUMBER: _ClassVar[int]
    STANDALONE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    environment_id: str
    ar_config_id: str
    disabled: bool
    robot_mappings: _containers.RepeatedCompositeFieldContainer[RobotMapping]
    asset_mapping: _containers.RepeatedCompositeFieldContainer[AssetMapping]
    standalone: bool
    priority: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., environment_id: _Optional[str] = ..., ar_config_id: _Optional[str] = ..., disabled: bool = ..., robot_mappings: _Optional[_Iterable[_Union[RobotMapping, _Mapping]]] = ..., asset_mapping: _Optional[_Iterable[_Union[AssetMapping, _Mapping]]] = ..., standalone: bool = ..., priority: _Optional[int] = ...) -> None: ...

class MappingMessages(_message.Message):
    __slots__ = ("mappings",)
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    mappings: _containers.RepeatedCompositeFieldContainer[MappingMessage]
    def __init__(self, mappings: _Optional[_Iterable[_Union[MappingMessage, _Mapping]]] = ...) -> None: ...
