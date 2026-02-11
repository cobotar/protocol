from ar.v1 import permissions_pb2 as _permissions_pb2
from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import color_pb2 as _color_pb2
from geometry.v1 import anchor_pb2 as _anchor_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from geometry.v1 import vector3_pb2 as _vector3_pb2
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
    PROPERTY_TYPE_AGENT: _ClassVar[PropertyType]
    PROPERTY_TYPE_ENUM: _ClassVar[PropertyType]
    PROPERTY_TYPE_ENUM_MULTI: _ClassVar[PropertyType]
    PROPERTY_TYPE_ICON: _ClassVar[PropertyType]

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
PROPERTY_TYPE_AGENT: PropertyType
PROPERTY_TYPE_ENUM: PropertyType
PROPERTY_TYPE_ENUM_MULTI: PropertyType
PROPERTY_TYPE_ICON: PropertyType
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

class Property(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "minimum_required_permission", "origin", "origins", "mirror_property_id", "group", "ordering", "hide_group", "parent_id", "advanced", "bool_value", "int_value", "float_value", "double_value", "string_value", "vector3_value", "pose_value", "anchor_value", "color_value", "robot_id_value", "enum_value", "enum_multi_value", "icon_value", "number_extras", "enum_extras", "vector3_extras", "color_extras", "pose_extras", "anchor_extras")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_REQUIRED_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    ORIGINS_FIELD_NUMBER: _ClassVar[int]
    MIRROR_PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ORDERING_FIELD_NUMBER: _ClassVar[int]
    HIDE_GROUP_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_FIELD_NUMBER: _ClassVar[int]
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
    minimum_required_permission: _permissions_pb2.WorkerPermission
    origin: PropertyOrigin
    origins: _containers.RepeatedScalarFieldContainer[PropertyOrigin]
    mirror_property_id: str
    group: PropertyGroup
    ordering: int
    hide_group: bool
    parent_id: str
    advanced: bool
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
    number_extras: NumberExtras
    enum_extras: EnumExtras
    vector3_extras: Vector3Extras
    color_extras: ColorExtras
    pose_extras: PoseExtras
    anchor_extras: AnchorExtras
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[PropertyType, str]] = ..., minimum_required_permission: _Optional[_Union[_permissions_pb2.WorkerPermission, str]] = ..., origin: _Optional[_Union[PropertyOrigin, str]] = ..., origins: _Optional[_Iterable[_Union[PropertyOrigin, str]]] = ..., mirror_property_id: _Optional[str] = ..., group: _Optional[_Union[PropertyGroup, str]] = ..., ordering: _Optional[int] = ..., hide_group: bool = ..., parent_id: _Optional[str] = ..., advanced: bool = ..., bool_value: bool = ..., int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ..., vector3_value: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., pose_value: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., anchor_value: _Optional[_Union[_anchor_pb2.Anchor, _Mapping]] = ..., color_value: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., robot_id_value: _Optional[str] = ..., enum_value: _Optional[str] = ..., enum_multi_value: _Optional[_Iterable[str]] = ..., icon_value: _Optional[str] = ..., number_extras: _Optional[_Union[NumberExtras, _Mapping]] = ..., enum_extras: _Optional[_Union[EnumExtras, _Mapping]] = ..., vector3_extras: _Optional[_Union[Vector3Extras, _Mapping]] = ..., color_extras: _Optional[_Union[ColorExtras, _Mapping]] = ..., pose_extras: _Optional[_Union[PoseExtras, _Mapping]] = ..., anchor_extras: _Optional[_Union[AnchorExtras, _Mapping]] = ...) -> None: ...

class PropertyMessages(_message.Message):
    __slots__ = ("properties",)
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.RepeatedCompositeFieldContainer[Property]
    def __init__(self, properties: _Optional[_Iterable[_Union[Property, _Mapping]]] = ...) -> None: ...

class PropertyValueUpdate(_message.Message):
    __slots__ = ("id", "type", "origin", "mirror_property_id", "bool_value", "int_value", "float_value", "double_value", "string_value", "vector3_value", "pose_value", "anchor_value", "color_value", "robot_id_value", "enum_value", "enum_multi_value", "icon_value")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    MIRROR_PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
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
    id: str
    type: PropertyType
    origin: PropertyOrigin
    mirror_property_id: str
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
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[PropertyType, str]] = ..., origin: _Optional[_Union[PropertyOrigin, str]] = ..., mirror_property_id: _Optional[str] = ..., bool_value: bool = ..., int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ..., vector3_value: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., pose_value: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ..., anchor_value: _Optional[_Union[_anchor_pb2.Anchor, _Mapping]] = ..., color_value: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., robot_id_value: _Optional[str] = ..., enum_value: _Optional[str] = ..., enum_multi_value: _Optional[_Iterable[str]] = ..., icon_value: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("min", "max", "step", "labels", "unit")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float
    step: float
    labels: _containers.RepeatedScalarFieldContainer[str]
    unit: str
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ..., step: _Optional[float] = ..., labels: _Optional[_Iterable[str]] = ..., unit: _Optional[str] = ...) -> None: ...

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
