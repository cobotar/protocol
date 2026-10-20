from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import signal_pb2 as _signal_pb2
from resources.v1 import asset_adapter_pb2 as _asset_adapter_pb2
from resources.v1 import asset_definition_pb2 as _asset_definition_pb2
from robot.v1 import robot_adapter_pb2 as _robot_adapter_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceRequirementLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_REQUIREMENT_LEVEL_UNSPECIFIED: _ClassVar[ResourceRequirementLevel]
    RESOURCE_REQUIREMENT_LEVEL_REQUIRED: _ClassVar[ResourceRequirementLevel]
    RESOURCE_REQUIREMENT_LEVEL_OPTIONAL: _ClassVar[ResourceRequirementLevel]
RESOURCE_REQUIREMENT_LEVEL_UNSPECIFIED: ResourceRequirementLevel
RESOURCE_REQUIREMENT_LEVEL_REQUIRED: ResourceRequirementLevel
RESOURCE_REQUIREMENT_LEVEL_OPTIONAL: ResourceRequirementLevel

class ResourceCommandRequirement(_message.Message):
    __slots__ = ("robot_command", "asset_command")
    ROBOT_COMMAND_FIELD_NUMBER: _ClassVar[int]
    ASSET_COMMAND_FIELD_NUMBER: _ClassVar[int]
    robot_command: _robot_adapter_pb2.RobotAdapterCommandType
    asset_command: _asset_adapter_pb2.AssetAdapterCommandType
    def __init__(self, robot_command: _Optional[_Union[_robot_adapter_pb2.RobotAdapterCommandType, str]] = ..., asset_command: _Optional[_Union[_asset_adapter_pb2.AssetAdapterCommandType, str]] = ...) -> None: ...

class ResourceTelemetryRequirement(_message.Message):
    __slots__ = ("robot_telemetry", "asset_telemetry", "minimum_frequency_hz")
    ROBOT_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FREQUENCY_HZ_FIELD_NUMBER: _ClassVar[int]
    robot_telemetry: _robot_adapter_pb2.RobotAdapterTelemetryType
    asset_telemetry: _asset_adapter_pb2.AssetAdapterTelemetryType
    minimum_frequency_hz: float
    def __init__(self, robot_telemetry: _Optional[_Union[_robot_adapter_pb2.RobotAdapterTelemetryType, str]] = ..., asset_telemetry: _Optional[_Union[_asset_adapter_pb2.AssetAdapterTelemetryType, str]] = ..., minimum_frequency_hz: _Optional[float] = ...) -> None: ...

class ResourceSignalRequirement(_message.Message):
    __slots__ = ("data_type", "readable", "writable", "signal_id", "semantic", "signal_id_property_key")
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    READABLE_FIELD_NUMBER: _ClassVar[int]
    WRITABLE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_ID_PROPERTY_KEY_FIELD_NUMBER: _ClassVar[int]
    data_type: _signal_pb2.SignalDataType
    readable: bool
    writable: bool
    signal_id: str
    semantic: _signal_pb2.SignalSemantic
    signal_id_property_key: str
    def __init__(self, data_type: _Optional[_Union[_signal_pb2.SignalDataType, str]] = ..., readable: bool = ..., writable: bool = ..., signal_id: _Optional[str] = ..., semantic: _Optional[_Union[_signal_pb2.SignalSemantic, str]] = ..., signal_id_property_key: _Optional[str] = ...) -> None: ...

class ResourcePlanRequirement(_message.Message):
    __slots__ = ("robot_plan",)
    ROBOT_PLAN_FIELD_NUMBER: _ClassVar[int]
    robot_plan: _robot_adapter_pb2.RobotAdapterPlanType
    def __init__(self, robot_plan: _Optional[_Union[_robot_adapter_pb2.RobotAdapterPlanType, str]] = ...) -> None: ...

class ResourceAssetTypeRequirement(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _asset_definition_pb2.AssetType
    def __init__(self, type: _Optional[_Union[_asset_definition_pb2.AssetType, str]] = ...) -> None: ...

class ResourceRequirement(_message.Message):
    __slots__ = ("level", "command", "telemetry", "signal", "asset_type", "plan")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    level: ResourceRequirementLevel
    command: ResourceCommandRequirement
    telemetry: ResourceTelemetryRequirement
    signal: ResourceSignalRequirement
    asset_type: ResourceAssetTypeRequirement
    plan: ResourcePlanRequirement
    def __init__(self, level: _Optional[_Union[ResourceRequirementLevel, str]] = ..., command: _Optional[_Union[ResourceCommandRequirement, _Mapping]] = ..., telemetry: _Optional[_Union[ResourceTelemetryRequirement, _Mapping]] = ..., signal: _Optional[_Union[ResourceSignalRequirement, _Mapping]] = ..., asset_type: _Optional[_Union[ResourceAssetTypeRequirement, _Mapping]] = ..., plan: _Optional[_Union[ResourcePlanRequirement, _Mapping]] = ...) -> None: ...

class ResourceRequirements(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ResourceRequirement]
    def __init__(self, items: _Optional[_Iterable[_Union[ResourceRequirement, _Mapping]]] = ...) -> None: ...

class ConsumerResourceRequirement(_message.Message):
    __slots__ = ("resource_property_key", "requirement")
    RESOURCE_PROPERTY_KEY_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    resource_property_key: str
    requirement: ResourceRequirement
    def __init__(self, resource_property_key: _Optional[str] = ..., requirement: _Optional[_Union[ResourceRequirement, _Mapping]] = ...) -> None: ...
