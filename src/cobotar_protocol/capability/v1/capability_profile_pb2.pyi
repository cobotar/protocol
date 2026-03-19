from common.v1 import key_value_constraint_pb2 as _key_value_constraint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CapabilityProfile(_message.Message):
    __slots__ = ("min_force_n", "max_force_n", "min_torque_nm", "max_torque_nm", "repeatability_mm", "max_payload_g", "min_grip_width_mm", "max_grip_width_mm", "constraints")
    MIN_FORCE_N_FIELD_NUMBER: _ClassVar[int]
    MAX_FORCE_N_FIELD_NUMBER: _ClassVar[int]
    MIN_TORQUE_NM_FIELD_NUMBER: _ClassVar[int]
    MAX_TORQUE_NM_FIELD_NUMBER: _ClassVar[int]
    REPEATABILITY_MM_FIELD_NUMBER: _ClassVar[int]
    MAX_PAYLOAD_G_FIELD_NUMBER: _ClassVar[int]
    MIN_GRIP_WIDTH_MM_FIELD_NUMBER: _ClassVar[int]
    MAX_GRIP_WIDTH_MM_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    min_force_n: float
    max_force_n: float
    min_torque_nm: float
    max_torque_nm: float
    repeatability_mm: float
    max_payload_g: float
    min_grip_width_mm: float
    max_grip_width_mm: float
    constraints: _containers.RepeatedCompositeFieldContainer[_key_value_constraint_pb2.KeyValueConstraint]
    def __init__(self, min_force_n: _Optional[float] = ..., max_force_n: _Optional[float] = ..., min_torque_nm: _Optional[float] = ..., max_torque_nm: _Optional[float] = ..., repeatability_mm: _Optional[float] = ..., max_payload_g: _Optional[float] = ..., min_grip_width_mm: _Optional[float] = ..., max_grip_width_mm: _Optional[float] = ..., constraints: _Optional[_Iterable[_Union[_key_value_constraint_pb2.KeyValueConstraint, _Mapping]]] = ...) -> None: ...
