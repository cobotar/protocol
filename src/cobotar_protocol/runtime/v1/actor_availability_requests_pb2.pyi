import datetime

from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import actor_pb2 as _actor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from runtime.v1 import actor_availability_pb2 as _actor_availability_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActorAvailabilityReportRequest(_message.Message):
    __slots__ = ("actor", "status", "location", "source", "reason", "observed_at", "valid_until")
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    actor: _actor_pb2.ActorRef
    status: _actor_availability_pb2.ActorAvailabilityStatus
    location: _actor_availability_pb2.ActorLocation
    source: _actor_availability_pb2.ActorAvailabilitySource
    reason: str
    observed_at: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    def __init__(self, actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ..., status: _Optional[_Union[_actor_availability_pb2.ActorAvailabilityStatus, str]] = ..., location: _Optional[_Union[_actor_availability_pb2.ActorLocation, _Mapping]] = ..., source: _Optional[_Union[_actor_availability_pb2.ActorAvailabilitySource, str]] = ..., reason: _Optional[str] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ActorAvailabilityOverrideRequest(_message.Message):
    __slots__ = ("actor_availability_id", "status", "reason", "valid_until", "expected_revision")
    ACTOR_AVAILABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    actor_availability_id: str
    status: _actor_availability_pb2.ActorAvailabilityStatus
    reason: str
    valid_until: _timestamp_pb2.Timestamp
    expected_revision: int
    def __init__(self, actor_availability_id: _Optional[str] = ..., status: _Optional[_Union[_actor_availability_pb2.ActorAvailabilityStatus, str]] = ..., reason: _Optional[str] = ..., valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expected_revision: _Optional[int] = ...) -> None: ...

class ActorAvailabilityOverrideClearRequest(_message.Message):
    __slots__ = ("actor_availability_id", "expected_revision")
    ACTOR_AVAILABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    actor_availability_id: str
    expected_revision: int
    def __init__(self, actor_availability_id: _Optional[str] = ..., expected_revision: _Optional[int] = ...) -> None: ...
