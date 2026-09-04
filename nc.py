#!/usr/bin/env python3
import os
import re
import subprocess
import sys
import webbrowser

try:
    import readline  # noqa: F401
except ImportError:
    pass

try:
    import termios
    import tty
except ImportError:
    termios = None

ROOT = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(ROOT, "neetcode", "README.md")
LINE = re.compile(r"- \[( |x)\] \[(\d+)\. ([^\]]+)\]\(([^)]+)\) — (\w+) — `([^`]+)`")

BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
OFF = "\033[0m"


class Problem:
    def __init__(self, done, num, title, url, diff, rel):
        self.done = done
        self.num = int(num)
        self.title = title
        self.url = url
        self.diff = diff
        self.rel = rel
        self.cat = rel.split("/")[0]

    @property
    def path(self):
        return os.path.join(ROOT, "neetcode", self.rel)

    @property
    def cat_name(self):
        return self.cat.split("_", 1)[1].replace("_", " ")

    def label(self):
        mark = f"{GREEN}x{OFF}" if self.done else " "
        color = {"Easy": GREEN, "Medium": YELLOW, "Hard": RED}[self.diff]
        return f"[{mark}] {self.num:>4}. {self.title}  {color}{self.diff}{OFF} {DIM}{self.cat_name}{OFF}"


def load():
    with open(INDEX) as f:
        text = f.read()
    return [Problem(m.group(1) == "x", *m.groups()[1:]) for m in LINE.finditer(text)]


def set_done(problem, done):
    with open(INDEX) as f:
        text = f.read()
    old = f"- [{'x' if problem.done else ' '}] [{problem.num}. {problem.title}]"
    new = f"- [{'x' if done else ' '}] [{problem.num}. {problem.title}]"
    if old not in text:
        print("could not find index entry")
        return
    with open(INDEX, "w") as f:
        f.write(text.replace(old, new, 1))
    problem.done = done


def match(problems, query):
    query = query.strip().lower()
    if not query:
        return []
    if query.isdigit():
        exact = [p for p in problems if p.num == int(query)]
        if exact:
            return exact
    terms = query.split()
    return [p for p in problems
            if all(t in f"{p.num} {p.title} {p.rel}".lower() for t in terms)]


def pick(problems, query=None):
    while True:
        if query is None:
            done = sum(p.done for p in problems)
            print(f"\n{BOLD}NeetCode 150{OFF}  {done}/{len(problems)} done")
            query = input("search (number, title, or blank to list categories) > ").strip()
        if query.lower() in ("q", "quit", "exit"):
            return None
        if not query:
            cats = []
            for p in problems:
                if p.cat not in cats:
                    cats.append(p.cat)
            for i, c in enumerate(cats, 1):
                items = [p for p in problems if p.cat == c]
                print(f"{i:>2}. {c.split('_', 1)[1].replace('_', ' '):<28} "
                      f"{sum(p.done for p in items)}/{len(items)}")
            choice = input("category number > ").strip()
            if not choice.isdigit() or not 1 <= int(choice) <= len(cats):
                query = None
                continue
            hits = [p for p in problems if p.cat == cats[int(choice) - 1]]
        else:
            hits = match(problems, query)
        if not hits:
            print("no match")
            query = None
            continue
        if len(hits) == 1:
            return hits[0]
        for i, p in enumerate(hits, 1):
            print(f"{i:>3}. {p.label()}")
        choice = input("pick > ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(hits):
            return hits[int(choice) - 1]
        query = None


KEYS = ("t test  o open  e edit  r readme  p path  d done  "
        "n next  c change  / search  s stats  l clear  h help  q quit")


def getkey():
    if termios is None or not sys.stdin.isatty():
        line = sys.stdin.readline()
        if not line:
            raise EOFError
        return line.strip()
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    if ch in ("\x03", "\x04"):
        raise EOFError
    if ch in ("\r", "\n"):
        return "t"
    if ch == "\x0c":
        return "l"
    print(ch)
    return ch

HELP = """commands:
  t, test      run the tests for this problem
  o, open      open the leetcode page in your browser
  e, edit      open solution.py in $EDITOR
  r, readme    print the problem README
  p, path      print the problem directory
  d, done      mark solved (D to unmark)
  n, next      jump to the next unsolved problem
  c, change    pick a different problem
  /            search for another problem by number or title
  s, stats     progress by category
  l, clear     clear the screen (ctrl-l works too)
  h, help      this list
  q, quit"""


def show(problem):
    print(f"\n{BOLD}{problem.num}. {problem.title}{OFF}  {problem.diff}  "
          f"{DIM}{problem.cat_name}{OFF}")
    print(f"{DIM}{problem.url}{OFF}")
    print(f"{DIM}{problem.rel}{OFF}")


def stats(problems):
    cats = []
    for p in problems:
        if p.cat not in cats:
            cats.append(p.cat)
    for c in cats:
        items = [p for p in problems if p.cat == c]
        done = sum(p.done for p in items)
        bar = "#" * done + "." * (len(items) - done)
        print(f"{c.split('_', 1)[1].replace('_', ' '):<28} {bar} {done}/{len(items)}")
    print(f"{'total':<28} {sum(p.done for p in problems)}/{len(problems)}")


def session(problems, problem):
    while problem:
        show(problem)
        while True:
            print(f"{DIM}{KEYS}{OFF}")
            print(f"{BOLD}{problem.num}>{OFF} ", end="", flush=True)
            try:
                cmd = getkey()
            except EOFError:
                print()
                return
            if cmd in ("q", "quit", "exit"):
                return
            elif cmd in ("t", "test", ""):
                subprocess.run(["uv", "run", "pytest", problem.path, "-v"], cwd=ROOT)
            elif cmd in ("o", "open"):
                print(problem.url)
                webbrowser.open(problem.url)
            elif cmd in ("e", "edit"):
                subprocess.run([os.environ.get("EDITOR", "vi"),
                                os.path.join(problem.path, "solution.py")], cwd=ROOT)
            elif cmd in ("r", "readme"):
                with open(os.path.join(problem.path, "README.md")) as f:
                    print(f.read())
            elif cmd in ("p", "path"):
                print(problem.path)
            elif cmd in ("d", "done"):
                set_done(problem, True)
                print("marked done")
            elif cmd == "D":
                set_done(problem, False)
                print("marked not done")
            elif cmd in ("n", "next"):
                rest = [p for p in problems if not p.done and p.num != problem.num]
                if not rest:
                    print("all done")
                    continue
                problem = rest[0]
                break
            elif cmd == "/":
                nxt = pick(problems)
                if nxt is None:
                    return
                problem = nxt
                break
            elif cmd in ("c", "change"):
                nxt = pick(problems)
                if nxt is None:
                    return
                problem = nxt
                break
            elif cmd in ("s", "stats"):
                stats(problems)
            elif cmd in ("l", "clear", "cls"):
                print("\033[2J\033[H", end="")
                show(problem)
            elif cmd in ("h", "help", "?"):
                print(HELP)
            else:
                hits = match(problems, cmd)
                if len(hits) == 1:
                    problem = hits[0]
                    break
                print(f"unknown key: {cmd!r}  (h for help)")


def main():
    problems = load()
    query = " ".join(sys.argv[1:]) or None
    try:
        problem = pick(problems, query)
        if problem:
            session(problems, problem)
    except (KeyboardInterrupt, EOFError):
        print()


if __name__ == "__main__":
    main()
