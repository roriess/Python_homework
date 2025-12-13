def heapify(num_arr, size_arr, i):
    largest = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index < size_arr and num_arr[left_index] > num_arr[largest]:
        largest = left_index

    if right_index < size_arr and num_arr[right_index] > num_arr[largest]:
        largest = right_index

    if largest != i:
        num_arr[largest], num_arr[i] = num_arr[i], num_arr[largest]

        heapify(num_arr, size_arr, largest)


def heap_sort(num_arr):
    if num_arr is None:
        return None

    size_arr = len(num_arr)

    for i in range(size_arr // 2 - 1, -1, -1):
        heapify(num_arr, size_arr, i)

    for i in range(size_arr - 1, 0, -1):
        num_arr[0], num_arr[i] = num_arr[i], num_arr[0]
        heapify(num_arr, i, 0)
        
    return num_arr
