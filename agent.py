import json

from app.config import *

from app.logger import log

from app.skills.cpp_skill import (
    gen_cpp,
    gen_test,
    fix_function
)

from app.ast.ast_util import (
    extract_functions,
    find_related_functions,
    extract_function_code,
    replace_function
)

from app.tools.file_tools import (
    read_file,
    write_file
)

from app.tools.compiler_tools import (
    compile_cpp,
    run_exe
)

from app.tools.test_tools import (
    analyze_test_output
)


def run_agent():

    log("READ HEADER")

    header_res = read_file(INTERFACE)

    if not header_res["ok"]:
        return header_res

    header = header_res["data"]

    impl = gen_cpp(header)

    for round_id in range(5):

        log("ROUND", round_id + 1)

        write_file(CPP, impl)

        test = gen_test(
            header,
            impl
        )

        write_file(TEST, test)

        compile_res = compile_cpp(
            CPP,
            TEST,
            EXE
        )

        if not compile_res["ok"]:

            err = compile_res["data"]

            log(
                "COMPILE ERROR",
                err
            )

            funcs = extract_functions(CPP)

            related = (
                find_related_functions(
                    err,
                    funcs
                )
            )

            if related:

                for name in related:

                    meta = funcs[name]

                    func_code = (
                        extract_function_code(
                            CPP,
                            meta["start"],
                            meta["end"]
                        )
                    )

                    fixed = fix_function(
                        name,
                        func_code,
                        impl,
                        header,
                        test,
                        err
                    )

                    impl = replace_function(
                        impl,
                        meta["start"],
                        meta["end"],
                        fixed
                    )

            else:

                impl = gen_cpp(
                    header,
                    impl,
                    test,
                    err
                )

            continue

        run_res = run_exe(EXE)

        if not run_res["ok"]:

            impl = gen_cpp(
                header,
                impl,
                test,
                run_res["data"]
            )

            continue

        test_res = analyze_test_output(
            run_res["data"]
        )

        if test_res["ok"]:

            log("SUCCESS")

            return {
                "ok": True,
                "data": run_res["data"]
            }

    return {
        "ok": False,
        "data": "agent failed"
    }


if __name__ == "__main__":

    result = run_agent()

    print(
        json.dumps(
            result,
            indent=2,
            ensure_ascii=False
        )
    )