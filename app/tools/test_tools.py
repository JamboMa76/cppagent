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


def analyze_test_output(output):

    lower = output.lower()

    if "fail" in lower:
        return fail(output)

    if "error" in lower:
        return fail(output)

    return ok("pass")