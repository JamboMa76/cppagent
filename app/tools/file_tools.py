import os


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


def read_file(path):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return ok(f.read())

    except Exception as e:
        return fail(e)


def write_file(path, content):

    try:

        parent = os.path.dirname(path)

        if parent:
            os.makedirs(
                parent,
                exist_ok=True
            )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(content)

        return ok("written")

    except Exception as e:
        return fail(e)