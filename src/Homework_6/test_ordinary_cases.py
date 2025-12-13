from src.Homework_6.heap_sort import heap_sort

import pytest

@pytest.mark.parametrize(
      ["n", "expected"],
      [([0, 10, 8, 9, 3, 4], [0, 3, 4, 8, 9, 10]),
      ([1, 5, 4, 3, 8, 7], [1, 3, 4, 5, 7, 8]),
      ([10, -1, 8], [-1, 8, 10]),
      ]
)

def tests_ordinary_cases(n, expected):
   assert heap_sort(n) == expected
