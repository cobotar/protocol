from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RobotIODataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_IO_DATA_TYPE_UNSPECIFIED: _ClassVar[RobotIODataType]
    ROBOT_IO_DATA_TYPE_BOOL: _ClassVar[RobotIODataType]
    ROBOT_IO_DATA_TYPE_INT32: _ClassVar[RobotIODataType]
    ROBOT_IO_DATA_TYPE_DOUBLE: _ClassVar[RobotIODataType]
ROBOT_IO_DATA_TYPE_UNSPECIFIED: RobotIODataType
ROBOT_IO_DATA_TYPE_BOOL: RobotIODataType
ROBOT_IO_DATA_TYPE_INT32: RobotIODataType
ROBOT_IO_DATA_TYPE_DOUBLE: RobotIODataType

class RobotIOSignalDefinition(_message.Message):
    __slots__ = ("signal_id", "name", "data_type", "readable", "writable")
    SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    READABLE_FIELD_NUMBER: _ClassVar[int]
    WRITABLE_FIELD_NUMBER: _ClassVar[int]
    signal_id: str
    name: str
    data_type: RobotIODataType
    readable: bool
    writable: bool
    def __init__(self, signal_id: _Optional[str] = ..., name: _Optional[str] = ..., data_type: _Optional[_Union[RobotIODataType, str]] = ..., readable: bool = ..., writable: bool = ...) -> None: ...

class RobotIOSignalCatalog(_message.Message):
    __slots__ = ("robot_id", "signals")
    ROBOT_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNALS_FIELD_NUMBER: _ClassVar[int]
    robot_id: str
    signals: _containers.RepeatedCompositeFieldContainer[RobotIOSignalDefinition]
    def __init__(self, robot_id: _Optional[str] = ..., signals: _Optional[_Iterable[_Union[RobotIOSignalDefinition, _Mapping]]] = ...) -> None: ...
