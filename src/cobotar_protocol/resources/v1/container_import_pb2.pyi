from buf.validate import validate_pb2 as _validate_pb2
from cobotar_protocol.common.v1 import external_references_pb2 as _external_references_pb2
from cobotar_protocol.resources.v1 import container_definition_pb2 as _container_definition_pb2
from cobotar_protocol.resources.v1 import model_requests_pb2 as _model_requests_pb2
from cobotar_protocol.service.v1 import response_pb2 as _response_pb2
from cobotar_protocol.validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImportContainer(_message.Message):
    __slots__ = ("container", "model", "slot_references")
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SLOT_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    container: _container_definition_pb2.ContainerDefinition
    model: _model_requests_pb2.CreateModelArtifact
    slot_references: _containers.RepeatedCompositeFieldContainer[ImportedSlotReferences]
    def __init__(self, container: _Optional[_Union[_container_definition_pb2.ContainerDefinition, _Mapping]] = ..., model: _Optional[_Union[_model_requests_pb2.CreateModelArtifact, _Mapping]] = ..., slot_references: _Optional[_Iterable[_Union[ImportedSlotReferences, _Mapping]]] = ...) -> None: ...

class ImportedSlotReferences(_message.Message):
    __slots__ = ("slot_id", "products", "parts", "part_families")
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    PART_FAMILIES_FIELD_NUMBER: _ClassVar[int]
    slot_id: str
    products: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    parts: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    part_families: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    def __init__(self, slot_id: _Optional[str] = ..., products: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ..., parts: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ..., part_families: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ...) -> None: ...

class ImportContainerResult(_message.Message):
    __slots__ = ("container_id", "container_status", "model_id", "model_status")
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_STATUS_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_STATUS_FIELD_NUMBER: _ClassVar[int]
    container_id: str
    container_status: _response_pb2.MutationStatus
    model_id: str
    model_status: _response_pb2.MutationStatus
    def __init__(self, container_id: _Optional[str] = ..., container_status: _Optional[_Union[_response_pb2.MutationStatus, str]] = ..., model_id: _Optional[str] = ..., model_status: _Optional[_Union[_response_pb2.MutationStatus, str]] = ...) -> None: ...
