import pytest

from project_name.main import run


def test_main_run():
    run(3)


name = None


@pytest.fixture
def set_name():
    global name
    name = "Daki404"


def test_with_fixture(set_name):
    assert name == "Daki404"
