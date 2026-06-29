from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import external_references_pb2 as _external_references_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EditPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDIT_PERMISSION_UNSPECIFIED: _ClassVar[EditPermission]
    EDIT_PERMISSION_BASIC: _ClassVar[EditPermission]
    EDIT_PERMISSION_COSMETIC: _ClassVar[EditPermission]
    EDIT_PERMISSION_FULL: _ClassVar[EditPermission]

class Handedness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HANDEDNESS_UNSPECIFIED: _ClassVar[Handedness]
    HANDEDNESS_LEFT_HAND: _ClassVar[Handedness]
    HANDEDNESS_RIGHT_HAND: _ClassVar[Handedness]

class WorkerRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WORKER_ROLE_UNSPECIFIED: _ClassVar[WorkerRole]
    WORKER_ROLE_OPERATOR: _ClassVar[WorkerRole]
    WORKER_ROLE_SUPERVISOR: _ClassVar[WorkerRole]
    WORKER_ROLE_TECHNICIAN: _ClassVar[WorkerRole]
    WORKER_ROLE_ENGINEER: _ClassVar[WorkerRole]
    WORKER_ROLE_ADMIN: _ClassVar[WorkerRole]

class InteractionSide(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTERACTION_SIDE_UNSPECIFIED: _ClassVar[InteractionSide]
    INTERACTION_SIDE_LEFT: _ClassVar[InteractionSide]
    INTERACTION_SIDE_RIGHT: _ClassVar[InteractionSide]
    INTERACTION_SIDE_FRONT: _ClassVar[InteractionSide]
    INTERACTION_SIDE_NO_PREFERENCE: _ClassVar[InteractionSide]

class TextSizePreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEXT_SIZE_PREFERENCE_UNSPECIFIED: _ClassVar[TextSizePreference]
    TEXT_SIZE_PREFERENCE_NORMAL: _ClassVar[TextSizePreference]
    TEXT_SIZE_PREFERENCE_LARGE: _ClassVar[TextSizePreference]
EDIT_PERMISSION_UNSPECIFIED: EditPermission
EDIT_PERMISSION_BASIC: EditPermission
EDIT_PERMISSION_COSMETIC: EditPermission
EDIT_PERMISSION_FULL: EditPermission
HANDEDNESS_UNSPECIFIED: Handedness
HANDEDNESS_LEFT_HAND: Handedness
HANDEDNESS_RIGHT_HAND: Handedness
WORKER_ROLE_UNSPECIFIED: WorkerRole
WORKER_ROLE_OPERATOR: WorkerRole
WORKER_ROLE_SUPERVISOR: WorkerRole
WORKER_ROLE_TECHNICIAN: WorkerRole
WORKER_ROLE_ENGINEER: WorkerRole
WORKER_ROLE_ADMIN: WorkerRole
INTERACTION_SIDE_UNSPECIFIED: InteractionSide
INTERACTION_SIDE_LEFT: InteractionSide
INTERACTION_SIDE_RIGHT: InteractionSide
INTERACTION_SIDE_FRONT: InteractionSide
INTERACTION_SIDE_NO_PREFERENCE: InteractionSide
TEXT_SIZE_PREFERENCE_UNSPECIFIED: TextSizePreference
TEXT_SIZE_PREFERENCE_NORMAL: TextSizePreference
TEXT_SIZE_PREFERENCE_LARGE: TextSizePreference

class WorkerLocation(_message.Message):
    __slots__ = ("line_id", "cell_id", "station_id")
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    line_id: str
    cell_id: str
    station_id: str
    def __init__(self, line_id: _Optional[str] = ..., cell_id: _Optional[str] = ..., station_id: _Optional[str] = ...) -> None: ...

class WorkerDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "disabled", "employee_id", "ar_edit_permission", "external_references", "location", "height", "arms_length", "handedness", "role", "preferred_interaction_side", "text_size_preference", "personal_space_radius", "handoff_height_preference", "handoff_side_preference")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_ID_FIELD_NUMBER: _ClassVar[int]
    AR_EDIT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ARMS_LENGTH_FIELD_NUMBER: _ClassVar[int]
    HANDEDNESS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_INTERACTION_SIDE_FIELD_NUMBER: _ClassVar[int]
    TEXT_SIZE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_SPACE_RADIUS_FIELD_NUMBER: _ClassVar[int]
    HANDOFF_HEIGHT_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    HANDOFF_SIDE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    disabled: bool
    employee_id: str
    ar_edit_permission: EditPermission
    external_references: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    location: WorkerLocation
    height: int
    arms_length: int
    handedness: Handedness
    role: WorkerRole
    preferred_interaction_side: InteractionSide
    text_size_preference: TextSizePreference
    personal_space_radius: int
    handoff_height_preference: int
    handoff_side_preference: InteractionSide
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., disabled: bool = ..., employee_id: _Optional[str] = ..., ar_edit_permission: _Optional[_Union[EditPermission, str]] = ..., external_references: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ..., location: _Optional[_Union[WorkerLocation, _Mapping]] = ..., height: _Optional[int] = ..., arms_length: _Optional[int] = ..., handedness: _Optional[_Union[Handedness, str]] = ..., role: _Optional[_Union[WorkerRole, str]] = ..., preferred_interaction_side: _Optional[_Union[InteractionSide, str]] = ..., text_size_preference: _Optional[_Union[TextSizePreference, str]] = ..., personal_space_radius: _Optional[int] = ..., handoff_height_preference: _Optional[int] = ..., handoff_side_preference: _Optional[_Union[InteractionSide, str]] = ...) -> None: ...

class WorkerDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[WorkerDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[WorkerDefinition, _Mapping]]] = ...) -> None: ...
