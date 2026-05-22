import os

# ==========================================
# PATHS
# ==========================================

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

INTERFACE_DIR = os.path.join(
    ROOT_DIR,
    "interfaces"
)

GENERATED_DIR = os.path.join(
    ROOT_DIR,
    "generated"
)

TEST_DIR = os.path.join(
    ROOT_DIR,
    "tests"
)

BUILD_DIR = os.path.join(
    ROOT_DIR,
    "build"
)

LOG_DIR = os.path.join(
    ROOT_DIR,
    "logs"
)

TMP_DIR = os.path.join(
    ROOT_DIR,
    "tmp"
)

# ==========================================
# DEFAULT FILES
# ==========================================

INTERFACE = os.path.join(
    INTERFACE_DIR,
    "math_api.h"
)

CPP = os.path.join(
    GENERATED_DIR,
    "math_api.cpp"
)

TEST = os.path.join(
    TEST_DIR,
    "test.cpp"
)

EXE = os.path.join(
    BUILD_DIR,
    "app.exe"
)

# ==========================================
# OPENAI
# ==========================================

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    ""
)

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4.1"
)