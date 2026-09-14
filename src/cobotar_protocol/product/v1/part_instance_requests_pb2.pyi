from buf.validate import validate_pb2 as _validate_pb2
from product.v1 import part_instance_pb2 as _part_instance_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartInstanceBulkCreateSpec(_message.Message):
    __slots__ = ("part_definition_id", "instance_count", "quantity_per_instance")
    PART_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_PER_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    part_definition_id: str
    instance_count: int
    quantity_per_instance: _part_instance_pb2.QuantityStatus
    def __init__(self, part_definition_id: _Optional[str] = ..., instance_count: _Optional[int] = ..., quantity_per_instance: _Optional[_Union[_part_instance_pb2.QuantityStatus, _Mapping]] = ...) -> None: ...

class BulkCreatePartInstancesRequest(_message.Message):
    __slots__ = ("parts", "location", "idempotency_key")
    PARTS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[PartInstanceBulkCreateSpec]
    location: _part_instance_pb2.PartInstanceLocation
    idempotency_key: str
    def __init__(self, parts: _Optional[_Iterable[_Union[PartInstanceBulkCreateSpec, _Mapping]]] = ..., location: _Optional[_Union[_part_instance_pb2.PartInstanceLocation, _Mapping]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...
