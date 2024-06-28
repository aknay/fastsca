import pytest

from data.data_helper import get_aes128_arduino_uno_project_container
from fastsca.domain.container import Container


@pytest.fixture
def container() -> Container:
    return get_aes128_arduino_uno_project_container()


def test_container_is_valid(container: Container):
    traces = container.take((0, 2))
    print(traces.shape)
