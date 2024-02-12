def solution(index, number):
    if number == m:
        print(*arr)
        return

    for i in range(index, n):
        if numbers[i] in arr:
            continue

        arr.append(numbers[i])
        solution(i + 1, number + 1)
        arr.pop()


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = []

solution(0, 0)
