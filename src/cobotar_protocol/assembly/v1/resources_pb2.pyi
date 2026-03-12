import datetime

from assembly.v1 import common_pb2 as _common_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToolType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOOL_TYPE_UNSPECIFIED: _ClassVar[ToolType]
    TOOL_TYPE_FASTENING: _ClassVar[ToolType]
    TOOL_TYPE_GRIPPING: _ClassVar[ToolType]
    TOOL_TYPE_CUTTING: _ClassVar[ToolType]
    TOOL_TYPE_MEASURING: _ClassVar[ToolType]
    TOOL_TYPE_POSITIONING: _ClassVar[ToolType]
    TOOL_TYPE_DISPENSING: _ClassVar[ToolType]
    TOOL_TYPE_INSPECTION: _ClassVar[ToolType]
    TOOL_TYPE_SAFETY: _ClassVar[ToolType]
    TOOL_TYPE_ELECTRONICS: _ClassVar[ToolType]
    TOOL_TYPE_FIXTURE_ACCESSORY: _ClassVar[ToolType]
    TOOL_TYPE_SHAPING: _ClassVar[ToolType]
    TOOL_TYPE_TURNING: _ClassVar[ToolType]
    TOOL_TYPE_STRIKING: _ClassVar[ToolType]
    TOOL_TYPE_MARKING: _ClassVar[ToolType]
    TOOL_TYPE_FINISHING: _ClassVar[ToolType]
    TOOL_TYPE_ABRASIVE: _ClassVar[ToolType]
    TOOL_TYPE_CLEANING: _ClassVar[ToolType]

class ToolRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOOL_ROLE_UNSPECIFIED: _ClassVar[ToolRole]
    TOOL_ROLE_GRIP_WORKPIECE: _ClassVar[ToolRole]
    TOOL_ROLE_POSITION_COMPONENT: _ClassVar[ToolRole]
    TOOL_ROLE_ALIGN_COMPONENT: _ClassVar[ToolRole]
    TOOL_ROLE_APPLY_TORQUE: _ClassVar[ToolRole]
    TOOL_ROLE_APPLY_LINEAR_FORCE: _ClassVar[ToolRole]
    TOOL_ROLE_MEASURE_DIMENSION: _ClassVar[ToolRole]
    TOOL_ROLE_DETECT_PRESENCE: _ClassVar[ToolRole]
    TOOL_ROLE_DISPENSE_MATERIAL: _ClassVar[ToolRole]
    TOOL_ROLE_EXECUTE_MOTION: _ClassVar[ToolRole]
    TOOL_ROLE_SAFETY_INTERACTION: _ClassVar[ToolRole]
    TOOL_ROLE_HANDLE_ESD: _ClassVar[ToolRole]
    TOOL_ROLE_VISUAL_INSPECTION: _ClassVar[ToolRole]
    TOOL_ROLE_WIPE_CLEAN: _ClassVar[ToolRole]

class ToolProperty(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOOL_PROPERTY_UNSPECIFIED: _ClassVar[ToolProperty]
    TOOL_PROPERTY_TORQUE_CONTROLLED: _ClassVar[ToolProperty]
    TOOL_PROPERTY_ESD_SAFE: _ClassVar[ToolProperty]
    TOOL_PROPERTY_INSULATED: _ClassVar[ToolProperty]
    TOOL_PROPERTY_COLLABORATIVE_SAFE: _ClassVar[ToolProperty]
    TOOL_PROPERTY_CALIBRATED: _ClassVar[ToolProperty]
    TOOL_PROPERTY_QUICK_CHANGE: _ClassVar[ToolProperty]

class FixtureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIXTURE_TYPE_UNSPECIFIED: _ClassVar[FixtureType]
    FIXTURE_TYPE_BASE: _ClassVar[FixtureType]
    FIXTURE_TYPE_CLAMP: _ClassVar[FixtureType]
    FIXTURE_TYPE_JIG: _ClassVar[FixtureType]
    FIXTURE_TYPE_PALLET: _ClassVar[FixtureType]

class RobotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_TYPE_UNSPECIFIED: _ClassVar[RobotType]
    ROBOT_TYPE_UR3E: _ClassVar[RobotType]
    ROBOT_TYPE_UR5E: _ClassVar[RobotType]
    ROBOT_TYPE_UR10E: _ClassVar[RobotType]
    ROBOT_TYPE_KUKA_IIWA: _ClassVar[RobotType]

class RobotDriverType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_DRIVER_TYPE_UNSPECIFIED: _ClassVar[RobotDriverType]
    ROBOT_DRIVER_TYPE_UR: _ClassVar[RobotDriverType]
    ROBOT_DRIVER_TYPE_GENERIC: _ClassVar[RobotDriverType]

class AssetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_TYPE_UNSPECIFIED: _ClassVar[AssetType]
    ASSET_TYPE_CAMERA: _ClassVar[AssetType]
    ASSET_TYPE_LIGHT: _ClassVar[AssetType]
    ASSET_TYPE_CONVEYOR: _ClassVar[AssetType]
    ASSET_TYPE_SENSOR: _ClassVar[AssetType]
    ASSET_TYPE_HMI: _ClassVar[AssetType]

class AssetDriverType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_DRIVER_TYPE_UNSPECIFIED: _ClassVar[AssetDriverType]
    ASSET_DRIVER_TYPE_DEFAULT: _ClassVar[AssetDriverType]
TOOL_TYPE_UNSPECIFIED: ToolType
TOOL_TYPE_FASTENING: ToolType
TOOL_TYPE_GRIPPING: ToolType
TOOL_TYPE_CUTTING: ToolType
TOOL_TYPE_MEASURING: ToolType
TOOL_TYPE_POSITIONING: ToolType
TOOL_TYPE_DISPENSING: ToolType
TOOL_TYPE_INSPECTION: ToolType
TOOL_TYPE_SAFETY: ToolType
TOOL_TYPE_ELECTRONICS: ToolType
TOOL_TYPE_FIXTURE_ACCESSORY: ToolType
TOOL_TYPE_SHAPING: ToolType
TOOL_TYPE_TURNING: ToolType
TOOL_TYPE_STRIKING: ToolType
TOOL_TYPE_MARKING: ToolType
TOOL_TYPE_FINISHING: ToolType
TOOL_TYPE_ABRASIVE: ToolType
TOOL_TYPE_CLEANING: ToolType
TOOL_ROLE_UNSPECIFIED: ToolRole
TOOL_ROLE_GRIP_WORKPIECE: ToolRole
TOOL_ROLE_POSITION_COMPONENT: ToolRole
TOOL_ROLE_ALIGN_COMPONENT: ToolRole
TOOL_ROLE_APPLY_TORQUE: ToolRole
TOOL_ROLE_APPLY_LINEAR_FORCE: ToolRole
TOOL_ROLE_MEASURE_DIMENSION: ToolRole
TOOL_ROLE_DETECT_PRESENCE: ToolRole
TOOL_ROLE_DISPENSE_MATERIAL: ToolRole
TOOL_ROLE_EXECUTE_MOTION: ToolRole
TOOL_ROLE_SAFETY_INTERACTION: ToolRole
TOOL_ROLE_HANDLE_ESD: ToolRole
TOOL_ROLE_VISUAL_INSPECTION: ToolRole
TOOL_ROLE_WIPE_CLEAN: ToolRole
TOOL_PROPERTY_UNSPECIFIED: ToolProperty
TOOL_PROPERTY_TORQUE_CONTROLLED: ToolProperty
TOOL_PROPERTY_ESD_SAFE: ToolProperty
TOOL_PROPERTY_INSULATED: ToolProperty
TOOL_PROPERTY_COLLABORATIVE_SAFE: ToolProperty
TOOL_PROPERTY_CALIBRATED: ToolProperty
TOOL_PROPERTY_QUICK_CHANGE: ToolProperty
FIXTURE_TYPE_UNSPECIFIED: FixtureType
FIXTURE_TYPE_BASE: FixtureType
FIXTURE_TYPE_CLAMP: FixtureType
FIXTURE_TYPE_JIG: FixtureType
FIXTURE_TYPE_PALLET: FixtureType
ROBOT_TYPE_UNSPECIFIED: RobotType
ROBOT_TYPE_UR3E: RobotType
ROBOT_TYPE_UR5E: RobotType
ROBOT_TYPE_UR10E: RobotType
ROBOT_TYPE_KUKA_IIWA: RobotType
ROBOT_DRIVER_TYPE_UNSPECIFIED: RobotDriverType
ROBOT_DRIVER_TYPE_UR: RobotDriverType
ROBOT_DRIVER_TYPE_GENERIC: RobotDriverType
ASSET_TYPE_UNSPECIFIED: AssetType
ASSET_TYPE_CAMERA: AssetType
ASSET_TYPE_LIGHT: AssetType
ASSET_TYPE_CONVEYOR: AssetType
ASSET_TYPE_SENSOR: AssetType
ASSET_TYPE_HMI: AssetType
ASSET_DRIVER_TYPE_UNSPECIFIED: AssetDriverType
ASSET_DRIVER_TYPE_DEFAULT: AssetDriverType

class CapabilityProfile(_message.Message):
    __slots__ = ("min_force_n", "max_force_n", "min_torque_nm", "max_torque_nm", "repeatability_mm", "max_payload_g", "min_grip_width_mm", "max_grip_width_mm", "constraints")
    MIN_FORCE_N_FIELD_NUMBER: _ClassVar[int]
    MAX_FORCE_N_FIELD_NUMBER: _ClassVar[int]
    MIN_TORQUE_NM_FIELD_NUMBER: _ClassVar[int]
    MAX_TORQUE_NM_FIELD_NUMBER: _ClassVar[int]
    REPEATABILITY_MM_FIELD_NUMBER: _ClassVar[int]
    MAX_PAYLOAD_G_FIELD_NUMBER: _ClassVar[int]
    MIN_GRIP_WIDTH_MM_FIELD_NUMBER: _ClassVar[int]
    MAX_GRIP_WIDTH_MM_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    min_force_n: float
    max_force_n: float
    min_torque_nm: float
    max_torque_nm: float
    repeatability_mm: float
    max_payload_g: float
    min_grip_width_mm: float
    max_grip_width_mm: float
    constraints: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValueConstraint]
    def __init__(self, min_force_n: _Optional[float] = ..., max_force_n: _Optional[float] = ..., min_torque_nm: _Optional[float] = ..., max_torque_nm: _Optional[float] = ..., repeatability_mm: _Optional[float] = ..., max_payload_g: _Optional[float] = ..., min_grip_width_mm: _Optional[float] = ..., max_grip_width_mm: _Optional[float] = ..., constraints: _Optional[_Iterable[_Union[_common_pb2.KeyValueConstraint, _Mapping]]] = ...) -> None: ...

class ToolDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "type", "actor_kind", "roles", "properties", "capability_profile", "model_id", "external_references", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_KIND_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    type: ToolType
    actor_kind: _common_pb2.ActorKind
    roles: _containers.RepeatedScalarFieldContainer[ToolRole]
    properties: _containers.RepeatedScalarFieldContainer[ToolProperty]
    capability_profile: CapabilityProfile
    model_id: str
    external_references: _containers.RepeatedCompositeFieldContainer[_common_pb2.ExternalReference]
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., type: _Optional[_Union[ToolType, str]] = ..., actor_kind: _Optional[_Union[_common_pb2.ActorKind, str]] = ..., roles: _Optional[_Iterable[_Union[ToolRole, str]]] = ..., properties: _Optional[_Iterable[_Union[ToolProperty, str]]] = ..., capability_profile: _Optional[_Union[CapabilityProfile, _Mapping]] = ..., model_id: _Optional[str] = ..., external_references: _Optional[_Iterable[_Union[_common_pb2.ExternalReference, _Mapping]]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class ToolDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ToolDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[ToolDefinition, _Mapping]]] = ...) -> None: ...

class ToolInstance(_message.Message):
    __slots__ = ("id", "tool_definition_id", "serial_number", "station_id", "status", "calibrated", "calibration_valid_until", "pose", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CALIBRATED_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    tool_definition_id: str
    serial_number: str
    station_id: str
    status: _common_pb2.ResourceStatus
    calibrated: bool
    calibration_valid_until: _timestamp_pb2.Timestamp
    pose: _pose_pb2.LocalizedPose
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., tool_definition_id: _Optional[str] = ..., serial_number: _Optional[str] = ..., station_id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.ResourceStatus, str]] = ..., calibrated: bool = ..., calibration_valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class ToolInstances(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ToolInstance]
    def __init__(self, items: _Optional[_Iterable[_Union[ToolInstance, _Mapping]]] = ...) -> None: ...

class FixtureDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "type", "supported_product_definition_ids", "supported_root_part_definition_ids", "model_id", "constraints", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PRODUCT_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ROOT_PART_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    type: FixtureType
    supported_product_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    supported_root_part_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    model_id: str
    constraints: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValueConstraint]
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., type: _Optional[_Union[FixtureType, str]] = ..., supported_product_definition_ids: _Optional[_Iterable[str]] = ..., supported_root_part_definition_ids: _Optional[_Iterable[str]] = ..., model_id: _Optional[str] = ..., constraints: _Optional[_Iterable[_Union[_common_pb2.KeyValueConstraint, _Mapping]]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class FixtureDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FixtureDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[FixtureDefinition, _Mapping]]] = ...) -> None: ...

class FixtureInstance(_message.Message):
    __slots__ = ("id", "fixture_definition_id", "station_id", "status", "pose", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIXTURE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    fixture_definition_id: str
    station_id: str
    status: _common_pb2.ResourceStatus
    pose: _pose_pb2.LocalizedPose
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., fixture_definition_id: _Optional[str] = ..., station_id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.ResourceStatus, str]] = ..., pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class FixtureInstances(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FixtureInstance]
    def __init__(self, items: _Optional[_Iterable[_Union[FixtureInstance, _Mapping]]] = ...) -> None: ...

class RobotDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "type", "driver_type", "model_id", "coupler_model_id", "supported_tool_definition_ids", "default_tool_definition_id", "tool_slots", "capability_profile", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DRIVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    COUPLER_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_TOOL_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TOOL_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_SLOTS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    type: RobotType
    driver_type: RobotDriverType
    model_id: str
    coupler_model_id: str
    supported_tool_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    default_tool_definition_id: str
    tool_slots: int
    capability_profile: CapabilityProfile
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., type: _Optional[_Union[RobotType, str]] = ..., driver_type: _Optional[_Union[RobotDriverType, str]] = ..., model_id: _Optional[str] = ..., coupler_model_id: _Optional[str] = ..., supported_tool_definition_ids: _Optional[_Iterable[str]] = ..., default_tool_definition_id: _Optional[str] = ..., tool_slots: _Optional[int] = ..., capability_profile: _Optional[_Union[CapabilityProfile, _Mapping]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class RobotDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[RobotDefinitions]
    def __init__(self, items: _Optional[_Iterable[_Union[RobotDefinitions, _Mapping]]] = ...) -> None: ...

class RobotInstance(_message.Message):
    __slots__ = ("id", "robot_definition_id", "station_id", "mounted_tool_instance_id", "available_tool_instance_ids", "supports_tool_change", "status", "base_pose", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROBOT_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_TOOL_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_TOOL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_TOOL_CHANGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BASE_POSE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    robot_definition_id: str
    station_id: str
    mounted_tool_instance_id: str
    available_tool_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    supports_tool_change: bool
    status: _common_pb2.ResourceStatus
    base_pose: _pose_pb2.LocalizedPose
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., robot_definition_id: _Optional[str] = ..., station_id: _Optional[str] = ..., mounted_tool_instance_id: _Optional[str] = ..., available_tool_instance_ids: _Optional[_Iterable[str]] = ..., supports_tool_change: bool = ..., status: _Optional[_Union[_common_pb2.ResourceStatus, str]] = ..., base_pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class RobotInstances(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[RobotInstance]
    def __init__(self, items: _Optional[_Iterable[_Union[RobotInstance, _Mapping]]] = ...) -> None: ...

class AssetDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "type", "driver_type", "model_id", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DRIVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    type: AssetType
    driver_type: AssetDriverType
    model_id: str
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., type: _Optional[_Union[AssetType, str]] = ..., driver_type: _Optional[_Union[AssetDriverType, str]] = ..., model_id: _Optional[str] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class AssetDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AssetDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[AssetDefinition, _Mapping]]] = ...) -> None: ...

class AssetInstance(_message.Message):
    __slots__ = ("id", "asset_definition_id", "station_id", "status", "pose", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    asset_definition_id: str
    station_id: str
    status: _common_pb2.ResourceStatus
    pose: _pose_pb2.LocalizedPose
    custom: _common_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., asset_definition_id: _Optional[str] = ..., station_id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.ResourceStatus, str]] = ..., pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., custom: _Optional[_Union[_common_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class AssetInstances(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AssetInstance]
    def __init__(self, items: _Optional[_Iterable[_Union[AssetInstance, _Mapping]]] = ...) -> None: ...
