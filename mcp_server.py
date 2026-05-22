import asyncio
import json

from mcp.server import Server
from mcp.server.stdio import stdio_server

from mcp.server.models import (
    InitializationOptions,
    ServerCapabilities
)

from mcp.types import TextContent

from app.tools.file_tools import (
    read_file,
    write_file
)

from app.tools.compiler_tools import (
    compile_cpp,
    run_exe
)

server = Server("cpp-tools")


TOOLS = [

    {
        "name": "read_file",

        "description": "read file",

        "inputSchema": {
            "type": "object",

            "properties": {
                "path": {
                    "type": "string"
                }
            },

            "required": ["path"]
        }
    },

    {
        "name": "write_file",

        "description": "write file",

        "inputSchema": {
            "type": "object",

            "properties": {

                "path": {
                    "type": "string"
                },

                "content": {
                    "type": "string"
                }
            },

            "required": [
                "path",
                "content"
            ]
        }
    },

    {
        "name": "compile_cpp",

        "description": "compile cpp",

        "inputSchema": {
            "type": "object",

            "properties": {

                "cpp": {
                    "type": "string"
                },

                "test": {
                    "type": "string"
                },

                "out": {
                    "type": "string"
                }
            },

            "required": [
                "cpp",
                "test",
                "out"
            ]
        }
    },

    {
        "name": "run_exe",

        "description": "run executable",

        "inputSchema": {
            "type": "object",

            "properties": {

                "exe": {
                    "type": "string"
                }
            },

            "required": ["exe"]
        }
    }
]


@server.list_tools()
async def list_tools():
    return TOOLS


@server.call_tool()
async def call_tool(
    name,
    arguments
):

    if name == "read_file":

        result = read_file(
            arguments["path"]
        )

    elif name == "write_file":

        result = write_file(
            arguments["path"],
            arguments["content"]
        )

    elif name == "compile_cpp":

        result = compile_cpp(
            arguments["cpp"],
            arguments["test"],
            arguments["out"]
        )

    elif name == "run_exe":

        result = run_exe(
            arguments["exe"]
        )

    else:

        result = {
            "ok": False,
            "data": "unknown tool"
        }

    return [
        TextContent(
            type="text",
            text=json.dumps(
                result,
                ensure_ascii=False,
                indent=2
            )
        )
    ]


async def main():

    async with stdio_server() as (
        read,
        write
    ):

        await server.run(
            read_stream=read,
            write_stream=write,

            initialization_options=(
                InitializationOptions(
                    server_name="cpp-tools",
                    server_version="1.0",
                    capabilities=(
                        ServerCapabilities()
                    )
                )
            )
        )


if __name__ == "__main__":
    asyncio.run(main())