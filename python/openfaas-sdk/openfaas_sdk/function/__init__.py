"""
The function module provides utility methods to help simplify and standardize
the development of OpenFaaS functions in Python.

Examples
--------
Import the whole function module
>>> from openfaas_sdk import function
>>> password = function.secrets.get_secret("password")
>>> username = function.env.get_env("username")

Or just the function you need
>>> from openfaas_sdk.function.secrets import get_secret
>>> password = get_secret("password")
"""
from . import env, secrets

assert env
assert secrets
