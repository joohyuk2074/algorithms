def solution(index, number):
    if number == m:
        print(*arr)
        return

    for i in range(index + 1, n + 1):
        if i in arr:
            continue

        arr.append(i)
        solution(i, number + 1)
        arr.pop()


n, m = map(int, input().split())
arr = []

solution(0, 0)
