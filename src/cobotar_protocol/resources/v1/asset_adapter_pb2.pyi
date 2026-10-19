from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import signal_pb2 as _signal_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssetAdapterCommandType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_ADAPTER_COMMAND_TYPE_UNSPECIFIED: _ClassVar[AssetAdapterCommandType]
    ASSET_ADAPTER_COMMAND_TYPE_WRITE_SIGNALS: _ClassVar[AssetAdapterCommandType]
    ASSET_ADAPTER_COMMAND_TYPE_TRIGGER: _ClassVar[AssetAdapterCommandType]
    ASSET_ADAPTER_COMMAND_TYPE_START: _ClassVar[AssetAdapterCommandType]
    ASSET_ADAPTER_COMMAND_TYPE_STOP: _ClassVar[AssetAdapterCommandType]
    ASSET_ADAPTER_COMMAND_TYPE_RESET: _ClassVar[AssetAdapterCommandType]
    ASSET_ADAPTER_COMMAND_TYPE_SET_SPEED: _ClassVar[AssetAdapterCommandType]

class AssetAdapterTelemetryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_ADAPTER_TELEMETRY_TYPE_UNSPECIFIED: _ClassVar[AssetAdapterTelemetryType]
    ASSET_ADAPTER_TELEMETRY_TYPE_STATE: _ClassVar[AssetAdapterTelemetryType]
    ASSET_ADAPTER_TELEMETRY_TYPE_SIGNAL_STATE: _ClassVar[AssetAdapterTelemetryType]
    ASSET_ADAPTER_TELEMETRY_TYPE_FAULT: _ClassVar[AssetAdapterTelemetryType]
    ASSET_ADAPTER_TELEMETRY_TYPE_RESULT: _ClassVar[AssetAdapterTelemetryType]
ASSET_ADAPTER_COMMAND_TYPE_UNSPECIFIED: AssetAdapterCommandType
ASSET_ADAPTER_COMMAND_TYPE_WRITE_SIGNALS: AssetAdapterCommandType
ASSET_ADAPTER_COMMAND_TYPE_TRIGGER: AssetAdapterCommandType
ASSET_ADAPTER_COMMAND_TYPE_START: AssetAdapterCommandType
ASSET_ADAPTER_COMMAND_TYPE_STOP: AssetAdapterCommandType
ASSET_ADAPTER_COMMAND_TYPE_RESET: AssetAdapterCommandType
ASSET_ADAPTER_COMMAND_TYPE_SET_SPEED: AssetAdapterCommandType
ASSET_ADAPTER_TELEMETRY_TYPE_UNSPECIFIED: AssetAdapterTelemetryType
ASSET_ADAPTER_TELEMETRY_TYPE_STATE: AssetAdapterTelemetryType
ASSET_ADAPTER_TELEMETRY_TYPE_SIGNAL_STATE: AssetAdapterTelemetryType
ASSET_ADAPTER_TELEMETRY_TYPE_FAULT: AssetAdapterTelemetryType
ASSET_ADAPTER_TELEMETRY_TYPE_RESULT: AssetAdapterTelemetryType

class AssetAdapterCommandCapability(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: AssetAdapterCommandType
    def __init__(self, type: _Optional[_Union[AssetAdapterCommandType, str]] = ...) -> None: ...

class AssetAdapterTelemetryCapability(_message.Message):
    __slots__ = ("type", "frequency_hz")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_HZ_FIELD_NUMBER: _ClassVar[int]
    type: AssetAdapterTelemetryType
    frequency_hz: float
    def __init__(self, type: _Optional[_Union[AssetAdapterTelemetryType, str]] = ..., frequency_hz: _Optional[float] = ...) -> None: ...

class AssetControllerIdentity(_message.Message):
    __slots__ = ("manufacturer", "model", "serial_number", "controller_software_version")
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    manufacturer: str
    model: str
    serial_number: str
    controller_software_version: str
    def __init__(self, manufacturer: _Optional[str] = ..., model: _Optional[str] = ..., serial_number: _Optional[str] = ..., controller_software_version: _Optional[str] = ...) -> None: ...

class AssetAdapterInfoMessage(_message.Message):
    __slots__ = ("asset_id", "adapter_version", "controller", "capabilities_revision", "adapter_definition_id", "signal_catalog")
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_REVISION_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_CATALOG_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    adapter_version: str
    controller: AssetControllerIdentity
    capabilities_revision: str
    adapter_definition_id: str
    signal_catalog: _signal_pb2.SignalCatalog
    def __init__(self, asset_id: _Optional[str] = ..., adapter_version: _Optional[str] = ..., controller: _Optional[_Union[AssetControllerIdentity, _Mapping]] = ..., capabilities_revision: _Optional[str] = ..., adapter_definition_id: _Optional[str] = ..., signal_catalog: _Optional[_Union[_signal_pb2.SignalCatalog, _Mapping]] = ...) -> None: ...
