# Contributing to simple-venn

## Development setup

Clone the repository and install dependencies with [uv](https://docs.astral.sh/uv/):

```console
$ git clone git@github.com:msto/simple-venn.git
$ cd simple-venn
$ uv sync --locked
```

This installs all runtime and development dependencies (pytest, mypy, ruff, etc.) in an
isolated virtual environment. Run commands via `uv run`:

```console
$ uv run poe check-all
```

## Running checks

All checks must pass before committing. The task runner is
[poethepoet](https://github.com/nat-n/poethepoet):

```console
$ uv run poe fix-and-check-all  # Auto-fix lint/format, then run typing and tests
$ uv run poe check-all          # Run all checks without auto-fixing
$ uv run poe check-tests        # Run tests only
$ uv run poe check-typing       # Run mypy only
$ uv run poe check-lint         # Run ruff lint only
$ uv run poe check-format       # Run ruff format check only
```

Run a single test file or function:

```console
$ uv run pytest tests/test_venn.py
$ uv run pytest tests/test_venn.py::test_function_name
```

## Commit and PR guidelines

- Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages
  (e.g. `feat:`, `fix:`, `docs:`, `refactor:`, `test:`)
- Run `uv run poe fix-and-check-all` before each commit; all checks must pass
- Keep commits focused: one logical change per commit
- Never mix formatting and functional changes in the same commit
- PR titles should follow Conventional Commit format, under 72 characters

## Release process

1. **Review and merge all PRs** intended for the release.
2. **Create a version-bump PR.** With Claude Code, run `/prepare-release X.Y.Z`
   which automates the version bump and commit. Or do it manually:
   - Run `uv version <new_version>` (e.g. `uv version 0.2.0`) to update `pyproject.toml`.
   - Run `uv lock` to update the lock file.
   - Commit and open a PR (e.g. `chore: Release v0.2.0`).
3. **Merge the version-bump PR.**
4. **Tag the merge commit** on `master` with the version number (e.g. `0.2.0`). Pushing
   the tag triggers the publish workflow, which builds the package, publishes to TestPyPI
   and PyPI, generates a changelog with git-cliff, and creates a GitHub release.
5. **Create and merge a follow-up PR** bumping the version to the next minor dev version.
   With Claude Code: `/prepare-dev X.Y.0-dev`. Or manually: `uv version X.Y.0-dev`,
   `uv lock`, commit, and open a PR.
