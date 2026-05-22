import datetime
import os
import sys

LOG_FILE = os.path.join(
    "logs",
    "agent.log"
)

os.makedirs("logs", exist_ok=True)


def log(
    *args,
    sep=" ",
    end="\n",
    file=None,
    flush=False
):
    msg = sep.join(
        str(x)
        for x in args
    )

    ts = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    final = f"[{ts}] {msg}"

    print(
        final,
        end=end,
        file=file or sys.stdout,
        flush=flush
    )

    try:
        with open(
            LOG_FILE,
            "a",
            encoding="utf-8"
        ) as f:
            f.write(final + end)

    except Exception:
        pass