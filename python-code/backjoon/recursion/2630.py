def isSameColor(start_x, start_y, end_x, end_y):
    color = boards[start_x][start_y]

    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            if color != boards[i][j]:
                return False

    return True


def recursive(start_x, start_y, end_x, end_y):
    if isSameColor(start_x, start_y, end_x, end_y):
        answer[boards[start_x][start_y]] += 1
        return

    current_size = end_x - start_x + 1
    length = current_size // 2

    # 좌측 상위
    recursive(start_x, start_y, start_x + length - 1, start_y + length - 1)

    # 우측 상위
    recursive(start_x, start_y + length, start_x + length - 1, start_y + current_size - 1)

    # 좌측 하위
    recursive(start_x + length, start_y, start_x + current_size - 1, start_y + length - 1)

    # 우측 하위
    recursive(start_x + length, start_y + length, start_x + current_size - 1, start_y + current_size - 1)


n = int(input())
boards = [list(map(int, input().split())) for _ in range(n)]
answer = {
    0: 0,
    1: 0
}

recursive(0, 0, n - 1, n - 1)

print(answer[0])
print(answer[1])
