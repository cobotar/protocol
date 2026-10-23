from buf.validate import validate_pb2 as _validate_pb2
from cobotar_protocol.validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignalDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNAL_DATA_TYPE_UNSPECIFIED: _ClassVar[SignalDataType]
    SIGNAL_DATA_TYPE_BOOL: _ClassVar[SignalDataType]
    SIGNAL_DATA_TYPE_INT32: _ClassVar[SignalDataType]
    SIGNAL_DATA_TYPE_DOUBLE: _ClassVar[SignalDataType]
    SIGNAL_DATA_TYPE_STRING: _ClassVar[SignalDataType]

class SignalSemantic(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNAL_SEMANTIC_UNSPECIFIED: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ASSET_CAMERA_ACTIVE: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ASSET_CAMERA_ERROR_DETECTED: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ASSET_LIGHT_RED: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ASSET_LIGHT_YELLOW: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ASSET_LIGHT_GREEN: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ASSET_CONVEYOR_MOVING: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ASSET_SENSOR_TRIGGERED: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ASSET_HMI_INSTRUCTIONS_VISIBLE: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ASSET_PART_FEEDER_READY: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ASSET_PART_FEEDER_EMPTY: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ROBOT_ACKNOWLEDGE: _ClassVar[SignalSemantic]
    SIGNAL_SEMANTIC_ROBOT_FREE_DRIVE: _ClassVar[SignalSemantic]
SIGNAL_DATA_TYPE_UNSPECIFIED: SignalDataType
SIGNAL_DATA_TYPE_BOOL: SignalDataType
SIGNAL_DATA_TYPE_INT32: SignalDataType
SIGNAL_DATA_TYPE_DOUBLE: SignalDataType
SIGNAL_DATA_TYPE_STRING: SignalDataType
SIGNAL_SEMANTIC_UNSPECIFIED: SignalSemantic
SIGNAL_SEMANTIC_ASSET_CAMERA_ACTIVE: SignalSemantic
SIGNAL_SEMANTIC_ASSET_CAMERA_ERROR_DETECTED: SignalSemantic
SIGNAL_SEMANTIC_ASSET_LIGHT_RED: SignalSemantic
SIGNAL_SEMANTIC_ASSET_LIGHT_YELLOW: SignalSemantic
SIGNAL_SEMANTIC_ASSET_LIGHT_GREEN: SignalSemantic
SIGNAL_SEMANTIC_ASSET_CONVEYOR_MOVING: SignalSemantic
SIGNAL_SEMANTIC_ASSET_SENSOR_TRIGGERED: SignalSemantic
SIGNAL_SEMANTIC_ASSET_HMI_INSTRUCTIONS_VISIBLE: SignalSemantic
SIGNAL_SEMANTIC_ASSET_PART_FEEDER_READY: SignalSemantic
SIGNAL_SEMANTIC_ASSET_PART_FEEDER_EMPTY: SignalSemantic
SIGNAL_SEMANTIC_ROBOT_ACKNOWLEDGE: SignalSemantic
SIGNAL_SEMANTIC_ROBOT_FREE_DRIVE: SignalSemantic

class SignalDefinition(_message.Message):
    __slots__ = ("signal_id", "name", "data_type", "readable", "writable", "semantic")
    SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    READABLE_FIELD_NUMBER: _ClassVar[int]
    WRITABLE_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_FIELD_NUMBER: _ClassVar[int]
    signal_id: str
    name: str
    data_type: SignalDataType
    readable: bool
    writable: bool
    semantic: SignalSemantic
    def __init__(self, signal_id: _Optional[str] = ..., name: _Optional[str] = ..., data_type: _Optional[_Union[SignalDataType, str]] = ..., readable: bool = ..., writable: bool = ..., semantic: _Optional[_Union[SignalSemantic, str]] = ...) -> None: ...

class SignalCatalog(_message.Message):
    __slots__ = ("resource_id", "signals")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNALS_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    signals: _containers.RepeatedCompositeFieldContainer[SignalDefinition]
    def __init__(self, resource_id: _Optional[str] = ..., signals: _Optional[_Iterable[_Union[SignalDefinition, _Mapping]]] = ...) -> None: ...
