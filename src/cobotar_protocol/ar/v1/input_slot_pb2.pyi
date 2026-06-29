from buf.validate import validate_pb2 as _validate_pb2
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

class ARRunSelection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AR_RUN_SELECTION_UNSPECIFIED: _ClassVar[ARRunSelection]
    AR_RUN_SELECTION_FIRST_WORKABLE: _ClassVar[ARRunSelection]
    AR_RUN_SELECTION_CURRENT_ASSIGNED: _ClassVar[ARRunSelection]
    AR_RUN_SELECTION_NEXT_EXPECTED: _ClassVar[ARRunSelection]
    AR_RUN_SELECTION_LAST_COMPLETED: _ClassVar[ARRunSelection]
    AR_RUN_SELECTION_FIRST_IN_ERROR: _ClassVar[ARRunSelection]
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
AR_RUN_SELECTION_UNSPECIFIED: ARRunSelection
AR_RUN_SELECTION_FIRST_WORKABLE: ARRunSelection
AR_RUN_SELECTION_CURRENT_ASSIGNED: ARRunSelection
AR_RUN_SELECTION_NEXT_EXPECTED: ARRunSelection
AR_RUN_SELECTION_LAST_COMPLETED: ARRunSelection
AR_RUN_SELECTION_FIRST_IN_ERROR: ARRunSelection

class ARActorSelector(_message.Message):
    __slots__ = ("current_worker", "resource_slot_id")
    CURRENT_WORKER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    current_worker: bool
    resource_slot_id: str
    def __init__(self, current_worker: bool = ..., resource_slot_id: _Optional[str] = ...) -> None: ...

class ARRunContextSelector(_message.Message):
    __slots__ = ("selection", "actor")
    SELECTION_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    selection: ARRunSelection
    actor: ARActorSelector
    def __init__(self, selection: _Optional[_Union[ARRunSelection, str]] = ..., actor: _Optional[_Union[ARActorSelector, _Mapping]] = ...) -> None: ...

class ARInputSlotMessage(_message.Message):
    __slots__ = ("id", "config_id", "name", "icon", "description", "required", "generated_property_id", "resource_type", "context_type", "run_selector")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    GENERATED_PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RUN_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    config_id: str
    name: str
    icon: str
    description: str
    required: bool
    generated_property_id: str
    resource_type: ARResourceSlotType
    context_type: ARContextSlotType
    run_selector: ARRunContextSelector
    def __init__(self, id: _Optional[str] = ..., config_id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., required: bool = ..., generated_property_id: _Optional[str] = ..., resource_type: _Optional[_Union[ARResourceSlotType, str]] = ..., context_type: _Optional[_Union[ARContextSlotType, str]] = ..., run_selector: _Optional[_Union[ARRunContextSelector, _Mapping]] = ...) -> None: ...

class ARInputSlotMessages(_message.Message):
    __slots__ = ("slots",)
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    slots: _containers.RepeatedCompositeFieldContainer[ARInputSlotMessage]
    def __init__(self, slots: _Optional[_Iterable[_Union[ARInputSlotMessage, _Mapping]]] = ...) -> None: ...

class ARInputSlotAddMessage(_message.Message):
    __slots__ = ("config_id", "name", "icon", "description", "required", "resource_type", "context_type", "run_selector")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RUN_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    config_id: str
    name: str
    icon: str
    description: str
    required: bool
    resource_type: ARResourceSlotType
    context_type: ARContextSlotType
    run_selector: ARRunContextSelector
    def __init__(self, config_id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., required: bool = ..., resource_type: _Optional[_Union[ARResourceSlotType, str]] = ..., context_type: _Optional[_Union[ARContextSlotType, str]] = ..., run_selector: _Optional[_Union[ARRunContextSelector, _Mapping]] = ...) -> None: ...

class ARInputSlotUpdateMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "required", "run_selector")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    RUN_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    required: bool
    run_selector: ARRunContextSelector
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., required: bool = ..., run_selector: _Optional[_Union[ARRunContextSelector, _Mapping]] = ...) -> None: ...

class ARInputSlotDeleteMessage(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
