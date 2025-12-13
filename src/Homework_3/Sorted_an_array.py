def quick_sort(arr):
    lenghtOfArr = len(arr)

    if lenghtOfArr <= 1: 
        return arr

    elif lenghtOfArr == 2:
        if arr[0] > arr[1]: 
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    
    elif lenghtOfArr >= 3:
        middle = arr[lenghtOfArr // 2]

        left = [i for i in arr if i < middle]
        center = [i for i in arr if i == middle]
        right = [i for i in arr if i > middle]

        sortedArr = quick_sort(left) + center + quick_sort(right)

        return sortedArr


arr = [int(i) for i in input("Enter the elements separated by space: ").split()]

print(f'Sorted array: {quick_sort(arr)}')
