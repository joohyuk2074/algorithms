def recursive_solution(index):
    if index == n:
        return 0

    if index > n:
        return -9999999999

    if dp[index] != -1:
        return dp[index]

    dp[index] = max(recursive_solution(index + interview[index][0]) + interview[index][1],
                    recursive_solution(index + 1))

    return dp[index]


n = int(input())
interview = [list(map(int, input().split())) for _ in range(n)]
dp = [-1 for _ in range(n + 1)]

answer = 0

solution = recursive_solution(0)

print(solution)
