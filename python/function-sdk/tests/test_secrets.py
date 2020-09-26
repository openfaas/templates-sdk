import os
from distutils import dir_util

import pytest
from function_sdk import secrets
from function_sdk.secrets import get_secret


@pytest.fixture
def datadir(tmpdir, request):
    '''
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    '''
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(tmpdir))

    return tmpdir


def test_get_default_value():

    assert get_secret("not_found") is None, "default value is not None"

    assert get_secret(
        "not_found", "foo") == "foo", "optional default value should be 'foo'"


def test_get_value(datadir):
    secrets._secrets_folder = datadir
    assert get_secret("password") == "secretvalue"
