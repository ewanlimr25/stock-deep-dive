# Stock Deep Dive Project

This is an end-to-end quantitative analysis tool for single-equity research, synthesizing options flow, dark pool prints, dealer positioning, and multi-timeframe context into actionable trade plans.

## Necessary Agents for This Project

Use ONLY these agents when the task requires spawning a specialized team:

### Always Relevant
- **sweep-tracker** — Identifies aggressive options sweeps and smart money flow for directional momentum trades
- **accumulation-hunter** — Detects quiet institutional accumulation using dark pool prints, OI buildup, and volume before a price move
- **risk-monitor** — Monitors watchlist for correlated risk, regime changes, and conflicting signals

### Frequently Relevant
- **contrarian-scanner** — Finds overcrowded bullish/bearish positions using put/call extremes and flow divergence
- **earnings-scout** — Evaluates upcoming earnings plays by cross-referencing options flow and IV rank

### Code/Analysis Work (if needed)
- **python-reviewer** — For any Python code changes or analysis scripts
- **code-reviewer** — General code review for quality/security/simplification
- **tdd-guide** — When writing new analysis features or fixing bugs
- **database-reviewer** — For DuckDB query optimization and local data access patterns
- **planner** — For complex feature design or architectural decisions

### DO NOT USE
- All language-specific reviewers: typescript-reviewer, rust-reviewer, kotlin-reviewer, java-reviewer, cpp-reviewer, go-reviewer, flutter-reviewer
- All build resolvers for non-Python: rust-build-resolver, kotlin-build-resolver, cpp-build-resolver, go-build-resolver, java-build-resolver
- Job/career agents: job-scout
- Communication agents: chief-of-staff
- Infrastructure/meta agents: refactor-cleaner, doc-updater, harness-optimizer, loop-operator, security-reviewer, e2e-runner

## Workspace & Environment

- **Primary directory:** `/Users/ewan/Development/stock-deep-dive`
- **Data substrate:** `~/Documents/Stocks/` parquet files (via uw-pp MCP)
- **CLI tools:** `uw` CLI (Finviz, Unusual Whales, etc.)
- **Local analysis:** DuckDB for custom queries
- **Python version:** 3.12.3 (via pyenv)

## Key Skills

- `/stock-deep-dive` — Main skill for end-to-end deep dive research
- `/deep-dive-calibration` — Calibration and quality checks
- `/python-patterns` — Pythonic idioms and best practices
- `/python-testing` — TDD and test coverage for analysis scripts
- `/python-review` — Code quality for Python analysis

## Git Workflow

Use conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`

Commit messages should be concise and reflect the "why" of changes. See `~/.claude/rules/common/git-workflow.md` for details.
