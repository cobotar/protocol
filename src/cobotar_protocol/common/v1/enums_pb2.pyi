from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

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
