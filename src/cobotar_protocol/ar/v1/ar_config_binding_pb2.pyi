from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import property_pb2 as _property_pb2
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

class ARResourceBinding(_message.Message):
    __slots__ = ("slot_id", "robot_instance_id", "asset_instance_id")
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    ROBOT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    slot_id: str
    robot_instance_id: str
    asset_instance_id: str
    def __init__(self, slot_id: _Optional[str] = ..., robot_instance_id: _Optional[str] = ..., asset_instance_id: _Optional[str] = ...) -> None: ...

class ARConfigBindingMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "station_id", "cell_id", "ar_config_id", "disabled", "standalone", "priority", "resource_bindings", "property_overrides")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    AR_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    STANDALONE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    station_id: str
    cell_id: str
    ar_config_id: str
    disabled: bool
    standalone: bool
    priority: int
    resource_bindings: _containers.RepeatedCompositeFieldContainer[ARResourceBinding]
    property_overrides: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValueUpdate]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., station_id: _Optional[str] = ..., cell_id: _Optional[str] = ..., ar_config_id: _Optional[str] = ..., disabled: bool = ..., standalone: bool = ..., priority: _Optional[int] = ..., resource_bindings: _Optional[_Iterable[_Union[ARResourceBinding, _Mapping]]] = ..., property_overrides: _Optional[_Iterable[_Union[_property_pb2.PropertyValueUpdate, _Mapping]]] = ...) -> None: ...

class ARConfigBindingMessages(_message.Message):
    __slots__ = ("bindings",)
    BINDINGS_FIELD_NUMBER: _ClassVar[int]
    bindings: _containers.RepeatedCompositeFieldContainer[ARConfigBindingMessage]
    def __init__(self, bindings: _Optional[_Iterable[_Union[ARConfigBindingMessage, _Mapping]]] = ...) -> None: ...
