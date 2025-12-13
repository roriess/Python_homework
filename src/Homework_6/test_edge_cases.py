from src.Homework_6.heap_sort import heap_sort


def test_empty():
    assert heap_sort([]) == []


def test_one_elm():
    assert heap_sort([5]) == [5]


def test_negative_elm():
    assert heap_sort([-1, -2, -3]) == [-3, -2, -1]


def test_large_elm():
    assert heap_sort([1000000000, 2000000000]) == [1000000000, 2000000000]


def test_none():
    assert heap_sort(None) is None
