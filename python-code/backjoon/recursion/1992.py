# 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
def isSameBlock(start_x, start_y, end_x, end_y):
    color = map[start_x][start_y]

    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            if map[i][j] != color:
                return False

    return True


def recur(start_x, start_y, end_x, end_y):
    # 색깔이 전체적으로 통일인지 확인

    res = ''
    if isSameBlock(start_x, start_y, end_x, end_y):
        res += map[start_x][start_y]
        return res
    else:
        # 왼쪽 위
        res += '('
        res += recur(start_x, start_y, (start_x + end_x) // 2, (start_y + end_y) // 2)
        res += recur(start_x, (start_y + end_y) // 2 + 1, (start_x + end_x) // 2, end_y)
        res += recur((start_x + end_x) // 2 + 1, start_y, end_x, (start_y + end_y) // 2)
        res += recur((start_x + end_x) // 2 + 1, (start_y + end_y) // 2 + 1, end_x, end_y)
        res += ')'

    return res


n = int(input())
map = []
for i in range(n):
    s = input()
    map.append([char for char in s])

answer = recur(0, 0, n - 1, n - 1)

print(answer)
