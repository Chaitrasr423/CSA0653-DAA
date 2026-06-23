def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j      # Corrected

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [64, 25, 12, 22, 11]
print("Sorted Array:", selection_sort(arr))
