# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

simple-venn is a Python library for plotting two-way, three-way, and four-way Venn diagrams using matplotlib. It exposes three public functions: `venn2`, `venn3`, `venn4` from `simple_venn/venn.py`. API is mostly compatible with matplotlib_venn but returns `AxesSubplot` instead of `VennDiagram`.

## Development

Uses uv for dependency management and poethepoet for task running.

```bash
uv sync --locked          # Install dependencies
uv run poe check-all      # Run all checks (lock, format, lint, typing, tests)
uv run poe fix-and-check-all  # Auto-fix then check
uv run pytest             # Run tests only
uv run pytest tests/test_foo.py::test_name  # Run a single test
uv run poe check-typing   # mypy only
uv run poe check-lint     # ruff lint only
uv run poe fix-format     # Auto-format with ruff
```

## Code Style

- Ruff for linting and formatting (line length 100, target Python 3.12)
- Google-style docstrings enforced via ruff's pydocstyle rules
- isort configured with force-single-line imports
- mypy with strict settings (untyped defs disallowed, strict optional, etc.)
- No tests directory exists yet; pytest is configured with `--import-mode=importlib`

## Git Workflow

### Commit Granularity

Commit after completing one of:
- A single function/method implementation
- One refactoring step (rename, extract, move)
- A bug fix with its regression test
- A documentation update

**Size guidelines:**
- Per commit: 100–300 lines preferred, 400 max
- Per PR: No hard limit, but consider splitting if >800 lines or >5 unrelated files

**Good commit scope examples:**
- `Add FastaIndex.validate() method`
- `Rename species_map → species_to_ref_fasta_map`
- `Fix off-by-one in BED coordinate parsing`

### Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages and PR
titles. Common types: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`.

```
<type>: <imperative description> (<72 chars total)

Detailed body explaining:
- What changed
- Why (link issues with "Closes #123" or "Related to #456")
- Any non-obvious implementation choices
```

### Commit Rules
- Run `uv run poe fix-and-check-all` before each commit; all checks must pass
- No merge commits
- Do not rebase without explicit user approval
- **Never mix formatting and functional changes.** If unavoidable, isolate formatting into separate commits at start or end of branch.

### Pull Requests
- Title: Conventional Commit format, <72 chars (e.g., "feat: Add FASTA index validation")
- Body: What changed, why, testing done, migration notes if applicable
- Link issues: "Closes #123" or "Related to #456"

### Release Process

See CONTRIBUTING.md for the full process. In short: (1) merge all PRs, (2) create a PR
bumping version with `uv version` and moving CHANGELOG entries, (3) merge it, (4) create
GitHub release with tag, (5) merge a follow-up PR bumping to `{next_minor}-dev`.

## Coding Conventions

### Organization
- Extract logic into small–medium functions with clear inputs/outputs
- Scope variables tightly; limit visibility to where needed
- Use block comments for visual separation when function extraction isn't practical

### Naming
- Meaningful names, even if long: `species_to_ref_fasta_map` not `species_map`
- Short names only for tight scope (loop indices, single-line lambdas)
- Signal behavior in function names: `to_y()`, `is_valid()` → returns value; `update_x()` → side effect

### Documentation

**Doc comments (required on all public functions/classes):**
- What it does
- Parameters and return value
- Constraints, exceptions raised, side effects

**Code comments:**
- Explain non-obvious choices and complex logic
- Never comment self-evident code

### Type Signatures
- **Parameters:** Accept the most general type practical (e.g., `Iterable` over `List`)
- **Returns:** Return the most specific type without exposing implementation details

### Functions
- Functions should have **either** returns **or** side effects, not both
- Exceptions: logging, caching (where side effect is performance-only)

### Pragmatism
- Balance functional, OOP, and imperative—use what's clearest
- When in doubt, prefer pure functions and immutable data
- Know your utility libraries; contribute upstream rather than writing one-offs

## Testing

### Principles
- Generate test data programmatically; avoid committing test data files
- Test behavior, not implementation—tests should survive refactoring
- Cover: expected behavior, error conditions, boundary cases
- Scale rigor to code longevity: thorough for shared code, lighter for one-off scripts

### Coverage Expectations
- New public functions: at least one happy-path test + one error case
- Bug fixes: add a regression test that would have caught the bug
- Performance-critical code: include benchmark or explain in PR why not needed

## Documentation Maintenance

When modifying code, update as needed:
- [ ] Docstrings (if signature or behavior changed)
- [ ] CHANGELOG.md — **required** for every PR with user-facing changes (new features, bug fixes, breaking changes). Add entries under the `[Unreleased]` section using [Keep a Changelog](https://keepachangelog.com/) categories: Added, Changed, Deprecated, Removed, Fixed, Security.
- [ ] README.md (if usage patterns changed)
- [ ] Migration notes (if breaking change)

Reference issue/PR numbers in CHANGELOG entries.

## Python-Specific

### Style
- Heavier use of classes and type annotations than typical Python
- Prefer `@dataclass(frozen=True)` and Pydantic models with `frozen=True`
- Isolate I/O at module boundaries; keep core logic as pure functions
- Google-style docstrings with `Args:`, `Returns:`, `Yields:`, and `Raises:` blocks

### Typing
- **Required:** Type annotations on all function parameters and returns
- Annotate locals when: they become return values, or called function lacks hints
- Use type aliases or `NewType` for complex structures
- Avoid `Any`—prefer type alias or `TypeVar`
- Avoid `cast()` or `type: ignore` - reconsider and suggest workarounds.

