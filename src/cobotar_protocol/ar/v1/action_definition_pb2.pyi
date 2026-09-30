from ar.v1 import action_pb2 as _action_pb2
from ar.v1 import definition_status_pb2 as _definition_status_pb2
from ar.v1 import execution_contract_pb2 as _execution_contract_pb2
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

class ActionGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_GROUP_UNSPECIFIED: _ClassVar[ActionGroup]
    ACTION_GROUP_GENERAL: _ClassVar[ActionGroup]
    ACTION_GROUP_ROBOT: _ClassVar[ActionGroup]
    ACTION_GROUP_TASK: _ClassVar[ActionGroup]
ACTION_GROUP_UNSPECIFIED: ActionGroup
ACTION_GROUP_GENERAL: ActionGroup
ACTION_GROUP_ROBOT: ActionGroup
ACTION_GROUP_TASK: ActionGroup

class ActionDefinition(_message.Message):
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
    type: _action_pb2.ActionType
    group: ActionGroup
    revision: int
    status: _definition_status_pb2.DefinitionStatus
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyTemplate]
    execution: _execution_contract_pb2.ExecutionContract
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_action_pb2.ActionType, str]] = ..., group: _Optional[_Union[ActionGroup, str]] = ..., revision: _Optional[int] = ..., status: _Optional[_Union[_definition_status_pb2.DefinitionStatus, str]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyTemplate, _Mapping]]] = ..., execution: _Optional[_Union[_execution_contract_pb2.ExecutionContract, _Mapping]] = ...) -> None: ...

class ActionDefinitions(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ActionDefinition]
    def __init__(self, items: _Optional[_Iterable[_Union[ActionDefinition, _Mapping]]] = ...) -> None: ...
