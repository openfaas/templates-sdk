import functools
from typing import Optional

_secrets_folder = "/var/openfaas/secrets"


@functools.lru_cache(maxsize=None)
def get_secret(name: str, default: Optional[str] = None) -> Optional[str]:
    """Return the value of the named secret if it exists, or default if it doesn't.

    The secret is read from `/var/openfaas/secrets/{name}` and then stored
    in cache. Additional calls to `get_secret` will read the cached value.
    """

    try:
        with open(f"{_secrets_folder}/{name}", "r") as f:
            value = f.read()
            return value
    except FileNotFoundError:
        return default
