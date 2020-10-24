# pylint: disable-msg=C0114,C0116

import os
from distutils import dir_util

import pytest
from openfaas_sdk.function import secrets
from openfaas_sdk.function.secrets import get_secret


@pytest.fixture(name="secrets_dir")
def fixture_secrets_dir(tmpdir, request):
    """
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    """
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(tmpdir))

    return tmpdir


def test_get_default_value():

    assert get_secret("not_found") is None, "default value is not None"

    assert (
        get_secret("not_found", "foo") == "foo"
    ), "optional default value should be 'foo'"


def test_get_value(secrets_dir):
    secrets.SECRETS_FOLDER = secrets_dir
    assert get_secret("password") == "secretvalue"
