from common.v1 import external_references_pb2 as _external_references_pb2
from process.v1 import sequence_definition_pb2 as _sequence_definition_pb2
from process.v1 import task_definition_pb2 as _task_definition_pb2
from variance.v1 import variant_rule_pb2 as _variant_rule_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESS_TYPE_UNSPECIFIED: _ClassVar[ProcessType]
    PROCESS_TYPE_ASSEMBLY: _ClassVar[ProcessType]
    PROCESS_TYPE_DISASSEMBLY: _ClassVar[ProcessType]
    PROCESS_TYPE_INSPECTION: _ClassVar[ProcessType]
    PROCESS_TYPE_CHECKLIST: _ClassVar[ProcessType]
    PROCESS_TYPE_KITTING: _ClassVar[ProcessType]
    PROCESS_TYPE_MAINTENANCE: _ClassVar[ProcessType]
PROCESS_TYPE_UNSPECIFIED: ProcessType
PROCESS_TYPE_ASSEMBLY: ProcessType
PROCESS_TYPE_DISASSEMBLY: ProcessType
PROCESS_TYPE_INSPECTION: ProcessType
PROCESS_TYPE_CHECKLIST: ProcessType
PROCESS_TYPE_KITTING: ProcessType
PROCESS_TYPE_MAINTENANCE: ProcessType

class RecipeApplicability(_message.Message):
    __slots__ = ("include", "exclude")
    INCLUDE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    include: _containers.RepeatedCompositeFieldContainer[_variant_rule_pb2.VariantRule]
    exclude: _containers.RepeatedCompositeFieldContainer[_variant_rule_pb2.VariantRule]
    def __init__(self, include: _Optional[_Iterable[_Union[_variant_rule_pb2.VariantRule, _Mapping]]] = ..., exclude: _Optional[_Iterable[_Union[_variant_rule_pb2.VariantRule, _Mapping]]] = ...) -> None: ...

class ProcessRecipe(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "product_definition_id", "applicability", "root_sequence_id", "sequences", "tasks", "supported_container_definition_ids", "external_references")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICABILITY_FIELD_NUMBER: _ClassVar[int]
    ROOT_SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CONTAINER_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: ProcessType
    product_definition_id: str
    applicability: RecipeApplicability
    root_sequence_id: str
    sequences: _containers.RepeatedCompositeFieldContainer[_sequence_definition_pb2.SequenceDefinition]
    tasks: _containers.RepeatedCompositeFieldContainer[_task_definition_pb2.TaskDefinition]
    supported_container_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    external_references: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[ProcessType, str]] = ..., product_definition_id: _Optional[str] = ..., applicability: _Optional[_Union[RecipeApplicability, _Mapping]] = ..., root_sequence_id: _Optional[str] = ..., sequences: _Optional[_Iterable[_Union[_sequence_definition_pb2.SequenceDefinition, _Mapping]]] = ..., tasks: _Optional[_Iterable[_Union[_task_definition_pb2.TaskDefinition, _Mapping]]] = ..., supported_container_definition_ids: _Optional[_Iterable[str]] = ..., external_references: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ...) -> None: ...

class ProcessRecipes(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ProcessRecipe]
    def __init__(self, items: _Optional[_Iterable[_Union[ProcessRecipe, _Mapping]]] = ...) -> None: ...
