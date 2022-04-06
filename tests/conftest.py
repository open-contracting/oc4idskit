# See ocdskit/tests/conftest.py
import logging
import os.path

import pytest

logger = logging.getLogger("vcr")
logger.setLevel(logging.WARNING)


@pytest.fixture(scope='module')
def vcr_config():
    # Avoid ImportWarning from YAML on PyPy 3.7. https://github.com/yaml/pyyaml/issues/534
    return {'serializer': 'json'}


@pytest.fixture()
def vcr_cassette_name(request):
    return f"{os.path.splitext(os.path.basename(request.node.fspath))[0]}-{request.node.name}"
