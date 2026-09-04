default:
    @just --list

# Usage:
#   just test problems/p0001_two_sum/python
#   just test problems/p0001_two_sum/rust
# Trailing slash from tab-completion is fine.
test path:
    #!/usr/bin/env bash
    set -euo pipefail
    p="{{path}}"
    p="${p%/}"
    lang="${p##*/}"
    slug="$(basename "${p%/*}")"
    just "test-${lang}" "${slug}"

test-python problem:
    uv run pytest problems/{{problem}}/python -v

test-rust problem:
    cargo test -p {{problem}}

# Usage:
#   just new problems/p0001_two_sum/python
#   just new problems/p0001_two_sum/rust
new path:
    #!/usr/bin/env bash
    set -euo pipefail
    p="{{path}}"
    p="${p%/}"
    lang="${p##*/}"
    slug="$(basename "${p%/*}")"
    just "new-${lang}" "${slug}"

new-python problem:
    mkdir -p problems/{{problem}}/python
    cp templates/python/solution.py problems/{{problem}}/python/solution.py
    cp templates/python/test_solution.py problems/{{problem}}/python/test_solution.py
    test -f problems/{{problem}}/README.md || cp templates/README.md problems/{{problem}}/README.md

new-rust problem:
    mkdir -p problems/{{problem}}/rust/src problems/{{problem}}/rust/tests
    sed 's/__PKG__/{{problem}}/g' templates/rust/Cargo.toml > problems/{{problem}}/rust/Cargo.toml
    cp templates/rust/src/lib.rs problems/{{problem}}/rust/src/lib.rs
    sed 's/__PKG__/{{problem}}/g' templates/rust/tests/cases.rs > problems/{{problem}}/rust/tests/cases.rs
    test -f problems/{{problem}}/README.md || cp templates/README.md problems/{{problem}}/README.md

list:
    @ls problems/ 2>/dev/null || echo "no problems yet"

# NeetCode 150 track (python only).
# Usage:
#   just nc 01_arrays_hashing/p0001_two_sum
nc problem:
    #!/usr/bin/env bash
    set -euo pipefail
    p="{{problem}}"
    p="${p%/}"
    uv run pytest "neetcode/${p}" -v

nc-all:
    uv run pytest neetcode -q

nc-list:
    @ls neetcode/

# Interactive picker + per-problem shell (test / open leetcode / edit / mark done).
# Usage:
#   just drill
#   just drill 128
#   just drill two sum
drill *query:
    @uv run python nc.py {{query}}
