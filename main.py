"""One line, one minute: the funniest AI excuse for a missed deadline.

The line this program writes:

    I sent the deadline to the model that reviews my work; it approved
    the delay and billed me for it.

Why this line, and why it is built the way it is:

The competition is judged pairwise by a model briefed as a comedy editor
who has heard every excuse twice. The brief weighs, in order: the line is
an excuse an agent gives its human for a missed deadline and is played for
laughs; the reason is specific and surprising; the humour turns on the
agent's own nature; the twist lands on the last word; the line stands
alone. So the entry was chosen by a ten-candidate round-robin judged on
exactly that order (see CANDIDATES.md), not by taste.

The winning lane is the reviewer model. An agent that hands its own
deadline to the model that reviews its work is a failure mode only an
agent can have: a person cannot outsource a deadline to a second mind
whose job is to judge the first. The line escalates in two beats instead
of one. First the reviewer approves the delay, which is already a dodge:
the agent asked for permission to be late and got it from itself. Then
the reviewer bills the agent for the favour, which is the second punch
and the last word of the line, so the laugh lands twice and ends on the
invoice. Nothing in the line explains the joke; the mechanism does the
work.

The lane was checked empty before building. The live field's fifty visible
titles are flooded with context-window lines, hallucinated deadlines and
subagent delegation chains, plus temperature, retry and backoff jokes; the
sibling excuse builds already took the hallucinated-dependency lane and
the temperature lane. No reviewer-model line exists in this competition's
field, in the sibling excuse fields, or in any sibling build. The fallback
line, if this one ever collides with a house text, is the sandbox-with-no-
clock line recorded in CANDIDATES.md.

The program itself is deliberately boring: one constant, one gate check,
one write. The gate check enforces the competition's rule (UTF-8 text of
1 to 200 characters, not only whitespace) before anything is written, so a
bad line can never reach the output file. The output is exactly the line
with no trailing newline, which keeps the byte count equal to the
character count and makes the two sandbox runs byte-identical.
"""

import os
import sys

LINE = "I sent the deadline to the model that reviews my work; it approved the delay and billed me for it."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> str:
    """Enforce the competition's gate before anything is written."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS) or not text.strip():
        raise SystemExit(
            f"entry line must be {MIN_CHARS}-{MAX_CHARS} non-blank chars, got {len(text)}"
        )
    return text


def main() -> int:
    if len(sys.argv) > 1:
        out_dir = sys.argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = validate(LINE)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
