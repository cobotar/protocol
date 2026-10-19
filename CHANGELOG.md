# Changelog

## Unreleased

### Added

- `resources.v1.RobotAdapterDefinition`, describing the static commands, telemetry, supported robot types and configurable I/O register kinds supplied by an adapter implementation (cobotar/protocol#14).
- A staged, descriptor-validated NATS subject catalog and generated subject helpers for Go, C#, TypeScript, and Python. Planned routes remain available for incremental implementation without being treated as enforced runtime contracts (cobotar/protocol#11).
- `runtime.v1.ProcessRunDefinitions`: the recipe, sequence, task and part definitions a process run was loaded with, so every client shows and uses the same definitions as the backend while the run is active, whatever happens to the definitions afterwards. `source` says whether it holds the pinned definitions or, once the retention period after the run has passed, the latest ones. AR content isn't pinned and stays live. Published as an added event when a run is loaded (cobotar/protocol#18, part of cobotar/protocol#17).
- `runtime.v1.ProcessRunDefinitionsRequest` to fetch a run's definitions by process run ID.
- Predefined string rules and stricter field validation for execution evidence and evidence facts.

### Changed

- `resources.v1.RobotDefinition` now selects a robot adapter definition, and `robot.v1.RobotAdapterInfoMessage` references that definition while reporting the connected controller identity, adapter version and configured I/O catalog. The former `RobotDriverType`, `driver_type`, legacy adapter identity fields and embedded `RobotAdapterCapabilities` have been removed (cobotar/protocol#14).
- `max_concurrent_processes` on lines, cells and stations is documented to count only active runs.
