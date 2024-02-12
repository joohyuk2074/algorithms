def solution(index, number):
    if number == m:
        print(*arr)
        return

    for i in range(index, n + 1):
        arr.append(i)
        solution(i, number + 1)
        arr.pop()


n, m = map(int, input().split())
arr = []

solution(1, 0)
