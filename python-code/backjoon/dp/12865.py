def recursive_solution(idx, total_weight):
    if total_weight > k:
        return -99999999

    if idx == n:
        return 0

    if dp[idx][total_weight] != -1:
        return dp[idx][total_weight]

    dp[idx][total_weight] = max(recursive_solution(idx + 1, total_weight + items[idx][0]) + items[idx][1],
                                recursive_solution(idx + 1, total_weight))
    return dp[idx][total_weight]


n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(100_001)] for _ in range(n + 1)]

result = recursive_solution(0, 0)

print(result)
