from buf.validate import validate_pb2 as _validate_pb2
from common.v1 import actor_pb2 as _actor_pb2
from common.v1 import key_value_constraint_pb2 as _key_value_constraint_pb2
from runtime.v1 import process_run_pb2 as _process_run_pb2
from runtime.v1 import runtime_restriction_pb2 as _runtime_restriction_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from variance.v1 import variant_configuration_pb2 as _variant_configuration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessLoadStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESS_LOAD_STRATEGY_UNSPECIFIED: _ClassVar[ProcessLoadStrategy]
    PROCESS_LOAD_STRATEGY_FIRST_FEASIBLE: _ClassVar[ProcessLoadStrategy]
    PROCESS_LOAD_STRATEGY_PREFER_AVAILABLE: _ClassVar[ProcessLoadStrategy]
    PROCESS_LOAD_STRATEGY_PREFER_TARGET_SCOPE: _ClassVar[ProcessLoadStrategy]
    PROCESS_LOAD_STRATEGY_BEST_MATCH: _ClassVar[ProcessLoadStrategy]

class ProcessLoadFailure(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESS_LOAD_FAILURE_UNSPECIFIED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_PROCESS_RECIPE_NOT_FOUND: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_PRODUCT_NOT_SUPPORTED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_RESOURCE_STATE_UNKNOWN: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_NO_COMPATIBLE_CONTAINER: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_REQUIRED_SLOT_NOT_FOUND: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_REQUIRED_SLOT_TYPE_NOT_FOUND: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_MISSING_TOOL_ROLE: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_TOOL_NOT_CALIBRATED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_TOOL_CAPABILITY_INSUFFICIENT: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_ROBOT_UNAVAILABLE: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_ROBOT_TOOLING_MISMATCH: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_NO_QUALIFIED_OPERATOR: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_NO_FEASIBLE_ACTOR: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_REQUIRED_SKILL_RESTRICTED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_REQUIRED_SKILL_EXPIRED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_COLLABORATION_MODE_UNSUPPORTED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_SAFETY_MODE_MISMATCH: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_VISION_ASSET_UNAVAILABLE: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_VALIDATION_SOURCE_MISSING: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_NO_FEASIBLE_VALIDATION_METHOD: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_LINE_NOT_FOUND: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_LINE_CLOSED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_LINE_BUSY: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_LINE_BLOCKED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_CELL_NOT_FOUND: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_CELL_CLOSED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_CELL_BUSY: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_CELL_BLOCKED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_STATION_NOT_FOUND: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_STATION_CLOSED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_STATION_BUSY: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_STATION_BLOCKED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_REQUIRED_PART_NOT_PRESENT: _ClassVar[ProcessLoadFailure]

class ProcessRunIssueSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESS_RUN_ISSUE_SEVERITY_UNSPECIFIED: _ClassVar[ProcessRunIssueSeverity]
    PROCESS_RUN_ISSUE_SEVERITY_BLOCKING: _ClassVar[ProcessRunIssueSeverity]
    PROCESS_RUN_ISSUE_SEVERITY_WARNING: _ClassVar[ProcessRunIssueSeverity]

class RequirementImportance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REQUIREMENT_IMPORTANCE_UNSPECIFIED: _ClassVar[RequirementImportance]
    REQUIREMENT_IMPORTANCE_REQUIRED: _ClassVar[RequirementImportance]
    REQUIREMENT_IMPORTANCE_PREFERRED: _ClassVar[RequirementImportance]

class ProcessRunPrecheckStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESS_RUN_PRECHECK_STATUS_UNSPECIFIED: _ClassVar[ProcessRunPrecheckStatus]
    PROCESS_RUN_PRECHECK_STATUS_OK: _ClassVar[ProcessRunPrecheckStatus]
    PROCESS_RUN_PRECHECK_STATUS_OK_WITH_WARNINGS: _ClassVar[ProcessRunPrecheckStatus]
    PROCESS_RUN_PRECHECK_STATUS_BLOCKED: _ClassVar[ProcessRunPrecheckStatus]

class ProcessLoadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESS_LOAD_STATUS_UNSPECIFIED: _ClassVar[ProcessLoadStatus]
    PROCESS_LOAD_STATUS_PRECHECK_FAILED: _ClassVar[ProcessLoadStatus]
    PROCESS_LOAD_STATUS_READY: _ClassVar[ProcessLoadStatus]
    PROCESS_LOAD_STATUS_LOADED: _ClassVar[ProcessLoadStatus]
PROCESS_LOAD_STRATEGY_UNSPECIFIED: ProcessLoadStrategy
PROCESS_LOAD_STRATEGY_FIRST_FEASIBLE: ProcessLoadStrategy
PROCESS_LOAD_STRATEGY_PREFER_AVAILABLE: ProcessLoadStrategy
PROCESS_LOAD_STRATEGY_PREFER_TARGET_SCOPE: ProcessLoadStrategy
PROCESS_LOAD_STRATEGY_BEST_MATCH: ProcessLoadStrategy
PROCESS_LOAD_FAILURE_UNSPECIFIED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_PROCESS_RECIPE_NOT_FOUND: ProcessLoadFailure
PROCESS_LOAD_FAILURE_PRODUCT_NOT_SUPPORTED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_RESOURCE_STATE_UNKNOWN: ProcessLoadFailure
PROCESS_LOAD_FAILURE_NO_COMPATIBLE_CONTAINER: ProcessLoadFailure
PROCESS_LOAD_FAILURE_REQUIRED_SLOT_NOT_FOUND: ProcessLoadFailure
PROCESS_LOAD_FAILURE_REQUIRED_SLOT_TYPE_NOT_FOUND: ProcessLoadFailure
PROCESS_LOAD_FAILURE_MISSING_TOOL_ROLE: ProcessLoadFailure
PROCESS_LOAD_FAILURE_TOOL_NOT_CALIBRATED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_TOOL_CAPABILITY_INSUFFICIENT: ProcessLoadFailure
PROCESS_LOAD_FAILURE_ROBOT_UNAVAILABLE: ProcessLoadFailure
PROCESS_LOAD_FAILURE_ROBOT_TOOLING_MISMATCH: ProcessLoadFailure
PROCESS_LOAD_FAILURE_NO_QUALIFIED_OPERATOR: ProcessLoadFailure
PROCESS_LOAD_FAILURE_NO_FEASIBLE_ACTOR: ProcessLoadFailure
PROCESS_LOAD_FAILURE_REQUIRED_SKILL_RESTRICTED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_REQUIRED_SKILL_EXPIRED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_COLLABORATION_MODE_UNSUPPORTED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_SAFETY_MODE_MISMATCH: ProcessLoadFailure
PROCESS_LOAD_FAILURE_VISION_ASSET_UNAVAILABLE: ProcessLoadFailure
PROCESS_LOAD_FAILURE_VALIDATION_SOURCE_MISSING: ProcessLoadFailure
PROCESS_LOAD_FAILURE_NO_FEASIBLE_VALIDATION_METHOD: ProcessLoadFailure
PROCESS_LOAD_FAILURE_LINE_NOT_FOUND: ProcessLoadFailure
PROCESS_LOAD_FAILURE_LINE_CLOSED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_LINE_BUSY: ProcessLoadFailure
PROCESS_LOAD_FAILURE_LINE_BLOCKED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_CELL_NOT_FOUND: ProcessLoadFailure
PROCESS_LOAD_FAILURE_CELL_CLOSED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_CELL_BUSY: ProcessLoadFailure
PROCESS_LOAD_FAILURE_CELL_BLOCKED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_STATION_NOT_FOUND: ProcessLoadFailure
PROCESS_LOAD_FAILURE_STATION_CLOSED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_STATION_BUSY: ProcessLoadFailure
PROCESS_LOAD_FAILURE_STATION_BLOCKED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_REQUIRED_PART_NOT_PRESENT: ProcessLoadFailure
PROCESS_RUN_ISSUE_SEVERITY_UNSPECIFIED: ProcessRunIssueSeverity
PROCESS_RUN_ISSUE_SEVERITY_BLOCKING: ProcessRunIssueSeverity
PROCESS_RUN_ISSUE_SEVERITY_WARNING: ProcessRunIssueSeverity
REQUIREMENT_IMPORTANCE_UNSPECIFIED: RequirementImportance
REQUIREMENT_IMPORTANCE_REQUIRED: RequirementImportance
REQUIREMENT_IMPORTANCE_PREFERRED: RequirementImportance
PROCESS_RUN_PRECHECK_STATUS_UNSPECIFIED: ProcessRunPrecheckStatus
PROCESS_RUN_PRECHECK_STATUS_OK: ProcessRunPrecheckStatus
PROCESS_RUN_PRECHECK_STATUS_OK_WITH_WARNINGS: ProcessRunPrecheckStatus
PROCESS_RUN_PRECHECK_STATUS_BLOCKED: ProcessRunPrecheckStatus
PROCESS_LOAD_STATUS_UNSPECIFIED: ProcessLoadStatus
PROCESS_LOAD_STATUS_PRECHECK_FAILED: ProcessLoadStatus
PROCESS_LOAD_STATUS_READY: ProcessLoadStatus
PROCESS_LOAD_STATUS_LOADED: ProcessLoadStatus

class ProcessLoadRequest(_message.Message):
    __slots__ = ("process_recipe_id", "target_line_id", "target_cell_id", "target_station_id", "variant_configuration", "dry_run", "queue_if_occupied", "strategy", "order_id", "parameters")
    PROCESS_RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_LINE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CELL_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_STATION_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    QUEUE_IF_OCCUPIED_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    process_recipe_id: str
    target_line_id: str
    target_cell_id: str
    target_station_id: str
    variant_configuration: _variant_configuration_pb2.VariantConfiguration
    dry_run: bool
    queue_if_occupied: bool
    strategy: ProcessLoadStrategy
    order_id: str
    parameters: _containers.RepeatedCompositeFieldContainer[_key_value_constraint_pb2.KeyValueConstraint]
    def __init__(self, process_recipe_id: _Optional[str] = ..., target_line_id: _Optional[str] = ..., target_cell_id: _Optional[str] = ..., target_station_id: _Optional[str] = ..., variant_configuration: _Optional[_Union[_variant_configuration_pb2.VariantConfiguration, _Mapping]] = ..., dry_run: bool = ..., queue_if_occupied: bool = ..., strategy: _Optional[_Union[ProcessLoadStrategy, str]] = ..., order_id: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[_key_value_constraint_pb2.KeyValueConstraint, _Mapping]]] = ...) -> None: ...

class ProcessRunIssue(_message.Message):
    __slots__ = ("failure", "message", "severity", "process_recipe_id", "sequence_definition_id", "task_definition_id", "required_tool_role", "required_skill_id", "fixture_definition_id", "cell_id", "station_id", "actor_id", "resource_id", "remediation", "importance")
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    PROCESS_RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_TOOL_ROLE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    FIXTURE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    failure: ProcessLoadFailure
    message: str
    severity: ProcessRunIssueSeverity
    process_recipe_id: str
    sequence_definition_id: str
    task_definition_id: str
    required_tool_role: str
    required_skill_id: str
    fixture_definition_id: str
    cell_id: str
    station_id: str
    actor_id: str
    resource_id: str
    remediation: str
    importance: RequirementImportance
    def __init__(self, failure: _Optional[_Union[ProcessLoadFailure, str]] = ..., message: _Optional[str] = ..., severity: _Optional[_Union[ProcessRunIssueSeverity, str]] = ..., process_recipe_id: _Optional[str] = ..., sequence_definition_id: _Optional[str] = ..., task_definition_id: _Optional[str] = ..., required_tool_role: _Optional[str] = ..., required_skill_id: _Optional[str] = ..., fixture_definition_id: _Optional[str] = ..., cell_id: _Optional[str] = ..., station_id: _Optional[str] = ..., actor_id: _Optional[str] = ..., resource_id: _Optional[str] = ..., remediation: _Optional[str] = ..., importance: _Optional[_Union[RequirementImportance, str]] = ...) -> None: ...

class CandidateActorEvaluation(_message.Message):
    __slots__ = ("actor", "feasible", "restrictions", "issues")
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    FEASIBLE_FIELD_NUMBER: _ClassVar[int]
    RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    actor: _actor_pb2.ActorRef
    feasible: bool
    restrictions: _containers.RepeatedCompositeFieldContainer[_runtime_restriction_pb2.RuntimeRestriction]
    issues: _containers.RepeatedCompositeFieldContainer[ProcessRunIssue]
    def __init__(self, actor: _Optional[_Union[_actor_pb2.ActorRef, _Mapping]] = ..., feasible: bool = ..., restrictions: _Optional[_Iterable[_Union[_runtime_restriction_pb2.RuntimeRestriction, _Mapping]]] = ..., issues: _Optional[_Iterable[_Union[ProcessRunIssue, _Mapping]]] = ...) -> None: ...

class TaskFeasibility(_message.Message):
    __slots__ = ("task_definition_id", "feasible", "candidate_actors", "candidate_robot_instance_ids", "candidate_tool_instance_ids", "candidate_container_instance_ids", "candidate_asset_instance_ids", "candidate_part_instance_ids", "issues", "candidate_actor_evaluations")
    TASK_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    FEASIBLE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_ACTORS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_ROBOT_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_TOOL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_CONTAINER_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_ASSET_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_PART_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_ACTOR_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    task_definition_id: str
    feasible: bool
    candidate_actors: _containers.RepeatedCompositeFieldContainer[_actor_pb2.ActorRef]
    candidate_robot_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    candidate_tool_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    candidate_container_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    candidate_asset_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    candidate_part_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    issues: _containers.RepeatedCompositeFieldContainer[ProcessRunIssue]
    candidate_actor_evaluations: _containers.RepeatedCompositeFieldContainer[CandidateActorEvaluation]
    def __init__(self, task_definition_id: _Optional[str] = ..., feasible: bool = ..., candidate_actors: _Optional[_Iterable[_Union[_actor_pb2.ActorRef, _Mapping]]] = ..., candidate_robot_instance_ids: _Optional[_Iterable[str]] = ..., candidate_tool_instance_ids: _Optional[_Iterable[str]] = ..., candidate_container_instance_ids: _Optional[_Iterable[str]] = ..., candidate_asset_instance_ids: _Optional[_Iterable[str]] = ..., candidate_part_instance_ids: _Optional[_Iterable[str]] = ..., issues: _Optional[_Iterable[_Union[ProcessRunIssue, _Mapping]]] = ..., candidate_actor_evaluations: _Optional[_Iterable[_Union[CandidateActorEvaluation, _Mapping]]] = ...) -> None: ...

class ProcessRunPrecheckResult(_message.Message):
    __slots__ = ("ok", "issues", "blocking_issue_count", "warning_issue_count", "process_recipe_id", "target_line_id", "task_feasibility", "status")
    OK_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_ISSUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    WARNING_ISSUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROCESS_RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_LINE_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_FEASIBILITY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    issues: _containers.RepeatedCompositeFieldContainer[ProcessRunIssue]
    blocking_issue_count: int
    warning_issue_count: int
    process_recipe_id: str
    target_line_id: str
    task_feasibility: _containers.RepeatedCompositeFieldContainer[TaskFeasibility]
    status: ProcessRunPrecheckStatus
    def __init__(self, ok: bool = ..., issues: _Optional[_Iterable[_Union[ProcessRunIssue, _Mapping]]] = ..., blocking_issue_count: _Optional[int] = ..., warning_issue_count: _Optional[int] = ..., process_recipe_id: _Optional[str] = ..., target_line_id: _Optional[str] = ..., task_feasibility: _Optional[_Iterable[_Union[TaskFeasibility, _Mapping]]] = ..., status: _Optional[_Union[ProcessRunPrecheckStatus, str]] = ...) -> None: ...

class ProcessLoadResult(_message.Message):
    __slots__ = ("status", "precheck", "process_run")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRECHECK_FIELD_NUMBER: _ClassVar[int]
    PROCESS_RUN_FIELD_NUMBER: _ClassVar[int]
    status: ProcessLoadStatus
    precheck: ProcessRunPrecheckResult
    process_run: _process_run_pb2.ProcessRun
    def __init__(self, status: _Optional[_Union[ProcessLoadStatus, str]] = ..., precheck: _Optional[_Union[ProcessRunPrecheckResult, _Mapping]] = ..., process_run: _Optional[_Union[_process_run_pb2.ProcessRun, _Mapping]] = ...) -> None: ...
