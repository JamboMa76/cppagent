from clang import cindex

cindex.Config.set_library_file(
    r"C:\Program Files\LLVM\bin\libclang.dll"
)


def load_translation_unit(cpp_path):

    index = cindex.Index.create()

    return index.parse(
        cpp_path,
        args=["-std=c++17"]
    )


def extract_functions(cpp_path):

    tu = load_translation_unit(cpp_path)

    funcs = {}

    for node in tu.cursor.walk_preorder():

        if node.kind.name in [
            "FUNCTION_DECL",
            "CXX_METHOD"
        ]:

            funcs[node.spelling] = {
                "start": node.extent.start.line,
                "end": node.extent.end.line
            }

    return funcs


def find_related_functions(
    error_msg,
    funcs,
    topk=3
):

    arr = []

    lower = error_msg.lower()

    for name in funcs:

        score = 0

        if name in error_msg:
            score += 10

        if name.lower() in lower:
            score += 5

        arr.append((score, name))

    arr.sort(reverse=True)

    return [
        name
        for score, name in arr[:topk]
        if score > 0
    ]


def extract_function_code(
    cpp_path,
    start,
    end
):

    with open(
        cpp_path,
        "r",
        encoding="utf-8"
    ) as f:

        lines = f.read().splitlines()

    return "\n".join(
        lines[start - 1:end]
    )


def replace_function(
    original,
    start,
    end,
    new_code
):

    lines = original.splitlines()

    new_lines = (
        lines[:start - 1]
        + new_code.splitlines()
        + lines[end:]
    )

    return "\n".join(new_lines)