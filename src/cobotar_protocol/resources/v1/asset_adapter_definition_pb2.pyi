from buf.validate import validate_pb2 as _validate_pb2
from cobotar_protocol.common.v1 import catalog_status_pb2 as _catalog_status_pb2
from cobotar_protocol.common.v1 import signal_pb2 as _signal_pb2
from cobotar_protocol.resources.v1 import asset_adapter_pb2 as _asset_adapter_pb2
from cobotar_protocol.resources.v1 import asset_definition_pb2 as _asset_definition_pb2
from cobotar_protocol.validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssetAdapterDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "adapter_type", "supported_asset_types", "commands", "telemetry", "signals", "status", "status_issue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    SIGNALS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_ISSUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    adapter_type: str
    supported_asset_types: _containers.RepeatedScalarFieldContainer[_asset_definition_pb2.AssetType]
    commands: _containers.RepeatedCompositeFieldContainer[_asset_adapter_pb2.AssetAdapterCommandCapability]
    telemetry: _containers.RepeatedCompositeFieldContainer[_asset_adapter_pb2.AssetAdapterTelemetryCapability]
    signals: _containers.RepeatedCompositeFieldContainer[_signal_pb2.SignalDefinition]
    status: _catalog_status_pb2.CatalogStatus
    status_issue: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., adapter_type: _Optional[str] = ..., supported_asset_types: _Optional[_Iterable[_Union[_asset_definition_pb2.AssetType, str]]] = ..., commands: _Optional[_Iterable[_Union[_asset_adapter_pb2.AssetAdapterCommandCapability, _Mapping]]] = ..., telemetry: _Optional[_Iterable[_Union[_asset_adapter_pb2.AssetAdapterTelemetryCapability, _Mapping]]] = ..., signals: _Optional[_Iterable[_Union[_signal_pb2.SignalDefinition, _Mapping]]] = ..., status: _Optional[_Union[_catalog_status_pb2.CatalogStatus, str]] = ..., status_issue: _Optional[str] = ...) -> None: ...

class AssetAdapterDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AssetAdapterDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[AssetAdapterDefinition, _Mapping]]] = ...) -> None: ...
