"""
function provides utility methods to help simplify and standardize
the development of OpenFaaS functions in Python.

Usage:
    from openfaas_sdk import function

    password = function.secrets.get_secret("password")


    from openfaas_sdk.function.secrets import get_secret

    password = get_secret("password")
"""
from . import env, secrets
