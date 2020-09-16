def quickSort(arr, low, high):
    if low < high:
        key = partition(arr, low, high)
        quickSort(arr, low, key - 1)
        quickSort(arr, key + 1, high)
    return arr


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr = swap(arr, i, j)
    arr = swap(arr, i + 1, high)
    return i + 1


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


arr = [3, 5, 4, 1, 9, 8, 6, 5]
final = quickSort(arr, 0, len(arr) - 1)
print(final)

# Time Complexities - 
#   Worst Case - n2
#   Best Case - nlogn
#   Avg. Case - nlogn 
