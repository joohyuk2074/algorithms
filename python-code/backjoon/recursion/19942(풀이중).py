def solution(index, p_sum, f_sum, s_sum, v_sum, price, index_arr):
    global min_price
    global min_indexes

    if index == n:
        if p_sum >= mp and f_sum >= mf and s_sum >= ms and v_sum >= mv:
            if min_price == price:
                min_indexes.append(index_arr.copy())
            else:
                min_price = min(min_price, price)
                min_indexes.clear()
                min_indexes.append(index_arr.copy())
            return
        return

    index_arr.append(index + 1)
    solution(index + 1, p_sum + ingre[index][0], f_sum + ingre[index][1], s_sum + ingre[index][2],
             v_sum + ingre[index][3], price + ingre[index][4], index_arr)
    index_arr.remove(index + 1)
    solution(index + 1, p_sum, f_sum, s_sum, v_sum, price, index_arr)





n = int(input())
mp, mf, ms, mv = map(int, input().split())
ingre = [list(map(int, input().split())) for _ in range(n)]

min_price = int(1e9)
min_indexes = []

solution(0, 0, 0, 0, 0, 0, [])

print(min_price)
print(*min_indexes)
