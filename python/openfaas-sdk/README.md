# openfaas-sdk for OpenFaas

## Usage
First install the library
```sh
pip install openfaas-sdk
```

Then in your function code

```py
# handler.py
from openfaas.sdk.secrets import get_secret


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    foo_value = get_secret("foo")

    if foo == "":
        return "secret 'foo' not found"

    return req
```

## Development

### Requirements
1. install [`pyenv`](https://github.com/pyenv/pyenv)
2. install [`poetry`](https://python-poetry.org/docs/)


### Setup environment

Run the following commands

```sh
$ pyenv install 3.8.5
$ poetry install
```

#### Using with you IDE
If you are using VSCode, you need to add the virtualenv cache to the list of locations that VSCode will search.

Add `~/.cache/pypoetry/virtualenvs` to `python.venvFolders` setting in VSCode, now you can select the virtual environment created by Poetry.

**Note** this path location will be different in each OS, see https://python-poetry.org/docs/configuration/#virtualenvspath-string


### Tests

You can run tests using

```sh
$ poetry run pylint openfaas_sdk tests
$ poetry run pytest
```

of

```sh
make lint test
```

### Versioning

The `funciton_sdk` use SemVer. New builds need to increment and commit the new version first.

To set a sepecific version value, use

```sh
poetry version <...>
```
You can also pass it `major`, `minor`, and `patch` to let it auto increment the version correctly.


### Build and Publish
After updating the version, run

```sh
$ poetry build
$ poetry publish
```
