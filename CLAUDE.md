# LeetCode Workspace

User solves LeetCode here in Python and Rust, then pastes final solution back to leetcode.com. Your job: scaffold problems, write tests from problem examples + edge cases, leave solution body for user to implement.

## Layout

```
problems/
  p<NNNN>_<snake_name>/         # e.g. p0001_two_sum
    README.md                    # problem statement, constraints, complexity target
    python/
      solution.py                # class Solution with leetcode signature
      test_solution.py           # pytest, parametrized
    rust/
      Cargo.toml                 # package name = p<NNNN>_<snake_name>
      src/lib.rs                 # struct Solution with leetcode signature
      tests/cases.rs             # integration tests
templates/
  python/                        # copied by `just new`
  rust/
Cargo.toml                       # workspace root, members = ["problems/*/rust"]
justfile
```

Folder name: zero-padded 4-digit problem number + snake_case title. Examples: `p0001_two_sum`, `p0146_lru_cache`.

## Workflow

1. User gives problem (URL, title, or paste of problem text) + target language(s).
2. Run `just new problems/<slug>/<lang>` to scaffold from template. If user wants both langs, run twice.
3. Fill in `README.md`: problem statement, constraints, examples, time/space complexity target, approach hints if asked.
4. Fill in `solution.py` / `src/lib.rs`:
   - Exact LeetCode method signature (same name, same types).
   - Body left as `raise NotImplementedError` / `unimplemented!()` — user writes it. Do NOT solve unless asked.
5. Fill in tests with **all LeetCode examples** plus 2–3 edge cases (empty input, single element, max bound, duplicates, negative — whichever apply).
6. Tell user the test command: `just test problems/<slug>/<lang>`.

## Commands

- `just new problems/<slug>/<lang>` — scaffold (lang = `python` | `rust`)
- `just test problems/<slug>/<lang>` — run tests
- Trailing slash from tab-completion is fine: `just test problems/p0001_two_sum/python/`
- Direct: `just test-python <slug>` / `just test-rust <slug>`
- Python env managed by `uv`. Test recipe runs `uv run pytest ...`. Add deps with `uv add --dev <pkg>`.

## Conventions

### Python
- One class `Solution` matching LeetCode exactly.
- Tests: `pytest`, use `@pytest.mark.parametrize` for cases.
- No external deps beyond stdlib + pytest. If a problem needs `ListNode` / `TreeNode`, define helpers inside `solution.py` matching LeetCode's definitions.

### Rust
- `struct Solution;` with `impl Solution { pub fn ... }` — match LeetCode signature exactly (`i32`, `Vec<i32>`, etc.).
- Package name in `Cargo.toml` = folder name (so `cargo test -p p0001_two_sum` works).
- Tests in `tests/cases.rs` as integration tests; `use <pkg_name>::Solution;`.
- For `ListNode` / `TreeNode`, paste LeetCode's exact definition into `src/lib.rs`.

### Tests
- Cover every example from problem statement first.
- Add edge cases relevant to constraints.
- For unordered output (e.g. 3Sum), sort before compare or use set comparison.

## What NOT to do

- Don't solve the problem unless explicitly asked. User wants to drill.
- Don't add abstractions, helpers, or utility crates "for later".
- Don't reorder/rename method signatures — they must paste back to LeetCode cleanly.
- Don't write comments explaining what the code does. User reads code.
- Don't add CI, formatters, linters, pre-commit, etc. unless asked.
