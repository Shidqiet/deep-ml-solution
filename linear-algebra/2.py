import pytest


def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    if not a:
        return []
    return [list(row) for row in zip(*a)]

    # More readable version
    # transposed_matrix = [[] for _ in range(len(a[0]))]
    # for row in a:
    #     for idx, item in enumerate(row):
    #         transposed_matrix[idx].append(item)
    # return transposed_matrix


@pytest.mark.parametrize(
    "input_matrix, expected_output",
    [
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([[1], [2], [3]], [[1, 2, 3]]),
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
        ([[1]], [[1]]),
        ([], []),
    ],
)
def test_transpose_matrix(input_matrix, expected_output):
    assert transpose_matrix(input_matrix) == expected_output
