# Sources and evidence

All online sources below belong to Conductor. The study accessed them on October 12, 2026 through ego-browser. Notes paraphrase the source and identify its use in the report. The study retains links and focused API observations instead of copying complete documentation pages.

| Source | Evidence used |
| --- | --- |
| [Harness overview](https://www.conductor.build/docs/reference/harnesses) | Conductor, harness, session, and model responsibilities. Bundled executables and supported harnesses. |
| [Isolated workspaces](https://www.conductor.build/docs/concepts/workspaces-and-branches) | Project and repository relationship. Branches, working trees, processes, and local worktree isolation. |
| [Parallel agents](https://www.conductor.build/docs/concepts/parallel-agents) | Separate workspaces for independent tasks. Shared workspaces for coordinated work on one branch. |
| [Workflow](https://www.conductor.build/docs/concepts/workflow) | Delegation, feedback, PR integration, merge, archive, and restoration. |
| [Multiple Codex sessions](https://www.conductor.build/docs/guides/parallel-agents/run-multiple-codex-sessions) | Workspace ownership of chats, terminals, diffs, and review state. Scoped prompts and context practices. |
| [Multiple Claude Code sessions](https://www.conductor.build/docs/guides/parallel-agents/run-multiple-claude-code-sessions) | Equivalent workspace-based organization for Claude Code. Shared files across chats. |
| [Agent behavior](https://www.conductor.build/docs/reference/agent-behavior) | Session controls, repository instructions, instruction files, skills, and task context. |
| [Claude Code harness](https://www.conductor.build/docs/reference/harnesses/claude-code) | Managed or configured executable and provider configuration. |
| [Codex harness](https://www.conductor.build/docs/reference/harnesses/codex) | Managed or configured executable and supported controls. |
| [MCP reference](https://www.conductor.build/docs/reference/mcp) | Harness-specific MCP configuration and session status reporting. |
| [Scripts](https://www.conductor.build/docs/reference/scripts) | Setup, run, and archive hooks. Port allocation and process concurrency controls. |
| [Environment variables](https://www.conductor.build/docs/reference/environment-variables) | Workspace and session environment scope. Local and cloud differences. |
| [Settings](https://www.conductor.build/docs/reference/settings) | User, repository, local override, and managed configuration layers. |
| [Conductor Cloud](https://www.conductor.build/docs/cloud) | Organization, Cloud Computer, workspace sandbox, and build inheritance. |
| [Multiplayer](https://www.conductor.build/docs/cloud/collaboration) | Shared workspaces and chats. Assignment, following, and teammate handoff. |
| [Cloud workspace operations](https://www.conductor.build/docs/cloud/working-with-cloud-workspaces) | Sandbox lifecycle, process interruption, SSH, and one-way file synchronization. |
| [Security and permissions](https://www.conductor.build/docs/reference/security-and-permissions) | Local execution privileges and cloud Linux sandboxes. |
| [Conductor API](https://www.conductor.build/docs/api) | Cloud management operations, manager examples, explicit briefs, supervision, and routines. |
| [Conductor MCP server](https://www.conductor.build/docs/api/mcp) | Hosted cloud management tools, authentication, sessions, messages, and cancellation. |
| [OpenAPI contract](https://api.conductor.build/v0/openapi.json) | Distinct identifiers, exact state values, message delivery, retry behavior, and asynchronous cancellation. |
| [Diff viewer](https://www.conductor.build/docs/reference/diff-viewer) | Feedback attached to changed code and suggested PR actions. |
| [Checks](https://www.conductor.build/docs/reference/checks) | Review readiness signals and integration blockers. |
| [Todos](https://www.conductor.build/docs/reference/todos) | Work items that remain before merge. |
| [Checkpoints](https://www.conductor.build/docs/reference/checkpoints) | Private Git references, turn restoration, and shared-chat caution. |

## Local evidence

The installed app reports version `0.90.1` through its `Info.plist`. Local bundled files can differ from live documentation. The study read these files without executing the checkpoint helper or altering application state.

| File | Observation |
| --- | --- |
| `/Applications/Conductor.app/Contents/Resources/conductor-skill/skills/conductor/SKILL.md` | Documents workspace scope, configuration, local versus cloud controls, scripts, and agent controls. It says local workspaces have no management CLI or API. |
| `/Applications/Conductor.app/Contents/Resources/bin/checkpointer.sh` | Saves private checkpoint refs and separate staged and working-file snapshots. Uses Git object operations and a temporary index. |
| `/Applications/Conductor.app/Contents/Resources/bin/conductor` | A short wrapper invokes `.internal/conductor-runtime` with `cli`. Its presence alone does not establish local workspace management support. |
| `/Applications/Conductor.app/Contents/Info.plist` | Supplies installed app version `0.90.1`. |

## Evidence limits

The report treats official documentation as evidence of supported behavior. It treats the OpenAPI document as the external contract at the retrieval date. It treats readable bundled scripts as evidence of that installed helper implementation.

The report does not derive internal architecture from executable strings or private application databases. Diagram edges describe ownership rather than internal process boundaries. The manager pattern is documented, but this study did not launch a manager or worker to test it.
