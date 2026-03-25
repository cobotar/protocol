from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import custom_properties_pb2 as _custom_properties_pb2
from geometry.v1 import pose_pb2 as _pose_pb2
from geometry.v1 import vector3_pb2 as _vector3_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from variance.v1 import variant_rule_pb2 as _variant_rule_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_KIND_UNSPECIFIED: _ClassVar[NodeKind]
    NODE_KIND_GROUP: _ClassVar[NodeKind]
    NODE_KIND_PART_OCCURRENCE: _ClassVar[NodeKind]
    NODE_KIND_SUBASSEMBLY_OCCURRENCE: _ClassVar[NodeKind]
    NODE_KIND_PATTERN: _ClassVar[NodeKind]

class JoinMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOIN_METHOD_UNSPECIFIED: _ClassVar[JoinMethod]
    JOIN_METHOD_NONE: _ClassVar[JoinMethod]
    JOIN_METHOD_FASTEN: _ClassVar[JoinMethod]
    JOIN_METHOD_PRESS_FIT: _ClassVar[JoinMethod]
    JOIN_METHOD_SNAP_FIT: _ClassVar[JoinMethod]
    JOIN_METHOD_ADHESIVE: _ClassVar[JoinMethod]
    JOIN_METHOD_WELD: _ClassVar[JoinMethod]
    JOIN_METHOD_PLACE: _ClassVar[JoinMethod]
NODE_KIND_UNSPECIFIED: NodeKind
NODE_KIND_GROUP: NodeKind
NODE_KIND_PART_OCCURRENCE: NodeKind
NODE_KIND_SUBASSEMBLY_OCCURRENCE: NodeKind
NODE_KIND_PATTERN: NodeKind
JOIN_METHOD_UNSPECIFIED: JoinMethod
JOIN_METHOD_NONE: JoinMethod
JOIN_METHOD_FASTEN: JoinMethod
JOIN_METHOD_PRESS_FIT: JoinMethod
JOIN_METHOD_SNAP_FIT: JoinMethod
JOIN_METHOD_ADHESIVE: JoinMethod
JOIN_METHOD_WELD: JoinMethod
JOIN_METHOD_PLACE: JoinMethod

class AssemblyNode(_message.Message):
    __slots__ = ("id", "name", "parent_node_id", "kind", "part_definition_id", "override_model_id", "local_pose", "sequence_hint", "cad_occurrence_path", "join_method_hint", "insertion_offset_hint", "approach_offset_hint", "optional", "applicability", "custom")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    PART_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_POSE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_HINT_FIELD_NUMBER: _ClassVar[int]
    CAD_OCCURRENCE_PATH_FIELD_NUMBER: _ClassVar[int]
    JOIN_METHOD_HINT_FIELD_NUMBER: _ClassVar[int]
    INSERTION_OFFSET_HINT_FIELD_NUMBER: _ClassVar[int]
    APPROACH_OFFSET_HINT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    APPLICABILITY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    parent_node_id: str
    kind: NodeKind
    part_definition_id: str
    override_model_id: str
    local_pose: _pose_pb2.Pose
    sequence_hint: int
    cad_occurrence_path: str
    join_method_hint: JoinMethod
    insertion_offset_hint: _vector3_pb2.Vector3
    approach_offset_hint: _vector3_pb2.Vector3
    optional: bool
    applicability: _containers.RepeatedCompositeFieldContainer[_variant_rule_pb2.VariantRule]
    custom: _custom_properties_pb2.CustomProperties
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., parent_node_id: _Optional[str] = ..., kind: _Optional[_Union[NodeKind, str]] = ..., part_definition_id: _Optional[str] = ..., override_model_id: _Optional[str] = ..., local_pose: _Optional[_Union[_pose_pb2.Pose, _Mapping]] = ..., sequence_hint: _Optional[int] = ..., cad_occurrence_path: _Optional[str] = ..., join_method_hint: _Optional[_Union[JoinMethod, str]] = ..., insertion_offset_hint: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., approach_offset_hint: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., optional: bool = ..., applicability: _Optional[_Iterable[_Union[_variant_rule_pb2.VariantRule, _Mapping]]] = ..., custom: _Optional[_Union[_custom_properties_pb2.CustomProperties, _Mapping]] = ...) -> None: ...
