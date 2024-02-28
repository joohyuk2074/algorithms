n = int(input())
coordinates = [list(map(int, input().split())) for _ in range(n)]

sorted_points = sorted(coordinates, key=lambda point: (point[1], point[0]))

for x, y in sorted_points:
    print(fr"{x} {y}")
