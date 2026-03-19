from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import external_references_pb2 as _external_references_pb2
from product.v1 import assembly_node_pb2 as _assembly_node_pb2
from variance.v1 import variant_axis_pb2 as _variant_axis_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductDefinition(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "variant_axes", "root_node_id", "nodes", "external_references", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VARIANT_AXES_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    variant_axes: _containers.RepeatedCompositeFieldContainer[_variant_axis_pb2.VariantAxis]
    root_node_id: str
    nodes: _containers.RepeatedCompositeFieldContainer[_assembly_node_pb2.AssemblyNode]
    external_references: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., variant_axes: _Optional[_Iterable[_Union[_variant_axis_pb2.VariantAxis, _Mapping]]] = ..., root_node_id: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[_assembly_node_pb2.AssemblyNode, _Mapping]]] = ..., external_references: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class ProductDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ProductDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[ProductDefinition, _Mapping]]] = ...) -> None: ...
