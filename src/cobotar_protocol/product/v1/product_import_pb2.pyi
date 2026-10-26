from buf.validate import validate_pb2 as _validate_pb2
from cobotar_protocol.product.v1 import part_definition_pb2 as _part_definition_pb2
from cobotar_protocol.product.v1 import part_family_pb2 as _part_family_pb2
from cobotar_protocol.product.v1 import product_definition_pb2 as _product_definition_pb2
from cobotar_protocol.resources.v1 import model_requests_pb2 as _model_requests_pb2
from cobotar_protocol.service.v1 import response_pb2 as _response_pb2
from cobotar_protocol.validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImportProduct(_message.Message):
    __slots__ = ("models", "parts", "product", "product_model_key", "families")
    MODELS_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_MODEL_KEY_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[ImportedModel]
    parts: _containers.RepeatedCompositeFieldContainer[ImportedPart]
    product: _product_definition_pb2.ProductDefinition
    product_model_key: str
    families: _containers.RepeatedCompositeFieldContainer[ImportedPartFamily]
    def __init__(self, models: _Optional[_Iterable[_Union[ImportedModel, _Mapping]]] = ..., parts: _Optional[_Iterable[_Union[ImportedPart, _Mapping]]] = ..., product: _Optional[_Union[_product_definition_pb2.ProductDefinition, _Mapping]] = ..., product_model_key: _Optional[str] = ..., families: _Optional[_Iterable[_Union[ImportedPartFamily, _Mapping]]] = ...) -> None: ...

class ImportedModel(_message.Message):
    __slots__ = ("key", "model")
    KEY_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    key: str
    model: _model_requests_pb2.CreateModelArtifact
    def __init__(self, key: _Optional[str] = ..., model: _Optional[_Union[_model_requests_pb2.CreateModelArtifact, _Mapping]] = ...) -> None: ...

class ImportedPart(_message.Message):
    __slots__ = ("key", "part", "model_key", "families")
    KEY_FIELD_NUMBER: _ClassVar[int]
    PART_FIELD_NUMBER: _ClassVar[int]
    MODEL_KEY_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    key: str
    part: _part_definition_pb2.PartDefinition
    model_key: str
    families: ImportedPartFamilyMemberships
    def __init__(self, key: _Optional[str] = ..., part: _Optional[_Union[_part_definition_pb2.PartDefinition, _Mapping]] = ..., model_key: _Optional[str] = ..., families: _Optional[_Union[ImportedPartFamilyMemberships, _Mapping]] = ...) -> None: ...

class ImportedPartFamilyMemberships(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ImportedPartFamilyMembership]
    def __init__(self, items: _Optional[_Iterable[_Union[ImportedPartFamilyMembership, _Mapping]]] = ...) -> None: ...

class ImportedPartFamilyMembership(_message.Message):
    __slots__ = ("family_key", "values")
    class ValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FAMILY_KEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    family_key: str
    values: _containers.ScalarMap[str, str]
    def __init__(self, family_key: _Optional[str] = ..., values: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ImportedPartFamily(_message.Message):
    __slots__ = ("key", "family")
    KEY_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    key: str
    family: _part_family_pb2.PartFamily
    def __init__(self, key: _Optional[str] = ..., family: _Optional[_Union[_part_family_pb2.PartFamily, _Mapping]] = ...) -> None: ...

class ImportProductResult(_message.Message):
    __slots__ = ("product", "models", "parts", "families")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    product: ImportedEntity
    models: _containers.RepeatedCompositeFieldContainer[ImportedEntity]
    parts: _containers.RepeatedCompositeFieldContainer[ImportedEntity]
    families: _containers.RepeatedCompositeFieldContainer[ImportedEntity]
    def __init__(self, product: _Optional[_Union[ImportedEntity, _Mapping]] = ..., models: _Optional[_Iterable[_Union[ImportedEntity, _Mapping]]] = ..., parts: _Optional[_Iterable[_Union[ImportedEntity, _Mapping]]] = ..., families: _Optional[_Iterable[_Union[ImportedEntity, _Mapping]]] = ...) -> None: ...

class ImportedEntity(_message.Message):
    __slots__ = ("key", "id", "status")
    KEY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    key: str
    id: str
    status: _response_pb2.MutationStatus
    def __init__(self, key: _Optional[str] = ..., id: _Optional[str] = ..., status: _Optional[_Union[_response_pb2.MutationStatus, str]] = ...) -> None: ...
