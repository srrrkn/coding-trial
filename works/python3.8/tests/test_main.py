import pytest
from main import solution


@pytest.mark.parametrize("input_value, expected", [
    (1, 1),
    (2, 2),
    (3, 3),
])
def test_solution(input_value, expected):
    assert solution(input_value) == expected