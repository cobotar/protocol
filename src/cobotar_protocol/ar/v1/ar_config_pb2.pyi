from ar.v1 import input_slot_pb2 as _input_slot_pb2
from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class ARConfigMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "ar_disappear_distance", "feedback_ids", "action_ids", "helper_ids", "property_ids", "input_slots")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AR_DISAPPEAR_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_IDS_FIELD_NUMBER: _ClassVar[int]
    ACTION_IDS_FIELD_NUMBER: _ClassVar[int]
    HELPER_IDS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_IDS_FIELD_NUMBER: _ClassVar[int]
    INPUT_SLOTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    ar_disappear_distance: int
    feedback_ids: _containers.RepeatedScalarFieldContainer[str]
    action_ids: _containers.RepeatedScalarFieldContainer[str]
    helper_ids: _containers.RepeatedScalarFieldContainer[str]
    property_ids: _containers.RepeatedScalarFieldContainer[str]
    input_slots: _containers.RepeatedCompositeFieldContainer[_input_slot_pb2.ARInputSlotMessage]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., ar_disappear_distance: _Optional[int] = ..., feedback_ids: _Optional[_Iterable[str]] = ..., action_ids: _Optional[_Iterable[str]] = ..., helper_ids: _Optional[_Iterable[str]] = ..., property_ids: _Optional[_Iterable[str]] = ..., input_slots: _Optional[_Iterable[_Union[_input_slot_pb2.ARInputSlotMessage, _Mapping]]] = ...) -> None: ...

class ARConfigMessages(_message.Message):
    __slots__ = ("configs",)
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[ARConfigMessage]
    def __init__(self, configs: _Optional[_Iterable[_Union[ARConfigMessage, _Mapping]]] = ...) -> None: ...
