from ar.v1 import ar_config_pb2 as _ar_config_pb2
from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResolvedConfigurationScopeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOLVED_CONFIGURATION_SCOPE_TYPE_UNSPECIFIED: _ClassVar[ResolvedConfigurationScopeType]
    RESOLVED_CONFIGURATION_SCOPE_TYPE_STATION: _ClassVar[ResolvedConfigurationScopeType]
    RESOLVED_CONFIGURATION_SCOPE_TYPE_CELL: _ClassVar[ResolvedConfigurationScopeType]

class ConfigurationResolveIssueSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONFIGURATION_RESOLVE_ISSUE_SEVERITY_UNSPECIFIED: _ClassVar[ConfigurationResolveIssueSeverity]
    CONFIGURATION_RESOLVE_ISSUE_SEVERITY_INFO: _ClassVar[ConfigurationResolveIssueSeverity]
    CONFIGURATION_RESOLVE_ISSUE_SEVERITY_WARNING: _ClassVar[ConfigurationResolveIssueSeverity]
    CONFIGURATION_RESOLVE_ISSUE_SEVERITY_ERROR: _ClassVar[ConfigurationResolveIssueSeverity]
RESOLVED_CONFIGURATION_SCOPE_TYPE_UNSPECIFIED: ResolvedConfigurationScopeType
RESOLVED_CONFIGURATION_SCOPE_TYPE_STATION: ResolvedConfigurationScopeType
RESOLVED_CONFIGURATION_SCOPE_TYPE_CELL: ResolvedConfigurationScopeType
CONFIGURATION_RESOLVE_ISSUE_SEVERITY_UNSPECIFIED: ConfigurationResolveIssueSeverity
CONFIGURATION_RESOLVE_ISSUE_SEVERITY_INFO: ConfigurationResolveIssueSeverity
CONFIGURATION_RESOLVE_ISSUE_SEVERITY_WARNING: ConfigurationResolveIssueSeverity
CONFIGURATION_RESOLVE_ISSUE_SEVERITY_ERROR: ConfigurationResolveIssueSeverity

class ConfigurationResolveContext(_message.Message):
    __slots__ = ("line_id", "cell_id", "station_id", "worker_id", "process_run_id", "sequence_run_id", "task_run_id")
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    line_id: str
    cell_id: str
    station_id: str
    worker_id: str
    process_run_id: str
    sequence_run_id: str
    task_run_id: str
    def __init__(self, line_id: _Optional[str] = ..., cell_id: _Optional[str] = ..., station_id: _Optional[str] = ..., worker_id: _Optional[str] = ..., process_run_id: _Optional[str] = ..., sequence_run_id: _Optional[str] = ..., task_run_id: _Optional[str] = ...) -> None: ...

class ConfigurationResolveRequest(_message.Message):
    __slots__ = ("request_id", "context", "loaded_instance_ids")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LOADED_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    context: ConfigurationResolveContext
    loaded_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, request_id: _Optional[str] = ..., context: _Optional[_Union[ConfigurationResolveContext, _Mapping]] = ..., loaded_instance_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedResourceBinding(_message.Message):
    __slots__ = ("slot_id", "property_id", "robot_instance_id", "asset_instance_id")
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    ROBOT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    slot_id: str
    property_id: str
    robot_instance_id: str
    asset_instance_id: str
    def __init__(self, slot_id: _Optional[str] = ..., property_id: _Optional[str] = ..., robot_instance_id: _Optional[str] = ..., asset_instance_id: _Optional[str] = ...) -> None: ...

class ResolvedContextBinding(_message.Message):
    __slots__ = ("slot_id", "property_id", "type", "string_value")
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    slot_id: str
    property_id: str
    type: _ar_config_pb2.ARContextSlotType
    string_value: str
    def __init__(self, slot_id: _Optional[str] = ..., property_id: _Optional[str] = ..., type: _Optional[_Union[_ar_config_pb2.ARContextSlotType, str]] = ..., string_value: _Optional[str] = ...) -> None: ...

class ConfigurationResolveIssue(_message.Message):
    __slots__ = ("severity", "binding_id", "config_id", "message")
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    BINDING_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    severity: ConfigurationResolveIssueSeverity
    binding_id: str
    config_id: str
    message: str
    def __init__(self, severity: _Optional[_Union[ConfigurationResolveIssueSeverity, str]] = ..., binding_id: _Optional[str] = ..., config_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ResolvedConfiguration(_message.Message):
    __slots__ = ("instance_id", "binding_id", "config_id", "scope", "line_id", "cell_id", "station_id", "standalone", "priority", "effective_config", "resolved_resource_bindings", "resolved_context_bindings")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BINDING_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    STANDALONE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_RESOURCE_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CONTEXT_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    binding_id: str
    config_id: str
    scope: ResolvedConfigurationScopeType
    line_id: str
    cell_id: str
    station_id: str
    standalone: bool
    priority: int
    effective_config: _ar_config_pb2.ARConfigMessage
    resolved_resource_bindings: _containers.RepeatedCompositeFieldContainer[ResolvedResourceBinding]
    resolved_context_bindings: _containers.RepeatedCompositeFieldContainer[ResolvedContextBinding]
    def __init__(self, instance_id: _Optional[str] = ..., binding_id: _Optional[str] = ..., config_id: _Optional[str] = ..., scope: _Optional[_Union[ResolvedConfigurationScopeType, str]] = ..., line_id: _Optional[str] = ..., cell_id: _Optional[str] = ..., station_id: _Optional[str] = ..., standalone: bool = ..., priority: _Optional[int] = ..., effective_config: _Optional[_Union[_ar_config_pb2.ARConfigMessage, _Mapping]] = ..., resolved_resource_bindings: _Optional[_Iterable[_Union[ResolvedResourceBinding, _Mapping]]] = ..., resolved_context_bindings: _Optional[_Iterable[_Union[ResolvedContextBinding, _Mapping]]] = ...) -> None: ...

class ConfigurationResolveResult(_message.Message):
    __slots__ = ("request_id", "configurations", "unload_instance_ids", "issues")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    UNLOAD_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    configurations: _containers.RepeatedCompositeFieldContainer[ResolvedConfiguration]
    unload_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    issues: _containers.RepeatedCompositeFieldContainer[ConfigurationResolveIssue]
    def __init__(self, request_id: _Optional[str] = ..., configurations: _Optional[_Iterable[_Union[ResolvedConfiguration, _Mapping]]] = ..., unload_instance_ids: _Optional[_Iterable[str]] = ..., issues: _Optional[_Iterable[_Union[ConfigurationResolveIssue, _Mapping]]] = ...) -> None: ...
