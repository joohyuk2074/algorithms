def recursive(index, current_point, drive_distance):
    global min_dist

    if current_point == d:
        min_dist = min(min_dist, drive_distance)
        return

    if current_point > d:
        return

    for i in range(index, n):
        # 현재 current_point보다 start지점이 앞에 있는지 확인
        start, end, 지름길 = arr[i]
        if current_point == start:
            if end - start > 지름길:
                recursive(i + 1, end, drive_distance + 지름길)
            else:
                recursive(i + 1, current_point + 1, drive_distance + 1)
        else:
            recursive(i + 1, current_point + 1, drive_distance + 1)


n, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
min_dist = 10000

recursive(0, 0, 0)

print(min_dist)
