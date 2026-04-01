from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import enums_pb2 as _enums_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuantityStatus(_message.Message):
    __slots__ = ("amount", "unit", "nominal_amount")
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    amount: float
    unit: str
    nominal_amount: float
    def __init__(self, amount: _Optional[float] = ..., unit: _Optional[str] = ..., nominal_amount: _Optional[float] = ...) -> None: ...

class PartInstanceLocation(_message.Message):
    __slots__ = ("container_instance_id", "slot_id", "line_id", "cell_id", "station_id", "pose")
    CONTAINER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    container_instance_id: str
    slot_id: str
    line_id: str
    cell_id: str
    station_id: str
    pose: _pose_pb2.LocalizedPose
    def __init__(self, container_instance_id: _Optional[str] = ..., slot_id: _Optional[str] = ..., line_id: _Optional[str] = ..., cell_id: _Optional[str] = ..., station_id: _Optional[str] = ..., pose: _Optional[_Union[_pose_pb2.LocalizedPose, _Mapping]] = ...) -> None: ...

class PartInstance(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "part_definition_id", "status", "location", "quantity", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PART_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    part_definition_id: str
    status: _enums_pb2.ResourceStatus
    location: PartInstanceLocation
    quantity: QuantityStatus
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., part_definition_id: _Optional[str] = ..., status: _Optional[_Union[_enums_pb2.ResourceStatus, str]] = ..., location: _Optional[_Union[PartInstanceLocation, _Mapping]] = ..., quantity: _Optional[_Union[QuantityStatus, _Mapping]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class PartInstances(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PartInstance]
    def __init__(self, items: _Optional[_Iterable[_Union[PartInstance, _Mapping]]] = ...) -> None: ...
