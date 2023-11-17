def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Пример использования
arr = [1, 3, 5, 7, 9, 11, 13, 15]
value = 2

index = binary_search(arr, value)
if index != -1:
    print(f"Искомый элемент {value} найден в массиве на индексе {index}")
else:
    print(f"Искомый элемент {value} не найден в массиве")