from assembly.v1 import execution_pb2 as _execution_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessLoadFailure(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESS_LOAD_FAILURE_UNSPECIFIED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_LINE_NOT_FOUND: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_PROCESS_RECIPE_NOT_FOUND: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_PRODUCT_NOT_SUPPORTED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_RESOURCE_STATE_UNKNOWN: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_NO_COMPATIBLE_FIXTURE: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_MISSING_TOOL_ROLE: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_TOOL_NOT_CALIBRATED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_TOOL_CAPABILITY_INSUFFICIENT: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_ROBOT_UNAVAILABLE: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_ROBOT_TOOLING_MISMATCH: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_NO_QUALIFIED_OPERATOR: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_REQUIRED_SKILL_EXPIRED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_NO_FEASIBLE_ACTOR: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_COLLABORATION_MODE_UNSUPPORTED: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_SAFETY_MODE_MISMATCH: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_VISION_ASSET_UNAVAILABLE: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_VALIDATION_SOURCE_MISSING: _ClassVar[ProcessLoadFailure]
    PROCESS_LOAD_FAILURE_NO_FEASIBLE_VALIDATION_METHOD: _ClassVar[ProcessLoadFailure]

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
PROCESS_LOAD_FAILURE_UNSPECIFIED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_LINE_NOT_FOUND: ProcessLoadFailure
PROCESS_LOAD_FAILURE_PROCESS_RECIPE_NOT_FOUND: ProcessLoadFailure
PROCESS_LOAD_FAILURE_PRODUCT_NOT_SUPPORTED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_RESOURCE_STATE_UNKNOWN: ProcessLoadFailure
PROCESS_LOAD_FAILURE_NO_COMPATIBLE_FIXTURE: ProcessLoadFailure
PROCESS_LOAD_FAILURE_MISSING_TOOL_ROLE: ProcessLoadFailure
PROCESS_LOAD_FAILURE_TOOL_NOT_CALIBRATED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_TOOL_CAPABILITY_INSUFFICIENT: ProcessLoadFailure
PROCESS_LOAD_FAILURE_ROBOT_UNAVAILABLE: ProcessLoadFailure
PROCESS_LOAD_FAILURE_ROBOT_TOOLING_MISMATCH: ProcessLoadFailure
PROCESS_LOAD_FAILURE_NO_QUALIFIED_OPERATOR: ProcessLoadFailure
PROCESS_LOAD_FAILURE_REQUIRED_SKILL_EXPIRED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_NO_FEASIBLE_ACTOR: ProcessLoadFailure
PROCESS_LOAD_FAILURE_COLLABORATION_MODE_UNSUPPORTED: ProcessLoadFailure
PROCESS_LOAD_FAILURE_SAFETY_MODE_MISMATCH: ProcessLoadFailure
PROCESS_LOAD_FAILURE_VISION_ASSET_UNAVAILABLE: ProcessLoadFailure
PROCESS_LOAD_FAILURE_VALIDATION_SOURCE_MISSING: ProcessLoadFailure
PROCESS_LOAD_FAILURE_NO_FEASIBLE_VALIDATION_METHOD: ProcessLoadFailure
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
    __slots__ = ("process_recipe_id", "target_line_id", "dry_run")
    PROCESS_RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_LINE_ID_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    process_recipe_id: str
    target_line_id: str
    dry_run: bool
    def __init__(self, process_recipe_id: _Optional[str] = ..., target_line_id: _Optional[str] = ..., dry_run: bool = ...) -> None: ...

class ProcessRunIssue(_message.Message):
    __slots__ = ("failure", "message", "severity", "process_recipe_id", "sequence_definition_id", "task_definition_id", "required_tool_role", "required_skill_id", "fixture_definition_id", "station_id", "actor_id", "resource_id", "remediation", "importance")
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    PROCESS_RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_TOOL_ROLE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    FIXTURE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
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
    station_id: str
    actor_id: str
    resource_id: str
    remediation: str
    importance: RequirementImportance
    def __init__(self, failure: _Optional[_Union[ProcessLoadFailure, str]] = ..., message: _Optional[str] = ..., severity: _Optional[_Union[ProcessRunIssueSeverity, str]] = ..., process_recipe_id: _Optional[str] = ..., sequence_definition_id: _Optional[str] = ..., task_definition_id: _Optional[str] = ..., required_tool_role: _Optional[str] = ..., required_skill_id: _Optional[str] = ..., fixture_definition_id: _Optional[str] = ..., station_id: _Optional[str] = ..., actor_id: _Optional[str] = ..., resource_id: _Optional[str] = ..., remediation: _Optional[str] = ..., importance: _Optional[_Union[RequirementImportance, str]] = ...) -> None: ...

class TaskFeasibility(_message.Message):
    __slots__ = ("task_definition_id", "feasible", "candidate_actor_ids", "candidate_tool_instance_ids", "candidate_fixture_instance_ids", "candidate_asset_instance_ids", "issues")
    TASK_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    FEASIBLE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_ACTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_TOOL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FIXTURE_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_ASSET_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    task_definition_id: str
    feasible: bool
    candidate_actor_ids: _containers.RepeatedScalarFieldContainer[str]
    candidate_tool_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    candidate_fixture_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    candidate_asset_instance_ids: _containers.RepeatedScalarFieldContainer[str]
    issues: _containers.RepeatedCompositeFieldContainer[ProcessRunIssue]
    def __init__(self, task_definition_id: _Optional[str] = ..., feasible: bool = ..., candidate_actor_ids: _Optional[_Iterable[str]] = ..., candidate_tool_instance_ids: _Optional[_Iterable[str]] = ..., candidate_fixture_instance_ids: _Optional[_Iterable[str]] = ..., candidate_asset_instance_ids: _Optional[_Iterable[str]] = ..., issues: _Optional[_Iterable[_Union[ProcessRunIssue, _Mapping]]] = ...) -> None: ...

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
    process_run: _execution_pb2.ProcessRun
    def __init__(self, status: _Optional[_Union[ProcessLoadStatus, str]] = ..., precheck: _Optional[_Union[ProcessRunPrecheckResult, _Mapping]] = ..., process_run: _Optional[_Union[_execution_pb2.ProcessRun, _Mapping]] = ...) -> None: ...
