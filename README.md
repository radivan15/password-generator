# Password/Secrets Generator CLI

A CLI to generate cryptographically secure random passwords, with configurable length and charset.


> Status: Phase 1 in progress 

---

## What it does

By the end of this project:

- Passwords are generated with Python's `secrets` module (CSPRNG), not `random`, which is predictable and unsafe for cryptographic purposes
- Length, character categories (uppercase, lowercase, digits, symbols) and number of passwords are configurable via CLI flags
- Invalid input (non-positive length, every charset disabled) fails fast with a clear message and a non-zero exit code, not a traceback
- stdout carries only the passwords, logs and errors go to stderr, so output can be piped safely and the password value is never logged
- Code quality is enforced by tooling: ruff + mypy for lint and types, pytest for tests, pip-audit for dependency scanning, all wired into `just check` and pre-commit

---

## Why I'm building it

With a background in SRE/Cloud Engineering, I'm familiar with secrets management and credential rotation concepts in production, but had never written a generator myself. I'm building this to learn Python fundamentals (`secrets`, `argparse`) while connecting them to real-world security practices.

---

## Stack

| Component | Technology | Notes |
|---|---|---|
| Language | Python >= 3.13 | |
| Package manager | uv | |
| CLI parsing | `argparse` (stdlib) | |
| Random generator | `secrets` (stdlib) | CSPRNG, not `random` |
| Logging | loguru | Writes to stderr, never logs password values |
| Linting & formatting | ruff | Phase 2 |
| Type checking | mypy | Phase 2 |
| Testing | pytest + pytest-cov | Phase 2 |
| Dependency security scan | pip-audit | Phase 2 |
| Task runner | Just (`Justfile`) | Phase 2 |
| Pre-commit hooks | pre-commit | Phase 2 |

---

## Folder Structure

Current (Phase 1, small project):

```
password-generator/
├── main.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
├── LICENSE
├── ROADMAP.md
└── README.md
```

Will grow in Phase 2 (`src/`, `tests/`, `Justfile`).

---

## Installation

Requires [uv](https://docs.astral.sh/uv/) and Python >= 3.13.

```powershell
git clone https://github.com/radivan15/password-generator.git
cd password-generator
uv sync
```

---

## How to Run

```powershell
uv run python main.py
```

CLI flags (`--length`, `--count`, charset toggles) are not available yet, see [ROADMAP.md](ROADMAP.md).

---

## Roadmap

Detailed execution roadmap is in [ROADMAP.md](ROADMAP.md).

---

## License

MIT — see [LICENSE](LICENSE).