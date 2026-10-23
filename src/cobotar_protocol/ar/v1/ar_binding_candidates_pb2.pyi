from cobotar_protocol.ar.v1 import ar_config_binding_pb2 as _ar_config_binding_pb2
from buf.validate import validate_pb2 as _validate_pb2
from cobotar_protocol.resources.v1 import resource_requirement_pb2 as _resource_requirement_pb2
from cobotar_protocol.validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ARBindingCandidatesRequest(_message.Message):
    __slots__ = ("ar_config_id", "slot_id", "robot_instance_ids", "asset_instance_ids")
    AR_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    ROBOT_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    ASSET_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    ar_config_id: str
    slot_id: str
    robot_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    asset_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ar_config_id: _Optional[str] = ..., slot_id: _Optional[str] = ..., robot_instance_ids: _Optional[_Iterable[str]] = ..., asset_instance_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ARResourceRequirementUsage(_message.Message):
    __slots__ = ("requirement", "consumers")
    REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    requirement: _resource_requirement_pb2.ResourceRequirement
    consumers: _containers.RepeatedCompositeFieldContainer[_ar_config_binding_pb2.ARResourceRequirementConsumer]
    def __init__(self, requirement: _Optional[_Union[_resource_requirement_pb2.ResourceRequirement, _Mapping]] = ..., consumers: _Optional[_Iterable[_Union[_ar_config_binding_pb2.ARResourceRequirementConsumer, _Mapping]]] = ...) -> None: ...

class ARBindingCandidate(_message.Message):
    __slots__ = ("robot_instance_id", "asset_instance_id", "status", "unmet_requirements", "unverified_requirements", "bindable")
    ROBOT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNMET_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    UNVERIFIED_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    BINDABLE_FIELD_NUMBER: _ClassVar[int]
    robot_instance_id: str
    asset_instance_id: str
    status: _ar_config_binding_pb2.ARResourceBindingStatus
    unmet_requirements: _containers.RepeatedCompositeFieldContainer[_ar_config_binding_pb2.ARUnmetResourceRequirement]
    unverified_requirements: _containers.RepeatedCompositeFieldContainer[ARResourceRequirementUsage]
    bindable: bool
    def __init__(self, robot_instance_id: _Optional[str] = ..., asset_instance_id: _Optional[str] = ..., status: _Optional[_Union[_ar_config_binding_pb2.ARResourceBindingStatus, str]] = ..., unmet_requirements: _Optional[_Iterable[_Union[_ar_config_binding_pb2.ARUnmetResourceRequirement, _Mapping]]] = ..., unverified_requirements: _Optional[_Iterable[_Union[ARResourceRequirementUsage, _Mapping]]] = ..., bindable: bool = ...) -> None: ...

class ARBindingCandidatesResponse(_message.Message):
    __slots__ = ("requirements", "candidates")
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    requirements: _containers.RepeatedCompositeFieldContainer[ARResourceRequirementUsage]
    candidates: _containers.RepeatedCompositeFieldContainer[ARBindingCandidate]
    def __init__(self, requirements: _Optional[_Iterable[_Union[ARResourceRequirementUsage, _Mapping]]] = ..., candidates: _Optional[_Iterable[_Union[ARBindingCandidate, _Mapping]]] = ...) -> None: ...
