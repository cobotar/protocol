import datetime

from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import actor_pb2 as _actor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActorAvailabilityStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTOR_AVAILABILITY_STATUS_UNSPECIFIED: _ClassVar[ActorAvailabilityStatus]
    ACTOR_AVAILABILITY_STATUS_AVAILABLE: _ClassVar[ActorAvailabilityStatus]
    ACTOR_AVAILABILITY_STATUS_UNAVAILABLE: _ClassVar[ActorAvailabilityStatus]
    ACTOR_AVAILABILITY_STATUS_UNKNOWN: _ClassVar[ActorAvailabilityStatus]

class ActorAvailabilitySource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTOR_AVAILABILITY_SOURCE_UNSPECIFIED: _ClassVar[ActorAvailabilitySource]
    ACTOR_AVAILABILITY_SOURCE_MANUAL: _ClassVar[ActorAvailabilitySource]
    ACTOR_AVAILABILITY_SOURCE_DEVICE: _ClassVar[ActorAvailabilitySource]
    ACTOR_AVAILABILITY_SOURCE_SCHEDULE: _ClassVar[ActorAvailabilitySource]
    ACTOR_AVAILABILITY_SOURCE_SYSTEM: _ClassVar[ActorAvailabilitySource]
    ACTOR_AVAILABILITY_SOURCE_SUPERVISOR: _ClassVar[ActorAvailabilitySource]
ACTOR_AVAILABILITY_STATUS_UNSPECIFIED: ActorAvailabilityStatus
ACTOR_AVAILABILITY_STATUS_AVAILABLE: ActorAvailabilityStatus
ACTOR_AVAILABILITY_STATUS_UNAVAILABLE: ActorAvailabilityStatus
ACTOR_AVAILABILITY_STATUS_UNKNOWN: ActorAvailabilityStatus
ACTOR_AVAILABILITY_SOURCE_UNSPECIFIED: ActorAvailabilitySource
ACTOR_AVAILABILITY_SOURCE_MANUAL: ActorAvailabilitySource
ACTOR_AVAILABILITY_SOURCE_DEVICE: ActorAvailabilitySource
ACTOR_AVAILABILITY_SOURCE_SCHEDULE: ActorAvailabilitySource
ACTOR_AVAILABILITY_SOURCE_SYSTEM: ActorAvailabilitySource
ACTOR_AVAILABILITY_SOURCE_SUPERVISOR: ActorAvailabilitySource

class ActorLocation(_message.Message):
    __slots__ = ("line_id", "cell_id", "station_id")
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    line_id: str
    cell_id: str
    station_id: str
    def __init__(self, line_id: _Optional[str] = ..., cell_id: _Optional[str] = ..., station_id: _Optional[str] = ...) -> None: ...

class ActorAvailability(_message.Message):
    __slots__ = ("id", "name", "icon", "actor", "status", "location", "source", "reason", "observed_at", "valid_until", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    actor: _actor_pb2.ActorRef
    status: ActorAvailabilityStatus
    location: ActorLocation
    source: ActorAvailabilitySource
    reason: str
    observed_at: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    revision: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ..., status: _Optional[_Union[ActorAvailabilityStatus, str]] = ..., location: _Optional[_Union[ActorLocation, _Mapping]] = ..., source: _Optional[_Union[ActorAvailabilitySource, str]] = ..., reason: _Optional[str] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revision: _Optional[int] = ...) -> None: ...

class ActorAvailabilities(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ActorAvailability]
    def __init__(self, items: _Optional[_Iterable[_Union[ActorAvailability, _Mapping]]] = ...) -> None: ...
