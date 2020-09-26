"""
The secrets modules provides utilities related to using secrets in OpenFaaS
function.
"""

import functools
from typing import Optional

SECRETS_FOLDER = "/var/openfaas/secrets"


@functools.lru_cache(maxsize=None)
def get_secret(name: str, default: Optional[str] = None) -> Optional[str]:
    """Return the value of the named secret if it exists, or default if it doesn't.

    The secret is read from `/var/openfaas/secrets/{name}` and then stored
    in cache. Additional calls to `get_secret` will read the cached value.
    """

    try:
        with open(f"{SECRETS_FOLDER}/{name}", "r") as secret:
            value = secret.read()
            return value
    except FileNotFoundError:
        return default
