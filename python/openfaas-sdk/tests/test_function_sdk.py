# pylint: disable-msg=C0114,C0116
from openfaas_sdk import __version__


def test_version():
    assert __version__ == "0.1.0"
