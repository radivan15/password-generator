# Roadmap — Password/Secrets Generator CLI

My execution plan for this project, broken into phases. I'll check items off as I go.

## Phase 1 — Small Project

- [ ] Set up project (`uv init`) → verify: `main.py` & `pyproject.toml` created
- [ ] Understand why `secrets` is used instead of `random` → verify: able to explain the difference
- [ ] Generate 1 secure character from a single charset → verify: code runs, prints 1 character
- [ ] Loop into a string of length N → verify: password of length N printed
- [ ] Add `argparse` for `--length` → verify: length configurable via CLI
- [ ] Add charset toggles (`--no-uppercase`, etc.) → verify: charset changes according to flags
- [ ] Add `--count` to generate multiple passwords at once → verify: multiple passwords printed
- [ ] Validate input (length <= 0, every charset disabled) → verify: clear error message + non-zero exit code, no traceback
- [ ] Add `loguru` logging to stderr, keep stdout for passwords only → verify: `uv run python main.py 2>$null` prints only passwords, password value never appears in logs

Throughout Phase 1: every function has type hints (`def generate(length: int) -> str:`).

## Phase 2 — Medium Project

- [ ] Set up `ruff` + `mypy` in `pyproject.toml` → verify: `ruff check .` and `mypy .` clean on existing code
- [ ] Move password logic to `src/generator.py` as testable pure functions → verify: `main.py` still works via CLI
- [ ] Write tests in `tests/` with `pytest` (`@pytest.mark.parametrize` for charset combinations & length edge cases) → verify: `pytest tests/ -v` green, coverage ≥ 70% (`pytest --cov=src tests/`)
- [ ] (Optional) Property-based tests with `hypothesis`: for any length/charset, output length == length and every char is in the charset
- [ ] Set up `pip-audit` for dependency scanning → verify: scan runs (expect few findings, the project uses only stdlib at runtime)
- [ ] Create `Justfile` (`lint`, `test`, `security`, `check`, `format`) → verify: `just check` all green
- [ ] Set up pre-commit hooks (`ruff` + `mypy`) → verify: a deliberately bad commit gets blocked
- [ ] Push per feature

## Phase 3 — Large Project (optional)

This CLI is realistically "done" after Phase 2. I'd only come back to this phase if I decide to turn it into something bigger than a local CLI:

- [ ] Add `structlog` for audit logging (log the generate *event*, never the password value itself — that's the whole hygiene lesson)
- [ ] Load default policy (length, charset) from environment variables via `pydantic-settings`, instead of hardcoding
- [ ] Wrap it as a small FastAPI endpoint with `lifespan` + graceful SIGTERM shutdown, if I ever want to run it as a service instead of a local CLI

## Backlog — ideas for later

Things I might explore after Phase 2 is solid. Not committing to these yet.

- Guarantee at least 1 character per active category (common real-world policy, e.g. AWS IAM / AD) — first candidate after Phase 2
- Passphrase mode (diceware-style, word-based)
- Exclude ambiguous characters
- Entropy/strength indicator in the output
