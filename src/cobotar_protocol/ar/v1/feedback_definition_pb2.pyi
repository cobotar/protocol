from ar.v1 import definition_status_pb2 as _definition_status_pb2
from ar.v1 import execution_contract_pb2 as _execution_contract_pb2
from ar.v1 import feedback_pb2 as _feedback_pb2
from ar.v1 import feedback_capability_pb2 as _feedback_capability_pb2
from ar.v1 import feedback_features_pb2 as _feedback_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import property_pb2 as _property_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeedbackGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEEDBACK_GROUP_UNSPECIFIED: _ClassVar[FeedbackGroup]
    FEEDBACK_GROUP_GENERAL: _ClassVar[FeedbackGroup]
    FEEDBACK_GROUP_SPATIAL: _ClassVar[FeedbackGroup]
    FEEDBACK_GROUP_RESOURCE: _ClassVar[FeedbackGroup]
    FEEDBACK_GROUP_PROCESS: _ClassVar[FeedbackGroup]
    FEEDBACK_GROUP_VALIDATION: _ClassVar[FeedbackGroup]
    FEEDBACK_GROUP_ROBOT: _ClassVar[FeedbackGroup]
    FEEDBACK_GROUP_COLLABORATION: _ClassVar[FeedbackGroup]
FEEDBACK_GROUP_UNSPECIFIED: FeedbackGroup
FEEDBACK_GROUP_GENERAL: FeedbackGroup
FEEDBACK_GROUP_SPATIAL: FeedbackGroup
FEEDBACK_GROUP_RESOURCE: FeedbackGroup
FEEDBACK_GROUP_PROCESS: FeedbackGroup
FEEDBACK_GROUP_VALIDATION: FeedbackGroup
FEEDBACK_GROUP_ROBOT: FeedbackGroup
FEEDBACK_GROUP_COLLABORATION: FeedbackGroup

class FeedbackDefinition(_message.Message):
    __slots__ = ("id", "key", "name", "icon", "description", "type", "group", "revision", "status", "properties", "features", "capabilities", "execution")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    name: str
    icon: str
    description: str
    type: _feedback_pb2.FeedbackType
    group: FeedbackGroup
    revision: int
    status: _definition_status_pb2.DefinitionStatus
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyTemplate]
    features: _containers.RepeatedCompositeFieldContainer[_feedback_features_pb2.FeedbackFeature]
    capabilities: _containers.RepeatedCompositeFieldContainer[_feedback_capability_pb2.FeedbackCapability]
    execution: _execution_contract_pb2.ExecutionContract
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_feedback_pb2.FeedbackType, str]] = ..., group: _Optional[_Union[FeedbackGroup, str]] = ..., revision: _Optional[int] = ..., status: _Optional[_Union[_definition_status_pb2.DefinitionStatus, str]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyTemplate, _Mapping]]] = ..., features: _Optional[_Iterable[_Union[_feedback_features_pb2.FeedbackFeature, _Mapping]]] = ..., capabilities: _Optional[_Iterable[_Union[_feedback_capability_pb2.FeedbackCapability, _Mapping]]] = ..., execution: _Optional[_Union[_execution_contract_pb2.ExecutionContract, _Mapping]] = ...) -> None: ...

class FeedbackDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FeedbackDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[FeedbackDefinition, _Mapping]]] = ...) -> None: ...
