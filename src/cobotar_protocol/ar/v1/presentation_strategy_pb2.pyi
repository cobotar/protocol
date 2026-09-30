from ar.v1 import semantic_source_pb2 as _semantic_source_pb2
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

class PresentationFidelity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRESENTATION_FIDELITY_UNSPECIFIED: _ClassVar[PresentationFidelity]
    PRESENTATION_FIDELITY_LOW: _ClassVar[PresentationFidelity]
    PRESENTATION_FIDELITY_MEDIUM: _ClassVar[PresentationFidelity]
    PRESENTATION_FIDELITY_HIGH: _ClassVar[PresentationFidelity]
PRESENTATION_FIDELITY_UNSPECIFIED: PresentationFidelity
PRESENTATION_FIDELITY_LOW: PresentationFidelity
PRESENTATION_FIDELITY_MEDIUM: PresentationFidelity
PRESENTATION_FIDELITY_HIGH: PresentationFidelity

class PropertyValueAssignment(_message.Message):
    __slots__ = ("property_key", "value")
    PROPERTY_KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    property_key: str
    value: _property_pb2.PropertyValue
    def __init__(self, property_key: _Optional[str] = ..., value: _Optional[_Union[_property_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class PresentationRole(_message.Message):
    __slots__ = ("key", "name", "description", "required_semantics", "default_feedback_definition_id", "default_action_definition_id")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SEMANTICS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FEEDBACK_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ACTION_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    key: str
    name: str
    description: str
    required_semantics: _containers.RepeatedScalarFieldContainer[_semantic_source_pb2.AssistanceSemantic]
    default_feedback_definition_id: str
    default_action_definition_id: str
    def __init__(self, key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., required_semantics: _Optional[_Iterable[_Union[_semantic_source_pb2.AssistanceSemantic, str]]] = ..., default_feedback_definition_id: _Optional[str] = ..., default_action_definition_id: _Optional[str] = ...) -> None: ...

class PresentationRolePreset(_message.Message):
    __slots__ = ("role_key", "properties")
    ROLE_KEY_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    role_key: str
    properties: _containers.RepeatedCompositeFieldContainer[PropertyValueAssignment]
    def __init__(self, role_key: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[PropertyValueAssignment, _Mapping]]] = ...) -> None: ...

class PresentationFidelityAnchor(_message.Message):
    __slots__ = ("fidelity", "target_coverage", "presentations")
    FIDELITY_FIELD_NUMBER: _ClassVar[int]
    TARGET_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    PRESENTATIONS_FIELD_NUMBER: _ClassVar[int]
    fidelity: PresentationFidelity
    target_coverage: float
    presentations: _containers.RepeatedCompositeFieldContainer[PresentationRolePreset]
    def __init__(self, fidelity: _Optional[_Union[PresentationFidelity, str]] = ..., target_coverage: _Optional[float] = ..., presentations: _Optional[_Iterable[_Union[PresentationRolePreset, _Mapping]]] = ...) -> None: ...

class AssistancePresentationRule(_message.Message):
    __slots__ = ("semantic", "anchors")
    SEMANTIC_FIELD_NUMBER: _ClassVar[int]
    ANCHORS_FIELD_NUMBER: _ClassVar[int]
    semantic: _semantic_source_pb2.AssistanceSemantic
    anchors: _containers.RepeatedCompositeFieldContainer[PresentationFidelityAnchor]
    def __init__(self, semantic: _Optional[_Union[_semantic_source_pb2.AssistanceSemantic, str]] = ..., anchors: _Optional[_Iterable[_Union[PresentationFidelityAnchor, _Mapping]]] = ...) -> None: ...

class PresentationStrategy(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "key", "roles", "rules")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    key: str
    roles: _containers.RepeatedCompositeFieldContainer[PresentationRole]
    rules: _containers.RepeatedCompositeFieldContainer[AssistancePresentationRule]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., key: _Optional[str] = ..., roles: _Optional[_Iterable[_Union[PresentationRole, _Mapping]]] = ..., rules: _Optional[_Iterable[_Union[AssistancePresentationRule, _Mapping]]] = ...) -> None: ...

class PresentationStrategyAdd(_message.Message):
    __slots__ = ("name", "icon", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    icon: str
    description: str
    def __init__(self, name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class PresentationStrategies(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PresentationStrategy]
    def __init__(self, items: _Optional[_Iterable[_Union[PresentationStrategy, _Mapping]]] = ...) -> None: ...
