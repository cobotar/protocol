# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [common/v1/color.proto](#common_v1_color-proto)
    - [Color](#common-v1-Color)
  
- [geometry/v1/anchor.proto](#geometry_v1_anchor-proto)
    - [Anchor](#geometry-v1-Anchor)
  
- [geometry/v1/point.proto](#geometry_v1_point-proto)
    - [Point](#geometry-v1-Point)
  
- [geometry/v1/quad.proto](#geometry_v1_quad-proto)
    - [Quad](#geometry-v1-Quad)
  
- [geometry/v1/pose.proto](#geometry_v1_pose-proto)
    - [LocalizedPose](#geometry-v1-LocalizedPose)
    - [Pose](#geometry-v1-Pose)
  
    - [LocalizedState](#geometry-v1-LocalizedState)
  
- [geometry/v1/vector3.proto](#geometry_v1_vector3-proto)
    - [Vector3](#geometry-v1-Vector3)
  
- [validation/v1/predefined_string_rules.proto](#validation_v1_predefined_string_rules-proto)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
    - [File-level Extensions](#validation_v1_predefined_string_rules-proto-extensions)
  
- [common/v1/property.proto](#common_v1_property-proto)
    - [AnchorExtras](#common-v1-AnchorExtras)
    - [ColorExtras](#common-v1-ColorExtras)
    - [EnumExtras](#common-v1-EnumExtras)
    - [EnumOption](#common-v1-EnumOption)
    - [NumberExtras](#common-v1-NumberExtras)
    - [PoseExtras](#common-v1-PoseExtras)
    - [Property](#common-v1-Property)
    - [PropertyMessages](#common-v1-PropertyMessages)
    - [PropertyValueUpdate](#common-v1-PropertyValueUpdate)
    - [Vector3Extras](#common-v1-Vector3Extras)
  
    - [PropertyGroup](#common-v1-PropertyGroup)
    - [PropertyOrigin](#common-v1-PropertyOrigin)
    - [PropertyPermission](#common-v1-PropertyPermission)
    - [PropertyType](#common-v1-PropertyType)
  
- [ar/v1/action.proto](#ar_v1_action-proto)
    - [ActionAddMessage](#ar-v1-ActionAddMessage)
    - [ActionCloneMessage](#ar-v1-ActionCloneMessage)
    - [ActionMessage](#ar-v1-ActionMessage)
    - [ActionMessages](#ar-v1-ActionMessages)
    - [ActionUpdateMessage](#ar-v1-ActionUpdateMessage)
  
    - [ActionType](#ar-v1-ActionType)
  
- [ar/v1/events.proto](#ar_v1_events-proto)
    - [ExchangeSupport](#ar-v1-ExchangeSupport)
    - [ExchangeType](#ar-v1-ExchangeType)
    - [HandlerRequirement](#ar-v1-HandlerRequirement)
    - [SupportedExchangesMessage](#ar-v1-SupportedExchangesMessage)
  
    - [CommandType](#ar-v1-CommandType)
    - [EventType](#ar-v1-EventType)
    - [HandlerCardinality](#ar-v1-HandlerCardinality)
    - [PlanType](#ar-v1-PlanType)
    - [TelemetryType](#ar-v1-TelemetryType)
  
- [ar/v1/action_info.proto](#ar_v1_action_info-proto)
    - [ActionInfoMessage](#ar-v1-ActionInfoMessage)
    - [ActionInfoMessages](#ar-v1-ActionInfoMessages)
  
    - [ActionGroup](#ar-v1-ActionGroup)
  
- [ar/v1/feedback.proto](#ar_v1_feedback-proto)
    - [FeedbackAddMessage](#ar-v1-FeedbackAddMessage)
    - [FeedbackCloneMessage](#ar-v1-FeedbackCloneMessage)
    - [FeedbackMessage](#ar-v1-FeedbackMessage)
    - [FeedbackMessages](#ar-v1-FeedbackMessages)
    - [FeedbackUpdateMessage](#ar-v1-FeedbackUpdateMessage)
  
    - [FeedbackType](#ar-v1-FeedbackType)
  
- [ar/v1/helper.proto](#ar_v1_helper-proto)
    - [HelperAddMessage](#ar-v1-HelperAddMessage)
    - [HelperMessage](#ar-v1-HelperMessage)
    - [HelperMessages](#ar-v1-HelperMessages)
    - [HelperUpdateMessage](#ar-v1-HelperUpdateMessage)
  
    - [HelperType](#ar-v1-HelperType)
  
- [ar/v1/ar_config.proto](#ar_v1_ar_config-proto)
    - [ARConfigInfoMessage](#ar-v1-ARConfigInfoMessage)
    - [ARConfigInfoMessages](#ar-v1-ARConfigInfoMessages)
    - [ARConfigMessage](#ar-v1-ARConfigMessage)
    - [ARConfigMessages](#ar-v1-ARConfigMessages)
  
- [ar/v1/config_load.proto](#ar_v1_config_load-proto)
    - [ConfigurationLoadMessage](#ar-v1-ConfigurationLoadMessage)
  
- [ar/v1/environment.proto](#ar_v1_environment-proto)
    - [AssetLocation](#ar-v1-AssetLocation)
    - [EnvironmentMessage](#ar-v1-EnvironmentMessage)
    - [EnvironmentMessages](#ar-v1-EnvironmentMessages)
    - [FixtureLocation](#ar-v1-FixtureLocation)
    - [MarkerLocation](#ar-v1-MarkerLocation)
    - [PartLocation](#ar-v1-PartLocation)
    - [RobotLocation](#ar-v1-RobotLocation)
    - [ToolLocation](#ar-v1-ToolLocation)
  
    - [EnvironmentType](#ar-v1-EnvironmentType)
  
- [ar/v1/feedback_info.proto](#ar_v1_feedback_info-proto)
    - [FeedbackInfoMessage](#ar-v1-FeedbackInfoMessage)
    - [FeedbackInfoMessages](#ar-v1-FeedbackInfoMessages)
  
    - [FeedbackGroup](#ar-v1-FeedbackGroup)
  
- [ar/v1/helper_info.proto](#ar_v1_helper_info-proto)
    - [HelperInfoMessage](#ar-v1-HelperInfoMessage)
    - [HelperInfoMessages](#ar-v1-HelperInfoMessages)
  
    - [HelperGroup](#ar-v1-HelperGroup)
  
- [ar/v1/mapping.proto](#ar_v1_mapping-proto)
    - [AssetMapping](#ar-v1-AssetMapping)
    - [MappingMessage](#ar-v1-MappingMessage)
    - [MappingMessages](#ar-v1-MappingMessages)
    - [RobotMapping](#ar-v1-RobotMapping)
  
- [common/v1/actor.proto](#common_v1_actor-proto)
    - [ActorRef](#common-v1-ActorRef)
  
    - [ActorKind](#common-v1-ActorKind)
  
- [common/v1/enums.proto](#common_v1_enums-proto)
    - [CollaborationMode](#common-v1-CollaborationMode)
    - [ResourceStatus](#common-v1-ResourceStatus)
    - [SafetyRelevance](#common-v1-SafetyRelevance)
  
- [common/v1/key_value_constraint.proto](#common_v1_key_value_constraint-proto)
    - [KeyValueConstraint](#common-v1-KeyValueConstraint)
  
    - [ConstraintOperator](#common-v1-ConstraintOperator)
  
- [capability/v1/actor_constraint.proto](#capability_v1_actor_constraint-proto)
    - [ActorConstraint](#capability-v1-ActorConstraint)
  
- [capability/v1/actor_skill.proto](#capability_v1_actor_skill-proto)
    - [ActorSkill](#capability-v1-ActorSkill)
    - [ActorSkills](#capability-v1-ActorSkills)
    - [SkillEvidenceStats](#capability-v1-SkillEvidenceStats)
    - [ValidityPolicyRef](#capability-v1-ValidityPolicyRef)
  
    - [SkillInvalidityReason](#capability-v1-SkillInvalidityReason)
    - [SkillLevel](#capability-v1-SkillLevel)
    - [SkillNextAction](#capability-v1-SkillNextAction)
    - [SkillStatus](#capability-v1-SkillStatus)
  
- [capability/v1/capability_profile.proto](#capability_v1_capability_profile-proto)
    - [CapabilityProfile](#capability-v1-CapabilityProfile)
  
- [capability/v1/skill_definition.proto](#capability_v1_skill_definition-proto)
    - [SkillDefinition](#capability-v1-SkillDefinition)
    - [SkillDefinitions](#capability-v1-SkillDefinitions)
  
    - [SkillDomain](#capability-v1-SkillDomain)
    - [ToolRole](#capability-v1-ToolRole)
  
- [capability/v1/skill_requirement.proto](#capability_v1_skill_requirement-proto)
    - [SkillRequirement](#capability-v1-SkillRequirement)
  
- [capability/v1/tool_requirement.proto](#capability_v1_tool_requirement-proto)
    - [ToolRequirement](#capability-v1-ToolRequirement)
  
    - [ToolProperty](#capability-v1-ToolProperty)
  
- [capability/v1/validity_policy.proto](#capability_v1_validity_policy-proto)
    - [ValidityPolicies](#capability-v1-ValidityPolicies)
    - [ValidityPolicy](#capability-v1-ValidityPolicy)
  
- [common/v1/custom_properties.proto](#common_v1_custom_properties-proto)
    - [CustomProperties](#common-v1-CustomProperties)
  
- [common/v1/delete.proto](#common_v1_delete-proto)
    - [DeleteMessage](#common-v1-DeleteMessage)
  
- [common/v1/display_text.proto](#common_v1_display_text-proto)
    - [DisplayText](#common-v1-DisplayText)
  
- [common/v1/empty.proto](#common_v1_empty-proto)
    - [EmptyMessage](#common-v1-EmptyMessage)
  
- [common/v1/external_references.proto](#common_v1_external_references-proto)
    - [ExternalReference](#common-v1-ExternalReference)
  
- [common/v1/get.proto](#common_v1_get-proto)
    - [GetByFieldMessage](#common-v1-GetByFieldMessage)
    - [GetByIdMessage](#common-v1-GetByIdMessage)
    - [GetMessage](#common-v1-GetMessage)
  
- [common/v1/ref.proto](#common_v1_ref-proto)
    - [NamedRef](#common-v1-NamedRef)
    - [Ref](#common-v1-Ref)
  
- [common/v1/time.proto](#common_v1_time-proto)
    - [EstimatedDuration](#common-v1-EstimatedDuration)
    - [TimeWindow](#common-v1-TimeWindow)
  
- [geometry/v1/local_target.proto](#geometry_v1_local_target-proto)
    - [LocalTarget](#geometry-v1-LocalTarget)
  
- [geometry/v1/wrench.proto](#geometry_v1_wrench-proto)
    - [Wrench](#geometry-v1-Wrench)
  
- [plm/v1/capability.proto](#plm_v1_capability-proto)
    - [Capabilities](#plm-v1-Capabilities)
    - [Capability](#plm-v1-Capability)
  
- [plm/v1/fixture.proto](#plm_v1_fixture-proto)
    - [FixtureMessage](#plm-v1-FixtureMessage)
    - [FixtureMessages](#plm-v1-FixtureMessages)
  
    - [FixtureType](#plm-v1-FixtureType)
  
- [plm/v1/process_abort.proto](#plm_v1_process_abort-proto)
    - [ProcessAbortMessage](#plm-v1-ProcessAbortMessage)
  
- [plm/v1/sequence.proto](#plm_v1_sequence-proto)
    - [SequenceMessage](#plm-v1-SequenceMessage)
    - [SequenceUpdatedMessage](#plm-v1-SequenceUpdatedMessage)
  
    - [SequenceState](#plm-v1-SequenceState)
  
- [plm/v1/task.proto](#plm_v1_task-proto)
    - [TaskMessage](#plm-v1-TaskMessage)
    - [TaskUpdatedMessage](#plm-v1-TaskUpdatedMessage)
  
    - [TaskAssignmentPreference](#plm-v1-TaskAssignmentPreference)
    - [TaskState](#plm-v1-TaskState)
    - [TaskType](#plm-v1-TaskType)
  
- [plm/v1/process_old.proto](#plm_v1_process_old-proto)
    - [ProcessMessage](#plm-v1-ProcessMessage)
    - [ProcessMessages](#plm-v1-ProcessMessages)
    - [ProcessUpdatedMessage](#plm-v1-ProcessUpdatedMessage)
  
    - [ProcessState](#plm-v1-ProcessState)
    - [ProcessType](#plm-v1-ProcessType)
  
- [plm/v1/process_authoring.proto](#plm_v1_process_authoring-proto)
    - [NewProcessMessage](#plm-v1-NewProcessMessage)
    - [StoredProcessMessage](#plm-v1-StoredProcessMessage)
    - [StoredProcessMessages](#plm-v1-StoredProcessMessages)
    - [UpdateProcessMessage](#plm-v1-UpdateProcessMessage)
  
- [plm/v1/process_load.proto](#plm_v1_process_load-proto)
    - [ProcessLoadMessage](#plm-v1-ProcessLoadMessage)
  
    - [AllocationStrategy](#plm-v1-AllocationStrategy)
  
- [plm/v1/requests.proto](#plm_v1_requests-proto)
    - [ProcessAtLocationMessage](#plm-v1-ProcessAtLocationMessage)
  
- [plm/v1/sequence_authoring.proto](#plm_v1_sequence_authoring-proto)
    - [NewSequenceMessage](#plm-v1-NewSequenceMessage)
    - [StoredSequenceMessage](#plm-v1-StoredSequenceMessage)
    - [StoredSequenceMessages](#plm-v1-StoredSequenceMessages)
    - [UpdateSequenceMessage](#plm-v1-UpdateSequenceMessage)
  
    - [SequenceType](#plm-v1-SequenceType)
  
- [plm/v1/sequence_complete.proto](#plm_v1_sequence_complete-proto)
    - [SequenceBulkCompleteMessage](#plm-v1-SequenceBulkCompleteMessage)
  
- [plm/v1/sequence_reassign.proto](#plm_v1_sequence_reassign-proto)
    - [SequenceReassignMessage](#plm-v1-SequenceReassignMessage)
  
- [plm/v1/task_authoring.proto](#plm_v1_task_authoring-proto)
    - [NewTaskMessage](#plm-v1-NewTaskMessage)
    - [StoredTaskMessage](#plm-v1-StoredTaskMessage)
    - [StoredTaskMessages](#plm-v1-StoredTaskMessages)
    - [UpdateTaskMessage](#plm-v1-UpdateTaskMessage)
  
- [plm/v1/task_progress.proto](#plm_v1_task_progress-proto)
    - [TaskProgressMessage](#plm-v1-TaskProgressMessage)
  
- [plm/v1/task_reassign.proto](#plm_v1_task_reassign-proto)
    - [TaskReassignMessage](#plm-v1-TaskReassignMessage)
  
- [plm/v1/task_state_change.proto](#plm_v1_task_state_change-proto)
    - [TaskStateChangeMessage](#plm-v1-TaskStateChangeMessage)
  
    - [TaskStateRequest](#plm-v1-TaskStateRequest)
  
- [plm/v1/tasks_list.proto](#plm_v1_tasks_list-proto)
    - [TasksForAgentRequest](#plm-v1-TasksForAgentRequest)
    - [TasksForAgentResponse](#plm-v1-TasksForAgentResponse)
  
- [process/v1/sequence_definition.proto](#process_v1_sequence_definition-proto)
    - [SequenceDefinition](#process-v1-SequenceDefinition)
    - [SequenceDefinitions](#process-v1-SequenceDefinitions)
  
    - [SequenceOperator](#process-v1-SequenceOperator)
  
- [resources/v1/asset_definition.proto](#resources_v1_asset_definition-proto)
    - [AssetDefinition](#resources-v1-AssetDefinition)
    - [AssetDefinitions](#resources-v1-AssetDefinitions)
    - [VisionCapability](#resources-v1-VisionCapability)
  
    - [AssetDriverType](#resources-v1-AssetDriverType)
    - [AssetType](#resources-v1-AssetType)
    - [ValidationMode](#resources-v1-ValidationMode)
  
- [resources/v1/container_definition.proto](#resources_v1_container_definition-proto)
    - [ContainerDefinition](#resources-v1-ContainerDefinition)
    - [ContainerDefinitions](#resources-v1-ContainerDefinitions)
    - [ContainerSlotDefinition](#resources-v1-ContainerSlotDefinition)
    - [ContainerSlotRef](#resources-v1-ContainerSlotRef)
  
    - [ContainerSlotType](#resources-v1-ContainerSlotType)
    - [ContainerType](#resources-v1-ContainerType)
  
- [variance/v1/variant_rule.proto](#variance_v1_variant_rule-proto)
    - [VariantPredicate](#variance-v1-VariantPredicate)
    - [VariantRule](#variance-v1-VariantRule)
  
- [process/v1/task_definition.proto](#process_v1_task_definition-proto)
    - [ContainerTarget](#process-v1-ContainerTarget)
    - [ProductTarget](#process-v1-ProductTarget)
    - [ResourceTarget](#process-v1-ResourceTarget)
    - [TaskDefinition](#process-v1-TaskDefinition)
    - [TaskDefinitions](#process-v1-TaskDefinitions)
    - [TaskEndpoint](#process-v1-TaskEndpoint)
    - [TaskExecutionPolicy](#process-v1-TaskExecutionPolicy)
    - [TaskOverride](#process-v1-TaskOverride)
    - [TaskTarget](#process-v1-TaskTarget)
    - [ValidationRequirement](#process-v1-ValidationRequirement)
  
    - [TaskAssignmentPreference](#process-v1-TaskAssignmentPreference)
    - [TaskType](#process-v1-TaskType)
  
- [process/v1/process_recipe.proto](#process_v1_process_recipe-proto)
    - [AddChildSequenceRequest](#process-v1-AddChildSequenceRequest)
    - [AddChildTaskRequest](#process-v1-AddChildTaskRequest)
    - [AddRootSequenceRequest](#process-v1-AddRootSequenceRequest)
    - [CreateProcessRecipe](#process-v1-CreateProcessRecipe)
    - [ProcessRecipe](#process-v1-ProcessRecipe)
    - [ProcessRecipes](#process-v1-ProcessRecipes)
    - [RecipeApplicability](#process-v1-RecipeApplicability)
    - [RemoveSequenceRequest](#process-v1-RemoveSequenceRequest)
    - [RemoveTaskRequest](#process-v1-RemoveTaskRequest)
  
    - [ProcessType](#process-v1-ProcessType)
  
- [variance/v1/variant_configuration.proto](#variance_v1_variant_configuration-proto)
    - [VariantConfiguration](#variance-v1-VariantConfiguration)
    - [VariantSelection](#variance-v1-VariantSelection)
  
- [process/v1/generation_requests.proto](#process_v1_generation_requests-proto)
    - [DraftProcessRecipeGenerateIssue](#process-v1-DraftProcessRecipeGenerateIssue)
    - [DraftProcessRecipeGenerateRequest](#process-v1-DraftProcessRecipeGenerateRequest)
    - [DraftProcessRecipeGenerateResult](#process-v1-DraftProcessRecipeGenerateResult)
  
- [product/v1/assembly_node.proto](#product_v1_assembly_node-proto)
    - [AssemblyNode](#product-v1-AssemblyNode)
  
    - [JoinMethod](#product-v1-JoinMethod)
    - [NodeKind](#product-v1-NodeKind)
  
- [product/v1/part_definition.proto](#product_v1_part_definition-proto)
    - [Dimensions](#product-v1-Dimensions)
    - [MaterialSpec](#product-v1-MaterialSpec)
    - [PartDefinition](#product-v1-PartDefinition)
    - [PartDefinitions](#product-v1-PartDefinitions)
    - [PartHandlingProfile](#product-v1-PartHandlingProfile)
  
    - [MaterialCategory](#product-v1-MaterialCategory)
    - [PartType](#product-v1-PartType)
  
- [product/v1/part_instance.proto](#product_v1_part_instance-proto)
    - [PartInstance](#product-v1-PartInstance)
    - [PartInstanceLocation](#product-v1-PartInstanceLocation)
    - [PartInstances](#product-v1-PartInstances)
    - [QuantityStatus](#product-v1-QuantityStatus)
  
- [variance/v1/variant_axis.proto](#variance_v1_variant_axis-proto)
    - [VariantAxis](#variance-v1-VariantAxis)
    - [VariantOption](#variance-v1-VariantOption)
  
- [product/v1/product_definition.proto](#product_v1_product_definition-proto)
    - [ProductDefinition](#product-v1-ProductDefinition)
    - [ProductDefinitions](#product-v1-ProductDefinitions)
  
- [resources/v1/asset_instance.proto](#resources_v1_asset_instance-proto)
    - [AssetInstance](#resources-v1-AssetInstance)
    - [AssetInstances](#resources-v1-AssetInstances)
  
- [resources/v1/placement.proto](#resources_v1_placement-proto)
    - [AssetPlacement](#resources-v1-AssetPlacement)
    - [MarkerPlacement](#resources-v1-MarkerPlacement)
    - [RobotPlacement](#resources-v1-RobotPlacement)
    - [ToolPlacement](#resources-v1-ToolPlacement)
  
- [resources/v1/cell_definition.proto](#resources_v1_cell_definition-proto)
    - [CellDefinition](#resources-v1-CellDefinition)
    - [CellDefinitions](#resources-v1-CellDefinitions)
  
    - [CellStatus](#resources-v1-CellStatus)
  
- [resources/v1/container_instance.proto](#resources_v1_container_instance-proto)
    - [ContainerInstance](#resources-v1-ContainerInstance)
    - [ContainerInstances](#resources-v1-ContainerInstances)
    - [ContainerLocation](#resources-v1-ContainerLocation)
  
- [resources/v1/device.proto](#resources_v1_device-proto)
    - [DeviceHeartbeat](#resources-v1-DeviceHeartbeat)
    - [DeviceMessage](#resources-v1-DeviceMessage)
    - [DeviceMessages](#resources-v1-DeviceMessages)
  
    - [DeviceBatteryStatus](#resources-v1-DeviceBatteryStatus)
    - [DeviceStatus](#resources-v1-DeviceStatus)
    - [DeviceType](#resources-v1-DeviceType)
  
- [resources/v1/line_definition.proto](#resources_v1_line_definition-proto)
    - [LineDefinition](#resources-v1-LineDefinition)
    - [LineDefinitions](#resources-v1-LineDefinitions)
  
    - [LineStatus](#resources-v1-LineStatus)
    - [LineType](#resources-v1-LineType)
  
- [resources/v1/marker_instance.proto](#resources_v1_marker_instance-proto)
    - [MarkerInstance](#resources-v1-MarkerInstance)
    - [MarkerInstances](#resources-v1-MarkerInstances)
  
    - [MarkerType](#resources-v1-MarkerType)
  
- [resources/v1/model.proto](#resources_v1_model-proto)
    - [ModelArtifact](#resources-v1-ModelArtifact)
    - [ModelArtifacts](#resources-v1-ModelArtifacts)
  
    - [ModelFormat](#resources-v1-ModelFormat)
    - [ModelGroup](#resources-v1-ModelGroup)
    - [ModelOrigin](#resources-v1-ModelOrigin)
  
- [resources/v1/robot_definition.proto](#resources_v1_robot_definition-proto)
    - [RobotDefinition](#resources-v1-RobotDefinition)
    - [RobotDefinitions](#resources-v1-RobotDefinitions)
  
    - [RobotDriverType](#resources-v1-RobotDriverType)
    - [RobotType](#resources-v1-RobotType)
  
- [resources/v1/robot_instance.proto](#resources_v1_robot_instance-proto)
    - [RobotInstance](#resources-v1-RobotInstance)
    - [RobotInstances](#resources-v1-RobotInstances)
  
- [resources/v1/station_definition.proto](#resources_v1_station_definition-proto)
    - [StationDefinition](#resources-v1-StationDefinition)
    - [StationDefinitions](#resources-v1-StationDefinitions)
  
    - [StationStatus](#resources-v1-StationStatus)
    - [StationType](#resources-v1-StationType)
  
- [resources/v1/tool_definition.proto](#resources_v1_tool_definition-proto)
    - [ToolDefinition](#resources-v1-ToolDefinition)
    - [ToolDefinitions](#resources-v1-ToolDefinitions)
  
    - [ToolType](#resources-v1-ToolType)
  
- [resources/v1/tool_instance.proto](#resources_v1_tool_instance-proto)
    - [ToolInstance](#resources-v1-ToolInstance)
    - [ToolInstances](#resources-v1-ToolInstances)
  
- [resources/v1/worker_definition.proto](#resources_v1_worker_definition-proto)
    - [WorkerDefinition](#resources-v1-WorkerDefinition)
    - [WorkerDefinitions](#resources-v1-WorkerDefinitions)
    - [WorkerLocation](#resources-v1-WorkerLocation)
  
    - [EditPermission](#resources-v1-EditPermission)
  
- [robot/v1/end_effector.proto](#robot_v1_end_effector-proto)
    - [EndEffectorStateMessage](#robot-v1-EndEffectorStateMessage)
  
- [robot/v1/jointstate.proto](#robot_v1_jointstate-proto)
    - [JointStateMessage](#robot-v1-JointStateMessage)
  
- [robot/v1/path.proto](#robot_v1_path-proto)
    - [PathMessage](#robot-v1-PathMessage)
  
- [robot/v1/popup.proto](#robot_v1_popup-proto)
    - [RobotHidePopupRequest](#robot-v1-RobotHidePopupRequest)
    - [RobotShowPopupRequest](#robot-v1-RobotShowPopupRequest)
  
- [robot/v1/program_state.proto](#robot_v1_program_state-proto)
    - [ProgramStateMessage](#robot-v1-ProgramStateMessage)
  
    - [ProgramState](#robot-v1-ProgramState)
  
- [robot/v1/program_state_request.proto](#robot_v1_program_state_request-proto)
    - [ProgramStateRequest](#robot-v1-ProgramStateRequest)
  
- [robot/v1/robot_state.proto](#robot_v1_robot_state-proto)
    - [RobotStateMessage](#robot-v1-RobotStateMessage)
  
    - [RobotState](#robot-v1-RobotState)
  
- [robot/v1/robot_visibility.proto](#robot_v1_robot_visibility-proto)
    - [RobotVisibilityMessage](#robot-v1-RobotVisibilityMessage)
  
- [robot/v1/tcp.proto](#robot_v1_tcp-proto)
    - [TcpMessage](#robot-v1-TcpMessage)
  
- [robot/v1/waypoints.proto](#robot_v1_waypoints-proto)
    - [WaypointMessage](#robot-v1-WaypointMessage)
    - [WaypointsMessage](#robot-v1-WaypointsMessage)
  
- [robot/v1/zone.proto](#robot_v1_zone-proto)
    - [ZoneMessage](#robot-v1-ZoneMessage)
  
- [runtime/v1/actor_assignment.proto](#runtime_v1_actor_assignment-proto)
    - [ActorAssignment](#runtime-v1-ActorAssignment)
    - [ActorAssignments](#runtime-v1-ActorAssignments)
  
- [runtime/v1/execution_evidence.proto](#runtime_v1_execution_evidence-proto)
    - [EvidenceFact](#runtime-v1-EvidenceFact)
    - [ExecutionEvidence](#runtime-v1-ExecutionEvidence)
    - [ExecutionEvidences](#runtime-v1-ExecutionEvidences)
  
- [runtime/v1/process_run.proto](#runtime_v1_process_run-proto)
    - [ProcessRun](#runtime-v1-ProcessRun)
    - [ProcessRuns](#runtime-v1-ProcessRuns)
    - [RunParameter](#runtime-v1-RunParameter)
  
    - [ProcessRunState](#runtime-v1-ProcessRunState)
  
- [runtime/v1/runtime_restriction.proto](#runtime_v1_runtime_restriction-proto)
    - [RuntimeRestriction](#runtime-v1-RuntimeRestriction)
  
    - [RestrictionType](#runtime-v1-RestrictionType)
  
- [runtime/v1/process_requests.proto](#runtime_v1_process_requests-proto)
    - [CandidateActorEvaluation](#runtime-v1-CandidateActorEvaluation)
    - [ProcessLoadRequest](#runtime-v1-ProcessLoadRequest)
    - [ProcessLoadResult](#runtime-v1-ProcessLoadResult)
    - [ProcessRunIssue](#runtime-v1-ProcessRunIssue)
    - [ProcessRunPrecheckResult](#runtime-v1-ProcessRunPrecheckResult)
    - [TaskFeasibility](#runtime-v1-TaskFeasibility)
  
    - [ProcessLoadFailure](#runtime-v1-ProcessLoadFailure)
    - [ProcessLoadStatus](#runtime-v1-ProcessLoadStatus)
    - [ProcessLoadStrategy](#runtime-v1-ProcessLoadStrategy)
    - [ProcessRunIssueSeverity](#runtime-v1-ProcessRunIssueSeverity)
    - [ProcessRunPrecheckStatus](#runtime-v1-ProcessRunPrecheckStatus)
    - [RequirementImportance](#runtime-v1-RequirementImportance)
  
- [runtime/v1/sequence_run.proto](#runtime_v1_sequence_run-proto)
    - [SequenceRun](#runtime-v1-SequenceRun)
    - [SequenceRuns](#runtime-v1-SequenceRuns)
  
    - [SequenceRunState](#runtime-v1-SequenceRunState)
  
- [runtime/v1/task_run.proto](#runtime_v1_task_run-proto)
    - [TaskRun](#runtime-v1-TaskRun)
    - [TaskRuns](#runtime-v1-TaskRuns)
    - [TaskRuntimeBinding](#runtime-v1-TaskRuntimeBinding)
  
    - [TaskRunState](#runtime-v1-TaskRunState)
  
- [runtime/v1/validation_result.proto](#runtime_v1_validation_result-proto)
    - [ValidationResult](#runtime-v1-ValidationResult)
  
    - [ValidationStatus](#runtime-v1-ValidationStatus)
  
- [service/v1/ar_client.proto](#service_v1_ar_client-proto)
    - [ARClientMessage](#service-v1-ARClientMessage)
  
    - [ARClientRole](#service-v1-ARClientRole)
  
- [service/v1/response.proto](#service_v1_response-proto)
    - [Response](#service-v1-Response)
  
- [service/v1/robot_adapter.proto](#service_v1_robot_adapter-proto)
    - [RobotAdapterInfoMessage](#service-v1-RobotAdapterInfoMessage)
  
- [service/v1/server.proto](#service_v1_server-proto)
    - [ServerHeartbeat](#service-v1-ServerHeartbeat)
    - [ServerInfo](#service-v1-ServerInfo)
  
- [service/v1/status.proto](#service_v1_status-proto)
    - [ServiceStatus](#service-v1-ServiceStatus)
  
    - [Status](#service-v1-Status)
  
- [Scalar Value Types](#scalar-value-types)



<a name="common_v1_color-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/color.proto



<a name="common-v1-Color"></a>

### Color
Represents a color. Where (255, 255, 255, 255) is solid white, (255, 0, 0, 128) is half transparent red, and so on.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| red | [uint32](#uint32) |  | Ranging from [0:255] |
| green | [uint32](#uint32) |  | Ranging from [0:255] |
| blue | [uint32](#uint32) |  | Ranging from [0:255] |
| alpha | [uint32](#uint32) |  | Ranging from [0:255] --&gt; [transparent : opaque] |





 

 

 

 



<a name="geometry_v1_anchor-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/anchor.proto



<a name="geometry-v1-Anchor"></a>

### Anchor



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reference | [string](#string) |  | Reference point towards an object or a thing, e.g. the environment, a robot, the user, ... |
| frame | [string](#string) |  | Frame is something in relation to the reference, e.g. wrist, tcp, left-hand, ... |





 

 

 

 



<a name="geometry_v1_point-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/point.proto



<a name="geometry-v1-Point"></a>

### Point



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [float](#float) |  |  |
| y | [float](#float) |  |  |
| z | [float](#float) |  |  |





 

 

 

 



<a name="geometry_v1_quad-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/quad.proto



<a name="geometry-v1-Quad"></a>

### Quad



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [float](#float) |  |  |
| y | [float](#float) |  |  |
| z | [float](#float) |  |  |
| w | [float](#float) |  |  |





 

 

 

 



<a name="geometry_v1_pose-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/pose.proto



<a name="geometry-v1-LocalizedPose"></a>

### LocalizedPose
A localized pose with reference to an anchorId. The state and last updated time of the pose can be specified.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| position | [Point](#geometry-v1-Point) |  |  |
| orientation | [Quad](#geometry-v1-Quad) |  |  |
| anchor | [Anchor](#geometry-v1-Anchor) |  |  |
| state | [LocalizedState](#geometry-v1-LocalizedState) |  |  |
| last_updated | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |






<a name="geometry-v1-Pose"></a>

### Pose
A simple pose consisting of a position and orientation


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [Point](#geometry-v1-Point) |  |  |
| orientation | [Quad](#geometry-v1-Quad) |  |  |





 


<a name="geometry-v1-LocalizedState"></a>

### LocalizedState


| Name | Number | Description |
| ---- | ------ | ----------- |
| LOCALIZED_STATE_UNSPECIFIED | 0 |  |
| LOCALIZED_STATE_FOUND | 1 |  |
| LOCALIZED_STATE_LOST | 2 |  |
| LOCALIZED_STATE_STATIC | 3 |  |


 

 

 



<a name="geometry_v1_vector3-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/vector3.proto



<a name="geometry-v1-Vector3"></a>

### Vector3



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [float](#float) |  |  |
| y | [float](#float) |  |  |
| z | [float](#float) |  |  |





 

 

 

 



<a name="validation_v1_predefined_string_rules-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## validation/v1/predefined_string_rules.proto


 

 


<a name="validation_v1_predefined_string_rules-proto-extensions"></a>

### File-level Extensions
| Extension | Type | Base | Number | Description |
| --------- | ---- | ---- | ------ | ----------- |
| ar_config_id_component | bool | .buf.validate.StringRules | 10002 |  |
| asset_definition_id_component | bool | .buf.validate.StringRules | 10006 |  |
| asset_instance_id_component | bool | .buf.validate.StringRules | 10007 |  |
| cell_id_component | bool | .buf.validate.StringRules | 10023 |  |
| container_definition_id_component | bool | .buf.validate.StringRules | 10025 |  |
| container_instance_id_component | bool | .buf.validate.StringRules | 100026 |  |
| environment_id_component | bool | .buf.validate.StringRules | 10008 |  |
| fixture_id_component | bool | .buf.validate.StringRules | 10014 |  |
| line_id_component | bool | .buf.validate.StringRules | 10024 |  |
| marker_id_component | bool | .buf.validate.StringRules | 10013 |  |
| model_id_component | bool | .buf.validate.StringRules | 10001 |  |
| name_component | bool | .buf.validate.StringRules | 10000 |  |
| part_definition_id_component | bool | .buf.validate.StringRules | 10009 |  |
| part_instance_id_component | bool | .buf.validate.StringRules | 10010 |  |
| process_recipe_id_component | bool | .buf.validate.StringRules | 10020 |  |
| process_run_id_component | bool | .buf.validate.StringRules | 10017 |  |
| property_id_component | bool | .buf.validate.StringRules | 10003 |  |
| robot_definition_id_component | bool | .buf.validate.StringRules | 10004 |  |
| robot_instance_id_component | bool | .buf.validate.StringRules | 10005 |  |
| sequence_definition_id_component | bool | .buf.validate.StringRules | 10021 |  |
| sequence_run_id_component | bool | .buf.validate.StringRules | 10018 |  |
| skill_id_component | bool | .buf.validate.StringRules | 10016 |  |
| station_id_component | bool | .buf.validate.StringRules | 10015 |  |
| task_definition_id_component | bool | .buf.validate.StringRules | 10022 |  |
| task_run_id_component | bool | .buf.validate.StringRules | 10019 |  |
| tool_definition_id_component | bool | .buf.validate.StringRules | 10011 |  |
| tool_instance_id_component | bool | .buf.validate.StringRules | 10012 |  |
| worker_id_component | bool | .buf.validate.StringRules | 100027 |  |

 

 



<a name="common_v1_property-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/property.proto



<a name="common-v1-AnchorExtras"></a>

### AnchorExtras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| only_markers | [bool](#bool) |  |  |






<a name="common-v1-ColorExtras"></a>

### ColorExtras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| step | [double](#double) |  |  |
| default | [Color](#common-v1-Color) |  | TODO: allow user-preference override |






<a name="common-v1-EnumExtras"></a>

### EnumExtras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| placeholder | [string](#string) |  | Placeholder value shown in UI when no enum is selected |
| filter | [bool](#bool) |  | Show filter input |
| grouped | [bool](#bool) |  | If options should be grouped |
| show_icons | [bool](#bool) |  | If options have icons and these should be shown |
| max_selected_labels | [uint32](#uint32) |  | Only relevant for MultiSelect: limits number of selected labels |
| options | [EnumOption](#common-v1-EnumOption) | repeated |  |






<a name="common-v1-EnumOption"></a>

### EnumOption



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [string](#string) |  |  |
| label | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| group | [string](#string) |  |  |
| disabled | [bool](#bool) |  |  |






<a name="common-v1-NumberExtras"></a>

### NumberExtras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min | [double](#double) | optional |  |
| max | [double](#double) | optional |  |
| step | [double](#double) | optional |  |
| unit | [string](#string) |  | &#34;mm&#34;, &#34;deg&#34;, &#34;N&#34; |
| precision | [uint32](#uint32) |  | Decimal places for display |






<a name="common-v1-PoseExtras"></a>

### PoseExtras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| anchor_editable | [bool](#bool) |  |  |
| pose_editable | [bool](#bool) |  |  |






<a name="common-v1-Property"></a>

### Property
Properties are used by various components to define them, such as: feedback, actions, and conditions.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [PropertyType](#common-v1-PropertyType) |  |  |
| minimum_required_permission | [PropertyPermission](#common-v1-PropertyPermission) |  |  |
| origin | [PropertyOrigin](#common-v1-PropertyOrigin) |  |  |
| origins | [PropertyOrigin](#common-v1-PropertyOrigin) | repeated |  |
| mirror_property_id | [string](#string) |  |  |
| group | [PropertyGroup](#common-v1-PropertyGroup) |  |  |
| ordering | [int32](#int32) |  |  |
| hide_group | [bool](#bool) |  |  |
| parent_id | [string](#string) |  |  |
| advanced | [bool](#bool) |  | Hide behind &#34;Advanced&#34; toogle |
| scope_id | [string](#string) |  |  |
| disable_mirroring | [bool](#bool) |  | If true, this property is not allowed to be mirrored by other properties |
| bool_value | [bool](#bool) | optional |  |
| int_value | [sint64](#sint64) | optional |  |
| float_value | [float](#float) | optional |  |
| double_value | [double](#double) | optional |  |
| string_value | [string](#string) | optional |  |
| vector3_value | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| pose_value | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| anchor_value | [geometry.v1.Anchor](#geometry-v1-Anchor) |  |  |
| color_value | [Color](#common-v1-Color) |  |  |
| robot_id_value | [string](#string) | optional |  |
| enum_value | [string](#string) | optional |  |
| enum_multi_value | [string](#string) | repeated |  |
| icon_value | [string](#string) | optional |  |
| asset_id_value | [string](#string) | optional |  |
| number_extras | [NumberExtras](#common-v1-NumberExtras) |  |  |
| enum_extras | [EnumExtras](#common-v1-EnumExtras) |  |  |
| vector3_extras | [Vector3Extras](#common-v1-Vector3Extras) |  |  |
| color_extras | [ColorExtras](#common-v1-ColorExtras) |  |  |
| pose_extras | [PoseExtras](#common-v1-PoseExtras) |  |  |
| anchor_extras | [AnchorExtras](#common-v1-AnchorExtras) |  |  |






<a name="common-v1-PropertyMessages"></a>

### PropertyMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| properties | [Property](#common-v1-Property) | repeated |  |






<a name="common-v1-PropertyValueUpdate"></a>

### PropertyValueUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| type | [PropertyType](#common-v1-PropertyType) |  |  |
| origin | [PropertyOrigin](#common-v1-PropertyOrigin) |  |  |
| mirror_property_id | [string](#string) |  |  |
| bool_value | [bool](#bool) | optional |  |
| int_value | [sint64](#sint64) | optional |  |
| float_value | [float](#float) | optional |  |
| double_value | [double](#double) | optional |  |
| string_value | [string](#string) | optional |  |
| vector3_value | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| pose_value | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| anchor_value | [geometry.v1.Anchor](#geometry-v1-Anchor) |  |  |
| color_value | [Color](#common-v1-Color) |  |  |
| robot_id_value | [string](#string) | optional |  |
| enum_value | [string](#string) | optional |  |
| enum_multi_value | [string](#string) | repeated |  |
| icon_value | [string](#string) | optional |  |
| asset_id_value | [string](#string) | optional |  |






<a name="common-v1-Vector3Extras"></a>

### Vector3Extras



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min | [double](#double) | optional |  |
| max | [double](#double) | optional |  |
| step | [double](#double) | optional |  |
| label_x | [string](#string) |  |  |
| label_y | [string](#string) |  |  |
| label_z | [string](#string) |  |  |
| unit | [string](#string) |  |  |





 


<a name="common-v1-PropertyGroup"></a>

### PropertyGroup


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROPERTY_GROUP_UNSPECIFIED | 0 |  |
| PROPERTY_GROUP_OUTPUT | 1 |  |
| PROPERTY_GROUP_NON_EDITABLE | 2 |  |
| PROPERTY_GROUP_STYLING | 3 |  |
| PROPERTY_GROUP_LOCATION | 4 |  |
| PROPERTY_GROUP_ICON | 5 |  |
| PROPERTY_GROUP_CONFIGURATION | 6 |  |
| PROPERTY_GROUP_HIDDEN | 7 |  |



<a name="common-v1-PropertyOrigin"></a>

### PropertyOrigin
Specifies where the value of a property originates from.

| Name | Number | Description |
| ---- | ------ | ----------- |
| PROPERTY_ORIGIN_UNSPECIFIED | 0 |  |
| PROPERTY_ORIGIN_FIXED | 1 | The value of the property is fixed and must be changed manually |
| PROPERTY_ORIGIN_MIRROR | 2 | The value of the property mirrors the value of another property |



<a name="common-v1-PropertyPermission"></a>

### PropertyPermission


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROPERTY_PERMISSION_UNSPECIFIED | 0 | Unspecified: can be edited by all |
| PROPERTY_PERMISSION_BASIC | 10 | Basic: can be edited by users with some permission to edit |
| PROPERTY_PERMISSION_COSMETIC | 20 | Cosmetic: can be edited by users with cosmetic&#43;full permission |
| PROPERTY_PERMISSION_FULL | 30 | Full: can be edited by users with full permission |
| PROPERTY_PERMISSION_NONE | 40 | None: can&#39;t be edited (e.g. outputs or stuff that requires a delete &#43; create new) |



<a name="common-v1-PropertyType"></a>

### PropertyType
Used to specify the type of a property

| Name | Number | Description |
| ---- | ------ | ----------- |
| PROPERTY_TYPE_UNSPECIFIED | 0 |  |
| PROPERTY_TYPE_BOOL | 1 | Bool type property (true/false) |
| PROPERTY_TYPE_INT | 2 | Int type property |
| PROPERTY_TYPE_FLOAT | 3 | Float type property |
| PROPERTY_TYPE_DOUBLE | 4 | Double type property |
| PROPERTY_TYPE_STRING | 5 | String type property |
| PROPERTY_TYPE_VECTOR3 | 6 | Vector3 type property - {x, y, z} |
| PROPERTY_TYPE_POSE | 7 | Pose type property - LocalizedPose(id, anchor, position, orientation, state, ...) |
| PROPERTY_TYPE_ANCHOR | 8 | Anchor type property - Anchor(reference, frame) |
| PROPERTY_TYPE_COLOR | 9 | Color type property - Color(r,g,b,a) |
| PROPERTY_TYPE_ROBOT | 10 | Robot type property - robot_id as string |
| PROPERTY_TYPE_ENUM | 11 | Enum type property - string from list of strings (defined in EnumExtras) |
| PROPERTY_TYPE_ENUM_MULTI | 12 | Enum-multi type property - select multiple strings from list of strings (defined in EnumExtras) |
| PROPERTY_TYPE_ICON | 13 | Icon property type - icon-name-something from https://pictogrammers.com/ |
| PROPERTY_TYPE_ASSET | 14 | Asset type property - asset_id as string |


 

 

 



<a name="ar_v1_action-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/action.proto



<a name="ar-v1-ActionAddMessage"></a>

### ActionAddMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| config_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ActionType](#ar-v1-ActionType) |  |  |
| agent_id | [string](#string) |  |  |
| activating_property_id | [string](#string) |  |  |






<a name="ar-v1-ActionCloneMessage"></a>

### ActionCloneMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| original_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |






<a name="ar-v1-ActionMessage"></a>

### ActionMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ActionType](#ar-v1-ActionType) |  |  |
| properties | [common.v1.Property](#common-v1-Property) | repeated |  |
| config_id | [string](#string) |  |  |






<a name="ar-v1-ActionMessages"></a>

### ActionMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| actions | [ActionMessage](#ar-v1-ActionMessage) | repeated |  |






<a name="ar-v1-ActionUpdateMessage"></a>

### ActionUpdateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |





 


<a name="ar-v1-ActionType"></a>

### ActionType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ACTION_TYPE_UNSPECIFIED | 0 |  |
| ACTION_TYPE_TASK_COMPLETE | 10 |  |
| ACTION_TYPE_TASK_UNDO | 11 |  |
| ACTION_TYPE_TASK_ASSIGN | 12 |  |
| ACTION_TYPE_TASK_HIGHLIGHT | 13 |  |
| ACTION_TYPE_TASK_HELP | 14 |  |
| ACTION_TYPE_ROBOT_PLAY_PAUSE | 50 |  |
| ACTION_TYPE_ROBOT_ACKNOWLEDGE | 51 |  |
| ACTION_TYPE_ROBOT_FREE_DRIVE | 52 |  |
| ACTION_TYPE_ROBOT_COLLABORATE | 53 |  |


 

 

 



<a name="ar_v1_events-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/events.proto



<a name="ar-v1-ExchangeSupport"></a>

### ExchangeSupport



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| message | [ExchangeType](#ar-v1-ExchangeType) |  |  |
| rationale | [string](#string) |  | optional but super helpful for UI |






<a name="ar-v1-ExchangeType"></a>

### ExchangeType
ExchangeType represent a single &#39;event&#39; or exchange.

Example: robot motion
1) UI produces: { Command: ROBOT_START_STOP }
2) Planner produces: { Plan: ROBOT_PATH }
3) Driver publishes: { Telemetry: ROBOT_TCP }
4) System emits: { Event: ROBOT_STARTED_TASK }


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command | [CommandType](#ar-v1-CommandType) |  | Requested intent (future) |
| event | [EventType](#ar-v1-EventType) |  | Confirmed fact (past) |
| telemetry | [TelemetryType](#ar-v1-TelemetryType) |  | Observed state (now) |
| plan | [PlanType](#ar-v1-PlanType) |  | Planned intent (future) |






<a name="ar-v1-HandlerRequirement"></a>

### HandlerRequirement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| message | [ExchangeType](#ar-v1-ExchangeType) |  |  |
| cardinality | [HandlerCardinality](#ar-v1-HandlerCardinality) |  |  |
| rationale | [string](#string) |  | optional but super helpful for UI |






<a name="ar-v1-SupportedExchangesMessage"></a>

### SupportedExchangesMessage
Supported events is a list of all supported events in the current configuration
TODO: should this be a field of ARConfig?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| exchanges | [ExchangeSupport](#ar-v1-ExchangeSupport) | repeated |  |





 


<a name="ar-v1-CommandType"></a>

### CommandType
Commands are intents, i.e. &#34;please do this&#34;. Example: Start/STOP from UI -&gt; Robot driver

| Name | Number | Description |
| ---- | ------ | ----------- |
| COMMAND_TYPE_UNSPECIFIED | 0 |  |
| COMMAND_TYPE_TASK_COMPLETE | 10 | Workflow/UI intent |
| COMMAND_TYPE_TASK_ASSIGN | 11 |  |
| COMMAND_TYPE_TASK_UNDO | 12 |  |
| COMMAND_TYPE_TASK_HIGHLIGHT | 13 |  |
| COMMAND_TYPE_TASK_HELP | 14 |  |
| COMMAND_TYPE_ROBOT_START_STOP | 100 | Robot control intent |
| COMMAND_TYPE_ROBOT_TOGGLE_FREE_DRIVE | 101 |  |
| COMMAND_TYPE_ROBOT_START_COLLABORATION | 102 |  |
| COMMAND_TYPE_ROBOT_STOP_COLLABORATION | 103 |  |
| COMMAND_TYPE_ROBOT_ACKNOWLEDGE | 104 |  |



<a name="ar-v1-EventType"></a>

### EventType
EventType: events are facts, i.e. &#34;this just happened&#34;.

It is intended for low-frequency events. One example could be WAYPOINT_REACHED contrary to TELEMETRY_ROBOT_TCP
Events must be grounded in actual events and not just because &#34;a prediction said so&#34;.

| Name | Number | Description |
| ---- | ------ | ----------- |
| EVENT_TYPE_UNSPECIFIED | 0 |  |
| EVENT_TYPE_PROCESS_COMPLETE | 10 | Workflow facts |
| EVENT_TYPE_SEQUENCE_COMPLETE | 11 |  |
| EVENT_TYPE_TASK_COMPLETE | 12 |  |
| EVENT_TYPE_ROBOT_WAYPOINT_REACHED | 100 |  |
| EVENT_TYPE_ROBOT_PLAN_STARTED | 130 |  |
| EVENT_TYPE_ROBOT_PLAN_CHANGED | 131 |  |
| EVENT_TYPE_ROBOT_PLAN_ABORTED | 132 |  |
| EVENT_TYPE_ROBOT_PLAN_COMPLETED | 133 |  |
| EVENT_TYPE_ROBOT_WAITING_FOR_ACKNOWLEDGE | 150 |  |
| EVENT_TYPE_ROBOT_WAITING_FOR_HELP | 151 |  |
| EVENT_TYPE_ROBOT_WAITING_TASK_RELEASE | 152 |  |



<a name="ar-v1-HandlerCardinality"></a>

### HandlerCardinality


| Name | Number | Description |
| ---- | ------ | ----------- |
| HANDLER_CARDINALITY_UNSPECIFIED | 0 |  |
| HANDLER_CARDINALITY_AT_LEAST_ONE | 1 |  |
| HANDLER_CARDINALITY_EXACTLY_ONE | 2 |  |
| HANDLER_CARDINALITY_AT_MOST_ONE | 3 |  |



<a name="ar-v1-PlanType"></a>

### PlanType
Plan is planned (or expected) future state.

| Name | Number | Description |
| ---- | ------ | ----------- |
| PLAN_TYPE_UNSPECIFIED | 0 |  |
| PLAN_TYPE_ROBOT_PATH | 100 | Planned path for the robot&#39;s next action(s) |
| PLAN_TYPE_ROBOT_JOINT_ANGLES | 101 | Planned joint angles for the robot&#39;s next action(s) |
| PLAN_TYPE_ROBOT_WAYPOINTS | 102 | Planned waypoints for the robot&#39;s next action(s) |
| PLAN_TYPE_ROBOT_ESTIMATED_COMPLETION | 123 |  |
| PLAN_TYPE_ROBOT_TASK_SEQUENCE | 124 |  |
| PLAN_TYPE_TASK_SEQUENCE | 200 |  |



<a name="ar-v1-TelemetryType"></a>

### TelemetryType
TelemetryType: telemetry is current state, i.e. &#34;here is my state&#34;
It is expected to be high-frequency updates or at least updates every time the state have changed

| Name | Number | Description |
| ---- | ------ | ----------- |
| TELEMETRY_TYPE_UNSPECIFIED | 0 |  |
| TELEMETRY_TYPE_ROBOT_TCP | 100 | Current TCP for the robot |
| TELEMETRY_TYPE_ROBOT_JOINT_ANGLES | 101 | Current joint angles for the robot |
| TELEMETRY_TYPE_ROBOT_FORCE_TORQUE | 102 | Current measured force/torque values |
| TELEMETRY_TYPE_ROBOT_STATE | 110 | Current robot state. Check robot.v1.robot_state.proto for actual values. |


 

 

 



<a name="ar_v1_action_info-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/action_info.proto



<a name="ar-v1-ActionInfoMessage"></a>

### ActionInfoMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ActionType](#ar-v1-ActionType) |  |  |
| group | [ActionGroup](#ar-v1-ActionGroup) |  |  |
| require_agent | [bool](#bool) |  |  |
| consumers_required | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs the action expects to receive |
| consumers_optional | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs that will enhance the action, but not needed to function |
| required_handlers | [HandlerRequirement](#ar-v1-HandlerRequirement) | repeated | Events that MUST have at least one handler somewhere else in the system. (i.e., if the action emits these, it expects the environment to react) |
| emits | [ExchangeType](#ar-v1-ExchangeType) | repeated | Outputs the action publishes |
| disabled | [bool](#bool) |  |  |






<a name="ar-v1-ActionInfoMessages"></a>

### ActionInfoMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| infos | [ActionInfoMessage](#ar-v1-ActionInfoMessage) | repeated |  |





 


<a name="ar-v1-ActionGroup"></a>

### ActionGroup


| Name | Number | Description |
| ---- | ------ | ----------- |
| ACTION_GROUP_UNSPECIFIED | 0 |  |
| ACTION_GROUP_GENERAL | 1 |  |
| ACTION_GROUP_ROBOT | 2 |  |
| ACTION_GROUP_TASK | 3 |  |


 

 

 



<a name="ar_v1_feedback-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/feedback.proto



<a name="ar-v1-FeedbackAddMessage"></a>

### FeedbackAddMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| config_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [FeedbackType](#ar-v1-FeedbackType) |  |  |
| robot_id | [string](#string) |  |  |
| anchor | [geometry.v1.Anchor](#geometry-v1-Anchor) |  |  |






<a name="ar-v1-FeedbackCloneMessage"></a>

### FeedbackCloneMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| original_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |






<a name="ar-v1-FeedbackMessage"></a>

### FeedbackMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [FeedbackType](#ar-v1-FeedbackType) |  |  |
| properties | [common.v1.Property](#common-v1-Property) | repeated |  |
| config_id | [string](#string) |  | repeated string property_ids = 6 [ (buf.validate.field).repeated.items.string.(.validation.v1.property_id_component) = true, (buf.validate.field).repeated.unique = true ]; |






<a name="ar-v1-FeedbackMessages"></a>

### FeedbackMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| feedbacks | [FeedbackMessage](#ar-v1-FeedbackMessage) | repeated |  |






<a name="ar-v1-FeedbackUpdateMessage"></a>

### FeedbackUpdateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |





 


<a name="ar-v1-FeedbackType"></a>

### FeedbackType


| Name | Number | Description |
| ---- | ------ | ----------- |
| FEEDBACK_TYPE_UNSPECIFIED | 0 |  |
| FEEDBACK_TYPE_TASK_HIGHLIGHT | 10 |  |
| FEEDBACK_TYPE_TASK_PART_HIGHLIGHT | 11 |  |
| FEEDBACK_TYPE_TASK_TOOL_HIGHLIGHT | 12 |  |
| FEEDBACK_TYPE_TASK_OVERVIEW | 13 | Provides an overview of all current tasks |
| FEEDBACK_TYPE_TASK_INSTRUCTION | 14 | Provide instructions of the current task |
| FEEDBACK_TYPE_TASK_CHECKLIST | 15 | Tailored towards tasks that are more checklist oriented than assembly |
| FEEDBACK_TYPE_ROBOT_PATH | 50 | Show the expected path of the robot |
| FEEDBACK_TYPE_ROBOT_SILHOUETTE | 51 |  |
| FEEDBACK_TYPE_ROBOT_WAYPOINTS | 52 |  |
| FEEDBACK_TYPE_ROBOT_STATUS | 53 |  |
| FEEDBACK_TYPE_ROBOT_LIGHT | 54 |  |
| FEEDBACK_TYPE_MESSAGE | 100 |  |
| FEEDBACK_TYPE_ICON | 101 |  |
| FEEDBACK_TYPE_ZONE | 102 |  |
| FEEDBACK_TYPE_PLAY_SOUND | 103 |  |
| FEEDBACK_TYPE_RULER | 104 |  |
| FEEDBACK_TYPE_HIGHLIGHT | 105 |  |


 

 

 



<a name="ar_v1_helper-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/helper.proto



<a name="ar-v1-HelperAddMessage"></a>

### HelperAddMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| config_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [HelperType](#ar-v1-HelperType) |  |  |






<a name="ar-v1-HelperMessage"></a>

### HelperMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [HelperType](#ar-v1-HelperType) |  |  |
| properties | [common.v1.Property](#common-v1-Property) | repeated |  |






<a name="ar-v1-HelperMessages"></a>

### HelperMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| helpers | [HelperMessage](#ar-v1-HelperMessage) | repeated |  |






<a name="ar-v1-HelperUpdateMessage"></a>

### HelperUpdateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |





 


<a name="ar-v1-HelperType"></a>

### HelperType


| Name | Number | Description |
| ---- | ------ | ----------- |
| HELPER_TYPE_UNSPECIFIED | 0 |  |
| HELPER_TYPE_PROXIMITY | 10 |  |
| HELPER_TYPE_STATIONARY | 11 |  |
| HELPER_TYPE_TIMER | 21 |  |
| HELPER_TYPE_AND | 100 |  |
| HELPER_TYPE_OR | 101 |  |
| HELPER_TYPE_NOT | 102 |  |


 

 

 



<a name="ar_v1_ar_config-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/ar_config.proto



<a name="ar-v1-ARConfigInfoMessage"></a>

### ARConfigInfoMessage
Just delete this?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |






<a name="ar-v1-ARConfigInfoMessages"></a>

### ARConfigInfoMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| infos | [ARConfigInfoMessage](#ar-v1-ARConfigInfoMessage) | repeated |  |






<a name="ar-v1-ARConfigMessage"></a>

### ARConfigMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| feedback | [FeedbackMessage](#ar-v1-FeedbackMessage) | repeated | TODO: just a list of Id&#39;s? |
| actions | [ActionMessage](#ar-v1-ActionMessage) | repeated |  |
| helpers | [HelperMessage](#ar-v1-HelperMessage) | repeated |  |
| properties | [common.v1.Property](#common-v1-Property) | repeated |  |
| ar_disappear_distance | [int64](#int64) |  | Threshold distance in cm all AR elements should disappear. 0 = ignored |






<a name="ar-v1-ARConfigMessages"></a>

### ARConfigMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| configs | [ARConfigMessage](#ar-v1-ARConfigMessage) | repeated |  |





 

 

 

 



<a name="ar_v1_config_load-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/config_load.proto



<a name="ar-v1-ConfigurationLoadMessage"></a>

### ConfigurationLoadMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| config_id | [string](#string) |  | Id of the configuration to be loaded |
| instance_id | [string](#string) |  | Instance id of the current loaded configuration - from the requestors perspective - used to avoid reloading a configuration. |





 

 

 

 



<a name="ar_v1_environment-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/environment.proto



<a name="ar-v1-AssetLocation"></a>

### AssetLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |






<a name="ar-v1-EnvironmentMessage"></a>

### EnvironmentMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [EnvironmentType](#ar-v1-EnvironmentType) |  | Type of environment |
| markers | [MarkerLocation](#ar-v1-MarkerLocation) | repeated | Markers associated with this environment. |
| robots | [RobotLocation](#ar-v1-RobotLocation) | repeated | Robot located in this environment |
| assets | [AssetLocation](#ar-v1-AssetLocation) | repeated | Assets located in this environment |
| parts | [PartLocation](#ar-v1-PartLocation) | repeated | Parts located in this environment |
| tools | [ToolLocation](#ar-v1-ToolLocation) | repeated | Tools located in this environment |
| fixtures | [FixtureLocation](#ar-v1-FixtureLocation) | repeated | Fixtures located in this environment |






<a name="ar-v1-EnvironmentMessages"></a>

### EnvironmentMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| environments | [EnvironmentMessage](#ar-v1-EnvironmentMessage) | repeated |  |






<a name="ar-v1-FixtureLocation"></a>

### FixtureLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |






<a name="ar-v1-MarkerLocation"></a>

### MarkerLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |






<a name="ar-v1-PartLocation"></a>

### PartLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |






<a name="ar-v1-RobotLocation"></a>

### RobotLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |






<a name="ar-v1-ToolLocation"></a>

### ToolLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| location | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |





 


<a name="ar-v1-EnvironmentType"></a>

### EnvironmentType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ENVIRONMENT_TYPE_UNSPECIFIED | 0 |  |
| ENVIRONMENT_TYPE_STORAGE | 1 |  |
| ENVIRONMENT_TYPE_MANUAL_STATION | 2 |  |
| ENVIRONMENT_TYPE_AUTOMATIC_STATION | 3 |  |
| ENVIRONMENT_TYPE_HYBRID_STATION | 4 |  |
| ENVIRONMENT_TYPE_MANUAL_LINE | 5 |  |
| ENVIRONMENT_TYPE_AUTOMATIC_LINE | 6 |  |
| ENVIRONMENT_TYPE_HYBRID_LINE | 7 |  |


 

 

 



<a name="ar_v1_feedback_info-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/feedback_info.proto



<a name="ar-v1-FeedbackInfoMessage"></a>

### FeedbackInfoMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [FeedbackType](#ar-v1-FeedbackType) |  |  |
| group | [FeedbackGroup](#ar-v1-FeedbackGroup) |  |  |
| require_agent | [bool](#bool) |  |  |
| require_frame | [bool](#bool) |  |  |
| consumers_required | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs the feedback expects to receive |
| consumers_optional | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs that will enhance the feedback, but not needed to function |
| required_handlers | [HandlerRequirement](#ar-v1-HandlerRequirement) | repeated | Events that MUST have at least one handler somewhere else in the system. (i.e., if the feedback emits these, it expects the environment to react) |
| emits | [ExchangeType](#ar-v1-ExchangeType) | repeated | Outputs the feedback publishes |
| disabled | [bool](#bool) |  |  |






<a name="ar-v1-FeedbackInfoMessages"></a>

### FeedbackInfoMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| infos | [FeedbackInfoMessage](#ar-v1-FeedbackInfoMessage) | repeated |  |





 


<a name="ar-v1-FeedbackGroup"></a>

### FeedbackGroup


| Name | Number | Description |
| ---- | ------ | ----------- |
| FEEDBACK_GROUP_UNSPECIFIED | 0 |  |
| FEEDBACK_GROUP_GENERAL | 1 |  |
| FEEDBACK_GROUP_ROBOT | 2 |  |
| FEEDBACK_GROUP_TASK | 3 |  |
| FEEDBACK_GROUP_ENVIRONMENT | 4 |  |


 

 

 



<a name="ar_v1_helper_info-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/helper_info.proto



<a name="ar-v1-HelperInfoMessage"></a>

### HelperInfoMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [HelperType](#ar-v1-HelperType) |  |  |
| group | [HelperGroup](#ar-v1-HelperGroup) |  |  |
| require_agent | [bool](#bool) |  |  |
| require_frame | [bool](#bool) |  |  |
| consumers_required | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs the action expects to receive |
| consumers_optional | [ExchangeType](#ar-v1-ExchangeType) | repeated | Inputs that will enhance the action, but not needed to function |
| required_handlers | [HandlerRequirement](#ar-v1-HandlerRequirement) | repeated | Events that MUST have at least one handler somewhere else in the system. (i.e., if the action emits these, it expects the environment to react) |
| emits | [ExchangeType](#ar-v1-ExchangeType) | repeated | Outputs the feedback publishes |
| disabled | [bool](#bool) |  |  |






<a name="ar-v1-HelperInfoMessages"></a>

### HelperInfoMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| infos | [HelperInfoMessage](#ar-v1-HelperInfoMessage) | repeated |  |





 


<a name="ar-v1-HelperGroup"></a>

### HelperGroup


| Name | Number | Description |
| ---- | ------ | ----------- |
| HELPER_GROUP_UNSPECIFIED | 0 |  |
| HELPER_GROUP_GENERAL | 1 |  |
| HELPER_GROUP_ROBOT | 2 |  |
| HELPER_GROUP_TASK | 3 |  |
| HELPER_GROUP_ENVIRONMENT | 4 |  |
| HELPER_GROUP_OPERATOR | 5 |  |
| HELPER_GROUP_SPATIAL | 6 |  |
| HELPER_GROUP_LOGIC | 7 |  |


 

 

 



<a name="ar_v1_mapping-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## ar/v1/mapping.proto



<a name="ar-v1-AssetMapping"></a>

### AssetMapping



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| asset_id | [string](#string) |  |  |
| property_id | [string](#string) |  |  |






<a name="ar-v1-MappingMessage"></a>

### MappingMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| environment_id | [string](#string) |  |  |
| ar_config_id | [string](#string) |  |  |
| disabled | [bool](#bool) |  |  |
| robot_mapping | [RobotMapping](#ar-v1-RobotMapping) | repeated |  |
| asset_mapping | [AssetMapping](#ar-v1-AssetMapping) | repeated |  |
| standalone | [bool](#bool) |  | Only this AR-config should be shown (winner have highest priority) |
| priority | [int32](#int32) |  | High value configs will be shown first |






<a name="ar-v1-MappingMessages"></a>

### MappingMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mappings | [MappingMessage](#ar-v1-MappingMessage) | repeated |  |






<a name="ar-v1-RobotMapping"></a>

### RobotMapping



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| property_id | [string](#string) |  |  |





 

 

 

 



<a name="common_v1_actor-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/actor.proto



<a name="common-v1-ActorRef"></a>

### ActorRef



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| kind | [ActorKind](#common-v1-ActorKind) |  |  |
| actor_id | [string](#string) |  | worker_definition_id or robot_instance_id |





 


<a name="common-v1-ActorKind"></a>

### ActorKind


| Name | Number | Description |
| ---- | ------ | ----------- |
| ACTOR_KIND_UNSPECIFIED | 0 |  |
| ACTOR_KIND_HUMAN | 1 |  |
| ACTOR_KIND_ROBOT | 2 |  |
| ACTOR_KIND_HYBRID | 3 |  |


 

 

 



<a name="common_v1_enums-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/enums.proto


 


<a name="common-v1-CollaborationMode"></a>

### CollaborationMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| COLLABORATION_MODE_UNSPECIFIED | 0 |  |
| COLLABORATION_MODE_HUMAN_ONLY | 1 |  |
| COLLABORATION_MODE_ROBOT_ONLY | 2 |  |
| COLLABORATION_MODE_SEQUENTIAL_HRC | 3 |  |
| COLLABORATION_MODE_SIMULTANEOUS_HRC | 4 |  |



<a name="common-v1-ResourceStatus"></a>

### ResourceStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| RESOURCE_STATUS_UNSPECIFIED | 0 |  |
| RESOURCE_STATUS_AVAILABLE | 1 |  |
| RESOURCE_STATUS_UNAVAILABLE | 2 |  |
| RESOURCE_STATUS_DISABLED | 3 |  |
| RESOURCE_STATUS_MAINTENANCE | 4 |  |



<a name="common-v1-SafetyRelevance"></a>

### SafetyRelevance
SafetyRelevance indicates how safety-critical a task, action, or capability is.

This value helps systems determine:
- whether additional validation or confirmation is required
- what actor permissions or certifications are needed
- whether supervision or restricted execution policies apply
- how prominently the task should be displayed or highlighted in UIs

Safety relevance does NOT necessarily mean the task is dangerous,
but rather the potential consequences if the task is performed
incorrectly or skipped.

The levels are intentionally coarse to keep authoring simple while
still allowing meaningful safety-aware behavior.

| Name | Number | Description |
| ---- | ------ | ----------- |
| SAFETY_RELEVANCE_UNSPECIFIED | 0 | Default value when safety relevance has not yet been determined.

Systems should typically treat this conservatively, often equivalent to MEDIUM unless explicitly overridden. |
| SAFETY_RELEVANCE_LOW | 1 | Minimal safety impact.

Errors are unlikely to cause harm to people, equipment, or product integrity.

Examples: - wiping a surface - organizing components - non-critical visual checks

Typically requires no special permissions or confirmations. |
| SAFETY_RELEVANCE_MEDIUM | 2 | Moderate safety impact.

Mistakes may affect product quality or create minor risk to equipment or operators.

Examples: - positioning components - inserting non-critical parts - non-torque-sensitive operations

Systems may require basic validation or confirmation. |
| SAFETY_RELEVANCE_HIGH | 3 | High safety impact.

Incorrect execution may lead to equipment damage, significant product defects, or operator risk.

Examples: - torque-controlled fastening - applying significant force - electrical assembly steps

Systems may enforce stricter validation, tool feedback, or actor capability checks. |
| SAFETY_RELEVANCE_CRITICAL | 4 | Safety-critical operations.

Incorrect execution may pose serious risk to human safety, regulatory compliance, or system integrity.

Examples: - safety-critical fasteners - interacting with safety systems - hazardous energy isolation steps - operations requiring certified personnel

Systems should require strict validation, restricted actor permissions, and explicit confirmation before completion. |


 

 

 



<a name="common_v1_key_value_constraint-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/key_value_constraint.proto



<a name="common-v1-KeyValueConstraint"></a>

### KeyValueConstraint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| op | [ConstraintOperator](#common-v1-ConstraintOperator) |  |  |
| value | [string](#string) |  |  |
| values | [string](#string) | repeated |  |





 


<a name="common-v1-ConstraintOperator"></a>

### ConstraintOperator


| Name | Number | Description |
| ---- | ------ | ----------- |
| CONSTRAINT_OPERATOR_UNSPECIFIED | 0 |  |
| CONSTRAINT_OPERATOR_EQ | 1 |  |
| CONSTRAINT_OPERATOR_NEQ | 2 |  |
| CONSTRAINT_OPERATOR_GT | 3 |  |
| CONSTRAINT_OPERATOR_GTE | 4 |  |
| CONSTRAINT_OPERATOR_LT | 5 |  |
| CONSTRAINT_OPERATOR_LTE | 6 |  |
| CONSTRAINT_OPERATOR_IN | 7 |  |
| CONSTRAINT_OPERATOR_NOT_IN | 8 |  |


 

 

 



<a name="capability_v1_actor_constraint-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## capability/v1/actor_constraint.proto



<a name="capability-v1-ActorConstraint"></a>

### ActorConstraint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| allowed_actor_kinds | [common.v1.ActorKind](#common-v1-ActorKind) | repeated |  |
| collaboration_mode | [common.v1.CollaborationMode](#common-v1-CollaborationMode) |  |  |
| constraints | [common.v1.KeyValueConstraint](#common-v1-KeyValueConstraint) | repeated |  |





 

 

 

 



<a name="capability_v1_actor_skill-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## capability/v1/actor_skill.proto



<a name="capability-v1-ActorSkill"></a>

### ActorSkill
ActorSkill stores the current operational summary of one skill for one actor.

It is intentionally a fast, runtime-friendly summary layer rather than a full
audit log. Runtime planners/loaders should use this message to determine
whether an actor is:
- allowed
- restricted
- expired

ExecutionEvidence and training/certification events are expected to update
this summary over time.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| actor | [common.v1.ActorRef](#common-v1-ActorRef) |  |  |
| skill_id | [string](#string) |  |  |
| level | [SkillLevel](#capability-v1-SkillLevel) |  |  |
| status | [SkillStatus](#capability-v1-SkillStatus) |  |  |
| confidence_score | [float](#float) |  | Optional derived confidence/proficiency score in [0,1]. |
| stats | [SkillEvidenceStats](#capability-v1-SkillEvidenceStats) |  | Aggregated evidence summary used for fast runtime decisions. |
| last_training_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Most recent training/refresher event relevant to this skill. |
| last_certified_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Most recent formal certification/re-certification event. |
| valid_until | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Explicit validity limit if known, otherwise policy-derived. |
| validity_policy | [ValidityPolicyRef](#capability-v1-ValidityPolicyRef) |  | Policy currently used to evaluate status/validity. |
| reasons | [SkillInvalidityReason](#capability-v1-SkillInvalidityReason) | repeated |  |
| next_actions | [SkillNextAction](#capability-v1-SkillNextAction) | repeated |  |






<a name="capability-v1-ActorSkills"></a>

### ActorSkills



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ActorSkill](#capability-v1-ActorSkill) | repeated |  |






<a name="capability-v1-SkillEvidenceStats"></a>

### SkillEvidenceStats
SkillEvidenceStats is a lightweight aggregated summary of recent evidence
relevant to one actor &#43; one skill.

This is intended for fast runtime decisions and policy evaluation. It is
typically derived from underlying execution evidence and training/certification
events rather than being treated as the primary source of truth.

The effective aggregation window is policy-dependent. For example, a policy
may consider only the last N executions, the last N days, or all evidence
since the most recent certification.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| success_count | [int32](#int32) |  | Aggregated successful executions/evidence in the active evaluation window. |
| failure_count | [int32](#int32) |  | Aggregated failed executions/evidence in the active evaluation window. |
| last_success_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| last_failure_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| last_activity_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| rolling_success_rate | [float](#float) |  | Optional derived metric in [0,1]. |






<a name="capability-v1-ValidityPolicyRef"></a>

### ValidityPolicyRef
ValidityPolicyRef identifies the policy definition and version currently used
to derive validity, degradation, and recovery behavior for this actor skill.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| policy_id | [string](#string) |  |  |
| version | [string](#string) |  |  |





 


<a name="capability-v1-SkillInvalidityReason"></a>

### SkillInvalidityReason
SkillInvalidityReason explains why an actor skill is currently restricted,
expired, or otherwise not fully valid.

These reasons are intended to be stable, machine-readable summary codes that
can be shown in UI, used in loaders/runtime checks, and derived from evidence,
policy evaluation, or engineering-change events.

| Name | Number | Description |
| ---- | ------ | ----------- |
| SKILL_INVALIDITY_REASON_UNSPECIFIED | 0 |  |
| SKILL_INVALIDITY_REASON_INACTIVITY | 1 | The skill has degraded due to lack of recent practice or evidence of use.

Typical examples: - no executions in the active policy window - no recent successful evidence for the skill |
| SKILL_INVALIDITY_REASON_FAILURE_RATE | 2 | The skill is restricted or invalid because observed failure rate or quality performance exceeded the allowed threshold.

Typical examples: - too many failed executions in the recent window - too many out-of-tolerance results - too many inspection failures or retries |
| SKILL_INVALIDITY_REASON_POLICY_EXPIRED | 3 | The governing validity/certification policy has expired the skill based on time or other policy-defined rules.

Typical examples: - certification period elapsed - revalidation deadline passed |
| SKILL_INVALIDITY_REASON_ENGINEERING_CHANGE | 4 | The skill has been invalidated because a relevant engineering or process change means previous validation/training can no longer be trusted.

Typical examples: - tool model or capability changed - torque/program parameters changed - product revision changed - robot program or fixture configuration changed |



<a name="capability-v1-SkillLevel"></a>

### SkillLevel
Alternative categories:
AWARE: Understands concept
ASSISTED: Can perform with guidance
COMPETENT: Can perform independently
EXPERT: Can troubleshoot and optimize
CERTIFIED: Officially qualified

| Name | Number | Description |
| ---- | ------ | ----------- |
| SKILL_LEVEL_UNSPECIFIED | 0 |  |
| SKILL_LEVEL_NOT_ALLOWED | 1 | Human: Untrained, Robot: Not programmed |
| SKILL_LEVEL_ASSISTED | 2 | Human: AR-guided, Robot: Supervised execution |
| SKILL_LEVEL_QUALIFIED | 3 | Human: Certified operator, Robot: validated program |
| SKILL_LEVEL_EXPERT | 4 | Human: Technician, Robot: Optimized &amp; adaptive |
| SKILL_LEVEL_AUTHORITY | 5 | Human: Trainer, Robot: Self-adjusting |



<a name="capability-v1-SkillNextAction"></a>

### SkillNextAction
SkillNextAction describes the recommended next action needed to restore,
strengthen, or safely compensate for a restricted/expired skill.

These actions are intended to be stable, machine-readable guidance codes that
can be surfaced in UI and used by operational workflows.

| Name | Number | Description |
| ---- | ------ | ----------- |
| SKILL_NEXT_ACTION_UNSPECIFIED | 0 |  |
| SKILL_NEXT_ACTION_MICRO_TRAINING | 1 | A short targeted intervention is recommended before normal independent use.

Typical examples: - brief AR-guided walkthrough - quick reminder of the critical steps - short digital refresher module |
| SKILL_NEXT_ACTION_REFRESHER_TRAINING | 2 | A broader retraining session is recommended because the skill has degraded beyond what a short intervention should address.

Typical examples: - instructor-led refresher - extended guided practice - retraining on updated process/tooling |
| SKILL_NEXT_ACTION_RE_CERTIFICATION | 3 | Formal re-certification or re-validation is required before the skill can return to normal unrestricted use.

Typical examples: - certification renewal - formal competency check - validated robot/program re-approval |
| SKILL_NEXT_ACTION_EXTRA_VALIDATION_REQUIRED | 4 | Additional runtime validation must be performed before or during task execution to safely use the skill in its current state.

Typical examples: - second check required - vision/tool confirmation required - extra verification step before completion |
| SKILL_NEXT_ACTION_SUPERVISOR_APPROVAL_REQUIRED | 5 | Supervisor or responsible authority approval is required before the actor may execute tasks relying on this skill.

Typical examples: - technician sign-off - team lead approval - engineering approval for temporary restricted use |



<a name="capability-v1-SkillStatus"></a>

### SkillStatus
SkillStatus describes the current usability of an actor&#39;s skill.

The status is operational and should be interpreted together with the
associated policy, validity timestamps, and any derived restrictions.

Typical semantics:
- ACTIVE      -&gt; skill is fully usable
- RESTRICTED  -&gt; skill is usable, but only under additional runtime
                 safeguards such as AR guidance, extra validation,
                 supervision, or other assistance
- EXPIRED     -&gt; skill is no longer valid and must not be used

Loaders and runtime planners should therefore treat:
- ACTIVE     -&gt; feasible
- RESTRICTED -&gt; feasible with restrictions
- EXPIRED    -&gt; infeasible

| Name | Number | Description |
| ---- | ------ | ----------- |
| SKILL_STATUS_UNSPECIFIED | 0 |  |
| SKILL_STATUS_ACTIVE | 1 | Skill is valid and can be used normally. |
| SKILL_STATUS_RESTRICTED | 2 | Skill is allowed but restricted. The actor may perform the task but additional safeguards

Examples: - AR guidance required - manual confirmation required - second check required - supervisor approval required |
| SKILL_STATUS_EXPIRED | 3 | Skill is no longer valid and cannot be used. |


 

 

 



<a name="capability_v1_capability_profile-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## capability/v1/capability_profile.proto



<a name="capability-v1-CapabilityProfile"></a>

### CapabilityProfile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min_force_n | [double](#double) |  |  |
| max_force_n | [double](#double) |  |  |
| min_torque_nm | [double](#double) |  |  |
| max_torque_nm | [double](#double) |  |  |
| repeatability_mm | [double](#double) |  |  |
| max_payload_g | [double](#double) |  |  |
| min_grip_width_mm | [double](#double) |  |  |
| max_grip_width_mm | [double](#double) |  |  |
| constraints | [common.v1.KeyValueConstraint](#common-v1-KeyValueConstraint) | repeated |  |





 

 

 

 



<a name="capability_v1_skill_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## capability/v1/skill_definition.proto



<a name="capability-v1-SkillDefinition"></a>

### SkillDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| domain | [SkillDomain](#capability-v1-SkillDomain) |  |  |
| tool_roles | [ToolRole](#capability-v1-ToolRole) | repeated |  |
| safety_relevance | [common.v1.SafetyRelevance](#common-v1-SafetyRelevance) |  |  |
| default_validity_policy | [ValidityPolicyRef](#capability-v1-ValidityPolicyRef) |  | default validity policy |
| standard_worker_skill | [bool](#bool) |  | Automatically add this skill to a worker when the worker is created |
| standard_robot_skill | [bool](#bool) |  | Automatically add this skill to a robot when the robot is created |






<a name="capability-v1-SkillDefinitions"></a>

### SkillDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [SkillDefinition](#capability-v1-SkillDefinition) | repeated |  |





 


<a name="capability-v1-SkillDomain"></a>

### SkillDomain
SkillDomain classifies a skill according to the type of work it primarily
represents. Domains are used for:
- organizing skills in UIs and editors
- filtering skills during task authoring
- reasoning about capabilities during planning and assignment

A domain does NOT define the exact operation itself (that is done by the
skill), but rather the general category of work the skill belongs to.

Domains should remain stable and relatively few in number, since they
typically appear in filters, dashboards, and analytics.

| Name | Number | Description |
| ---- | ------ | ----------- |
| SKILL_DOMAIN_UNSPECIFIED | 0 | Default value when the domain is unknown or not yet assigned. |
| SKILL_DOMAIN_HANDLING | 1 | General physical handling of parts, tools, or materials.

Examples: - gripping or stabilizing a workpiece - positioning a component - moving or placing a part - cleaning or wiping surfaces

This domain typically involves manipulation rather than modification. |
| SKILL_DOMAIN_ASSEMBLY | 2 | Mechanical assembly operations that combine components into an assembly.

Examples: - inserting components - aligning parts - mounting subassemblies - press-fitting components

Assembly usually precedes fastening or validation steps. |
| SKILL_DOMAIN_FASTENING | 3 | Operations involving threaded fasteners or torque-controlled joining.

Examples: - tightening bolts or screws - loosening fasteners - torque verification

This domain is separated from general assembly because fastening frequently requires specialized tools, torque control, and validation. |
| SKILL_DOMAIN_INSPECTION | 4 | Inspection, verification, and quality assurance activities.

Examples: - visual inspection - detecting part presence - measuring dimensions - verifying assembly completion

These skills are often used for validation steps within processes. |
| SKILL_DOMAIN_ELECTRICAL | 5 | Tasks involving electrical or electronic components and systems.

Examples: - connecting electrical components - handling ESD-sensitive parts - interacting with electrical assemblies or wiring

This domain may impose additional safety or handling constraints. |
| SKILL_DOMAIN_COLLABORATION | 6 | Skills related to coordination between multiple actors.

Examples: - human–robot collaboration - synchronized operations - shared workspace interactions

These skills are important when tasks involve cooperation between humans, robots, or automated equipment. |
| SKILL_DOMAIN_SAFETY | 7 | Safety-critical skills required to safely perform certain operations.

Examples: - interacting with safety systems - operating within guarded environments - acknowledging safety procedures

These skills may represent certifications or required training. |
| SKILL_DOMAIN_ROBOT_OPERATION | 8 | Skills related to operating, supervising, or interacting with robots.

Examples: - executing robot motion - supervising automated tasks - operating robot interfaces

This domain is particularly relevant in human-robot collaboration environments. |



<a name="capability-v1-ToolRole"></a>

### ToolRole


| Name | Number | Description |
| ---- | ------ | ----------- |
| TOOL_ROLE_UNSPECIFIED | 0 |  |
| TOOL_ROLE_GRIP_WORKPIECE | 1 |  |
| TOOL_ROLE_POSITION_COMPONENT | 2 |  |
| TOOL_ROLE_ALIGN_COMPONENT | 3 |  |
| TOOL_ROLE_APPLY_TORQUE | 4 |  |
| TOOL_ROLE_APPLY_LINEAR_FORCE | 5 |  |
| TOOL_ROLE_MEASURE_DIMENSION | 6 |  |
| TOOL_ROLE_DETECT_PRESENCE | 7 |  |
| TOOL_ROLE_DISPENSE_MATERIAL | 8 |  |
| TOOL_ROLE_EXECUTE_MOTION | 9 |  |
| TOOL_ROLE_SAFETY_INTERACTION | 10 |  |
| TOOL_ROLE_HANDLE_ESD | 11 |  |
| TOOL_ROLE_VISUAL_INSPECTION | 12 |  |
| TOOL_ROLE_WIPE_CLEAN | 13 |  |


 

 

 



<a name="capability_v1_skill_requirement-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## capability/v1/skill_requirement.proto



<a name="capability-v1-SkillRequirement"></a>

### SkillRequirement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| skill_id | [string](#string) |  |  |
| minimum_level | [SkillLevel](#capability-v1-SkillLevel) |  |  |
| constraints | [common.v1.KeyValueConstraint](#common-v1-KeyValueConstraint) | repeated |  |





 

 

 

 



<a name="capability_v1_tool_requirement-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## capability/v1/tool_requirement.proto



<a name="capability-v1-ToolRequirement"></a>

### ToolRequirement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| roles | [ToolRole](#capability-v1-ToolRole) | repeated |  |
| required_properties | [ToolProperty](#capability-v1-ToolProperty) | repeated |  |
| minimum_capability | [CapabilityProfile](#capability-v1-CapabilityProfile) |  |  |
| allowed_tool_definition_ids | [string](#string) | repeated |  |





 


<a name="capability-v1-ToolProperty"></a>

### ToolProperty


| Name | Number | Description |
| ---- | ------ | ----------- |
| TOOL_PROPERTY_UNSPECIFIED | 0 |  |
| TOOL_PROPERTY_TORQUE_CONTROLLED | 1 |  |
| TOOL_PROPERTY_ESD_SAFE | 2 |  |
| TOOL_PROPERTY_INSULATED | 3 |  |
| TOOL_PROPERTY_COLLABORATIVE_SAFE | 4 |  |
| TOOL_PROPERTY_CALIBRATED | 5 |  |
| TOOL_PROPERTY_QUICK_CHANGE | 6 |  |


 

 

 



<a name="capability_v1_validity_policy-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## capability/v1/validity_policy.proto



<a name="capability-v1-ValidityPolicies"></a>

### ValidityPolicies



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ValidityPolicy](#capability-v1-ValidityPolicy) | repeated |  |






<a name="capability-v1-ValidityPolicy"></a>

### ValidityPolicy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| version | [string](#string) |  |  |





 

 

 

 



<a name="common_v1_custom_properties-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/custom_properties.proto



<a name="common-v1-CustomProperties"></a>

### CustomProperties



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| properties | [Property](#common-v1-Property) | repeated |  |





 

 

 

 



<a name="common_v1_delete-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/delete.proto



<a name="common-v1-DeleteMessage"></a>

### DeleteMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  | Id of the entity to be deleted |
| message | [string](#string) |  | Optional message |





 

 

 

 



<a name="common_v1_display_text-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/display_text.proto



<a name="common-v1-DisplayText"></a>

### DisplayText



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| title | [string](#string) |  |  |
| description | [string](#string) |  |  |
| operator_instruction | [string](#string) |  |  |





 

 

 

 



<a name="common_v1_empty-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/empty.proto



<a name="common-v1-EmptyMessage"></a>

### EmptyMessage






 

 

 

 



<a name="common_v1_external_references-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/external_references.proto



<a name="common-v1-ExternalReference"></a>

### ExternalReference



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| system | [string](#string) |  |  |
| external_id | [string](#string) |  |  |
| url | [string](#string) |  |  |





 

 

 

 



<a name="common_v1_get-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/get.proto



<a name="common-v1-GetByFieldMessage"></a>

### GetByFieldMessage
Used to retrieve entities which have a field with the given value. The actual field is determined by the subject, e.g. robot.field.driver


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [string](#string) |  |  |






<a name="common-v1-GetByIdMessage"></a>

### GetByIdMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ids | [string](#string) | repeated |  |






<a name="common-v1-GetMessage"></a>

### GetMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |





 

 

 

 



<a name="common_v1_ref-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/ref.proto



<a name="common-v1-NamedRef"></a>

### NamedRef



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |






<a name="common-v1-Ref"></a>

### Ref



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |





 

 

 

 



<a name="common_v1_time-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common/v1/time.proto



<a name="common-v1-EstimatedDuration"></a>

### EstimatedDuration



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| nominal_seconds | [int32](#int32) |  | Expected time in seconds |
| min_seconds | [int32](#int32) |  |  |
| max_seconds | [int32](#int32) |  |  |






<a name="common-v1-TimeWindow"></a>

### TimeWindow



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| end | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |





 

 

 

 



<a name="geometry_v1_local_target-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/local_target.proto



<a name="geometry-v1-LocalTarget"></a>

### LocalTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| anchor | [Anchor](#geometry-v1-Anchor) |  |  |
| position | [Point](#geometry-v1-Point) |  |  |
| orientation | [Quad](#geometry-v1-Quad) |  |  |





 

 

 

 



<a name="geometry_v1_wrench-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## geometry/v1/wrench.proto



<a name="geometry-v1-Wrench"></a>

### Wrench



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| force | [Vector3](#geometry-v1-Vector3) |  |  |
| torque | [Vector3](#geometry-v1-Vector3) |  |  |





 

 

 

 



<a name="plm_v1_capability-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/capability.proto



<a name="plm-v1-Capabilities"></a>

### Capabilities



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| capabilities | [Capability](#plm-v1-Capability) | repeated |  |






<a name="plm-v1-Capability"></a>

### Capability



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| agent_id | [string](#string) |  | Id of the agent (either an operator or robot) |
| part_id | [string](#string) |  | Id of the part that the agent can handle |
| estimated_time | [int64](#int64) |  | Estimated time to complete a task with that part |





 

 

 

 



<a name="plm_v1_fixture-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/fixture.proto



<a name="plm-v1-FixtureMessage"></a>

### FixtureMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [FixtureType](#plm-v1-FixtureType) |  |  |
| accepted_part_ids | [string](#string) | repeated |  |






<a name="plm-v1-FixtureMessages"></a>

### FixtureMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fixtures | [FixtureMessage](#plm-v1-FixtureMessage) | repeated |  |





 


<a name="plm-v1-FixtureType"></a>

### FixtureType


| Name | Number | Description |
| ---- | ------ | ----------- |
| FIXTURE_TYPE_UNSPECIFIED | 0 |  |


 

 

 



<a name="plm_v1_process_abort-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/process_abort.proto



<a name="plm-v1-ProcessAbortMessage"></a>

### ProcessAbortMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| reason | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_sequence-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/sequence.proto



<a name="plm-v1-SequenceMessage"></a>

### SequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| offset | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| parent_id | [string](#string) |  |  |
| sequence_ids | [string](#string) | repeated |  |
| task_ids | [string](#string) | repeated |  |
| assigned_to | [string](#string) | repeated |  |
| state | [SequenceState](#plm-v1-SequenceState) |  |  |
| completed_tasks | [int32](#int32) |  |  |
| can_bulk_complete | [bool](#bool) |  |  |






<a name="plm-v1-SequenceUpdatedMessage"></a>

### SequenceUpdatedMessage
Update published when the state of a sequence have changed


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sequence_id | [string](#string) |  |  |
| assigned_to | [string](#string) | repeated |  |
| state | [SequenceState](#plm-v1-SequenceState) |  |  |
| completed_tasks | [int32](#int32) |  |  |





 


<a name="plm-v1-SequenceState"></a>

### SequenceState


| Name | Number | Description |
| ---- | ------ | ----------- |
| SEQUENCE_STATE_UNSPECIFIED | 0 |  |
| SEQUENCE_STATE_MISSING_PRECONDITION | 1 |  |
| SEQUENCE_STATE_WAITING | 2 |  |
| SEQUENCE_STATE_IN_PROGRESS | 3 |  |
| SEQUENCE_STATE_COMPLETED | 4 |  |


 

 

 



<a name="plm_v1_task-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/task.proto



<a name="plm-v1-TaskMessage"></a>

### TaskMessage
TODO: add required skill?
TODO: add tool_role?
TODO: add validation
TODO: add allowed_actors


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| instruction_text | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| part_id | [string](#string) |  |  |
| model_id | [string](#string) |  |  |
| task_type | [TaskType](#plm-v1-TaskType) |  |  |
| target | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| approach | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| parent_id | [string](#string) |  |  |
| agents_ids | [string](#string) | repeated |  |
| assigned_to | [string](#string) |  |  |
| state | [TaskState](#plm-v1-TaskState) |  |  |
| preconditions | [string](#string) | repeated |  |
| dependants | [string](#string) | repeated |  |
| assignment_preference | [TaskAssignmentPreference](#plm-v1-TaskAssignmentPreference) |  |  |
| can_reassign | [bool](#bool) |  |  |
| can_do | [bool](#bool) |  |  |
| can_undo | [bool](#bool) |  |  |
| horizon | [int32](#int32) |  | TODO: &#39;complete-importance&#39;: could be different levels of &#34;this must be explicitly completed&#34; or tie it together with user level, such that expertise level (expert, intermediate, novice) equal and above intermediate can {bulk, automatic, ... } complete and below must explicitly complete. This should potentially also be tied to the part and this field(s) can then be a custom override for this specific task.

steps needed to complete before this step is workable. Could be use to better calculate what task to do next, especially if paired with time estimate for each task. |
| estimated_completion_time | [int32](#int32) |  | estimated time to complete (in seconds) |






<a name="plm-v1-TaskUpdatedMessage"></a>

### TaskUpdatedMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| assigned_to | [string](#string) |  |  |
| state | [TaskState](#plm-v1-TaskState) |  |  |
| can_reassign | [bool](#bool) |  |  |
| can_do | [bool](#bool) |  |  |
| can_undo | [bool](#bool) |  |  |





 


<a name="plm-v1-TaskAssignmentPreference"></a>

### TaskAssignmentPreference


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_ASSIGNMENT_PREFERENCE_UNSPECIFIED | 0 |  |
| TASK_ASSIGNMENT_PREFERENCE_PREFER_HUMAN | 1 |  |
| TASK_ASSIGNMENT_PREFERENCE_ONLY_HUMAN | 2 |  |
| TASK_ASSIGNMENT_PREFERENCE_PREFER_ROBOT | 3 |  |
| TASK_ASSIGNMENT_PREFERENCE_ONLY_ROBOT | 4 |  |



<a name="plm-v1-TaskState"></a>

### TaskState


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_STATE_UNSPECIFIED | 0 |  |
| TASK_STATE_MISSING_PRECONDITION | 1 |  |
| TASK_STATE_WAITING | 2 |  |
| TASK_STATE_IN_PROGRESS | 3 |  |
| TASK_STATE_COMPLETED | 4 |  |
| TASK_STATE_ERROR | 6 |  |



<a name="plm-v1-TaskType"></a>

### TaskType


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_TYPE_UNSPECIFIED | 0 |  |
| TASK_TYPE_INSPECT | 1 |  |
| TASK_TYPE_FASTEN | 2 |  |
| TASK_TYPE_UNFASTEN | 3 |  |
| TASK_TYPE_MOUNT | 4 |  |
| TASK_TYPE_UNMOUNT | 5 |  |
| TASK_TYPE_MOVE | 6 |  |
| TASK_TYPE_REMOVE | 7 |  |
| TASK_TYPE_APPLY | 8 |  |
| TASK_TYPE_WIPE | 9 |  |


 

 

 



<a name="plm_v1_process_old-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/process_old.proto



<a name="plm-v1-ProcessMessage"></a>

### ProcessMessage
TODO: should &#39;running&#39; be called process and &#39;static&#39; recipe?
TODO: Add/assign the agent(s) at runtime, instead of allocating them to the environment. THen there could also be a situation where each agent is asked to take a task during execution.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| instance_id | [string](#string) |  |  |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#plm-v1-ProcessType) |  |  |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| root_sequence_id | [string](#string) |  |  |
| sequences | [SequenceMessage](#plm-v1-SequenceMessage) | repeated |  |
| tasks | [TaskMessage](#plm-v1-TaskMessage) | repeated |  |
| state | [ProcessState](#plm-v1-ProcessState) |  |  |
| initiated | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| ended | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| order_id | [string](#string) |  |  |
| line_id | [string](#string) |  |  |






<a name="plm-v1-ProcessMessages"></a>

### ProcessMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| processes | [ProcessMessage](#plm-v1-ProcessMessage) | repeated |  |






<a name="plm-v1-ProcessUpdatedMessage"></a>

### ProcessUpdatedMessage
Update published when the state of a process have changed


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| instance_id | [string](#string) |  |  |
| id | [string](#string) |  |  |
| state | [ProcessState](#plm-v1-ProcessState) |  |  |
| ended | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |





 


<a name="plm-v1-ProcessState"></a>

### ProcessState


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_STATE_UNSPECIFIED | 0 |  |
| PROCESS_STATE_WAITING | 1 |  |
| PROCESS_STATE_IN_PROGRESS | 2 |  |
| PROCESS_STATE_COMPLETED | 3 |  |
| PROCESS_STATE_ABORTED | 4 |  |



<a name="plm-v1-ProcessType"></a>

### ProcessType


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_TYPE_UNSPECIFIED | 0 |  |
| PROCESS_TYPE_ASSEMBLY | 1 |  |
| PROCESS_TYPE_DISASSEMBLY | 2 |  |
| PROCESS_TYPE_INSPECTION | 3 | TODO: what should this be? |
| PROCESS_TYPE_CHECKLIST | 4 | TODO: this could be startup procedures, fault fixing, ... |


 

 

 



<a name="plm_v1_process_authoring-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/process_authoring.proto



<a name="plm-v1-NewProcessMessage"></a>

### NewProcessMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#plm-v1-ProcessType) |  |  |






<a name="plm-v1-StoredProcessMessage"></a>

### StoredProcessMessage
TODO: rename to recipe?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#plm-v1-ProcessType) |  |  |
| fixture_offset | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| root_sequence_id | [string](#string) |  | TODO: add calculated customization possibilities (or something like that) Then when loadProcess is called, a list with selected IDS must be selected/send with |






<a name="plm-v1-StoredProcessMessages"></a>

### StoredProcessMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| processes | [StoredProcessMessage](#plm-v1-StoredProcessMessage) | repeated |  |






<a name="plm-v1-UpdateProcessMessage"></a>

### UpdateProcessMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#plm-v1-ProcessType) |  |  |
| fixture_offset | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| root_sequence_id | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_process_load-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/process_load.proto



<a name="plm-v1-ProcessLoadMessage"></a>

### ProcessLoadMessage
TODO: Assign agents at runtime?


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| process_id | [string](#string) |  |  |
| line_id | [string](#string) |  |  |
| order_id | [string](#string) |  |  |
| allocation_strategy | [AllocationStrategy](#plm-v1-AllocationStrategy) |  | TODO: list participating actors? |





 


<a name="plm-v1-AllocationStrategy"></a>

### AllocationStrategy


| Name | Number | Description |
| ---- | ------ | ----------- |
| ALLOCATION_STRATEGY_UNSPECIFIED | 0 |  |
| ALLOCATION_STRATEGY_STATIC | 1 |  |


 

 

 



<a name="plm_v1_requests-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/requests.proto



<a name="plm-v1-ProcessAtLocationMessage"></a>

### ProcessAtLocationMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| location_id | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_sequence_authoring-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/sequence_authoring.proto



<a name="plm-v1-NewSequenceMessage"></a>

### NewSequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |






<a name="plm-v1-StoredSequenceMessage"></a>

### StoredSequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| offset | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| sequence_ids | [string](#string) | repeated |  |
| task_ids | [string](#string) | repeated |  |
| can_bulk_complete | [bool](#bool) |  | TODO: if variant (or something) to allow for customizeable products |






<a name="plm-v1-StoredSequenceMessages"></a>

### StoredSequenceMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sequences | [StoredSequenceMessage](#plm-v1-StoredSequenceMessage) | repeated |  |






<a name="plm-v1-UpdateSequenceMessage"></a>

### UpdateSequenceMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| offset | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| sequence_ids | [string](#string) | repeated |  |
| task_ids | [string](#string) | repeated |  |
| can_bulk_complete | [bool](#bool) |  |  |





 


<a name="plm-v1-SequenceType"></a>

### SequenceType


| Name | Number | Description |
| ---- | ------ | ----------- |
| SEQUENCE_TYPE_UNSPECIFIED | 0 |  |
| SEQUENCE_TYPE_ALL_OF_CHILDREN | 1 |  |
| SEQUENCE_TYPE_ONE_OF_CHILDREN | 2 |  |


 

 

 



<a name="plm_v1_sequence_complete-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/sequence_complete.proto



<a name="plm-v1-SequenceBulkCompleteMessage"></a>

### SequenceBulkCompleteMessage
Complete all tasks or or sub-sequences (TODO: should that be possible?)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| sequence_id | [string](#string) |  |  |
| agent_id | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_sequence_reassign-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/sequence_reassign.proto



<a name="plm-v1-SequenceReassignMessage"></a>

### SequenceReassignMessage
Reassign all sub-tasks to the assignee (if possible)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| sequence_id | [string](#string) |  |  |
| assignee | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_task_authoring-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/task_authoring.proto



<a name="plm-v1-NewTaskMessage"></a>

### NewTaskMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| parent_id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |






<a name="plm-v1-StoredTaskMessage"></a>

### StoredTaskMessage
TODO: can this be made more generic, e.g. from a different pool of &#39;actions&#39; (screw, mount, ….), instead of creating a new stored step for each actual step.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| instruction_text | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| part_id | [string](#string) |  |  |
| model_id | [string](#string) |  |  |
| task_type | [TaskType](#plm-v1-TaskType) |  |  |
| target | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| approach | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| assignment_preference | [TaskAssignmentPreference](#plm-v1-TaskAssignmentPreference) |  |  |






<a name="plm-v1-StoredTaskMessages"></a>

### StoredTaskMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tasks | [StoredTaskMessage](#plm-v1-StoredTaskMessage) | repeated |  |






<a name="plm-v1-UpdateTaskMessage"></a>

### UpdateTaskMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| instruction_text | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| part_id | [string](#string) |  | TODO: what is the difference between part_id and model_id? doesn&#39;t all parts have a model? |
| model_id | [string](#string) |  |  |
| task_type | [TaskType](#plm-v1-TaskType) |  |  |
| target | [geometry.v1.Pose](#geometry-v1-Pose) |  |  |
| approach | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |
| assignment_preference | [TaskAssignmentPreference](#plm-v1-TaskAssignmentPreference) |  |  |





 

 

 

 



<a name="plm_v1_task_progress-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/task_progress.proto



<a name="plm-v1-TaskProgressMessage"></a>

### TaskProgressMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| task_id | [string](#string) |  |  |
| agent_id | [string](#string) |  |  |
| message | [string](#string) |  |  |
| elapsed_time | [int32](#int32) |  | elapsed time in seconds |
| estimated_time_left | [int32](#int32) |  | estimated time left in seconds |





 

 

 

 



<a name="plm_v1_task_reassign-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/task_reassign.proto



<a name="plm-v1-TaskReassignMessage"></a>

### TaskReassignMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| task_id | [string](#string) |  |  |
| assignee | [string](#string) |  |  |





 

 

 

 



<a name="plm_v1_task_state_change-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/task_state_change.proto



<a name="plm-v1-TaskStateChangeMessage"></a>

### TaskStateChangeMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| task_id | [string](#string) |  |  |
| state | [TaskStateRequest](#plm-v1-TaskStateRequest) |  |  |





 


<a name="plm-v1-TaskStateRequest"></a>

### TaskStateRequest


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_STATE_REQUEST_UNSPECIFIED | 0 |  |
| TASK_STATE_REQUEST_IN_PROGRESS | 3 |  |
| TASK_STATE_REQUEST_COMPLETED | 4 |  |
| TASK_STATE_REQUEST_UNDO | 5 |  |
| TASK_STATE_REQUEST_ERROR | 6 |  |


 

 

 



<a name="plm_v1_tasks_list-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## plm/v1/tasks_list.proto



<a name="plm-v1-TasksForAgentRequest"></a>

### TasksForAgentRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| agent_id | [string](#string) |  |  |
| state | [TaskState](#plm-v1-TaskState) |  | Filter based on state. 0 (unspecified) returns all |






<a name="plm-v1-TasksForAgentResponse"></a>

### TasksForAgentResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| instance_id | [string](#string) |  |  |
| agent_id | [string](#string) |  |  |
| task_ids | [string](#string) | repeated |  |





 

 

 

 



<a name="process_v1_sequence_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## process/v1/sequence_definition.proto



<a name="process-v1-SequenceDefinition"></a>

### SequenceDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| sequence_number | [int32](#int32) |  |  |
| parent_sequence_id | [string](#string) |  |  |
| operator | [SequenceOperator](#process-v1-SequenceOperator) |  |  |
| child_sequence_ids | [string](#string) | repeated |  |
| child_task_ids | [string](#string) | repeated |  |
| local_target | [geometry.v1.LocalTarget](#geometry-v1-LocalTarget) |  |  |
| optional | [bool](#bool) |  |  |
| can_bulk_complete | [bool](#bool) |  |  |






<a name="process-v1-SequenceDefinitions"></a>

### SequenceDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [SequenceDefinition](#process-v1-SequenceDefinition) | repeated |  |





 


<a name="process-v1-SequenceOperator"></a>

### SequenceOperator
Defines how the children of a SequenceDefinition are executed and how the
sequence determines completion.

A sequence may contain both child sequences and tasks. The operator
determines the control-flow semantics for those children.

| Name | Number | Description |
| ---- | ------ | ----------- |
| SEQUENCE_OPERATOR_UNSPECIFIED | 0 | Default / undefined behavior.

Should normally not appear in valid process definitions. Runtimes may treat this as SEQUENCE for backward compatibility or reject the recipe during validation. |
| SEQUENCE_OPERATOR_ORDERED | 1 | Children execute sequentially in the order they are defined.

Each child starts only after the previous child has completed. The sequence completes when the final child completes.

Example: Pick part → Align part → Fasten part → Inspect assembly |
| SEQUENCE_OPERATOR_PARALLEL | 2 | All children may execute concurrently.

The runtime may start all children at the same time if resources allow. The sequence completes only when all children have completed.

This operator is commonly used for human-robot collaboration or when multiple independent tasks can be performed in parallel.

Example: Robot holds component Human installs screws Vision system verifies alignment |
| SEQUENCE_OPERATOR_EXCLUSIVE | 3 | Exactly one child is selected and executed.

The runtime chooses a single branch based on conditions such as: - variant configuration - resource availability - actor capabilities - runtime decision logic

The sequence completes when the selected child completes.

Example: Robot tightening procedure OR Human tightening procedure |
| SEQUENCE_OPERATOR_INCLUSIVE | 4 | One or more children may execute.

The runtime evaluates each child independently and may execute any subset of them based on conditions such as variant configuration, process parameters, or runtime state.

The sequence completes when all selected children have completed.

Example: Optional inspections: - Visual inspection - Torque verification - Leak test |


 

 

 



<a name="resources_v1_asset_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/asset_definition.proto



<a name="resources-v1-AssetDefinition"></a>

### AssetDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  | Name of the asset |
| icon | [string](#string) |  | Optional icon representing the asset |
| description | [string](#string) |  | Optional description of the asset |
| type | [AssetType](#resources-v1-AssetType) |  |  |
| driver_type | [AssetDriverType](#resources-v1-AssetDriverType) |  |  |
| model_id | [string](#string) |  |  |
| vision | [VisionCapability](#resources-v1-VisionCapability) |  |  |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-AssetDefinitions"></a>

### AssetDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [AssetDefinition](#resources-v1-AssetDefinition) | repeated |  |






<a name="resources-v1-VisionCapability"></a>

### VisionCapability



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| supported_validation_modes | [ValidationMode](#resources-v1-ValidationMode) | repeated |  |
| supported_part_definition_ids | [string](#string) | repeated |  |
| supported_task_type_ids | [string](#string) | repeated |  |
| constraints | [common.v1.KeyValueConstraint](#common-v1-KeyValueConstraint) | repeated |  |





 


<a name="resources-v1-AssetDriverType"></a>

### AssetDriverType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ASSET_DRIVER_TYPE_UNSPECIFIED | 0 |  |
| ASSET_DRIVER_TYPE_DEFAULT | 1 |  |



<a name="resources-v1-AssetType"></a>

### AssetType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ASSET_TYPE_UNSPECIFIED | 0 |  |
| ASSET_TYPE_CAMERA | 1 | Vision device used for inspection, guidance, or detection. |
| ASSET_TYPE_LIGHT | 2 | Lighting device such as ring light, spot light, or backlight. |
| ASSET_TYPE_CONVEYOR | 3 | Conveying device used to move workpieces or pallets between areas. |
| ASSET_TYPE_SENSOR | 4 | Generic sensor asset such as prox sensor, load cell, scanner, or IO sensor. |
| ASSET_TYPE_HMI | 5 | Human-machine interface such as touch panel, button box, or stack-light UI endpoint. |
| ASSET_TYPE_PART_FEEDER | 8 | Feeder/presentation device used to supply parts in a controlled way. |



<a name="resources-v1-ValidationMode"></a>

### ValidationMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| VALIDATION_MODE_UNSPECIFIED | 0 |  |
| VALIDATION_MODE_PRESENCE_CHECK | 1 |  |
| VALIDATION_MODE_POSE_CHECK | 2 |  |
| VALIDATION_MODE_FASTENER_CHECK | 3 |  |
| VALIDATION_MODE_LABEL_CHECK | 4 |  |
| VALIDATION_MODE_SURFACE_CHECK | 5 |  |


 

 

 



<a name="resources_v1_container_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/container_definition.proto



<a name="resources-v1-ContainerDefinition"></a>

### ContainerDefinition
ContainerDefinition describes a physical holder/carrier with one or more slots.

This unifies what used to be modeled separately as fixtures, kit trays, storage
bins, and trays/totes. The semantic differences are captured by ContainerType and
ContainerSlotType rather than by separate top-level resources.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  | Stable identifier of the reusable container definition. |
| name | [string](#string) |  | Display name, e.g. &#34;Shelf Bin 01&#34;, &#34;Starter Kit Tray&#34;, or &#34;Motor Pallet&#34;. |
| icon | [string](#string) |  | UI icon representing the container. |
| description | [string](#string) |  | Human-readable description of the container&#39;s purpose. |
| type | [ContainerType](#resources-v1-ContainerType) |  | High-level category: storage, kit, tray, or fixture. |
| model_id | [string](#string) |  | Optional 3D model used in simulation, AR, and UI rendering. |
| slots | [ContainerSlotDefinition](#resources-v1-ContainerSlotDefinition) | repeated | Addressable places inside/on the container. |
| constraints | [common.v1.KeyValueConstraint](#common-v1-KeyValueConstraint) | repeated | Container-level constraints applying to the whole carrier. |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  | Extension point for domain-specific container metadata. |






<a name="resources-v1-ContainerDefinitions"></a>

### ContainerDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ContainerDefinition](#resources-v1-ContainerDefinition) | repeated | List wrapper used for transport/query responses. |






<a name="resources-v1-ContainerSlotDefinition"></a>

### ContainerSlotDefinition
ContainerSlotDefinition describes one addressable place inside a container.

A slot is the thing that operators, robots, and AR guidance normally target.
Examples:
- a shelf bin in storage
- a logical slot in a kit
- a tray pocket
- a fixture nest / clamp position / pallet pocket


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  | Stable identifier unique within the parent container definition. |
| name | [string](#string) |  | Human-readable slot name shown in UI and AR, e.g. &#34;Slot A&#34; or &#34;Motor Nest&#34;. |
| icon | [string](#string) |  | Optional icon override for UIs. If empty, the container icon may be reused. |
| description | [string](#string) |  | Optional longer description of the slot&#39;s purpose or usage constraints. |
| pose | [geometry.v1.Pose](#geometry-v1-Pose) |  | Pose of the slot relative to the container definition coordinate frame. |
| size | [geometry.v1.Vector3](#geometry-v1-Vector3) |  | Optional approximate slot extents/bounds, useful for UI, AR, and planning. |
| type | [ContainerSlotType](#resources-v1-ContainerSlotType) |  | Semantic role of the slot, e.g. storage bin, kit slot, tray cell, or fixture slot. |
| supported_product_definition_ids | [string](#string) | repeated | Products that this slot explicitly supports holding/presenting. |
| supported_root_part_definition_ids | [string](#string) | repeated | Root assemblies/root parts that this slot supports. |
| supported_part_definition_ids | [string](#string) | repeated | Specific part definitions that this slot supports. |
| constraints | [common.v1.KeyValueConstraint](#common-v1-KeyValueConstraint) | repeated | Additional semantic/compatibility constraints such as orientation, handedness, or required variants. |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  | Extension point for domain-specific slot data. |






<a name="resources-v1-ContainerSlotRef"></a>

### ContainerSlotRef
ContainerSlotRef points to a concrete slot on a concrete container instance.

This is the preferred task-planning reference for storage, kitting, tray, and
fixture interactions because it identifies both the physical carrier and the
addressable place inside it.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| container_instance_id | [string](#string) |  | Identifier of the container instance that owns the referenced slot. |
| slot_id | [string](#string) |  | Identifier of the slot definition within that container. |
| type | [ContainerSlotType](#resources-v1-ContainerSlotType) |  | Semantic kind of slot, used for interpretation, UI behavior, and routing. |





 


<a name="resources-v1-ContainerSlotType"></a>

### ContainerSlotType
ContainerSlotType classifies the semantic role of a slot within a container.

The slot type is what task planning, UI rendering, and robot/AR logic typically
interact with. For example, a tray and a fixture may both have slots, but their
semantics differ.

| Name | Number | Description |
| ---- | ------ | ----------- |
| CONTAINER_SLOT_TYPE_UNSPECIFIED | 0 |  |
| CONTAINER_SLOT_TYPE_STORAGE_BIN | 1 | A storage slot/bin used primarily as a source/sink location for material. |
| CONTAINER_SLOT_TYPE_KIT_SLOT | 2 | A logical slot in a kit used to collect and verify required contents. |
| CONTAINER_SLOT_TYPE_TRAY_CELL | 3 | A regular cell/pocket in a tray, tote, or carrier. |
| CONTAINER_SLOT_TYPE_FIXTURE_SLOT | 4 | A nest/clamp/jig/pallet position used to hold, present, or constrain a part/product. |



<a name="resources-v1-ContainerType"></a>

### ContainerType
ContainerType classifies physical holders/carriers used to store, stage, present,
or constrain products and parts in a station.

This unifies concepts that previously lived as separate resources such as storage
bins, kit trays, pallets, and fixtures. All of them are modeled as containers with
one or more addressable slots.

| Name | Number | Description |
| ---- | ------ | ----------- |
| CONTAINER_TYPE_UNSPECIFIED | 0 |  |
| CONTAINER_TYPE_STORAGE | 1 | A storage container used as a source/sink of material, e.g. shelf bin, drawer bin, tote, or rack bin. |
| CONTAINER_TYPE_KIT | 2 | A kit container used to collect the exact set of parts required for later work. |
| CONTAINER_TYPE_TRAY | 3 | A tray/tote/carrier with one or more regular cells or pockets. |
| CONTAINER_TYPE_FIXTURE | 4 | A workholding/presentation container such as a base, clamp, jig, or pallet. |


 

 

 



<a name="variance_v1_variant_rule-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## variance/v1/variant_rule.proto



<a name="variance-v1-VariantPredicate"></a>

### VariantPredicate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| axis_id | [string](#string) |  | Variant axis identifier, e.g. &#34;hinge_side&#34; |
| allowed_option_ids | [string](#string) | repeated | Allowed options on that axis, e.g. [&#34;left&#34;] |
| excluded_option_ids | [string](#string) | repeated | Options on that axis that must not be selected. |






<a name="variance-v1-VariantRule"></a>

### VariantRule
VariantRule: a rule matches if all predicates match


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| all_of | [VariantPredicate](#variance-v1-VariantPredicate) | repeated | All predicates must match for the rule to match. |





 

 

 

 



<a name="process_v1_task_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## process/v1/task_definition.proto



<a name="process-v1-ContainerTarget"></a>

### ContainerTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| container_definition_id | [string](#string) |  | Generic container type, e.g. pallet, tray, jig, fixture, bin. |
| slot_id | [string](#string) |  | Optional slot definition within that container definition. |
| slot_type | [resources.v1.ContainerSlotType](#resources-v1-ContainerSlotType) |  | Semantic slot kind if known. |






<a name="process-v1-ProductTarget"></a>

### ProductTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_id | [string](#string) |  | Assembly node occurrence the task acts on. |
| part_definition_id | [string](#string) |  | Optional denormalized helper. |
| local_target | [geometry.v1.LocalTarget](#geometry-v1-LocalTarget) |  | Pose/anchor relative to the chosen product reference. |






<a name="process-v1-ResourceTarget"></a>

### ResourceTarget
Generic authoring-time resource references.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| asset_definition_id | [string](#string) |  | Camera, feeder, HMI, sensor, conveyor, etc. |
| robot_definition_id | [string](#string) |  | Robot type required or referenced by the task. |
| container_definition_id | [string](#string) |  | Optional generic container used outside explicit workpiece targeting. |






<a name="process-v1-TaskDefinition"></a>

### TaskDefinition
TaskDefinition is the static/universal authoring-time description of a task.

It should remain reusable across workcells, deployments, and specific
equipment instances. Runtime-specific information such as concrete robot,
asset, station, or container bindings belongs in runtime.v1.TaskRun.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| instruction_text | [string](#string) |  | Human-readable instruction shown to the operator or author. |
| sequence_number | [int32](#int32) |  | Ordering hint within the parent sequence. |
| task_type | [TaskType](#process-v1-TaskType) |  | The semantic action to perform, e.g. FASTEN, PICK, PLACE, VERIFY. |
| target | [TaskTarget](#process-v1-TaskTarget) |  | The primary static/generic thing/location/resource this task acts on. |
| insertion_offset | [geometry.v1.Vector3](#geometry-v1-Vector3) |  | Optional static guidance/planning hint from final pose to pre-insertion pose, in mm. |
| approach_offset | [geometry.v1.Vector3](#geometry-v1-Vector3) |  | Optional static guidance/planning hint from final pose to preferred approach pose, in mm. |
| tool_requirement | [capability.v1.ToolRequirement](#capability-v1-ToolRequirement) |  | Tools or tool roles needed to perform the task. |
| skill_requirements | [capability.v1.SkillRequirement](#capability-v1-SkillRequirement) | repeated | Skills/qualifications needed by the acting human/robot. |
| validation | [ValidationRequirement](#process-v1-ValidationRequirement) |  | How task completion should be confirmed or validated. |
| execution_policy | [TaskExecutionPolicy](#process-v1-TaskExecutionPolicy) |  | Static execution policy, preferences, and permissions used by planning/runtime. |
| safety_relevance | [common.v1.SafetyRelevance](#common-v1-SafetyRelevance) |  | Safety significance of the task. |
| source | [TaskEndpoint](#process-v1-TaskEndpoint) |  | Optional static/generic source reference for move, pick/place, kitting, storage, tray, pallet, or fixture operations. |
| destination | [TaskEndpoint](#process-v1-TaskEndpoint) |  | Optional static/generic destination reference for move, pick/place, kitting, storage, tray, pallet, or fixture operations. |
| applicability | [variance.v1.VariantRule](#variance-v1-VariantRule) | repeated | Applies if any rule matches. Empty means always applicable. |
| overrides | [TaskOverride](#process-v1-TaskOverride) | repeated |  |






<a name="process-v1-TaskDefinitions"></a>

### TaskDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [TaskDefinition](#process-v1-TaskDefinition) | repeated |  |






<a name="process-v1-TaskEndpoint"></a>

### TaskEndpoint
TaskEndpoint is used for source/destination style references in tasks such
as pick/place, move, kitting, and transfer operations.

Like TaskTarget, TaskEndpoint is static/generic and should remain reusable
across workcells. Concrete runtime bindings belong in runtime.v1.TaskRun.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| product | [ProductTarget](#process-v1-ProductTarget) |  |  |
| container | [ContainerTarget](#process-v1-ContainerTarget) |  |  |






<a name="process-v1-TaskExecutionPolicy"></a>

### TaskExecutionPolicy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| assignment_preference | [TaskAssignmentPreference](#process-v1-TaskAssignmentPreference) |  |  |
| actor_constraint | [capability.v1.ActorConstraint](#capability-v1-ActorConstraint) |  |  |
| can_reassign | [bool](#bool) |  |  |
| can_do | [bool](#bool) |  |  |
| can_undo | [bool](#bool) |  |  |
| estimated_duration | [common.v1.EstimatedDuration](#common-v1-EstimatedDuration) |  |  |






<a name="process-v1-TaskOverride"></a>

### TaskOverride



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| when | [variance.v1.VariantRule](#variance-v1-VariantRule) | repeated |  |
| instruction_text | [string](#string) |  |  |
| target_node_id | [string](#string) |  |  |
| approach | [geometry.v1.Vector3](#geometry-v1-Vector3) |  |  |






<a name="process-v1-TaskTarget"></a>

### TaskTarget
TaskTarget captures the static authoring-time target of a task.

It intentionally avoids concrete runtime/deployment bindings such as
specific robot instances, camera instances, or pallet instances. Those should
instead be resolved into runtime.v1.TaskRun / TaskRuntimeBinding.

---------------------------------------------------------------------------
What the task acts on
---------------------------------------------------------------------------
These fields describe the static/generic authoring intent of the task.
They should stay reusable across workcells and deployments.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| product | [ProductTarget](#process-v1-ProductTarget) |  | Optional product-structure target. |
| container | [ContainerTarget](#process-v1-ContainerTarget) |  | Optional container/slot target. |
| resource | [ResourceTarget](#process-v1-ResourceTarget) |  | Optional generic resource target. |






<a name="process-v1-ValidationRequirement"></a>

### ValidationRequirement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| require_tool_feedback | [bool](#bool) |  |  |
| require_vision_check | [bool](#bool) |  |  |
| allow_manual_confirmation | [bool](#bool) |  |  |
| manual_confirmation_min_level | [capability.v1.SkillLevel](#capability-v1-SkillLevel) |  |  |
| mode | [resources.v1.ValidationMode](#resources-v1-ValidationMode) |  |  |
| constraints | [common.v1.KeyValueConstraint](#common-v1-KeyValueConstraint) | repeated |  |





 


<a name="process-v1-TaskAssignmentPreference"></a>

### TaskAssignmentPreference


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_ASSIGNMENT_PREFERENCE_UNSPECIFIED | 0 |  |
| TASK_ASSIGNMENT_PREFERENCE_PREFER_HUMAN | 1 |  |
| TASK_ASSIGNMENT_PREFERENCE_ONLY_HUMAN | 2 |  |
| TASK_ASSIGNMENT_PREFERENCE_PREFER_ROBOT | 3 |  |
| TASK_ASSIGNMENT_PREFERENCE_ONLY_ROBOT | 4 | Only use this if it truly must be done by a robot. Otherwise use prefer-robot |
| TASK_ASSIGNMENT_PREFERENCE_EITHER | 5 |  |



<a name="process-v1-TaskType"></a>

### TaskType


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_TYPE_UNSPECIFIED | 0 |  |
| TASK_TYPE_INSPECT | 1 |  |
| TASK_TYPE_FASTEN | 2 |  |
| TASK_TYPE_UNFASTEN | 3 |  |
| TASK_TYPE_MOUNT | 4 |  |
| TASK_TYPE_UNMOUNT | 5 |  |
| TASK_TYPE_MOVE | 6 |  |
| TASK_TYPE_REMOVE | 7 |  |
| TASK_TYPE_APPLY | 8 |  |
| TASK_TYPE_WIPE | 9 |  |
| TASK_TYPE_ALIGN | 10 |  |
| TASK_TYPE_INSERT | 11 |  |
| TASK_TYPE_HOLD | 12 |  |
| TASK_TYPE_VERIFY | 13 |  |
| TASK_TYPE_PICK | 14 |  |
| TASK_TYPE_PLACE | 15 |  |
| TASK_TYPE_SCAN | 16 |  |
| TASK_TYPE_WAIT | 17 |  |
| TASK_TYPE_CHECK | 18 |  |
| TASK_TYPE_ACKNOWLEDGE | 19 | Start, stop, reset, open, close, |


 

 

 



<a name="process_v1_process_recipe-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## process/v1/process_recipe.proto



<a name="process-v1-AddChildSequenceRequest"></a>

### AddChildSequenceRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recipe_id | [string](#string) |  |  |
| sequence_id | [string](#string) |  |  |






<a name="process-v1-AddChildTaskRequest"></a>

### AddChildTaskRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recipe_id | [string](#string) |  |  |
| sequence_id | [string](#string) |  |  |






<a name="process-v1-AddRootSequenceRequest"></a>

### AddRootSequenceRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recipe_id | [string](#string) |  |  |






<a name="process-v1-CreateProcessRecipe"></a>

### CreateProcessRecipe



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recipe | [ProcessRecipe](#process-v1-ProcessRecipe) |  |  |
| sequences | [SequenceDefinition](#process-v1-SequenceDefinition) | repeated |  |
| tasks | [TaskDefinition](#process-v1-TaskDefinition) | repeated |  |






<a name="process-v1-ProcessRecipe"></a>

### ProcessRecipe
ProcessRecipe describes the following:
- What work must be done
- What kinds of capabilities are required
- What tool roles are required
- What skills are required
- What actor constrains exist
- What validation is needed


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ProcessType](#process-v1-ProcessType) |  |  |
| product_definition_id | [string](#string) |  |  |
| applicability | [RecipeApplicability](#process-v1-RecipeApplicability) |  |  |
| root_sequence_id | [string](#string) |  |  |
| sequence_ids | [string](#string) | repeated |  |
| task_ids | [string](#string) | repeated |  |
| supported_container_definition_ids | [string](#string) | repeated | Containers (typically fixture/pallet definitions) that this recipe is intended to run with. |
| external_references | [common.v1.ExternalReference](#common-v1-ExternalReference) | repeated |  |






<a name="process-v1-ProcessRecipes"></a>

### ProcessRecipes



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ProcessRecipe](#process-v1-ProcessRecipe) | repeated |  |






<a name="process-v1-RecipeApplicability"></a>

### RecipeApplicability



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| include | [variance.v1.VariantRule](#variance-v1-VariantRule) | repeated | Recipe applies if any include rule matches. Empty means generally applicable. |
| exclude | [variance.v1.VariantRule](#variance-v1-VariantRule) | repeated | Recipe is rejected if any exclude rule matches. |






<a name="process-v1-RemoveSequenceRequest"></a>

### RemoveSequenceRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recipe_id | [string](#string) |  |  |
| sequence_id | [string](#string) |  |  |
| try_keep_children | [bool](#bool) |  | If true, all children are assign to the parent of the sequence - if the sequence have a parent |






<a name="process-v1-RemoveTaskRequest"></a>

### RemoveTaskRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recipe_id | [string](#string) |  |  |
| task_id | [string](#string) |  |  |





 


<a name="process-v1-ProcessType"></a>

### ProcessType


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_TYPE_UNSPECIFIED | 0 |  |
| PROCESS_TYPE_ASSEMBLY | 1 | Example: build gearbox |
| PROCESS_TYPE_DISASSEMBLY | 2 | Example: take mould apart for maintenance |
| PROCESS_TYPE_INSPECTION | 3 | Example: QC Check |
| PROCESS_TYPE_CHECKLIST | 4 | Example: line startup |
| PROCESS_TYPE_KITTING | 5 | Example: prepare parts kit |
| PROCESS_TYPE_MAINTENANCE | 6 | Example: replace filter |


 

 

 



<a name="variance_v1_variant_configuration-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## variance/v1/variant_configuration.proto



<a name="variance-v1-VariantConfiguration"></a>

### VariantConfiguration



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| selections | [VariantSelection](#variance-v1-VariantSelection) | repeated |  |






<a name="variance-v1-VariantSelection"></a>

### VariantSelection



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| axis_id | [string](#string) |  | &#34;hinge_side&#34; |
| option_id | [string](#string) |  | &#34;left&#34; |





 

 

 

 



<a name="process_v1_generation_requests-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## process/v1/generation_requests.proto



<a name="process-v1-DraftProcessRecipeGenerateIssue"></a>

### DraftProcessRecipeGenerateIssue
DraftProcessRecipeGenerateIssue describes a non-fatal issue or warning
encountered during recipe generation.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| message | [string](#string) |  |  |
| node_id | [string](#string) |  |  |
| part_definition_id | [string](#string) |  |  |






<a name="process-v1-DraftProcessRecipeGenerateRequest"></a>

### DraftProcessRecipeGenerateRequest
DraftProcessRecipeGenerateRequest asks the backend to generate a draft
ProcessRecipe from a ProductDefinition plus generation options.

This is intended for authoring-time generation, not runtime execution.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| product_definition_id | [string](#string) |  | The product structure that should be transformed into a draft recipe. |
| recipe_id | [string](#string) |  | Optional explicit recipe id for the generated recipe. If empty, the generator/backend may assign one. |
| recipe_name | [string](#string) |  | Human-readable name for the generated recipe. |
| recipe_icon | [string](#string) |  | Optional icon for the generated recipe. |
| recipe_description | [string](#string) |  | Optional human-readable description for the generated recipe. |
| variant_configuration | [variance.v1.VariantConfiguration](#variance-v1-VariantConfiguration) |  | Selected product variants used to filter applicability and annotate the generated recipe applicability. |
| insert_align_before_fasten_group | [bool](#bool) |  | If true, the generator may insert ALIGN tasks before grouped fastener work when that improves the generated task flow. |
| group_fasteners_threshold | [int32](#int32) |  | Minimum number of sibling fasteners required before grouping them into a shared fastener-oriented sequence. |
| group_repeated_parts_threshold | [int32](#int32) |  | Minimum number of repeated sibling parts required before grouping them into a shared repeated-parts sequence. |
| generate_verify_tasks | [bool](#bool) |  | If true, the generator may insert VERIFY tasks where appropriate. |
| prefer_move_tasks_when_possible | [bool](#bool) |  | If true, the generator may prefer MOVE tasks when the operation can be reasonably interpreted as repositioning rather than installation. |
| include_optional_nodes | [bool](#bool) |  | If true, nodes marked as optional will be included |






<a name="process-v1-DraftProcessRecipeGenerateResult"></a>

### DraftProcessRecipeGenerateResult
DraftProcessRecipeGenerateResult contains the generated draft recipe.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recipe | [ProcessRecipe](#process-v1-ProcessRecipe) |  |  |
| sequences | [SequenceDefinition](#process-v1-SequenceDefinition) | repeated |  |
| tasks | [TaskDefinition](#process-v1-TaskDefinition) | repeated |  |
| issues | [DraftProcessRecipeGenerateIssue](#process-v1-DraftProcessRecipeGenerateIssue) | repeated |  |





 

 

 

 



<a name="product_v1_assembly_node-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## product/v1/assembly_node.proto



<a name="product-v1-AssemblyNode"></a>

### AssemblyNode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  | Name of this assembly node |
| parent_node_id | [string](#string) |  | Empty if root, otherwise set to parent AssemblyNode id. |
| kind | [NodeKind](#product-v1-NodeKind) |  |  |
| part_definition_id | [string](#string) |  |  |
| override_model_id | [string](#string) |  |  |
| local_pose | [geometry.v1.Pose](#geometry-v1-Pose) |  | final pose, in mm |
| sequence_hint | [int32](#int32) |  | repeated string child_node_ids = 8; // Children of this node, their parent_node_id must be set to this.id |
| cad_occurrence_path | [string](#string) |  | CAD/BOM path if available, e.g. &#34;TopAssembly/DriveUnit:1/CoverSubAsm:1/Screw_M4x12:3&#34; |
| join_method_hint | [JoinMethod](#product-v1-JoinMethod) |  |  |
| insertion_offset_hint | [geometry.v1.Vector3](#geometry-v1-Vector3) |  | Offset from final pose to pre-insertion pose, in mm |
| approach_offset_hint | [geometry.v1.Vector3](#geometry-v1-Vector3) |  | Offset from final pose to preferred approach pose, in mm |
| optional | [bool](#bool) |  |  |
| applicability | [variance.v1.VariantRule](#variance-v1-VariantRule) | repeated | Applies if any rule matches. Empty means always applicable. |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  | TODO: string or anchor reference_frame = 17; // allow tasks to anchor not just to a part but to features, e.g. insert screw into hole_1 |





 


<a name="product-v1-JoinMethod"></a>

### JoinMethod


| Name | Number | Description |
| ---- | ------ | ----------- |
| JOIN_METHOD_UNSPECIFIED | 0 |  |
| JOIN_METHOD_NONE | 1 |  |
| JOIN_METHOD_FASTEN | 2 |  |
| JOIN_METHOD_PRESS_FIT | 3 |  |
| JOIN_METHOD_SNAP_FIT | 4 |  |
| JOIN_METHOD_ADHESIVE | 5 |  |
| JOIN_METHOD_WELD | 6 |  |
| JOIN_METHOD_PLACE | 7 |  |



<a name="product-v1-NodeKind"></a>

### NodeKind
NodeKind defines what kind of structural element the AssemblyNode is in the assembly hierarchy
NodeKind               Represents                    Physical part?   Has children?
GROUP                  logical grouping              ❌               yes
PART_OCCURRENCE        single physical part instance ✅               usually no
SUBASSEMBLY_OCCURRENCE assembly containing parts     ✅               yes
PATTERN                repeated pattern structure    ❌ (structure)   yes

| Name | Number | Description |
| ---- | ------ | ----------- |
| NODE_KIND_UNSPECIFIED | 0 |  |
| NODE_KIND_GROUP | 1 | A logical group node that does not correspond to a real physical part or subassembly. It exist only to organize the structure. Typical uses: CAD folders, BOM groupings, organizing fasteners, grouping operations, AR guidance grouping. part_definition_id should usually be empty. |
| NODE_KIND_PART_OCCURRENCE | 2 | The most common node type which is a single instance of a physical part used in the product as it references a PartDefinition. part_definition_id = required, child_node-Ids = empty. |
| NODE_KIND_SUBASSEMBLY_OCCURRENCE | 3 | A subassembly occurrence is a part that itself contains other parts. Thus a component that has its own internal structure. A subassembly is a real product structure (e.g. a Door assembly for a car) where group is a logical grouping. It usually appears in the BOM and often references a PartDefinition. |
| NODE_KIND_PATTERN | 4 | A repeated pattern of parts created by CAD pattern features. Examples: bolt circle, linear pattern, hole array, repeated clips, repeated LEDs. Instead of listing every occurrence individually, the CAD may represent them as a pattern. Thus a pattern is a special kind of group? |


 

 

 



<a name="product_v1_part_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## product/v1/part_definition.proto



<a name="product-v1-Dimensions"></a>

### Dimensions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x_mm | [double](#double) |  |  |
| y_mm | [double](#double) |  |  |
| z_mm | [double](#double) |  |  |






<a name="product-v1-MaterialSpec"></a>

### MaterialSpec
MaterialSpec is meant to capture the engineering material identity of a part.
name → the material family / type
grade → the standardized grade or specification
Examples:
name: aluminium, grade: 6061-T6
name: Steel, grade: S355JR
name: stainless steel, grade: AISI 304
name: ABS, grade: general purpose
name: Polycarbonate, grade: PC-110
name: Nylon, grade: PA6 GF15
name: TPU, grade: 70 Shore A


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| category | [MaterialCategory](#product-v1-MaterialCategory) |  | Broad material class, e.g. metal, polymer, elastomer |
| name | [string](#string) |  | Material family, e.g. aluminium, steel, ABS, FR-4, epoxy adhesive |
| grade | [string](#string) |  | Standard/specification, e.g. 6061-T6, S355JR, AISI 304 |






<a name="product-v1-PartDefinition"></a>

### PartDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [PartType](#product-v1-PartType) |  | Broad functional/BOM classification of the part |
| subtype | [string](#string) |  | Optional finer-grained classification, e.g. led, resistor, battery, circuit_breaker, wire_harness, grease |
| weight_g | [int64](#int64) |  | weight in grams |
| dimensions | [Dimensions](#product-v1-Dimensions) |  |  |
| material | [MaterialSpec](#product-v1-MaterialSpec) |  |  |
| default_model_id | [string](#string) |  | Can later be extended to: CAD model (STEP), AR model (FBX), and lightweight mesh (OBJ) |
| handling | [PartHandlingProfile](#product-v1-PartHandlingProfile) |  |  |
| external_references | [common.v1.ExternalReference](#common-v1-ExternalReference) | repeated |  |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="product-v1-PartDefinitions"></a>

### PartDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [PartDefinition](#product-v1-PartDefinition) | repeated |  |






<a name="product-v1-PartHandlingProfile"></a>

### PartHandlingProfile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fragile | [bool](#bool) |  |  |
| esd_sensitive | [bool](#bool) |  |  |
| requires_two_hand_lift | [bool](#bool) |  |  |
| requires_fixture_support | [bool](#bool) |  | If true, this part cannot realistically be handled/assembled without some fixture support |
| max_grip_force_n | [double](#double) |  |  |
| max_torque_nm | [double](#double) |  |  |
| constraints | [common.v1.KeyValueConstraint](#common-v1-KeyValueConstraint) | repeated |  |





 


<a name="product-v1-MaterialCategory"></a>

### MaterialCategory


| Name | Number | Description |
| ---- | ------ | ----------- |
| MATERIAL_CATEGORY_UNSPECIFIED | 0 |  |
| MATERIAL_CATEGORY_METAL | 1 | Metals and metal alloys |
| MATERIAL_CATEGORY_POLYMER | 2 | Thermoplastics / thermosets |
| MATERIAL_CATEGORY_ELASTOMER | 3 | Flexible rubber-like materials |
| MATERIAL_CATEGORY_COMPOSITE | 4 | Fiber-reinforced / layered materials |
| MATERIAL_CATEGORY_CERAMIC | 5 | Ceramics and similar brittle inorganic materials |
| MATERIAL_CATEGORY_GLASS | 6 | Glass and glass-like transparent materials |
| MATERIAL_CATEGORY_WOOD | 7 | Wood and wood-derived materials |
| MATERIAL_CATEGORY_FOAM | 8 | Cellular / expanded materials |
| MATERIAL_CATEGORY_ELECTRONICS_SUBSTRATE | 9 | PCB substrate materials such as FR-4, polyimide, CEM-1, ceramic PCB |
| MATERIAL_CATEGORY_CHEMICAL | 10 | Adhesive, grease, sealant, potting compound, coating, flux, etc. |
| MATERIAL_CATEGORY_OTHER | 99 | Anything not fitting the categories above |



<a name="product-v1-PartType"></a>

### PartType


| Name | Number | Description |
| ---- | ------ | ----------- |
| PART_TYPE_UNSPECIFIED | 0 |  |
| PART_TYPE_COMPONENT | 1 | General mechanical or non-specialized part/component |
| PART_TYPE_FASTENER | 2 | Screw, bolt, nut, washer, rivet, insert, clip, etc. |
| PART_TYPE_SUBASSEMBLY | 3 | A part that is itself composed of multiple child parts |
| PART_TYPE_CONSUMABLE | 4 | General consumable used up during assembly or maintenance |
| PART_TYPE_LABEL | 5 | Sticker, rating plate, barcode label, warning label, etc. |
| PART_TYPE_PACKAGING | 6 | Box, bag, foam insert, tray cover, spacer, etc. |
| PART_TYPE_PCB | 7 | Bare or populated printed circuit board |
| PART_TYPE_ELECTRONIC_COMPONENT | 8 | LED, resistor, capacitor, IC, connector, relay, fuse, etc. |
| PART_TYPE_ELECTRICAL_COMPONENT | 9 | Breaker, terminal block, battery, switch, power supply, wire harness, etc. |
| PART_TYPE_CABLE | 10 | Wire, cable, wire set, cable assembly, harness |
| PART_TYPE_DISPENSED_MATERIAL | 11 | Grease, glue, sealant, potting compound, solder paste, flux, etc. |


 

 

 



<a name="product_v1_part_instance-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## product/v1/part_instance.proto



<a name="product-v1-PartInstance"></a>

### PartInstance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| part_definition_id | [string](#string) |  |  |
| status | [common.v1.ResourceStatus](#common-v1-ResourceStatus) |  |  |
| location | [PartInstanceLocation](#product-v1-PartInstanceLocation) |  |  |
| quantity | [QuantityStatus](#product-v1-QuantityStatus) |  |  |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="product-v1-PartInstanceLocation"></a>

### PartInstanceLocation
PartInstanceLocation describes the current location of a part instance.

A part may be inside a container slot, or directly located in a station/work
area if not currently stored in a container.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| container_instance_id | [string](#string) |  |  |
| slot_id | [string](#string) |  | Optional slot inside the container. |
| line_id | [string](#string) |  | Optional direct workspace location if not inside a container. |
| cell_id | [string](#string) |  | Optional direct workspace location if not inside a container. |
| station_id | [string](#string) |  | Optional direct workspace location if not inside a container. |
| pose | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |






<a name="product-v1-PartInstances"></a>

### PartInstances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [PartInstance](#product-v1-PartInstance) | repeated |  |






<a name="product-v1-QuantityStatus"></a>

### QuantityStatus
QuantityStatus is a lightweight optional description of how much of a part
instance remains.

This is intentionally simple and optional. It is useful for consumables,
partial reels, partial kits, dispensed materials, or bags/boxes that are not
fully depleted yet.

For indivisible discrete parts, this field can be omitted entirely.
Examples:
	amount=3, unit=&#34;pcs&#34;, nominal_amount=25
	amount=125.0, unit=&#34;g&#34;, nominal_amount=500.0
	amount=7.2, unit=&#34;m&#34;, nominal_amount=20.0


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| amount | [double](#double) |  | Current amount left. |
| unit | [string](#string) |  | Optional unit such as &#34;pcs&#34;, &#34;g&#34;, &#34;ml&#34;, &#34;m&#34;, &#34;cm2&#34;. |
| nominal_amount | [double](#double) |  | Optional reference/original amount. |





 

 

 

 



<a name="variance_v1_variant_axis-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## variance/v1/variant_axis.proto



<a name="variance-v1-VariantAxis"></a>

### VariantAxis



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| options | [VariantOption](#variance-v1-VariantOption) | repeated |  |






<a name="variance-v1-VariantOption"></a>

### VariantOption



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |





 

 

 

 



<a name="product_v1_product_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## product/v1/product_definition.proto



<a name="product-v1-ProductDefinition"></a>

### ProductDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| variant_axes | [variance.v1.VariantAxis](#variance-v1-VariantAxis) | repeated |  |
| root_node_id | [string](#string) |  |  |
| nodes | [AssemblyNode](#product-v1-AssemblyNode) | repeated |  |
| external_references | [common.v1.ExternalReference](#common-v1-ExternalReference) | repeated |  |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="product-v1-ProductDefinitions"></a>

### ProductDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ProductDefinition](#product-v1-ProductDefinition) | repeated |  |





 

 

 

 



<a name="resources_v1_asset_instance-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/asset_instance.proto



<a name="resources-v1-AssetInstance"></a>

### AssetInstance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| asset_definition_id | [string](#string) |  |  |
| status | [common.v1.ResourceStatus](#common-v1-ResourceStatus) |  |  |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-AssetInstances"></a>

### AssetInstances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [AssetInstance](#resources-v1-AssetInstance) | repeated |  |





 

 

 

 



<a name="resources_v1_placement-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/placement.proto



<a name="resources-v1-AssetPlacement"></a>

### AssetPlacement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| asset_instance_id | [string](#string) |  |  |
| pose | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  | Optional placement pose relative to station/cell frame. |
| comment | [string](#string) |  |  |






<a name="resources-v1-MarkerPlacement"></a>

### MarkerPlacement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| marker_instance_id | [string](#string) |  |  |
| pose | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  | Optional pose override if needed for station/cell-local placement. |
| comment | [string](#string) |  |  |






<a name="resources-v1-RobotPlacement"></a>

### RobotPlacement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_instance_id | [string](#string) |  |  |
| pose | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  | Optional robot base pose relative to station/cell frame. |
| comment | [string](#string) |  |  |






<a name="resources-v1-ToolPlacement"></a>

### ToolPlacement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tool_instance_id | [string](#string) |  |  |
| pose | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  | Optional placement pose relative to station/cell frame. |
| comment | [string](#string) |  |  |





 

 

 

 



<a name="resources_v1_cell_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/cell_definition.proto



<a name="resources-v1-CellDefinition"></a>

### CellDefinition
CellDefinition describes an operational grouping of stations and shared
resources inside a line.

A cell is useful when multiple stations share workers, robots, assets,
safety boundaries, or scheduling constraints. It gives the model a clear
middle layer between line-level routing and station-level execution.

Typical cell responsibilities:
- group stations into a shared execution/safety zone
- own resources that are shared across several stations
- expose operational state and capacity above individual stations
- act as an optional target/selector scope for loaders and planners

Static resources such as tools, assets, robots, and markers are owned by
the workspace (station/cell) rather than the instance itself.
This makes workspace composition explicit and avoids duplicating placement
ownership across both the resource instance and the workspace.

Dynamic resources such as workers, containers, and part instances own their
current location because they move independently through the system.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| status | [CellStatus](#resources-v1-CellStatus) |  | Current operational availability of the cell as a whole. |
| max_concurrent_processes | [int32](#int32) |  | Maximum number of active/queued processes this cell should host concurrently. |
| allow_queued_process | [bool](#bool) |  | If true, loaders may create queued ProcessRuns when the cell is BUSY. |
| station_ids | [string](#string) | repeated | Stations belonging to this cell. |
| tools | [ToolPlacement](#resources-v1-ToolPlacement) | repeated | Shared tools mounted, parked, or otherwise directly available here. |
| robots | [RobotPlacement](#resources-v1-RobotPlacement) | repeated | Robots shared across multiple stations inside the cell. |
| assets | [AssetPlacement](#resources-v1-AssetPlacement) | repeated | Shared assets such as cameras, HMIs, or feeders serving several stations. |
| markers | [MarkerPlacement](#resources-v1-MarkerPlacement) | repeated | Markers shared for this cell for localization, AR anchoring, or identification. |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  | Cell-local reference frame or zone anchor. |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-CellDefinitions"></a>

### CellDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [CellDefinition](#resources-v1-CellDefinition) | repeated |  |





 


<a name="resources-v1-CellStatus"></a>

### CellStatus
CellStatus describes whether a cell can currently accept or host work.

A cell is typically a grouping of stations and related resources. The loader
can use this status to quickly reject or prefer a cell before evaluating
individual stations.

Status should be interpreted as:
- OPEN    -&gt; cell can accept new work now
- BUSY    -&gt; cell is occupied; queueing may still be possible
- CLOSED  -&gt; cell is intentionally unavailable
- BLOCKED -&gt; cell is unavailable due to fault, safety state, maintenance,
             or other blocking condition

This field is operational and should be considered together with
max_concurrent_processes and the status of contained stations.

| Name | Number | Description |
| ---- | ------ | ----------- |
| CELL_STATUS_UNSPECIFIED | 0 |  |
| CELL_STATUS_OPEN | 1 | Cell can accept new work now. |
| CELL_STATUS_BUSY | 2 | Cell is currently occupied by one or more active runs. Depending on policy, new runs may still be queued. |
| CELL_STATUS_CLOSED | 3 | Cell is intentionally unavailable for loading or running work. |
| CELL_STATUS_BLOCKED | 4 | Cell is temporarily unavailable due to fault, interlock, maintenance state, or similar blocking condition. |


 

 

 



<a name="resources_v1_container_instance-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/container_instance.proto



<a name="resources-v1-ContainerInstance"></a>

### ContainerInstance
ContainerInstance represents a concrete container in a station/cell.

Examples:
- the actual shelf bin mounted in station A
- the actual pallet currently loaded on an indexing table
- the actual jig installed on a workbench


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  | Stable identifier of the concrete container instance. |
| name | [string](#string) |  | Display name of the instance. Often copied from the definition, but may be station-specific. |
| icon | [string](#string) |  | UI icon for the instance. |
| description | [string](#string) |  | Human-readable description of this particular instance. |
| container_definition_id | [string](#string) |  | The reusable container definition that this instance realizes. |
| status | [common.v1.ResourceStatus](#common-v1-ResourceStatus) |  | Operational status such as available, disabled, or faulted. |
| location | [ContainerLocation](#resources-v1-ContainerLocation) |  | Dynamic location of the container instance. |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  | Extension point for instance-specific data. |






<a name="resources-v1-ContainerInstances"></a>

### ContainerInstances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ContainerInstance](#resources-v1-ContainerInstance) | repeated | List wrapper used for transport/query responses. |






<a name="resources-v1-ContainerLocation"></a>

### ContainerLocation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| line_id | [string](#string) |  |  |
| cell_id | [string](#string) |  |  |
| station_id | [string](#string) |  | Station/cell where this container currently belongs or is mounted. |
| pose | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |





 

 

 

 



<a name="resources_v1_device-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/device.proto



<a name="resources-v1-DeviceHeartbeat"></a>

### DeviceHeartbeat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| device_id | [string](#string) |  |  |
| battery_level | [int32](#int32) |  |  |
| battery_status | [DeviceBatteryStatus](#resources-v1-DeviceBatteryStatus) |  |  |






<a name="resources-v1-DeviceMessage"></a>

### DeviceMessage
DeviceMessage hold basic information about AR-devices, such as a HoloLens2


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [DeviceType](#resources-v1-DeviceType) |  |  |
| device_id | [string](#string) |  |  |
| status | [DeviceStatus](#resources-v1-DeviceStatus) |  |  |
| battery_level | [int32](#int32) |  |  |
| battery_status | [DeviceBatteryStatus](#resources-v1-DeviceBatteryStatus) |  |  |
| equipped_by_worker_id | [string](#string) |  |  |






<a name="resources-v1-DeviceMessages"></a>

### DeviceMessages



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| devices | [DeviceMessage](#resources-v1-DeviceMessage) | repeated |  |





 


<a name="resources-v1-DeviceBatteryStatus"></a>

### DeviceBatteryStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| DEVICE_BATTERY_STATUS_UNSPECIFIED | 0 | The device&#39;s battery status cannot be determined. If battery status is not available on your target platform, SystemInfo.batteryStatus will return this value. |
| DEVICE_BATTERY_STATUS_CHARGING | 1 | Device is plugged in and charging. |
| DEVICE_BATTERY_STATUS_DISCHARGING | 2 | Device is unplugged and discharging. |
| DEVICE_BATTERY_STATUS_NOT_CHARGING | 3 | Device is plugged in, but is not charging. |
| DEVICE_BATTERY_STATUS_FULL | 4 | Device is plugged in and the battery is full. |



<a name="resources-v1-DeviceStatus"></a>

### DeviceStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| DEVICE_STATUS_UNSPECIFIED | 0 |  |
| DEVICE_STATUS_ONLINE | 1 |  |
| DEVICE_STATUS_OFFLINE | 2 |  |



<a name="resources-v1-DeviceType"></a>

### DeviceType


| Name | Number | Description |
| ---- | ------ | ----------- |
| DEVICE_TYPE_UNSPECIFIED | 0 |  |
| DEVICE_TYPE_HOLOLENS2 | 1 |  |
| DEVICE_TYPE_PHONE | 2 |  |
| DEVICE_TYPE_TABLET | 3 |  |
| DEVICE_TYPE_PC | 4 |  |


 

 

 



<a name="resources_v1_line_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/line_definition.proto



<a name="resources-v1-LineDefinition"></a>

### LineDefinition
LineDefinition describes the highest operational routing context for loading
and dispatching work.

A line groups cells and/or stations into a production area that can be
targeted by ProcessLoadRequest. Loaders typically resolve a concrete cell and
station within the selected line.

Typical line responsibilities:
- act as the top-level routing target for process loading
- expose high-level operational status and capacity
- contain one or more cells and/or directly attached stations
- provide a coarse operational boundary for planning and dispatch


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| type | [LineType](#resources-v1-LineType) |  | Broad line classification. Keep optional until concrete line types are introduced. |
| status | [LineStatus](#resources-v1-LineStatus) |  | Current operational availability of the line as a whole. |
| max_concurrent_processes | [int32](#int32) |  | Maximum number of active/queued processes this line should host concurrently. |
| cell_ids | [string](#string) | repeated | Cells belonging to this line. |
| station_ids | [string](#string) | repeated | Optional directly attached stations when a line references stations without an intermediate cell. |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-LineDefinitions"></a>

### LineDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [LineDefinition](#resources-v1-LineDefinition) | repeated |  |





 


<a name="resources-v1-LineStatus"></a>

### LineStatus
LineStatus describes whether a production line can currently accept work.

A line is a higher-level operational grouping of cells and/or stations.
The loader can use this status as an early gate before checking specific
cells, stations, and resources.

Status should be interpreted as:
- OPEN    -&gt; line can accept new work now
- BUSY    -&gt; line is operational but currently occupied; queueing may still
             be allowed
- CLOSED  -&gt; line is intentionally unavailable
- BLOCKED -&gt; line is unavailable due to fault, safety state, maintenance,
             or similar blocking condition

This field is operational and should be considered together with
max_concurrent_processes and the statuses of child cells/stations.

| Name | Number | Description |
| ---- | ------ | ----------- |
| LINE_STATUS_UNSPECIFIED | 0 |  |
| LINE_STATUS_OPEN | 1 | Line can accept new work now. |
| LINE_STATUS_BUSY | 2 | Line is currently occupied by one or more active runs. Depending on policy, new runs may still be queued. |
| LINE_STATUS_CLOSED | 3 | Line is intentionally unavailable for loading or running work. |
| LINE_STATUS_BLOCKED | 4 | Line is temporarily unavailable due to fault, interlock, maintenance state, or similar blocking condition. |



<a name="resources-v1-LineType"></a>

### LineType


| Name | Number | Description |
| ---- | ------ | ----------- |
| LINE_TYPE_UNSPECIFIED | 0 |  |


 

 

 



<a name="resources_v1_marker_instance-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/marker_instance.proto



<a name="resources-v1-MarkerInstance"></a>

### MarkerInstance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| marker_text | [string](#string) |  | Text on the physical marker (QR-code) |
| type | [MarkerType](#resources-v1-MarkerType) |  |  |
| confirm_instantiate | [bool](#bool) |  | If true, the user must confirm that he/she want to instantiate the environment(s) associated with this marker. |
| status | [common.v1.ResourceStatus](#common-v1-ResourceStatus) |  |  |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-MarkerInstances"></a>

### MarkerInstances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| markers | [MarkerInstance](#resources-v1-MarkerInstance) | repeated |  |





 


<a name="resources-v1-MarkerType"></a>

### MarkerType


| Name | Number | Description |
| ---- | ------ | ----------- |
| MARKER_TYPE_UNSPECIFIED | 0 |  |
| MARKER_TYPE_QR_CODE | 1 |  |


 

 

 



<a name="resources_v1_model-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/model.proto



<a name="resources-v1-ModelArtifact"></a>

### ModelArtifact



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| group | [ModelGroup](#resources-v1-ModelGroup) |  |  |
| origin | [ModelOrigin](#resources-v1-ModelOrigin) |  |  |
| format | [ModelFormat](#resources-v1-ModelFormat) |  |  |
| filename | [string](#string) |  | Filename is required for BUILT_IN models, ignored otherwise |
| uri | [string](#string) |  | Uri is required for uploaded and external models |
| thumbnail_uri | [string](#string) |  |  |
| version | [string](#string) |  |  |
| unit | [string](#string) |  | Unit used for the model geometry coordinates. Typically &#34;mm&#34;, &#34;cm&#34;, &#34;m&#34;, &#34;in&#34;, etc. Used to scale the model correctly when loading. |
| up_axis | [string](#string) |  | &#34;X&#34;, &#34;Y&#34;, &#34;Z&#34; |
| external_references | [common.v1.ExternalReference](#common-v1-ExternalReference) | repeated |  |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-ModelArtifacts"></a>

### ModelArtifacts



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ModelArtifact](#resources-v1-ModelArtifact) | repeated |  |





 


<a name="resources-v1-ModelFormat"></a>

### ModelFormat


| Name | Number | Description |
| ---- | ------ | ----------- |
| MODEL_FORMAT_UNSPECIFIED | 0 |  |
| MODEL_FORMAT_GLB | 1 |  |
| MODEL_FORMAT_GLTF | 2 |  |
| MODEL_FORMAT_OBJ | 3 |  |
| MODEL_FORMAT_STEP | 4 |  |
| MODEL_FORMAT_STL | 5 |  |
| MODEL_FORMAT_USDZ | 6 |  |



<a name="resources-v1-ModelGroup"></a>

### ModelGroup


| Name | Number | Description |
| ---- | ------ | ----------- |
| MODEL_GROUP_UNSPECIFIED | 0 |  |
| MODEL_GROUP_PART | 1 |  |
| MODEL_GROUP_PRODUCT | 2 |  |
| MODEL_GROUP_TOOL | 3 |  |
| MODEL_GROUP_ROBOT | 4 |  |
| MODEL_GROUP_CONTAINER | 5 |  |
| MODEL_GROUP_ASSET | 6 |  |



<a name="resources-v1-ModelOrigin"></a>

### ModelOrigin


| Name | Number | Description |
| ---- | ------ | ----------- |
| MODEL_ORIGIN_UNSPECIFIED | 0 |  |
| MODEL_ORIGIN_BUILT_IN | 1 |  |
| MODEL_ORIGIN_UPLOADED | 2 |  |
| MODEL_ORIGIN_EXTERNAL | 3 |  |


 

 

 



<a name="resources_v1_robot_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/robot_definition.proto



<a name="resources-v1-RobotDefinition"></a>

### RobotDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  | Autogenerated id |
| name | [string](#string) |  | Name of the robot |
| icon | [string](#string) |  | Optional icon representing the robot |
| description | [string](#string) |  | Optional description of the robot |
| type | [RobotType](#resources-v1-RobotType) |  | Required type of robot |
| driver_type | [RobotDriverType](#resources-v1-RobotDriverType) |  | Required driver type for robot |
| model_id | [string](#string) |  |  |
| coupler_model_id | [string](#string) |  | Tool mounting capability |
| supported_tool_definition_ids | [string](#string) | repeated |  |
| default_tool_definition_id | [string](#string) |  |  |
| tool_slots | [int32](#int32) |  |  |
| capability_profile | [capability.v1.CapabilityProfile](#capability-v1-CapabilityProfile) |  |  |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-RobotDefinitions"></a>

### RobotDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [RobotDefinition](#resources-v1-RobotDefinition) | repeated |  |





 


<a name="resources-v1-RobotDriverType"></a>

### RobotDriverType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ROBOT_DRIVER_TYPE_UNSPECIFIED | 0 |  |
| ROBOT_DRIVER_TYPE_UR | 1 |  |
| ROBOT_DRIVER_TYPE_GENERIC | 2 |  |



<a name="resources-v1-RobotType"></a>

### RobotType


| Name | Number | Description |
| ---- | ------ | ----------- |
| ROBOT_TYPE_UNSPECIFIED | 0 |  |
| ROBOT_TYPE_UR3E | 10 |  |
| ROBOT_TYPE_UR5E | 11 |  |
| ROBOT_TYPE_UR10E | 12 |  |
| ROBOT_TYPE_KUKA_IIWA | 20 |  |


 

 

 



<a name="resources_v1_robot_instance-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/robot_instance.proto



<a name="resources-v1-RobotInstance"></a>

### RobotInstance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| robot_definition_id | [string](#string) |  |  |
| serial_number | [string](#string) |  |  |
| mounted_tool_instance_id | [string](#string) |  | The tool instance currently mounted on the robot, if any. |
| available_tool_instance_ids | [string](#string) | repeated | Tool instances available to this robot in the cell/tool dock/tool magazine. |
| supports_tool_change | [bool](#bool) |  | Whether this robot instance can dynamically change between available tools. |
| is_simulated | [bool](#bool) |  |  |
| status | [common.v1.ResourceStatus](#common-v1-ResourceStatus) |  |  |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-RobotInstances"></a>

### RobotInstances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [RobotInstance](#resources-v1-RobotInstance) | repeated |  |





 

 

 

 



<a name="resources_v1_station_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/station_definition.proto



<a name="resources-v1-StationDefinition"></a>

### StationDefinition
StationDefinition describes a concrete execution point inside a cell or line.

A station is the most specific location where work is typically loaded,
queued, executed, and tracked at runtime. Stations are therefore the primary
target for task/resource matching in loader/planner logic.

Typical station responsibilities:
- host concrete task execution
- own station-local tools, containers, robots, markers, and frame
- expose operational state such as OPEN/BUSY/CLOSED/BLOCKED
- optionally allow queueing when already occupied

Static resources such as tools, assets, robots, and markers are owned by
the workspace (station/cell) rather than the instance itself.
This makes workspace composition explicit and avoids duplicating placement
ownership across both the resource instance and the workspace.

Dynamic resources such as workers, containers, and part instances own their
current location because they move independently through the system.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| type | [StationType](#resources-v1-StationType) |  | Broad station classification, e.g. manual, automatic, or hybrid. |
| status | [StationStatus](#resources-v1-StationStatus) |  | Current operational availability used by loaders, planners, and UIs. |
| max_concurrent_processes | [int32](#int32) |  | Maximum number of active/queued processes this station should host concurrently. |
| allow_queued_process | [bool](#bool) |  | If true, loaders may create queued ProcessRuns when the station is BUSY. |
| tools | [ToolPlacement](#resources-v1-ToolPlacement) | repeated | Station-local tools mounted, parked, or otherwise directly available here. |
| robots | [RobotPlacement](#resources-v1-RobotPlacement) | repeated | Robots directly assigned to or executing within this station. |
| assets | [AssetPlacement](#resources-v1-AssetPlacement) | repeated | Station-local assets such as cameras, HMIs, feeders, or sensors. |
| markers | [MarkerPlacement](#resources-v1-MarkerPlacement) | repeated | Markers used specifically at this station for localization, AR anchoring, or identification. |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  | Station-local reference frame used for runtime bindings, AR anchoring, and execution geometry. |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-StationDefinitions"></a>

### StationDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [StationDefinition](#resources-v1-StationDefinition) | repeated |  |





 


<a name="resources-v1-StationStatus"></a>

### StationStatus
StationStatus describes whether a station can currently accept or execute work.

This is an operational/runtime-oriented state used by loaders, planners,
dispatchers, and UIs when deciding whether a ProcessRun can be started here.

Status should be interpreted as:
- OPEN    -&gt; can accept new work now
- BUSY    -&gt; currently occupied; may still allow queueing
- CLOSED  -&gt; intentionally unavailable for new work
- BLOCKED -&gt; unavailable due to a fault, interlock, maintenance lock, or
             other condition that should prevent execution

A station may also expose capacity constraints through
max_concurrent_processes, which is separate from this status field.

| Name | Number | Description |
| ---- | ------ | ----------- |
| STATION_STATUS_UNSPECIFIED | 0 |  |
| STATION_STATUS_OPEN | 1 | Station can accept new work now. |
| STATION_STATUS_BUSY | 2 | Station is currently occupied by one or more active runs. Depending on loader policy and allow_queued_process, new runs may be queued. |
| STATION_STATUS_CLOSED | 3 | Station is intentionally unavailable for loading or running work. |
| STATION_STATUS_BLOCKED | 4 | Station is temporarily unavailable due to fault, safety interlock, maintenance state, missing prerequisite, or similar blocking condition. |



<a name="resources-v1-StationType"></a>

### StationType


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATION_TYPE_UNSPECIFIED | 0 |  |
| STATION_TYPE_STORAGE | 1 |  |
| STATION_TYPE_MANUAL_STATION | 2 |  |
| STATION_TYPE_AUTOMATIC_STATION | 3 |  |
| STATION_TYPE_HYBRID_STATION | 4 |  |


 

 

 



<a name="resources_v1_tool_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/tool_definition.proto



<a name="resources-v1-ToolDefinition"></a>

### ToolDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [ToolType](#resources-v1-ToolType) |  |  |
| actor_kind | [common.v1.ActorKind](#common-v1-ActorKind) |  |  |
| roles | [capability.v1.ToolRole](#capability-v1-ToolRole) | repeated |  |
| properties | [capability.v1.ToolProperty](#capability-v1-ToolProperty) | repeated |  |
| capability_profile | [capability.v1.CapabilityProfile](#capability-v1-CapabilityProfile) |  |  |
| model_id | [string](#string) |  |  |
| external_references | [common.v1.ExternalReference](#common-v1-ExternalReference) | repeated |  |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-ToolDefinitions"></a>

### ToolDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ToolDefinition](#resources-v1-ToolDefinition) | repeated |  |





 


<a name="resources-v1-ToolType"></a>

### ToolType


| Name | Number | Description |
| ---- | ------ | ----------- |
| TOOL_TYPE_UNSPECIFIED | 0 |  |
| TOOL_TYPE_FASTENING | 1 |  |
| TOOL_TYPE_GRIPPING | 2 |  |
| TOOL_TYPE_CUTTING | 3 |  |
| TOOL_TYPE_MEASURING | 4 |  |
| TOOL_TYPE_POSITIONING | 5 |  |
| TOOL_TYPE_DISPENSING | 6 |  |
| TOOL_TYPE_INSPECTION | 7 |  |
| TOOL_TYPE_SAFETY | 8 |  |
| TOOL_TYPE_ELECTRONICS | 9 |  |
| TOOL_TYPE_FIXTURE_ACCESSORY | 10 |  |
| TOOL_TYPE_SHAPING | 11 |  |
| TOOL_TYPE_TURNING | 12 |  |
| TOOL_TYPE_STRIKING | 13 |  |
| TOOL_TYPE_MARKING | 14 |  |
| TOOL_TYPE_FINISHING | 15 |  |
| TOOL_TYPE_ABRASIVE | 16 |  |
| TOOL_TYPE_CLEANING | 17 |  |


 

 

 



<a name="resources_v1_tool_instance-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/tool_instance.proto



<a name="resources-v1-ToolInstance"></a>

### ToolInstance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| description | [string](#string) |  |  |
| tool_definition_id | [string](#string) |  |  |
| serial_number | [string](#string) |  |  |
| status | [common.v1.ResourceStatus](#common-v1-ResourceStatus) |  |  |
| calibrated | [bool](#bool) |  |  |
| calibration_valid_until | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-ToolInstances"></a>

### ToolInstances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ToolInstance](#resources-v1-ToolInstance) | repeated |  |





 

 

 

 



<a name="resources_v1_worker_definition-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## resources/v1/worker_definition.proto



<a name="resources-v1-WorkerDefinition"></a>

### WorkerDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| disabled | [bool](#bool) |  | If disabled, the worker can&#39;t be selected |
| employee_id | [string](#string) |  |  |
| ar_edit_permission | [EditPermission](#resources-v1-EditPermission) |  |  |
| external_references | [common.v1.ExternalReference](#common-v1-ExternalReference) | repeated |  |
| location | [WorkerLocation](#resources-v1-WorkerLocation) |  | Optional current location / operating area. |
| custom | [common.v1.CustomProperties](#common-v1-CustomProperties) |  |  |






<a name="resources-v1-WorkerDefinitions"></a>

### WorkerDefinitions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [WorkerDefinition](#resources-v1-WorkerDefinition) | repeated |  |






<a name="resources-v1-WorkerLocation"></a>

### WorkerLocation
WorkerLocation describes the current operating area of a worker.

Dynamic resources such as workers own their current location because they
move independently through the system.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| line_id | [string](#string) |  |  |
| cell_id | [string](#string) |  |  |
| station_id | [string](#string) |  |  |





 


<a name="resources-v1-EditPermission"></a>

### EditPermission


| Name | Number | Description |
| ---- | ------ | ----------- |
| EDIT_PERMISSION_UNSPECIFIED | 0 | Unspecified: can&#39;t edit any properties |
| EDIT_PERMISSION_BASIC | 1 | Basic: can edit {basic} properties |
| EDIT_PERMISSION_COSMETIC | 2 | Cosmetic: can edit {basic, cosmetic} properties |
| EDIT_PERMISSION_FULL | 3 | Full: can edit all editable properties |


 

 

 



<a name="robot_v1_end_effector-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/end_effector.proto



<a name="robot-v1-EndEffectorStateMessage"></a>

### EndEffectorStateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| live | [bool](#bool) |  |  |
| state | [string](#string) |  |  |





 

 

 

 



<a name="robot_v1_jointstate-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/jointstate.proto



<a name="robot-v1-JointStateMessage"></a>

### JointStateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| live | [bool](#bool) |  |  |
| position | [double](#double) | repeated |  |
| velocity | [double](#double) | repeated |  |





 

 

 

 



<a name="robot_v1_path-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/path.proto



<a name="robot-v1-PathMessage"></a>

### PathMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| robot_id | [string](#string) |  |  |
| points | [geometry.v1.Point](#geometry-v1-Point) | repeated |  |





 

 

 

 



<a name="robot_v1_popup-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/popup.proto



<a name="robot-v1-RobotHidePopupRequest"></a>

### RobotHidePopupRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| robot_id | [string](#string) |  |  |






<a name="robot-v1-RobotShowPopupRequest"></a>

### RobotShowPopupRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| robot_id | [string](#string) |  |  |
| text | [string](#string) |  |  |





 

 

 

 



<a name="robot_v1_program_state-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/program_state.proto



<a name="robot-v1-ProgramStateMessage"></a>

### ProgramStateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| state_code | [ProgramState](#robot-v1-ProgramState) |  |  |
| state | [string](#string) |  |  |
| program_file | [string](#string) |  |  |





 


<a name="robot-v1-ProgramState"></a>

### ProgramState


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROGRAM_STATE_UNSPECIFIED | 0 |  |
| PROGRAM_STATE_PLAY | 1 |  |
| PROGRAM_STATE_PAUSE | 2 |  |
| PROGRAM_STATE_STOP | 3 |  |


 

 

 



<a name="robot_v1_program_state_request-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/program_state_request.proto



<a name="robot-v1-ProgramStateRequest"></a>

### ProgramStateRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [string](#string) |  |  |
| robot_id | [string](#string) |  |  |
| state | [ProgramState](#robot-v1-ProgramState) |  |  |





 

 

 

 



<a name="robot_v1_robot_state-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/robot_state.proto



<a name="robot-v1-RobotStateMessage"></a>

### RobotStateMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| state_code | [RobotState](#robot-v1-RobotState) |  |  |
| state | [string](#string) |  |  |
| target_speed | [double](#double) |  |  |
| actual_speed | [double](#double) |  |  |





 


<a name="robot-v1-RobotState"></a>

### RobotState


| Name | Number | Description |
| ---- | ------ | ----------- |
| ROBOT_STATE_UNSPECIFIED | 0 |  |
| ROBOT_STATE_STOPPING | 1 |  |
| ROBOT_STATE_STOPPED | 2 |  |
| ROBOT_STATE_PLAYING | 3 |  |
| ROBOT_STATE_PAUSING | 4 |  |
| ROBOT_STATE_PAUSED | 5 |  |
| ROBOT_STATE_RESUMING | 6 |  |


 

 

 



<a name="robot_v1_robot_visibility-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/robot_visibility.proto



<a name="robot-v1-RobotVisibilityMessage"></a>

### RobotVisibilityMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| base_visible | [bool](#bool) |  |  |
| upper_arm_visible | [bool](#bool) |  |  |
| forearm_visible | [bool](#bool) |  |  |
| wrist_visible | [bool](#bool) |  |  |
| end_effector_visible | [bool](#bool) |  |  |
| tcp_visible | [bool](#bool) |  |  |





 

 

 

 



<a name="robot_v1_tcp-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/tcp.proto



<a name="robot-v1-TcpMessage"></a>

### TcpMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| position | [geometry.v1.Point](#geometry-v1-Point) |  |  |
| orientation | [geometry.v1.Quad](#geometry-v1-Quad) |  |  |





 

 

 

 



<a name="robot_v1_waypoints-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/waypoints.proto



<a name="robot-v1-WaypointMessage"></a>

### WaypointMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| point | [geometry.v1.Point](#geometry-v1-Point) |  |  |






<a name="robot-v1-WaypointsMessage"></a>

### WaypointsMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| robot_id | [string](#string) |  |  |
| frame_id | [string](#string) |  |  |
| highlight_idx | [int32](#int32) |  |  |
| waypoints | [WaypointMessage](#robot-v1-WaypointMessage) | repeated |  |





 

 

 

 



<a name="robot_v1_zone-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## robot/v1/zone.proto



<a name="robot-v1-ZoneMessage"></a>

### ZoneMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| frame_id | [string](#string) |  |  |
| points | [geometry.v1.Point](#geometry-v1-Point) | repeated |  |





 

 

 

 



<a name="runtime_v1_actor_assignment-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## runtime/v1/actor_assignment.proto



<a name="runtime-v1-ActorAssignment"></a>

### ActorAssignment



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| actor | [common.v1.ActorRef](#common-v1-ActorRef) |  |  |
| process_run_id | [string](#string) |  |  |
| sequence_run_id | [string](#string) |  |  |
| task_run_id | [string](#string) |  |  |
| assigned_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| released_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |






<a name="runtime-v1-ActorAssignments"></a>

### ActorAssignments



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ActorAssignment](#runtime-v1-ActorAssignment) | repeated |  |





 

 

 

 



<a name="runtime_v1_execution_evidence-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## runtime/v1/execution_evidence.proto



<a name="runtime-v1-EvidenceFact"></a>

### EvidenceFact
EvidenceFact stores a flexible key/value fact recorded during execution.
Use this for measurements, classifications, result details, operator notes,
and other structured runtime output.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |
| unit | [string](#string) |  |  |






<a name="runtime-v1-ExecutionEvidence"></a>

### ExecutionEvidence
ExecutionEvidence records runtime facts produced during task execution.

It is task-run-centric and primarily supports traceability, validation,
analytics, and downstream aggregation into actor skill state.

The normalized fields such as actor, skill_id, and success are optional but
strongly recommended when known, because they make later aggregation much
simpler and more robust than parsing facts alone.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| task_run_id | [string](#string) |  |  |
| source | [string](#string) |  | tool, vision, operator, robot driver, etc. |
| recorded_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| facts | [EvidenceFact](#runtime-v1-EvidenceFact) | repeated |  |
| blob_uri | [string](#string) |  | Optional external payload such as image, log, trace, or report. |
| actor | [common.v1.ActorRef](#common-v1-ActorRef) |  | Optional actor who produced or is primarily associated with this evidence. |
| skill_id | [string](#string) |  | Optional skill primarily exercised or validated by this evidence. |
| success | [bool](#bool) |  | normalized success signal when known |






<a name="runtime-v1-ExecutionEvidences"></a>

### ExecutionEvidences



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ExecutionEvidence](#runtime-v1-ExecutionEvidence) | repeated |  |





 

 

 

 



<a name="runtime_v1_process_run-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## runtime/v1/process_run.proto



<a name="runtime-v1-ProcessRun"></a>

### ProcessRun
ProcessRun is only created when a concrete cell can currently satisfy it.
Is is based upon a ProcessRecipe which defines what must be possible.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| process_recipe_id | [string](#string) |  |  |
| order_id | [string](#string) |  |  |
| station_id | [string](#string) |  |  |
| cell_id | [string](#string) |  |  |
| line_id | [string](#string) |  |  |
| frame | [geometry.v1.LocalizedPose](#geometry-v1-LocalizedPose) |  |  |
| root_sequence_run_id | [string](#string) |  |  |
| sequence_run_ids | [string](#string) | repeated |  |
| task_run_ids | [string](#string) | repeated |  |
| state | [ProcessRunState](#runtime-v1-ProcessRunState) |  |  |
| initiated_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| ended_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| assignments | [ActorAssignment](#runtime-v1-ActorAssignment) | repeated |  |
| variant_configuration | [variance.v1.VariantConfiguration](#variance-v1-VariantConfiguration) |  |  |
| parameters | [RunParameter](#runtime-v1-RunParameter) | repeated |  |






<a name="runtime-v1-ProcessRuns"></a>

### ProcessRuns



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ProcessRun](#runtime-v1-ProcessRun) | repeated |  |






<a name="runtime-v1-RunParameter"></a>

### RunParameter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  | &#34;color&#34;, &#34;label_text&#34;, &#34;customer_name&#34; |
| value | [string](#string) |  |  |





 


<a name="runtime-v1-ProcessRunState"></a>

### ProcessRunState


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_RUN_STATE_UNSPECIFIED | 0 |  |
| PROCESS_RUN_STATE_QUEUED | 1 | Queued, can not be started yet |
| PROCESS_RUN_STATE_READY | 2 | Waiting to be started (ready) |
| PROCESS_RUN_STATE_IN_PROGRESS | 3 | In progress |
| PROCESS_RUN_STATE_DONE | 4 | Completed, all tasks are complete |
| PROCESS_RUN_STATE_ABORTED | 5 |  |


 

 

 



<a name="runtime_v1_runtime_restriction-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## runtime/v1/runtime_restriction.proto



<a name="runtime-v1-RuntimeRestriction"></a>

### RuntimeRestriction
RuntimeRestriction describes an additional runtime condition that applies
to a task, typically due to actor capability state, policy evaluation,
resource limitations, or execution mode.

Restrictions may be actor-specific. This is important because a task may be:
- unrestricted for one candidate actor
- restricted for another
- infeasible for a third

During precheck / candidate evaluation, restrictions can be attached to
candidate actors. Once a task is assigned, the effective restrictions for
the assigned actor should be copied onto the TaskRun.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [RestrictionType](#runtime-v1-RestrictionType) |  |  |
| reason | [string](#string) |  | Human-readable explanation shown in UI/logs. |
| source_skill_id | [string](#string) |  | Optional originating skill that caused the restriction. |
| source_policy_id | [string](#string) |  | Optional originating policy that caused the restriction. |
| actor | [common.v1.ActorRef](#common-v1-ActorRef) |  | Optional actor this restriction applies to. If unset, the restriction is task-global rather than actor-specific. |





 


<a name="runtime-v1-RestrictionType"></a>

### RestrictionType


| Name | Number | Description |
| ---- | ------ | ----------- |
| RESTRICTION_TYPE_UNSPECIFIED | 0 |  |
| RESTRICTION_TYPE_REQUIRE_AR_GUIDANCE | 1 | The actor may perform the task only with AR guidance enabled. |
| RESTRICTION_TYPE_REQUIRE_MANUAL_CONFIRMATION | 2 | The task must be manually confirmed before completion. |
| RESTRICTION_TYPE_REQUIRE_SUPERVISOR_APPROVAL | 3 | The task requires supervisor approval before execution or completion. |
| RESTRICTION_TYPE_REQUIRE_SECOND_CHECK | 4 | The task requires an additional validation or second check. |
| RESTRICTION_TYPE_REQUIRE_VISION_VALIDATION | 5 | Vision-based validation must be used. |
| RESTRICTION_TYPE_REQUIRE_TOOL_FEEDBACK | 6 | Tool feedback must be used. |
| RESTRICTION_TYPE_REQUIRE_HUMAN_ACTOR | 7 | The task may only be executed by a human actor. |
| RESTRICTION_TYPE_REQUIRE_ROBOT_ACTOR | 8 | The task may only be executed by a robot actor. |


 

 

 



<a name="runtime_v1_process_requests-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## runtime/v1/process_requests.proto



<a name="runtime-v1-CandidateActorEvaluation"></a>

### CandidateActorEvaluation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| actor | [common.v1.ActorRef](#common-v1-ActorRef) |  |  |
| feasible | [bool](#bool) |  | Whether this actor is currently feasible for the task. |
| restrictions | [RuntimeRestriction](#runtime-v1-RuntimeRestriction) | repeated | Effective restrictions if this actor were assigned. |
| issues | [ProcessRunIssue](#runtime-v1-ProcessRunIssue) | repeated | Optional explanations or issues tied specifically to this actor. |






<a name="runtime-v1-ProcessLoadRequest"></a>

### ProcessLoadRequest
ProcessLoadRequest is used to instantiate a ProcessRecipe into a ProcessRun.

The loader should evaluate whether the recipe can be instantiated now within
the requested operational scope, using currently available actors, tools,
robots, containers, assets, and validation resources.

Target scope resolution:

- target_line_id is the top-level routing scope and is required.
- if target_cell_id is set, the loader must validate and use that cell.
- if target_station_id is set, the loader must validate and use that station.
- if cell/station are not set, the loader should choose the best feasible
  candidate within the selected line.

Occupancy handling:

- if a candidate station is BUSY and queue_if_occupied is true, the loader
  may create a queued ProcessRun.
- if queue_if_occupied is false, the loader should only queue when the chosen
  target explicitly allows queued processes.
- otherwise the load should fail with a blocking issue.

Thus the following must be evaluated:
- available robots (if any task requires or strongly prefers a robot, can that be satisfied?)
- available workers (if tasks requires only-human or need certain skills, can that be satisfied? Either check immediately or defer until operator is assigned. Perhaps assigned based on skills and availability? Check that: assigned worker exist, worker enabled, required skills present and valid)
- available tool instances (all ToolRequirements from all tasks, available ToolInstances is station/cell, tool status, calibration validity, required properties, minimum capability profile)
- valid calibration
- fixture availability/feasibility (recipe supported fixtures, available fixture instances, fixture status, product/recipe compatibility)
- safety mode / collaboration mode (check: recipe task collaboration modes, station/cell safety mode, whether simultaneous HRC is allowed, whether human-only or robot-only is possible right now)
- active faults / disabled resources
- asset / inspection feasibility (if validation required: vision, torque feedback, external QC, sensors --&gt; then verify those assets exist and are available.)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| process_recipe_id | [string](#string) |  | Required recipe to instantiate. |
| target_line_id | [string](#string) |  | Required top-level routing scope. |
| target_cell_id | [string](#string) |  | Optional narrowing of the target scope. If set, the loader must validate and respect these targets. |
| target_station_id | [string](#string) |  |  |
| variant_configuration | [variance.v1.VariantConfiguration](#variance-v1-VariantConfiguration) |  | Optional variant configuration used to evaluate recipe/task applicability. |
| dry_run | [bool](#bool) |  | true -&gt; perform precheck only false -&gt; perform precheck and instantiate ProcessRun if feasible |
| queue_if_occupied | [bool](#bool) |  | If true, the loader may create a queued ProcessRun when the preferred execution target is currently BUSY but otherwise feasible. |
| strategy | [ProcessLoadStrategy](#runtime-v1-ProcessLoadStrategy) |  | Optional execution preferences for the loader. |
| order_id | [string](#string) |  | Optional order/business reference to carry into the ProcessRun. |
| parameters | [common.v1.KeyValueConstraint](#common-v1-KeyValueConstraint) | repeated | Optional caller-provided parameters used during instantiation. |






<a name="runtime-v1-ProcessLoadResult"></a>

### ProcessLoadResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| status | [ProcessLoadStatus](#runtime-v1-ProcessLoadStatus) |  |  |
| precheck | [ProcessRunPrecheckResult](#runtime-v1-ProcessRunPrecheckResult) |  |  |
| process_run | [ProcessRun](#runtime-v1-ProcessRun) |  |  |






<a name="runtime-v1-ProcessRunIssue"></a>

### ProcessRunIssue



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| failure | [ProcessLoadFailure](#runtime-v1-ProcessLoadFailure) |  |  |
| message | [string](#string) |  |  |
| severity | [ProcessRunIssueSeverity](#runtime-v1-ProcessRunIssueSeverity) |  |  |
| process_recipe_id | [string](#string) |  | Scope |
| sequence_definition_id | [string](#string) |  |  |
| task_definition_id | [string](#string) |  |  |
| required_tool_role | [string](#string) |  | Related requirement/resource |
| required_skill_id | [string](#string) |  |  |
| fixture_definition_id | [string](#string) |  |  |
| cell_id | [string](#string) |  |  |
| station_id | [string](#string) |  |  |
| actor_id | [string](#string) |  |  |
| resource_id | [string](#string) |  | tool/robot/fixture/asset/part instance if known |
| remediation | [string](#string) |  | Optional remediation hint |
| importance | [RequirementImportance](#runtime-v1-RequirementImportance) |  |  |






<a name="runtime-v1-ProcessRunPrecheckResult"></a>

### ProcessRunPrecheckResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ok | [bool](#bool) |  |  |
| issues | [ProcessRunIssue](#runtime-v1-ProcessRunIssue) | repeated |  |
| blocking_issue_count | [int32](#int32) |  | Optional summary counts for UI / fast filtering |
| warning_issue_count | [int32](#int32) |  |  |
| process_recipe_id | [string](#string) |  | What was checked |
| target_line_id | [string](#string) |  |  |
| task_feasibility | [TaskFeasibility](#runtime-v1-TaskFeasibility) | repeated | Optional: useful if precheck computes feasible assignments/resources |
| status | [ProcessRunPrecheckStatus](#runtime-v1-ProcessRunPrecheckStatus) |  | Optional overall status |






<a name="runtime-v1-TaskFeasibility"></a>

### TaskFeasibility



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_definition_id | [string](#string) |  |  |
| feasible | [bool](#bool) |  |  |
| candidate_actors | [common.v1.ActorRef](#common-v1-ActorRef) | repeated |  |
| candidate_robot_instance_ids | [string](#string) | repeated |  |
| candidate_tool_instance_ids | [string](#string) | repeated |  |
| candidate_container_instance_ids | [string](#string) | repeated |  |
| candidate_asset_instance_ids | [string](#string) | repeated |  |
| candidate_part_instance_ids | [string](#string) | repeated |  |
| issues | [ProcessRunIssue](#runtime-v1-ProcessRunIssue) | repeated |  |
| candidate_actor_evaluations | [CandidateActorEvaluation](#runtime-v1-CandidateActorEvaluation) | repeated |  |





 


<a name="runtime-v1-ProcessLoadFailure"></a>

### ProcessLoadFailure


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_LOAD_FAILURE_UNSPECIFIED | 0 |  |
| PROCESS_LOAD_FAILURE_PROCESS_RECIPE_NOT_FOUND | 2 | General failures |
| PROCESS_LOAD_FAILURE_PRODUCT_NOT_SUPPORTED | 3 |  |
| PROCESS_LOAD_FAILURE_RESOURCE_STATE_UNKNOWN | 4 |  |
| PROCESS_LOAD_FAILURE_NO_COMPATIBLE_CONTAINER | 10 | Container related failures |
| PROCESS_LOAD_FAILURE_REQUIRED_SLOT_NOT_FOUND | 11 |  |
| PROCESS_LOAD_FAILURE_REQUIRED_SLOT_TYPE_NOT_FOUND | 12 |  |
| PROCESS_LOAD_FAILURE_MISSING_TOOL_ROLE | 20 | Tool related failures |
| PROCESS_LOAD_FAILURE_TOOL_NOT_CALIBRATED | 21 |  |
| PROCESS_LOAD_FAILURE_TOOL_CAPABILITY_INSUFFICIENT | 22 |  |
| PROCESS_LOAD_FAILURE_ROBOT_UNAVAILABLE | 30 | Robot related failures |
| PROCESS_LOAD_FAILURE_ROBOT_TOOLING_MISMATCH | 31 |  |
| PROCESS_LOAD_FAILURE_NO_QUALIFIED_OPERATOR | 40 | Agent/operator related failures

A human is required but no worker with valid skills exists. |
| PROCESS_LOAD_FAILURE_NO_FEASIBLE_ACTOR | 41 | No actor type can perform the task. |
| PROCESS_LOAD_FAILURE_REQUIRED_SKILL_RESTRICTED | 42 |  |
| PROCESS_LOAD_FAILURE_REQUIRED_SKILL_EXPIRED | 43 |  |
| PROCESS_LOAD_FAILURE_COLLABORATION_MODE_UNSUPPORTED | 50 | Safety / collaboration related failures |
| PROCESS_LOAD_FAILURE_SAFETY_MODE_MISMATCH | 51 |  |
| PROCESS_LOAD_FAILURE_VISION_ASSET_UNAVAILABLE | 60 | Validation related failures |
| PROCESS_LOAD_FAILURE_VALIDATION_SOURCE_MISSING | 61 |  |
| PROCESS_LOAD_FAILURE_NO_FEASIBLE_VALIDATION_METHOD | 62 |  |
| PROCESS_LOAD_FAILURE_LINE_NOT_FOUND | 70 | Line related failures |
| PROCESS_LOAD_FAILURE_LINE_CLOSED | 71 |  |
| PROCESS_LOAD_FAILURE_LINE_BUSY | 72 |  |
| PROCESS_LOAD_FAILURE_LINE_BLOCKED | 73 |  |
| PROCESS_LOAD_FAILURE_CELL_NOT_FOUND | 80 | Cell related failures |
| PROCESS_LOAD_FAILURE_CELL_CLOSED | 81 |  |
| PROCESS_LOAD_FAILURE_CELL_BUSY | 82 |  |
| PROCESS_LOAD_FAILURE_CELL_BLOCKED | 83 |  |
| PROCESS_LOAD_FAILURE_STATION_NOT_FOUND | 90 | Station related failures |
| PROCESS_LOAD_FAILURE_STATION_CLOSED | 91 |  |
| PROCESS_LOAD_FAILURE_STATION_BUSY | 92 |  |
| PROCESS_LOAD_FAILURE_STATION_BLOCKED | 93 |  |
| PROCESS_LOAD_FAILURE_REQUIRED_PART_NOT_PRESENT | 100 | Part related failures |



<a name="runtime-v1-ProcessLoadStatus"></a>

### ProcessLoadStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_LOAD_STATUS_UNSPECIFIED | 0 |  |
| PROCESS_LOAD_STATUS_PRECHECK_FAILED | 1 |  |
| PROCESS_LOAD_STATUS_READY | 2 | feasible, but not instantiated (dry run) |
| PROCESS_LOAD_STATUS_LOADED | 3 | feasible and instantiated |



<a name="runtime-v1-ProcessLoadStrategy"></a>

### ProcessLoadStrategy


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_LOAD_STRATEGY_UNSPECIFIED | 0 |  |
| PROCESS_LOAD_STRATEGY_FIRST_FEASIBLE | 1 | Prefer the first feasible candidate found. |
| PROCESS_LOAD_STRATEGY_PREFER_AVAILABLE | 2 | Prefer OPEN stations over BUSY ones, and BUSY over queued ones. |
| PROCESS_LOAD_STRATEGY_PREFER_TARGET_SCOPE | 3 | Prefer keeping work inside the explicitly selected cell if one is set. |
| PROCESS_LOAD_STRATEGY_BEST_MATCH | 4 | Prefer the candidate with the strongest resource/actor match. |



<a name="runtime-v1-ProcessRunIssueSeverity"></a>

### ProcessRunIssueSeverity


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_RUN_ISSUE_SEVERITY_UNSPECIFIED | 0 |  |
| PROCESS_RUN_ISSUE_SEVERITY_BLOCKING | 1 | Run cannot start. Some reasons: no compatible fixture, required tool missing, robot required but unavailable, safety mode incompatible, no feasible actor for only-human/only-robot task |
| PROCESS_RUN_ISSUE_SEVERITY_WARNING | 2 | Run may start, but quality/performance may suffer. Examples: preferred robot unavailable (but human can do task), calibration expires soon, only one qualified actor available, vision unavailable but manual confirmation allowed. |



<a name="runtime-v1-ProcessRunPrecheckStatus"></a>

### ProcessRunPrecheckStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| PROCESS_RUN_PRECHECK_STATUS_UNSPECIFIED | 0 |  |
| PROCESS_RUN_PRECHECK_STATUS_OK | 1 | Neither warning nor blocking issues |
| PROCESS_RUN_PRECHECK_STATUS_OK_WITH_WARNINGS | 2 | One or more warning issues, but no blocking |
| PROCESS_RUN_PRECHECK_STATUS_BLOCKED | 3 | One or more blocking issues |



<a name="runtime-v1-RequirementImportance"></a>

### RequirementImportance


| Name | Number | Description |
| ---- | ------ | ----------- |
| REQUIREMENT_IMPORTANCE_UNSPECIFIED | 0 |  |
| REQUIREMENT_IMPORTANCE_REQUIRED | 1 |  |
| REQUIREMENT_IMPORTANCE_PREFERRED | 2 |  |


 

 

 



<a name="runtime_v1_sequence_run-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## runtime/v1/sequence_run.proto



<a name="runtime-v1-SequenceRun"></a>

### SequenceRun



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| sequence_definition_id | [string](#string) |  |  |
| parent_sequence_run_id | [string](#string) |  |  |
| child_sequence_run_ids | [string](#string) | repeated |  |
| child_task_run_ids | [string](#string) | repeated |  |
| state | [SequenceRunState](#runtime-v1-SequenceRunState) |  |  |
| completed_tasks | [int32](#int32) |  |  |
| can_bulk_complete | [bool](#bool) |  |  |
| assigned_actors | [common.v1.ActorRef](#common-v1-ActorRef) | repeated |  |






<a name="runtime-v1-SequenceRuns"></a>

### SequenceRuns



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [SequenceRun](#runtime-v1-SequenceRun) | repeated |  |





 


<a name="runtime-v1-SequenceRunState"></a>

### SequenceRunState


| Name | Number | Description |
| ---- | ------ | ----------- |
| SEQUENCE_RUN_STATE_UNSPECIFIED | 0 |  |
| SEQUENCE_RUN_STATE_NOT_READY | 1 |  |
| SEQUENCE_RUN_STATE_READY | 2 |  |
| SEQUENCE_RUN_STATE_IN_PROGRESS | 3 |  |
| SEQUENCE_RUN_STATE_DONE | 4 |  |
| SEQUENCE_RUN_STATE_ABORTED | 5 |  |


 

 

 



<a name="runtime_v1_task_run-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## runtime/v1/task_run.proto



<a name="runtime-v1-TaskRun"></a>

### TaskRun



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| task_definition_id | [string](#string) |  |  |
| parent_sequence_run_id | [string](#string) |  |  |
| state | [TaskRunState](#runtime-v1-TaskRunState) |  |  |
| candidate_actors | [common.v1.ActorRef](#common-v1-ActorRef) | repeated |  |
| assigned_actor | [common.v1.ActorRef](#common-v1-ActorRef) |  |  |
| can_do | [bool](#bool) |  |  |
| can_undo | [bool](#bool) |  |  |
| workable_horizon | [int32](#int32) |  | steps needed to complete before this step is workable. |
| estimated_duration | [common.v1.EstimatedDuration](#common-v1-EstimatedDuration) |  |  |
| started_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| completed_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| error_code | [string](#string) |  |  |
| error_message | [string](#string) |  |  |
| evidence | [ExecutionEvidence](#runtime-v1-ExecutionEvidence) | repeated | TODO: consider delete, already &#39;linked to&#39; from ExecutionEvidence |
| binding | [TaskRuntimeBinding](#runtime-v1-TaskRuntimeBinding) |  |  |
| restrictions | [RuntimeRestriction](#runtime-v1-RuntimeRestriction) | repeated | Effective runtime restrictions that currently apply to this task.

These restrictions are the effective restrictions for the currently assigned actor and execution context. They may be copied from candidate-level evaluation results during assignment or reassignment.

Examples: - AR guidance required because the assigned actor&#39;s skill is restricted - supervisor approval required before completion - tool feedback required due to safety/quality constraints |
| candidate_actor_evaluations | [CandidateActorEvaluation](#runtime-v1-CandidateActorEvaluation) | repeated |  |






<a name="runtime-v1-TaskRuns"></a>

### TaskRuns



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [TaskRun](#runtime-v1-TaskRun) | repeated |  |






<a name="runtime-v1-TaskRuntimeBinding"></a>

### TaskRuntimeBinding
Concrete runtime/deployment bindings resolved for this task run.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| asset_instance_id | [string](#string) |  |  |
| robot_instance_id | [string](#string) |  |  |
| station_id | [string](#string) |  |  |
| cell_id | [string](#string) |  |  |
| container_slot | [resources.v1.ContainerSlotRef](#resources-v1-ContainerSlotRef) |  |  |





 


<a name="runtime-v1-TaskRunState"></a>

### TaskRunState


| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_RUN_STATE_UNSPECIFIED | 0 |  |
| TASK_RUN_STATE_NOT_READY | 1 |  |
| TASK_RUN_STATE_READY | 2 |  |
| TASK_RUN_STATE_IN_PROGRESS | 3 |  |
| TASK_RUN_STATE_DONE | 4 |  |
| TASK_RUN_STATE_ERROR | 5 |  |
| TASK_RUN_STATE_ABORTED | 6 |  |


 

 

 



<a name="runtime_v1_validation_result-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## runtime/v1/validation_result.proto



<a name="runtime-v1-ValidationResult"></a>

### ValidationResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| task_run_id | [string](#string) |  |  |
| status | [ValidationStatus](#runtime-v1-ValidationStatus) |  |  |
| method | [string](#string) |  | tool_feedback / vision / manual / external_qc |
| validated_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| measurements | [common.v1.KeyValueConstraint](#common-v1-KeyValueConstraint) | repeated |  |
| validated_by_actor | [common.v1.ActorRef](#common-v1-ActorRef) |  |  |
| comment | [string](#string) |  |  |





 


<a name="runtime-v1-ValidationStatus"></a>

### ValidationStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| VALIDATION_STATUS_UNSPECIFIED | 0 |  |
| VALIDATION_STATUS_PENDING | 1 |  |
| VALIDATION_STATUS_PASSED | 2 |  |
| VALIDATION_STATUS_FAILED | 3 |  |
| VALIDATION_STATUS_BYPASSED | 4 |  |


 

 

 



<a name="service_v1_ar_client-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## service/v1/ar_client.proto



<a name="service-v1-ARClientMessage"></a>

### ARClientMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| role | [ARClientRole](#service-v1-ARClientRole) |  |  |
| operator_id | [string](#string) |  |  |





 


<a name="service-v1-ARClientRole"></a>

### ARClientRole


| Name | Number | Description |
| ---- | ------ | ----------- |
| AR_CLIENT_ROLE_UNSPECIFIED | 0 |  |
| AR_CLIENT_ROLE_MAIN | 1 |  |
| AR_CLIENT_ROLE_SPECTATOR | 2 |  |


 

 

 



<a name="service_v1_response-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## service/v1/response.proto



<a name="service-v1-Response"></a>

### Response



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| success | [bool](#bool) |  | True if the request was carried out, false if an error occured |
| message | [string](#string) |  | Either a status/response message or an error message if the request wasn&#39;t a success |





 

 

 

 



<a name="service_v1_robot_adapter-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## service/v1/robot_adapter.proto



<a name="service-v1-RobotAdapterInfoMessage"></a>

### RobotAdapterInfoMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_id | [string](#string) |  |  |
| robot_type | [string](#string) |  | TODO: use type enum? |
| identifier | [string](#string) |  |  |





 

 

 

 



<a name="service_v1_server-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## service/v1/server.proto



<a name="service-v1-ServerHeartbeat"></a>

### ServerHeartbeat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| service | [string](#string) |  | e.g. &#34;backend&#34; |
| server_id | [string](#string) |  | stable id (hostname/uuid) |
| epoch | [uint64](#uint64) |  | increments on restart (same concept as your restart storm protection) |
| unix_ms | [int64](#int64) |  | server time |
| ip | [string](#string) |  | ip of server |






<a name="service-v1-ServerInfo"></a>

### ServerInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| service | [string](#string) |  | E.g. &#34;backend&#34; |
| instance_id | [string](#string) |  | random UUID per process start |
| epoch | [uint64](#uint64) |  | Increments each restart (or derived) |
| started_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| reset_reason | [string](#string) |  | e.g. &#34;process_restart&#34;, &#34;db_wiped&#34; |
| data_wiped | [bool](#bool) |  | If true clients should strongly consider refetching data |





 

 

 

 



<a name="service_v1_status-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## service/v1/status.proto



<a name="service-v1-ServiceStatus"></a>

### ServiceStatus



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| type | [string](#string) |  |  |
| ip | [string](#string) |  |  |
| status | [Status](#service-v1-Status) |  |  |





 


<a name="service-v1-Status"></a>

### Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS_UNSPECIFIED | 0 |  |
| STATUS_OFFLINE | 1 |  |
| STATUS_ONLINE | 2 |  |


 

 

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

