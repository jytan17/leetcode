# LeetCode Workspace

Local scratch for drilling LeetCode in Python and Rust. AI agent scaffolds problem + tests; you write the solution; paste back to leetcode.com when green.

## Prerequisites

- [just](https://github.com/casey/just) — `brew install just`
- Python 3.10+ with `pytest`
- Rust toolchain (`cargo`)

### Python setup

```fish
uv venv
uv pip install pytest
source .venv/bin/activate.fish
```

Or any equivalent (`python -m venv`, `pipx`, system pip).

## Layout

```
problems/
  p<NNNN>_<snake_name>/        # e.g. p0001_two_sum
    README.md                   # problem statement, constraints, examples
    python/
      solution.py
      test_solution.py
    rust/
      Cargo.toml
      src/lib.rs
      tests/cases.rs
templates/                      # scaffolding source
Cargo.toml                      # rust workspace, members = problems/*/rust
conftest.py                     # makes pytest find solution.py per problem
justfile
CLAUDE.md                       # rules for the AI agent
```

Folder name: zero-padded 4-digit problem number + snake_case title (`p0146_lru_cache`).

## Workflow

1. Give the agent a problem (URL, title, or pasted statement) and target language(s).
2. Agent runs `just new <slug> <lang>` and fills:
   - `README.md` — statement, constraints, examples, complexity target
   - `solution.py` / `src/lib.rs` — exact LeetCode signature, body left empty
   - tests — every LeetCode example + edge cases
3. You implement. Iterate with `just test <slug> <lang>` until green.
4. Copy `solution.py` / `lib.rs` body back into LeetCode and submit.

## Commands

```
just                            # list recipes
just new <slug> <lang>          # scaffold (lang = python | rust)
just test <slug> <lang>         # run tests for one problem
just test-python <slug>
just test-rust <slug>
just list                       # list scaffolded problems
```

Direct equivalents:

```
pytest problems/<slug>/python -v
cargo test -p <slug>
```

## Conventions

### Python
- Single `class Solution` with LeetCode's exact method name and types.
- Tests use `pytest.mark.parametrize`.
- `ListNode` / `TreeNode` definitions go inside `solution.py` (match LeetCode verbatim).

### Rust
- `struct Solution;` + `impl Solution { pub fn ... }` with LeetCode's exact signature (`i32`, `Vec<i32>`, etc.).
- Package name in `Cargo.toml` = folder name → enables `cargo test -p <slug>`.
- Integration tests in `tests/cases.rs`.
- For unordered output, sort or set-compare before asserting.

## Adding a problem manually

```
just new p0042_trapping_rain_water python
just new p0042_trapping_rain_water rust
```

Then fill `README.md`, signature, and test cases.

## Agent rules

See `CLAUDE.md`. Key points:
- Agent scaffolds and writes tests. Agent does **not** solve unless you ask.
- Signature must match LeetCode exactly so paste-back is clean.
- No extra tooling (CI, linters, formatters) unless requested.

## Cleanup

```
rm -rf problems/<slug>
cargo clean                     # if rust target/ grows
```
