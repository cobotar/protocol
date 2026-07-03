from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import color_pb2 as _color_pb2
from geometry.v1 import anchor_pb2 as _anchor_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from geometry.v1 import vector3_pb2 as _vector3_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROPERTY_TYPE_UNSPECIFIED: _ClassVar[PropertyType]
    PROPERTY_TYPE_BOOL: _ClassVar[PropertyType]
    PROPERTY_TYPE_INT: _ClassVar[PropertyType]
    PROPERTY_TYPE_FLOAT: _ClassVar[PropertyType]
    PROPERTY_TYPE_DOUBLE: _ClassVar[PropertyType]
    PROPERTY_TYPE_STRING: _ClassVar[PropertyType]
    PROPERTY_TYPE_VECTOR3: _ClassVar[PropertyType]
    PROPERTY_TYPE_POSE: _ClassVar[PropertyType]
    PROPERTY_TYPE_ANCHOR: _ClassVar[PropertyType]
    PROPERTY_TYPE_COLOR: _ClassVar[PropertyType]
    PROPERTY_TYPE_ROBOT: _ClassVar[PropertyType]
    PROPERTY_TYPE_ENUM: _ClassVar[PropertyType]
    PROPERTY_TYPE_ENUM_MULTI: _ClassVar[PropertyType]
    PROPERTY_TYPE_ICON: _ClassVar[PropertyType]
    PROPERTY_TYPE_ASSET: _ClassVar[PropertyType]
    PROPERTY_TYPE_WORKER: _ClassVar[PropertyType]

class PropertyOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROPERTY_ORIGIN_UNSPECIFIED: _ClassVar[PropertyOrigin]
    PROPERTY_ORIGIN_FIXED: _ClassVar[PropertyOrigin]
    PROPERTY_ORIGIN_MIRROR: _ClassVar[PropertyOrigin]

class PropertyGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROPERTY_GROUP_UNSPECIFIED: _ClassVar[PropertyGroup]
    PROPERTY_GROUP_OUTPUT: _ClassVar[PropertyGroup]
    PROPERTY_GROUP_NON_EDITABLE: _ClassVar[PropertyGroup]
    PROPERTY_GROUP_STYLING: _ClassVar[PropertyGroup]
    PROPERTY_GROUP_LOCATION: _ClassVar[PropertyGroup]
    PROPERTY_GROUP_ICON: _ClassVar[PropertyGroup]
    PROPERTY_GROUP_CONFIGURATION: _ClassVar[PropertyGroup]
    PROPERTY_GROUP_HIDDEN: _ClassVar[PropertyGroup]
    PROPERTY_GROUP_INPUT_SLOT: _ClassVar[PropertyGroup]
    PROPERTY_GROUP_ANIMATION: _ClassVar[PropertyGroup]
    PROPERTY_GROUP_TARGET_INDICATOR: _ClassVar[PropertyGroup]

class PropertyPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROPERTY_PERMISSION_UNSPECIFIED: _ClassVar[PropertyPermission]
    PROPERTY_PERMISSION_BASIC: _ClassVar[PropertyPermission]
    PROPERTY_PERMISSION_COSMETIC: _ClassVar[PropertyPermission]
    PROPERTY_PERMISSION_FULL: _ClassVar[PropertyPermission]
    PROPERTY_PERMISSION_NONE: _ClassVar[PropertyPermission]

class PropertySemanticRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROPERTY_SEMANTIC_ROLE_UNSPECIFIED: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_PANEL_BACKGROUND_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_PANEL_TEXT_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_PANEL_BORDER_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_PANEL_OPACITY: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_PANEL_CORNER_RADIUS: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_PRIMARY_TEXT_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_SECONDARY_TEXT_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_TEXT_SIZE: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_TITLE_TEXT_SIZE: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ACCENT_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_SUCCESS_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_WARNING_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ERROR_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_DISABLED_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_CURRENT_TASK_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_UPCOMING_TASK_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_COMPLETED_TASK_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_BLOCKED_TASK_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_OPTIONAL_TASK_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_OPERATOR_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ROBOT_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_SHARED_TASK_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_SUPERVISOR_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_PART_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_TOOL_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ASSET_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_CONTAINER_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_TARGET_GHOST_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_TARGET_HIGHLIGHT_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_PATH_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ZONE_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ANCHOR_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ROBOT_PATH_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ROBOT_SILHOUETTE_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ROBOT_INTENT_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ROBOT_OCCUPANCY_COLOR: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_SUCCESS_SOUND: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_WARNING_SOUND: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ERROR_SOUND: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_NOTIFICATION_ICON: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_PULSE_DURATION: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_FADE_DURATION: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_ANIMATION_SPEED: _ClassVar[PropertySemanticRole]
    PROPERTY_SEMANTIC_ROLE_HIGHLIGHT_THICKNESS: _ClassVar[PropertySemanticRole]

class PropertyScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROPERTY_SCOPE_UNSPECIFIED: _ClassVar[PropertyScope]
    PROPERTY_SCOPE_ENTITY: _ClassVar[PropertyScope]
    PROPERTY_SCOPE_RUNTIME: _ClassVar[PropertyScope]
PROPERTY_TYPE_UNSPECIFIED: PropertyType
PROPERTY_TYPE_BOOL: PropertyType
PROPERTY_TYPE_INT: PropertyType
PROPERTY_TYPE_FLOAT: PropertyType
PROPERTY_TYPE_DOUBLE: PropertyType
PROPERTY_TYPE_STRING: PropertyType
PROPERTY_TYPE_VECTOR3: PropertyType
PROPERTY_TYPE_POSE: PropertyType
PROPERTY_TYPE_ANCHOR: PropertyType
PROPERTY_TYPE_COLOR: PropertyType
PROPERTY_TYPE_ROBOT: PropertyType
PROPERTY_TYPE_ENUM: PropertyType
PROPERTY_TYPE_ENUM_MULTI: PropertyType
PROPERTY_TYPE_ICON: PropertyType
PROPERTY_TYPE_ASSET: PropertyType
PROPERTY_TYPE_WORKER: PropertyType
PROPERTY_ORIGIN_UNSPECIFIED: PropertyOrigin
PROPERTY_ORIGIN_FIXED: PropertyOrigin
PROPERTY_ORIGIN_MIRROR: PropertyOrigin
PROPERTY_GROUP_UNSPECIFIED: PropertyGroup
PROPERTY_GROUP_OUTPUT: PropertyGroup
PROPERTY_GROUP_NON_EDITABLE: PropertyGroup
PROPERTY_GROUP_STYLING: PropertyGroup
PROPERTY_GROUP_LOCATION: PropertyGroup
PROPERTY_GROUP_ICON: PropertyGroup
PROPERTY_GROUP_CONFIGURATION: PropertyGroup
PROPERTY_GROUP_HIDDEN: PropertyGroup
PROPERTY_GROUP_INPUT_SLOT: PropertyGroup
PROPERTY_GROUP_ANIMATION: PropertyGroup
PROPERTY_GROUP_TARGET_INDICATOR: PropertyGroup
PROPERTY_PERMISSION_UNSPECIFIED: PropertyPermission
PROPERTY_PERMISSION_BASIC: PropertyPermission
PROPERTY_PERMISSION_COSMETIC: PropertyPermission
PROPERTY_PERMISSION_FULL: PropertyPermission
PROPERTY_PERMISSION_NONE: PropertyPermission
PROPERTY_SEMANTIC_ROLE_UNSPECIFIED: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_PANEL_BACKGROUND_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_PANEL_TEXT_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_PANEL_BORDER_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_PANEL_OPACITY: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_PANEL_CORNER_RADIUS: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_PRIMARY_TEXT_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_SECONDARY_TEXT_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_TEXT_SIZE: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_TITLE_TEXT_SIZE: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ACCENT_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_SUCCESS_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_WARNING_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ERROR_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_DISABLED_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_CURRENT_TASK_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_UPCOMING_TASK_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_COMPLETED_TASK_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_BLOCKED_TASK_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_OPTIONAL_TASK_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_OPERATOR_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ROBOT_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_SHARED_TASK_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_SUPERVISOR_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_PART_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_TOOL_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ASSET_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_CONTAINER_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_TARGET_GHOST_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_TARGET_HIGHLIGHT_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_PATH_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ZONE_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ANCHOR_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ROBOT_PATH_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ROBOT_SILHOUETTE_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ROBOT_INTENT_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ROBOT_OCCUPANCY_COLOR: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_SUCCESS_SOUND: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_WARNING_SOUND: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ERROR_SOUND: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_NOTIFICATION_ICON: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_PULSE_DURATION: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_FADE_DURATION: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_ANIMATION_SPEED: PropertySemanticRole
PROPERTY_SEMANTIC_ROLE_HIGHLIGHT_THICKNESS: PropertySemanticRole
PROPERTY_SCOPE_UNSPECIFIED: PropertyScope
PROPERTY_SCOPE_ENTITY: PropertyScope
PROPERTY_SCOPE_RUNTIME: PropertyScope

class PropertyDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "parent_id", "authoring_context_id", "scope", "minimum_required_permission", "allowed_origins", "group", "ordering", "hide_group", "advanced", "allow_to_be_mirrored", "semantic_role", "number_extras", "enum_extras", "vector3_extras", "color_extras", "pose_extras", "anchor_extras")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORING_CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_REQUIRED_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ORIGINS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ORDERING_FIELD_NUMBER: _ClassVar[int]
    HIDE_GROUP_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_TO_BE_MIRRORED_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ROLE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    ENUM_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    VECTOR3_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    COLOR_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    POSE_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: PropertyType
    parent_id: str
    authoring_context_id: str
    scope: PropertyScope
    minimum_required_permission: PropertyPermission
    allowed_origins: _containers.RepeatedScalarFieldContainer[PropertyOrigin]
    group: PropertyGroup
    ordering: int
    hide_group: bool
    advanced: bool
    allow_to_be_mirrored: bool
    semantic_role: PropertySemanticRole
    number_extras: NumberExtras
    enum_extras: EnumExtras
    vector3_extras: Vector3Extras
    color_extras: ColorExtras
    pose_extras: PoseExtras
    anchor_extras: AnchorExtras
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[PropertyType, str]] = ..., parent_id: _Optional[str] = ..., authoring_context_id: _Optional[str] = ..., scope: _Optional[_Union[PropertyScope, str]] = ..., minimum_required_permission: _Optional[_Union[PropertyPermission, str]] = ..., allowed_origins: _Optional[_Iterable[_Union[PropertyOrigin, str]]] = ..., group: _Optional[_Union[PropertyGroup, str]] = ..., ordering: _Optional[int] = ..., hide_group: bool = ..., advanced: bool = ..., allow_to_be_mirrored: bool = ..., semantic_role: _Optional[_Union[PropertySemanticRole, str]] = ..., number_extras: _Optional[_Union[NumberExtras, _Mapping]] = ..., enum_extras: _Optional[_Union[EnumExtras, _Mapping]] = ..., vector3_extras: _Optional[_Union[Vector3Extras, _Mapping]] = ..., color_extras: _Optional[_Union[ColorExtras, _Mapping]] = ..., pose_extras: _Optional[_Union[PoseExtras, _Mapping]] = ..., anchor_extras: _Optional[_Union[AnchorExtras, _Mapping]] = ...) -> None: ...

class PropertyInstance(_message.Message):
    __slots__ = ("id", "property_definition_id", "scope", "scope_id", "origin", "mirror_property_definition_id", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    MIRROR_PROPERTY_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    property_definition_id: str
    scope: PropertyScope
    scope_id: str
    origin: PropertyOrigin
    mirror_property_definition_id: str
    value: PropertyValue
    def __init__(self, id: _Optional[str] = ..., property_definition_id: _Optional[str] = ..., scope: _Optional[_Union[PropertyScope, str]] = ..., scope_id: _Optional[str] = ..., origin: _Optional[_Union[PropertyOrigin, str]] = ..., mirror_property_definition_id: _Optional[str] = ..., value: _Optional[_Union[PropertyValue, _Mapping]] = ...) -> None: ...

class PropertyValue(_message.Message):
    __slots__ = ("type", "bool_value", "int_value", "float_value", "double_value", "string_value", "vector3_value", "pose_value", "anchor_value", "color_value", "robot_id_value", "enum_value", "enum_multi_value", "icon_value", "asset_id_value", "worker_id_value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    VECTOR3_VALUE_FIELD_NUMBER: _ClassVar[int]
    POSE_VALUE_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_VALUE_FIELD_NUMBER: _ClassVar[int]
    COLOR_VALUE_FIELD_NUMBER: _ClassVar[int]
    ROBOT_ID_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENUM_MULTI_VALUE_FIELD_NUMBER: _ClassVar[int]
    ICON_VALUE_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_VALUE_FIELD_NUMBER: _ClassVar[int]
    WORKER_ID_VALUE_FIELD_NUMBER: _ClassVar[int]
    type: PropertyType
    bool_value: bool
    int_value: int
    float_value: float
    double_value: float
    string_value: str
    vector3_value: _vector3_pb2.Vector3
    pose_value: _pose_pb2.LocalizedPose
    anchor_value: _anchor_pb2.Anchor
    color_value: _color_pb2.Color
    robot_id_value: str
    enum_value: str
    enum_multi_value: _containers.RepeatedScalarFieldContainer[str]
    icon_value: str
    asset_id_value: str
    worker_id_value: str
    def __init__(self, type: _Optional[_Union[PropertyType, str]] = ..., bool_value: bool = ..., int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ..., vector3_value: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., pose_value: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., anchor_value: _Optional[_Union[_anchor_pb2.Anchor, _Mapping]] = ..., color_value: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., robot_id_value: _Optional[str] = ..., enum_value: _Optional[str] = ..., enum_multi_value: _Optional[_Iterable[str]] = ..., icon_value: _Optional[str] = ..., asset_id_value: _Optional[str] = ..., worker_id_value: _Optional[str] = ...) -> None: ...

class PropertyInstanceUpdate(_message.Message):
    __slots__ = ("property_instance_id", "origin", "mirror_property_definition_id", "value")
    PROPERTY_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    MIRROR_PROPERTY_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    property_instance_id: str
    origin: PropertyOrigin
    mirror_property_definition_id: str
    value: PropertyValue
    def __init__(self, property_instance_id: _Optional[str] = ..., origin: _Optional[_Union[PropertyOrigin, str]] = ..., mirror_property_definition_id: _Optional[str] = ..., value: _Optional[_Union[PropertyValue, _Mapping]] = ...) -> None: ...

class PropertyDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PropertyDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[PropertyDefinition, _Mapping]]] = ...) -> None: ...

class PropertyInstances(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PropertyInstance]
    def __init__(self, items: _Optional[_Iterable[_Union[PropertyInstance, _Mapping]]] = ...) -> None: ...

class NumberExtras(_message.Message):
    __slots__ = ("min", "max", "step", "unit", "precision")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float
    step: float
    unit: str
    precision: int
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ..., step: _Optional[float] = ..., unit: _Optional[str] = ..., precision: _Optional[int] = ...) -> None: ...

class EnumOption(_message.Message):
    __slots__ = ("value", "label", "icon", "group", "disabled")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    value: str
    label: str
    icon: str
    group: str
    disabled: bool
    def __init__(self, value: _Optional[str] = ..., label: _Optional[str] = ..., icon: _Optional[str] = ..., group: _Optional[str] = ..., disabled: bool = ...) -> None: ...

class EnumExtras(_message.Message):
    __slots__ = ("placeholder", "filter", "grouped", "show_icons", "max_selected_labels", "options")
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUPED_FIELD_NUMBER: _ClassVar[int]
    SHOW_ICONS_FIELD_NUMBER: _ClassVar[int]
    MAX_SELECTED_LABELS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    placeholder: str
    filter: bool
    grouped: bool
    show_icons: bool
    max_selected_labels: int
    options: _containers.RepeatedCompositeFieldContainer[EnumOption]
    def __init__(self, placeholder: _Optional[str] = ..., filter: bool = ..., grouped: bool = ..., show_icons: bool = ..., max_selected_labels: _Optional[int] = ..., options: _Optional[_Iterable[_Union[EnumOption, _Mapping]]] = ...) -> None: ...

class Vector3Extras(_message.Message):
    __slots__ = ("min", "max", "step", "label_x", "label_y", "label_z", "unit")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    LABEL_X_FIELD_NUMBER: _ClassVar[int]
    LABEL_Y_FIELD_NUMBER: _ClassVar[int]
    LABEL_Z_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float
    step: float
    label_x: str
    label_y: str
    label_z: str
    unit: str
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ..., step: _Optional[float] = ..., label_x: _Optional[str] = ..., label_y: _Optional[str] = ..., label_z: _Optional[str] = ..., unit: _Optional[str] = ...) -> None: ...

class ColorExtras(_message.Message):
    __slots__ = ("step", "default")
    STEP_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    step: float
    default: _color_pb2.Color
    def __init__(self, step: _Optional[float] = ..., default: _Optional[_Union[_color_pb2.Color, _Mapping]] = ...) -> None: ...

class AnchorExtras(_message.Message):
    __slots__ = ("only_markers",)
    ONLY_MARKERS_FIELD_NUMBER: _ClassVar[int]
    only_markers: bool
    def __init__(self, only_markers: bool = ...) -> None: ...

class PoseExtras(_message.Message):
    __slots__ = ("anchor_editable", "pose_editable")
    ANCHOR_EDITABLE_FIELD_NUMBER: _ClassVar[int]
    POSE_EDITABLE_FIELD_NUMBER: _ClassVar[int]
    anchor_editable: bool
    pose_editable: bool
    def __init__(self, anchor_editable: bool = ..., pose_editable: bool = ...) -> None: ...

class CreatePropertyMessage(_message.Message):
    __slots__ = ("parent_id", "authoring_context_id", "name", "icon", "description", "type", "scope", "minimum_required_permission", "allowed_origins", "group", "ordering", "hide_group", "advanced", "allow_to_be_mirrored", "semantic_role", "origin", "scope_id", "mirror_property_definition_id", "initial_value", "number_extras", "enum_extras", "vector3_extras", "color_extras", "pose_extras", "anchor_extras")
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORING_CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_REQUIRED_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ORIGINS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ORDERING_FIELD_NUMBER: _ClassVar[int]
    HIDE_GROUP_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_TO_BE_MIRRORED_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ROLE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_ID_FIELD_NUMBER: _ClassVar[int]
    MIRROR_PROPERTY_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    ENUM_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    VECTOR3_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    COLOR_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    POSE_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    parent_id: str
    authoring_context_id: str
    name: str
    icon: str
    description: str
    type: PropertyType
    scope: PropertyScope
    minimum_required_permission: PropertyPermission
    allowed_origins: _containers.RepeatedScalarFieldContainer[PropertyOrigin]
    group: PropertyGroup
    ordering: int
    hide_group: bool
    advanced: bool
    allow_to_be_mirrored: bool
    semantic_role: PropertySemanticRole
    origin: PropertyOrigin
    scope_id: str
    mirror_property_definition_id: str
    initial_value: PropertyValue
    number_extras: NumberExtras
    enum_extras: EnumExtras
    vector3_extras: Vector3Extras
    color_extras: ColorExtras
    pose_extras: PoseExtras
    anchor_extras: AnchorExtras
    def __init__(self, parent_id: _Optional[str] = ..., authoring_context_id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[PropertyType, str]] = ..., scope: _Optional[_Union[PropertyScope, str]] = ..., minimum_required_permission: _Optional[_Union[PropertyPermission, str]] = ..., allowed_origins: _Optional[_Iterable[_Union[PropertyOrigin, str]]] = ..., group: _Optional[_Union[PropertyGroup, str]] = ..., ordering: _Optional[int] = ..., hide_group: bool = ..., advanced: bool = ..., allow_to_be_mirrored: bool = ..., semantic_role: _Optional[_Union[PropertySemanticRole, str]] = ..., origin: _Optional[_Union[PropertyOrigin, str]] = ..., scope_id: _Optional[str] = ..., mirror_property_definition_id: _Optional[str] = ..., initial_value: _Optional[_Union[PropertyValue, _Mapping]] = ..., number_extras: _Optional[_Union[NumberExtras, _Mapping]] = ..., enum_extras: _Optional[_Union[EnumExtras, _Mapping]] = ..., vector3_extras: _Optional[_Union[Vector3Extras, _Mapping]] = ..., color_extras: _Optional[_Union[ColorExtras, _Mapping]] = ..., pose_extras: _Optional[_Union[PoseExtras, _Mapping]] = ..., anchor_extras: _Optional[_Union[AnchorExtras, _Mapping]] = ...) -> None: ...
