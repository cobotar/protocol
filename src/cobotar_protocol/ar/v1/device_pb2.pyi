from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_TYPE_UNSPECIFIED: _ClassVar[DeviceType]
    DEVICE_TYPE_HOLOLENS2: _ClassVar[DeviceType]
    DEVICE_TYPE_PHONE: _ClassVar[DeviceType]
    DEVICE_TYPE_TABLET: _ClassVar[DeviceType]
    DEVICE_TYPE_PC: _ClassVar[DeviceType]

class DeviceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_STATUS_UNSPECIFIED: _ClassVar[DeviceStatus]
    DEVICE_STATUS_ONLINE: _ClassVar[DeviceStatus]
    DEVICE_STATUS_OFFLINE: _ClassVar[DeviceStatus]

class DeviceBatteryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_BATTERY_STATUS_UNSPECIFIED: _ClassVar[DeviceBatteryStatus]
    DEVICE_BATTERY_STATUS_CHARGING: _ClassVar[DeviceBatteryStatus]
    DEVICE_BATTERY_STATUS_DISCHARGING: _ClassVar[DeviceBatteryStatus]
    DEVICE_BATTERY_STATUS_NOT_CHARGING: _ClassVar[DeviceBatteryStatus]
    DEVICE_BATTERY_STATUS_FULL: _ClassVar[DeviceBatteryStatus]
DEVICE_TYPE_UNSPECIFIED: DeviceType
DEVICE_TYPE_HOLOLENS2: DeviceType
DEVICE_TYPE_PHONE: DeviceType
DEVICE_TYPE_TABLET: DeviceType
DEVICE_TYPE_PC: DeviceType
DEVICE_STATUS_UNSPECIFIED: DeviceStatus
DEVICE_STATUS_ONLINE: DeviceStatus
DEVICE_STATUS_OFFLINE: DeviceStatus
DEVICE_BATTERY_STATUS_UNSPECIFIED: DeviceBatteryStatus
DEVICE_BATTERY_STATUS_CHARGING: DeviceBatteryStatus
DEVICE_BATTERY_STATUS_DISCHARGING: DeviceBatteryStatus
DEVICE_BATTERY_STATUS_NOT_CHARGING: DeviceBatteryStatus
DEVICE_BATTERY_STATUS_FULL: DeviceBatteryStatus

class DeviceMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "device_id", "status", "battery_level", "battery_status")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BATTERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: DeviceType
    device_id: str
    status: DeviceStatus
    battery_level: int
    battery_status: DeviceBatteryStatus
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[DeviceType, str]] = ..., device_id: _Optional[str] = ..., status: _Optional[_Union[DeviceStatus, str]] = ..., battery_level: _Optional[int] = ..., battery_status: _Optional[_Union[DeviceBatteryStatus, str]] = ...) -> None: ...

class DeviceMessages(_message.Message):
    __slots__ = ("devices",)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[DeviceMessage]
    def __init__(self, devices: _Optional[_Iterable[_Union[DeviceMessage, _Mapping]]] = ...) -> None: ...
