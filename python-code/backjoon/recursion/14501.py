def recursive_solution(index, total_price):
    global answer

    if index == n - 1:
        answer = max(answer, total_price)
        return

    if index > n - 1:
        return

    recursive_solution(index + interview[index][0], total_price + interview[index][1])
    recursive_solution(index + 1, total_price)


n = int(input())
interview = [list(map(int, input().split())) for _ in range(n)]

answer = 0

recursive_solution(0, 0)

print(answer)
