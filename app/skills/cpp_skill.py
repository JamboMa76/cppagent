from app.llm.openai_llm import ask_llm


def gen_cpp(
    header,
    impl=None,
    test=None,
    err=None
):

    prompt = f"""
你是C++专家。

接口:
{header}
"""

    if impl:
        prompt += f"""

当前实现:
{impl}
"""

    if test:
        prompt += f"""

测试:
{test}
"""

    if err:
        prompt += f"""

错误:
{err}
"""

    prompt += """

要求:
1. 完整 cpp
2. C++17
3. 不要 markdown
4. 不要解释
"""

    return ask_llm(prompt)


def gen_test(
    header,
    impl
):

    prompt = f"""
生成 test.cpp

要求:
1. assert
2. 输出 PASS 或 FAIL
3. 完整可编译

接口:
{header}

实现:
{impl}

只输出代码
"""

    return ask_llm(prompt)


def fix_function(
    name,
    func_code,
    full_code,
    header,
    test,
    err
):

    prompt = f"""
修复函数:

{name}

接口:
{header}

完整代码:
{full_code}

函数:
{func_code}

测试:
{test}

错误:
{err}

要求:
1. 仅输出该函数
2. 不要解释
"""

    return ask_llm(prompt)