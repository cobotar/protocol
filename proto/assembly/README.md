## Assembly
Current structure:
- Product structure
  product.proto
  CAD/BOM-derived product hierarchy
- Process template
  process.proto
  what work must be done
- Runtime
  execution.proto
  actual execution state
- Resources
  resources.proto
  tools, robots, fixtures, assets
- Skills
  skill.proto
  actor capabilities
- Station/cell
  station.proto
  deployment environment
- Precheck
  process_requests.proto
  feasibility analysis



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