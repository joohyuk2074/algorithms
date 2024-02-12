def solution(number):
    if number == m:
        print(*arr)
        return

    for i in range(0, n):
        if numbers[i] in arr:
            continue

        arr.append(numbers[i])
        solution(number + 1)
        arr.pop()


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = []

solution(0)
