from buf.validate import validate_pb2 as _validate_pb2
from cobotar_protocol.common.v1 import external_references_pb2 as _external_references_pb2
from cobotar_protocol.validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartFamilyKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PART_FAMILY_KIND_UNSPECIFIED: _ClassVar[PartFamilyKind]
    PART_FAMILY_KIND_VARIANT_ALTERNATIVE: _ClassVar[PartFamilyKind]
    PART_FAMILY_KIND_SUBSTITUTE: _ClassVar[PartFamilyKind]
PART_FAMILY_KIND_UNSPECIFIED: PartFamilyKind
PART_FAMILY_KIND_VARIANT_ALTERNATIVE: PartFamilyKind
PART_FAMILY_KIND_SUBSTITUTE: PartFamilyKind

class PartFamilyDimension(_message.Message):
    __slots__ = ("key", "name")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    key: str
    name: str
    def __init__(self, key: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class PartFamily(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "kind", "dimensions", "external_references", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    kind: PartFamilyKind
    dimensions: _containers.RepeatedCompositeFieldContainer[PartFamilyDimension]
    external_references: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    revision: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., kind: _Optional[_Union[PartFamilyKind, str]] = ..., dimensions: _Optional[_Iterable[_Union[PartFamilyDimension, _Mapping]]] = ..., external_references: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ..., revision: _Optional[int] = ...) -> None: ...

class PartFamilies(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PartFamily]
    def __init__(self, items: _Optional[_Iterable[_Union[PartFamily, _Mapping]]] = ...) -> None: ...

class PartFamilyMembership(_message.Message):
    __slots__ = ("family_id", "values")
    class ValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    values: _containers.ScalarMap[str, str]
    def __init__(self, family_id: _Optional[str] = ..., values: _Optional[_Mapping[str, str]] = ...) -> None: ...
