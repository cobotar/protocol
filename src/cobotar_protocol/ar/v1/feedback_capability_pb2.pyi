from ar.v1 import property_influence_pb2 as _property_influence_pb2
from ar.v1 import semantic_source_pb2 as _semantic_source_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeedbackCapability(_message.Message):
    __slots__ = ("semantic", "target_types", "source_requirements", "property_influences")
    SEMANTIC_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_INFLUENCES_FIELD_NUMBER: _ClassVar[int]
    semantic: _semantic_source_pb2.AssistanceSemantic
    target_types: _containers.RepeatedScalarFieldContainer[_semantic_source_pb2.SemanticValueType]
    source_requirements: _containers.RepeatedCompositeFieldContainer[_semantic_source_pb2.SemanticSourceRequirement]
    property_influences: _containers.RepeatedCompositeFieldContainer[_property_influence_pb2.PropertyInfluence]
    def __init__(self, semantic: _Optional[_Union[_semantic_source_pb2.AssistanceSemantic, str]] = ..., target_types: _Optional[_Iterable[_Union[_semantic_source_pb2.SemanticValueType, str]]] = ..., source_requirements: _Optional[_Iterable[_Union[_semantic_source_pb2.SemanticSourceRequirement, _Mapping]]] = ..., property_influences: _Optional[_Iterable[_Union[_property_influence_pb2.PropertyInfluence, _Mapping]]] = ...) -> None: ...
