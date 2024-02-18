def recursive_solution(idx, total_weight, total_value):
    global answer
    global k

    if total_weight > k:
        return

    if idx == n:
        answer = max(answer, total_value)
        return

    recursive_solution(idx + 1, total_weight + items[idx][0], total_value + items[idx][1])
    recursive_solution(idx + 1, total_weight, total_value)


n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

answer = 0

recursive_solution(0, 0, 0)

print(answer)
