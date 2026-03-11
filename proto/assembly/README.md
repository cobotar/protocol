Consider a new structure:

## Product
```protobuf
message ProductDefinition
message PartDefinition
message AssemblyNode
```

## Resources
```protobuf
message ModelArtifact
message ToolDefinition
message ToolInstance
message FixtureDefinition
message FixtureInstance
message RobotDefinition
message RobotInstance
message WorkerDefinition
message StationDefinition
message CellDefinition
message AssetDefinition
message AssetInstance
```

## Capability
```protobuf
message SkillDefinition
message SkillRequirement
message ActorSkill
message ToolRequirement
message CapabilityProfile
message Constraint
```

## Process template
```protobuf
message ProcessRecipe
message SequenceDefinition
message TaskDefinition
```

## Runtime
```protobuf
message ProcessRun
message SequenceRun
message TaskRun
message Assignment
message ExecutionEvidence
message ValidationResult
```