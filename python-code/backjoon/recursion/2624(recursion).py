def solution(current_price, position):
    if current_price == 0:
        return 1

    if position >= k:
        return 0

    cnt = 0
    coins_price = coins[position][0]
    coin_num = coins[position][1]

    for i in range(coin_num + 1):
        remaining = current_price - i * coins_price
        if remaining < 0:
            break
        cnt += solution(remaining, position + 1)

    return cnt


t = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]

coins.sort(key=lambda x: x[0], reverse=True)

answer = solution(t, 0)

print(answer)
