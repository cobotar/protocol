from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssistanceSemantic(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSISTANCE_SEMANTIC_UNSPECIFIED: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_LOCATE_ENTITY: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_DIRECT_ATTENTION: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_SHOW_TARGET_POSITION: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_SHOW_TARGET_ORIENTATION: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_SUPPORT_ALIGNMENT: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_COMMUNICATE_ACTION: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_COMMUNICATE_CONSTRAINT: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_COMMUNICATE_EXCEPTION: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_COMMUNICATE_VARIANT: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_REQUEST_ACKNOWLEDGEMENT: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_VERIFY_STATE: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_ESTABLISH_COMPLETION: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_PRESENT_ACTION: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_COMMUNICATE_ACTION_CONSEQUENCE: _ClassVar[AssistanceSemantic]
    ASSISTANCE_SEMANTIC_PROTECT_ACTION: _ClassVar[AssistanceSemantic]

class SemanticSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEMANTIC_SOURCE_TYPE_UNSPECIFIED: _ClassVar[SemanticSourceType]
    SEMANTIC_SOURCE_TYPE_ACTION: _ClassVar[SemanticSourceType]
    SEMANTIC_SOURCE_TYPE_SUBJECT: _ClassVar[SemanticSourceType]
    SEMANTIC_SOURCE_TYPE_SUBJECT_LABEL: _ClassVar[SemanticSourceType]
    SEMANTIC_SOURCE_TYPE_SUBJECT_GEOMETRY: _ClassVar[SemanticSourceType]
    SEMANTIC_SOURCE_TYPE_CURRENT_POSE: _ClassVar[SemanticSourceType]
    SEMANTIC_SOURCE_TYPE_TARGET_POSE: _ClassVar[SemanticSourceType]
    SEMANTIC_SOURCE_TYPE_CONSTRAINT: _ClassVar[SemanticSourceType]
    SEMANTIC_SOURCE_TYPE_COMPLETION_CRITERION: _ClassVar[SemanticSourceType]
    SEMANTIC_SOURCE_TYPE_VARIANT_CONTEXT: _ClassVar[SemanticSourceType]
    SEMANTIC_SOURCE_TYPE_PROCESS_TRANSITION: _ClassVar[SemanticSourceType]

class SemanticValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEMANTIC_VALUE_TYPE_UNSPECIFIED: _ClassVar[SemanticValueType]
    SEMANTIC_VALUE_TYPE_ENTITY: _ClassVar[SemanticValueType]
    SEMANTIC_VALUE_TYPE_FACT: _ClassVar[SemanticValueType]
    SEMANTIC_VALUE_TYPE_ACTION: _ClassVar[SemanticValueType]
    SEMANTIC_VALUE_TYPE_SPATIAL_ANCHOR: _ClassVar[SemanticValueType]
    SEMANTIC_VALUE_TYPE_POSE: _ClassVar[SemanticValueType]
    SEMANTIC_VALUE_TYPE_GEOMETRY: _ClassVar[SemanticValueType]
    SEMANTIC_VALUE_TYPE_PATH: _ClassVar[SemanticValueType]
    SEMANTIC_VALUE_TYPE_REGION: _ClassVar[SemanticValueType]
    SEMANTIC_VALUE_TYPE_PROCESS_TRANSITION: _ClassVar[SemanticValueType]
ASSISTANCE_SEMANTIC_UNSPECIFIED: AssistanceSemantic
ASSISTANCE_SEMANTIC_LOCATE_ENTITY: AssistanceSemantic
ASSISTANCE_SEMANTIC_DIRECT_ATTENTION: AssistanceSemantic
ASSISTANCE_SEMANTIC_SHOW_TARGET_POSITION: AssistanceSemantic
ASSISTANCE_SEMANTIC_SHOW_TARGET_ORIENTATION: AssistanceSemantic
ASSISTANCE_SEMANTIC_SUPPORT_ALIGNMENT: AssistanceSemantic
ASSISTANCE_SEMANTIC_COMMUNICATE_ACTION: AssistanceSemantic
ASSISTANCE_SEMANTIC_COMMUNICATE_CONSTRAINT: AssistanceSemantic
ASSISTANCE_SEMANTIC_COMMUNICATE_EXCEPTION: AssistanceSemantic
ASSISTANCE_SEMANTIC_COMMUNICATE_VARIANT: AssistanceSemantic
ASSISTANCE_SEMANTIC_REQUEST_ACKNOWLEDGEMENT: AssistanceSemantic
ASSISTANCE_SEMANTIC_VERIFY_STATE: AssistanceSemantic
ASSISTANCE_SEMANTIC_ESTABLISH_COMPLETION: AssistanceSemantic
ASSISTANCE_SEMANTIC_PRESENT_ACTION: AssistanceSemantic
ASSISTANCE_SEMANTIC_COMMUNICATE_ACTION_CONSEQUENCE: AssistanceSemantic
ASSISTANCE_SEMANTIC_PROTECT_ACTION: AssistanceSemantic
SEMANTIC_SOURCE_TYPE_UNSPECIFIED: SemanticSourceType
SEMANTIC_SOURCE_TYPE_ACTION: SemanticSourceType
SEMANTIC_SOURCE_TYPE_SUBJECT: SemanticSourceType
SEMANTIC_SOURCE_TYPE_SUBJECT_LABEL: SemanticSourceType
SEMANTIC_SOURCE_TYPE_SUBJECT_GEOMETRY: SemanticSourceType
SEMANTIC_SOURCE_TYPE_CURRENT_POSE: SemanticSourceType
SEMANTIC_SOURCE_TYPE_TARGET_POSE: SemanticSourceType
SEMANTIC_SOURCE_TYPE_CONSTRAINT: SemanticSourceType
SEMANTIC_SOURCE_TYPE_COMPLETION_CRITERION: SemanticSourceType
SEMANTIC_SOURCE_TYPE_VARIANT_CONTEXT: SemanticSourceType
SEMANTIC_SOURCE_TYPE_PROCESS_TRANSITION: SemanticSourceType
SEMANTIC_VALUE_TYPE_UNSPECIFIED: SemanticValueType
SEMANTIC_VALUE_TYPE_ENTITY: SemanticValueType
SEMANTIC_VALUE_TYPE_FACT: SemanticValueType
SEMANTIC_VALUE_TYPE_ACTION: SemanticValueType
SEMANTIC_VALUE_TYPE_SPATIAL_ANCHOR: SemanticValueType
SEMANTIC_VALUE_TYPE_POSE: SemanticValueType
SEMANTIC_VALUE_TYPE_GEOMETRY: SemanticValueType
SEMANTIC_VALUE_TYPE_PATH: SemanticValueType
SEMANTIC_VALUE_TYPE_REGION: SemanticValueType
SEMANTIC_VALUE_TYPE_PROCESS_TRANSITION: SemanticValueType

class SemanticSourceRequirement(_message.Message):
    __slots__ = ("source", "value_type", "optional")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    source: SemanticSourceType
    value_type: SemanticValueType
    optional: bool
    def __init__(self, source: _Optional[_Union[SemanticSourceType, str]] = ..., value_type: _Optional[_Union[SemanticValueType, str]] = ..., optional: bool = ...) -> None: ...
