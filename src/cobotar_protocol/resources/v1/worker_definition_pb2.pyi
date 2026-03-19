from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from common.v1 import external_references_pb2 as _external_references_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EditPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDIT_PERMISSION_UNSPECIFIED: _ClassVar[EditPermission]
    EDIT_PERMISSION_BASIC: _ClassVar[EditPermission]
    EDIT_PERMISSION_COSMETIC: _ClassVar[EditPermission]
    EDIT_PERMISSION_FULL: _ClassVar[EditPermission]
EDIT_PERMISSION_UNSPECIFIED: EditPermission
EDIT_PERMISSION_BASIC: EditPermission
EDIT_PERMISSION_COSMETIC: EditPermission
EDIT_PERMISSION_FULL: EditPermission

class WorkerDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "icon", "disabled", "employee_id", "ar_edit_permission", "external_references", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_ID_FIELD_NUMBER: _ClassVar[int]
    AR_EDIT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    icon: str
    disabled: bool
    employee_id: str
    ar_edit_permission: EditPermission
    external_references: _containers.RepeatedCompositeFieldContainer[_external_references_pb2.ExternalReference]
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., disabled: bool = ..., employee_id: _Optional[str] = ..., ar_edit_permission: _Optional[_Union[EditPermission, str]] = ..., external_references: _Optional[_Iterable[_Union[_external_references_pb2.ExternalReference, _Mapping]]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...

class WorkerDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[WorkerDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[WorkerDefinition, _Mapping]]] = ...) -> None: ...
