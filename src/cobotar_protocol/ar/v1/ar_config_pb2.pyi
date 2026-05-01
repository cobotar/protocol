from ar.v1 import action_pb2 as _action_pb2
from ar.v1 import feedback_pb2 as _feedback_pb2
from ar.v1 import helper_pb2 as _helper_pb2
from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import property_pb2 as _property_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ARResourceSlotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AR_RESOURCE_SLOT_TYPE_UNSPECIFIED: _ClassVar[ARResourceSlotType]
    AR_RESOURCE_SLOT_TYPE_ROBOT: _ClassVar[ARResourceSlotType]
    AR_RESOURCE_SLOT_TYPE_ASSET: _ClassVar[ARResourceSlotType]

class ARContextSlotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AR_CONTEXT_SLOT_TYPE_UNSPECIFIED: _ClassVar[ARContextSlotType]
    AR_CONTEXT_SLOT_TYPE_LINE_ID: _ClassVar[ARContextSlotType]
    AR_CONTEXT_SLOT_TYPE_CELL_ID: _ClassVar[ARContextSlotType]
    AR_CONTEXT_SLOT_TYPE_STATION_ID: _ClassVar[ARContextSlotType]
    AR_CONTEXT_SLOT_TYPE_WORKER_ID: _ClassVar[ARContextSlotType]
    AR_CONTEXT_SLOT_TYPE_PROCESS_RUN_ID: _ClassVar[ARContextSlotType]
    AR_CONTEXT_SLOT_TYPE_SEQUENCE_RUN_ID: _ClassVar[ARContextSlotType]
    AR_CONTEXT_SLOT_TYPE_TASK_RUN_ID: _ClassVar[ARContextSlotType]
AR_RESOURCE_SLOT_TYPE_UNSPECIFIED: ARResourceSlotType
AR_RESOURCE_SLOT_TYPE_ROBOT: ARResourceSlotType
AR_RESOURCE_SLOT_TYPE_ASSET: ARResourceSlotType
AR_CONTEXT_SLOT_TYPE_UNSPECIFIED: ARContextSlotType
AR_CONTEXT_SLOT_TYPE_LINE_ID: ARContextSlotType
AR_CONTEXT_SLOT_TYPE_CELL_ID: ARContextSlotType
AR_CONTEXT_SLOT_TYPE_STATION_ID: ARContextSlotType
AR_CONTEXT_SLOT_TYPE_WORKER_ID: ARContextSlotType
AR_CONTEXT_SLOT_TYPE_PROCESS_RUN_ID: ARContextSlotType
AR_CONTEXT_SLOT_TYPE_SEQUENCE_RUN_ID: ARContextSlotType
AR_CONTEXT_SLOT_TYPE_TASK_RUN_ID: ARContextSlotType

class ARConfigInfoMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ARConfigInfoMessages(_message.Message):
    __slots__ = ("infos",)
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[ARConfigInfoMessage]
    def __init__(self, infos: _Optional[_Iterable[_Union[ARConfigInfoMessage, _Mapping]]] = ...) -> None: ...

class ARResourceSlot(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "required", "property_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: ARResourceSlotType
    required: bool
    property_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[ARResourceSlotType, str]] = ..., required: bool = ..., property_id: _Optional[str] = ...) -> None: ...

class ARContextSlot(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "required", "property_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: ARContextSlotType
    required: bool
    property_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[ARContextSlotType, str]] = ..., required: bool = ..., property_id: _Optional[str] = ...) -> None: ...

class ARConfigMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "feedback", "actions", "helpers", "properties", "ar_disappear_distance", "resource_slots", "context_slots")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    HELPERS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    AR_DISAPPEAR_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SLOTS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SLOTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    feedback: _containers.RepeatedCompositeFieldContainer[_feedback_pb2.FeedbackMessage]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.ActionMessage]
    helpers: _containers.RepeatedCompositeFieldContainer[_helper_pb2.HelperMessage]
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.Property]
    ar_disappear_distance: int
    resource_slots: _containers.RepeatedCompositeFieldContainer[ARResourceSlot]
    context_slots: _containers.RepeatedCompositeFieldContainer[ARContextSlot]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., feedback: _Optional[_Iterable[_Union[_feedback_pb2.FeedbackMessage, _Mapping]]] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.ActionMessage, _Mapping]]] = ..., helpers: _Optional[_Iterable[_Union[_helper_pb2.HelperMessage, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.Property, _Mapping]]] = ..., ar_disappear_distance: _Optional[int] = ..., resource_slots: _Optional[_Iterable[_Union[ARResourceSlot, _Mapping]]] = ..., context_slots: _Optional[_Iterable[_Union[ARContextSlot, _Mapping]]] = ...) -> None: ...

class ARConfigMessages(_message.Message):
    __slots__ = ("configs",)
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[ARConfigMessage]
    def __init__(self, configs: _Optional[_Iterable[_Union[ARConfigMessage, _Mapping]]] = ...) -> None: ...
