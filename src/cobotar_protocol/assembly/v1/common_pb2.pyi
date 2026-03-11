import datetime

from ar.v1 import property_pb2 as _property_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActorKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTOR_KIND_UNSPECIFIED: _ClassVar[ActorKind]
    ACTOR_KIND_HUMAN: _ClassVar[ActorKind]
    ACTOR_KIND_ROBOT: _ClassVar[ActorKind]
    ACTOR_KIND_HYBRID: _ClassVar[ActorKind]

class ResourceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_STATUS_UNSPECIFIED: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_AVAILABLE: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_UNAVAILABLE: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_DISABLED: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_MAINTENANCE: _ClassVar[ResourceStatus]

class SafetyRelevance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAFETY_RELEVANCE_UNSPECIFIED: _ClassVar[SafetyRelevance]
    SAFETY_RELEVANCE_LOW: _ClassVar[SafetyRelevance]
    SAFETY_RELEVANCE_MEDIUM: _ClassVar[SafetyRelevance]
    SAFETY_RELEVANCE_HIGH: _ClassVar[SafetyRelevance]
    SAFETY_RELEVANCE_CRITICAL: _ClassVar[SafetyRelevance]

class CollaborationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLLABORATION_MODE_UNSPECIFIED: _ClassVar[CollaborationMode]
    COLLABORATION_MODE_HUMAN_ONLY: _ClassVar[CollaborationMode]
    COLLABORATION_MODE_ROBOT_ONLY: _ClassVar[CollaborationMode]
    COLLABORATION_MODE_SEQUENTIAL_HRC: _ClassVar[CollaborationMode]
    COLLABORATION_MODE_SIMULTANEOUS_HRC: _ClassVar[CollaborationMode]

class ConstraintOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSTRAINT_OPERATOR_UNSPECIFIED: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_EQ: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_NEQ: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_GT: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_GTE: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_LT: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_LTE: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_IN: _ClassVar[ConstraintOperator]
    CONSTRAINT_OPERATOR_NOT_IN: _ClassVar[ConstraintOperator]
ACTOR_KIND_UNSPECIFIED: ActorKind
ACTOR_KIND_HUMAN: ActorKind
ACTOR_KIND_ROBOT: ActorKind
ACTOR_KIND_HYBRID: ActorKind
RESOURCE_STATUS_UNSPECIFIED: ResourceStatus
RESOURCE_STATUS_AVAILABLE: ResourceStatus
RESOURCE_STATUS_UNAVAILABLE: ResourceStatus
RESOURCE_STATUS_DISABLED: ResourceStatus
RESOURCE_STATUS_MAINTENANCE: ResourceStatus
SAFETY_RELEVANCE_UNSPECIFIED: SafetyRelevance
SAFETY_RELEVANCE_LOW: SafetyRelevance
SAFETY_RELEVANCE_MEDIUM: SafetyRelevance
SAFETY_RELEVANCE_HIGH: SafetyRelevance
SAFETY_RELEVANCE_CRITICAL: SafetyRelevance
COLLABORATION_MODE_UNSPECIFIED: CollaborationMode
COLLABORATION_MODE_HUMAN_ONLY: CollaborationMode
COLLABORATION_MODE_ROBOT_ONLY: CollaborationMode
COLLABORATION_MODE_SEQUENTIAL_HRC: CollaborationMode
COLLABORATION_MODE_SIMULTANEOUS_HRC: CollaborationMode
CONSTRAINT_OPERATOR_UNSPECIFIED: ConstraintOperator
CONSTRAINT_OPERATOR_EQ: ConstraintOperator
CONSTRAINT_OPERATOR_NEQ: ConstraintOperator
CONSTRAINT_OPERATOR_GT: ConstraintOperator
CONSTRAINT_OPERATOR_GTE: ConstraintOperator
CONSTRAINT_OPERATOR_LT: ConstraintOperator
CONSTRAINT_OPERATOR_LTE: ConstraintOperator
CONSTRAINT_OPERATOR_IN: ConstraintOperator
CONSTRAINT_OPERATOR_NOT_IN: ConstraintOperator

class Ref(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class NamedRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class KeyValueConstraint(_message.Message):
    __slots__ = ("key", "op", "value", "values")
    KEY_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    op: ConstraintOperator
    value: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., op: _Optional[_Union[ConstraintOperator, str]] = ..., value: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class TimeWindow(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LocalTarget(_message.Message):
    __slots__ = ("anchor_id", "offset")
    ANCHOR_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    anchor_id: str
    offset: _pose_pb2.Pose
    def __init__(self, anchor_id: _Optional[str] = ..., offset: _Optional[_Union[_pose_pb2.Pose, _Mapping]] = ...) -> None: ...

class EstimatedDuration(_message.Message):
    __slots__ = ("nominal", "min", "max")
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    nominal: _duration_pb2.Duration
    min: _duration_pb2.Duration
    max: _duration_pb2.Duration
    def __init__(self, nominal: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., min: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class DisplayText(_message.Message):
    __slots__ = ("title", "description", "operator_instruction")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    operator_instruction: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., operator_instruction: _Optional[str] = ...) -> None: ...

class ExternalReference(_message.Message):
    __slots__ = ("system", "external_id", "url")
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    system: str
    external_id: str
    url: str
    def __init__(self, system: _Optional[str] = ..., external_id: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class CustomProperties(_message.Message):
    __slots__ = ("properties",)
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.Property]
    def __init__(self, properties: _Optional[_Iterable[_Union[_property_pb2.Property, _Mapping]]] = ...) -> None: ...
