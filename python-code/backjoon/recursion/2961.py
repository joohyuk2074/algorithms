def recur(idx, dan, zzan, use):
    global min_price

    if idx == n:
        if use == 0:
            return

        result = abs(dan - zzan)
        answer = min(answer, result)
        return

    recur(idx + 1, dan + ingre[idx][0], zzan * ingre[idx][1], use + 1)
    recur(idx + 1, dan, zzan, use)


n = int(input())
ingre = [list(map(int, input().split())) for _ in range(n)]

min_price = 1_000_000_000

recur(0, 0, 1, 0)

print(min_price)
