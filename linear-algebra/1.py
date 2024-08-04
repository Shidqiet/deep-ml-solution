import pytest


def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float]:
    if len(a[0]) != len(b):
        return -1
    product = []
    for row in a:
        sum = 0
        for j, col in enumerate(row):
            sum += col * b[j]
        product.append(sum)
    return product


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3], [14, 32]),
        ([[1, 2], [3, 4]], [2, 1], [4, 10]),
        ([[1, 2]], [3, 4], [11]),
        ([[1]], [1], [1]),
        ([[1, 2], [3, 4]], [1], -1),
        ([[], []], [1, 2], -1),
    ],
)
def test_matrix_dot_vector(a, b, expected):
    assert matrix_dot_vector(a, b) == expected
