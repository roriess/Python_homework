from src.Homework_6.heap_sort import heap_sort
from hypothesis import given, settings, HealthCheck
from hypothesis.strategies import lists, integers


def selection_sort(num_arr):
    if num_arr is None:
        return None
    
    for i in range(len(num_arr)):
        min_elm_pos = i
        for k in range(i + 1, len(num_arr)):
            if num_arr[min_elm_pos] >= num_arr[k]:
                min_elm_pos = k

        if num_arr[min_elm_pos] != num_arr[i]:
            num_arr[min_elm_pos], num_arr[i] = num_arr[i], num_arr[min_elm_pos]

    return num_arr


@given(lists(integers()))
@settings(suppress_health_check = [HealthCheck.too_slow])
def test(num_arr):
    assert heap_sort(num_arr.copy()) == selection_sort(num_arr.copy())
