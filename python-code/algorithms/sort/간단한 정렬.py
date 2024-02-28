def bubbleSort(numbers):
    n = len(numbers)

    for i in range(1, n):
        for j in range(n - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


def selectionSort(numbers):
    n = len(numbers)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]


def insertionSort(numbers):
    n = len(numbers)

    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


numbers = [4, 2, 6, 8, 1, 2, 3, 5]

# bubbleSort(numbers)
insertionSort(numbers)

print(numbers)
