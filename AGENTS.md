# Agent instructions

## This repository

- **Purpose:** Language-neutral protobuf contracts for the CobotAR platform. The schemas cover AR experiences, capabilities, geometry, processes, products, resources, robots, runtime messages, services, validation, and variants, and are published for Go, Python, C#, and TypeScript consumers.
- **Canonical source:** All protocol changes start in `proto/`. Schemas use Buf's v2 module configuration and Protovalidate rules from `buf.build/bufbuild/protovalidate`.
- **Toolchain:** Buf handles schema linting, formatting, breaking-change detection, and generation. Remote Buf plugins generate Go protobufs, Python protobufs and type stubs, C#, TypeScript using `@bufbuild/protobuf`, and Markdown documentation.
- **Local workflow:** There is no application server or development runtime. Edit `.proto` files, run `buf format -d -w` (or `make format`), `buf lint` (or `make lint`), and `buf build`. Use `buf breaking --against ".git#branch=main"` (or `make breaking`) when checking compatibility.
- **Generation:** Run `buf generate` for a non-destructive generation pass, or `make generate` to clear and rebuild all generated language outputs. `make verify` currently runs formatting, linting, and the destructive generation target; inspect the resulting diff carefully.
- **Tests / builds:** The repository has no unit-test suite; `npm test` is only a placeholder. Schema validation is performed with Buf. When relevant, generated packages can additionally be checked with `go test ./...`, `dotnet build csharp/csharp.csproj`, `python3 -m build`, or the applicable consumer toolchain.
- **Source layout:** Domain schemas live under `proto/<domain>/v1/`; shared predefined validation rules live under `proto/validation/v1/`. `buf.yaml` defines the module and lint/breaking policies, while `buf.gen.yaml` defines all generated outputs.
- **Generated files, don't edit by hand:** `messages/` contains Go output, `src/cobotar_protocol/` Python output, `csharp/*.cs` C# output, `lib/` TypeScript output, and `documentation/README.md` generated reference documentation. Change `proto/` and regenerate instead. Keep hand-maintained packaging files such as `csharp/csharp.csproj` intact.
- **Packages / releases:** The same version is published as the Go module `github.com/cobotar/protocol`, npm package `@cobotar/protocol`, Python package `cobotar-protocol`, and NuGet package `cobotar.protocol`. `bump-my-version` synchronizes versions in the package manifests and creates `vX.Y.Z` tags; tagged releases run Buf CI before package publication. Use `make publish bump={patch,minor,major}` only when explicitly asked to publish because it commits, tags, and pushes.

## Issue tracking (applies to all cobotar repos)

Work is tracked in GitHub issues in the `cobotar` organisation and collected on the **CobotAR Roadmap** project board. See CONTRIBUTING.md in `cobotar/.github` for the details.

When you are asked to track, plan or pick up work:

1. **Search first.** Look for an existing issue (`gh issue list --repo cobotar/<repo> --search "<keywords>"`, or the GitHub MCP tools) before creating a new one.
2. **Create issues in the repo where the code changes.** Use issue type Bug, Feature or Task. Add the label `needs-decision` for open design or protocol questions, and `breaking-change` for protocol changes that consumers must follow.
3. **Issue body:** context, with permalinks to the relevant lines (a `blob/<sha>/path#Lx-Ly` URL), then a checklist, then a "Done when" section.
4. **Changes across repos:** create a parent issue (usually in `protocol`) and sub-issues in each affected repo.
5. **Put every new issue on the CobotAR Roadmap board.** With `gh`, always pass `--project "CobotAR Roadmap"` to `gh issue create` (a GitHub Action also adds new issues as a fallback). Then set Status, Priority (P0–P3), Area and Size on the board item (`gh project item-edit`, or in the browser).

## Code conventions

- When a TODO needs tracking, reference the issue: `// TODO(#42): ...` or `// TODO(cobotar/protocol#7): ...`. Don't add bare TODOs for anything larger than a local cleanup.
- Commit messages: Conventional Commits (`feat(scope): ...`, `fix(scope): ...`, `!` for breaking). Put `Fixes cobotar/<repo>#<n>` in the body when the commit resolves an issue.
- Protocol changes: never edit generated code; change `proto/`, then regenerate, bump the version and update the CHANGELOG.
