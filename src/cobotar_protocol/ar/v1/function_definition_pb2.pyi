from ar.v1 import definition_status_pb2 as _definition_status_pb2
from ar.v1 import execution_contract_pb2 as _execution_contract_pb2
from ar.v1 import function_pb2 as _function_pb2
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

class FunctionGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FUNCTION_GROUP_UNSPECIFIED: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_GENERAL: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_ROBOT: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_TASK: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_ENVIRONMENT: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_OPERATOR: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_SPATIAL: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_LOGIC: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_DATA: _ClassVar[FunctionGroup]
    FUNCTION_GROUP_TEMPORAL: _ClassVar[FunctionGroup]
FUNCTION_GROUP_UNSPECIFIED: FunctionGroup
FUNCTION_GROUP_GENERAL: FunctionGroup
FUNCTION_GROUP_ROBOT: FunctionGroup
FUNCTION_GROUP_TASK: FunctionGroup
FUNCTION_GROUP_ENVIRONMENT: FunctionGroup
FUNCTION_GROUP_OPERATOR: FunctionGroup
FUNCTION_GROUP_SPATIAL: FunctionGroup
FUNCTION_GROUP_LOGIC: FunctionGroup
FUNCTION_GROUP_DATA: FunctionGroup
FUNCTION_GROUP_TEMPORAL: FunctionGroup

class FunctionDefinition(_message.Message):
    __slots__ = ("id", "key", "name", "icon", "description", "type", "group", "revision", "status", "properties", "execution")
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
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    name: str
    icon: str
    description: str
    type: _function_pb2.FunctionType
    group: FunctionGroup
    revision: int
    status: _definition_status_pb2.DefinitionStatus
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyTemplate]
    execution: _execution_contract_pb2.ExecutionContract
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_function_pb2.FunctionType, str]] = ..., group: _Optional[_Union[FunctionGroup, str]] = ..., revision: _Optional[int] = ..., status: _Optional[_Union[_definition_status_pb2.DefinitionStatus, str]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyTemplate, _Mapping]]] = ..., execution: _Optional[_Union[_execution_contract_pb2.ExecutionContract, _Mapping]] = ...) -> None: ...

class FunctionDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FunctionDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[FunctionDefinition, _Mapping]]] = ...) -> None: ...
