import os
import subprocess
import sys


def ok(data):
    return {
        "ok": True,
        "data": data
    }


def fail(data):
    return {
        "ok": False,
        "data": str(data)
    }


def compile_cpp(
    cpp,
    test,
    out
):

    try:

        out_dir = os.path.dirname(out)

        if out_dir:
            os.makedirs(
                out_dir,
                exist_ok=True
            )

        include_dirs = [
            "./interfaces",
            "./include",
            "./generated",
            "."
        ]

        include_flags = []

        for d in include_dirs:

            if os.path.exists(d):

                include_flags.extend([
                    "-I",
                    os.path.abspath(d)
                ])

        cmd = [
            "g++",
            "-std=c++17",
            "-O2",

            *include_flags,

            cpp,
            test,

            "-o",
            out
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        if result.returncode != 0:
            return fail(result.stderr)

        return ok(result.stdout)

    except Exception as e:
        return fail(e)


def run_exe(exe):

    try:

        if sys.platform.startswith("win"):
            cmd = [exe]
        else:
            cmd = ["./" + exe]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode != 0:
            return fail(result.stderr)

        return ok(result.stdout)

    except Exception as e:
        return fail(e)