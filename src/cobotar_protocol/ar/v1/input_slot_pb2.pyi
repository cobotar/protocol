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

class ARInputSlotMessage(_message.Message):
    __slots__ = ("id", "config_id", "name", "icon", "description", "required", "generated_property_id", "resource_type", "context_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    GENERATED_PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    config_id: str
    name: str
    icon: str
    description: str
    required: bool
    generated_property_id: str
    resource_type: ARResourceSlotType
    context_type: ARContextSlotType
    def __init__(self, id: _Optional[str] = ..., config_id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., required: bool = ..., generated_property_id: _Optional[str] = ..., resource_type: _Optional[_Union[ARResourceSlotType, str]] = ..., context_type: _Optional[_Union[ARContextSlotType, str]] = ...) -> None: ...

class ARInputSlotMessages(_message.Message):
    __slots__ = ("slots",)
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    slots: _containers.RepeatedCompositeFieldContainer[ARInputSlotMessage]
    def __init__(self, slots: _Optional[_Iterable[_Union[ARInputSlotMessage, _Mapping]]] = ...) -> None: ...

class ARInputSlotAddMessage(_message.Message):
    __slots__ = ("config_id", "name", "icon", "description", "required", "resource_type", "context_type")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
    config_id: str
    name: str
    icon: str
    description: str
    required: bool
    resource_type: ARResourceSlotType
    context_type: ARContextSlotType
    def __init__(self, config_id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., required: bool = ..., resource_type: _Optional[_Union[ARResourceSlotType, str]] = ..., context_type: _Optional[_Union[ARContextSlotType, str]] = ...) -> None: ...

class ARInputSlotUpdateMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "required")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    required: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., required: bool = ...) -> None: ...

class ARInputSlotDeleteMessage(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
