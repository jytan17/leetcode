default:
    @just --list

test problem lang:
    @just test-{{lang}} {{problem}}

test-python problem:
    uv run pytest problems/{{problem}}/python -v

test-rust problem:
    cargo test -p {{problem}}

new problem lang:
    @just new-{{lang}} {{problem}}

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
