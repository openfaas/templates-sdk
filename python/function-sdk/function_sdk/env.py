import os
from typing import Optional


def get_env(name: str, default: Optional[str] = None) -> Optional[str]:
    """Return the value of the environment variable key if it exists,
    or default if it doesn’t. key, default and the result are str.
    """
    return os.getenv(name, default)
