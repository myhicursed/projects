from src.main import A
import pytest

@pytest.mark.parametrize("param", [1, 2, 10, 1])
def test_main(param):
    assert A.x == param