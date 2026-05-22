import re

from openai import OpenAI

from app.config import (
    OPENAI_API_KEY,
    OPENAI_MODEL
)

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def extract_code(text: str):

    m = re.search(
        r"```(?:cpp|c\+\+)?\s*([\s\S]*?)```",
        text,
        re.MULTILINE
    )

    if m:
        return m.group(1).strip()

    return text.strip()


def ask_llm(
    prompt: str,
    code_only=True
):

    resp = client.chat.completions.create(
        model=OPENAI_MODEL,

        messages=[
            {
                "role": "system",
                "content": (
                    "你是专业C++17工程师。"
                    "输出代码时不要解释。"
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2
    )

    text = (
        resp.choices[0]
        .message
        .content
    )

    if code_only:
        return extract_code(text)

    return text