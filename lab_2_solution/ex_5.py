import random


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_select(arr, low, high, k):
    if low < high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k - 1:
            return arr[:k]

        if pivot_index > k - 1:
            return quick_select(arr, low, pivot_index - 1, k)

        return quick_select(arr, pivot_index + 1, high, k)


def find_k_smallest_elements(arr, k):
    if k > len(arr):
        return arr

    return quick_select(arr, 0, len(arr) - 1, k)


# Приклад використання

n = 1000
arr = random.sample(range(n * 10), n)
k_values = [10, 100, 500, 900]

for k in k_values:
    smallest_elements = find_k_smallest_elements(arr, k)
    print(f"Перші {k} найменших елементів: {smallest_elements}")
