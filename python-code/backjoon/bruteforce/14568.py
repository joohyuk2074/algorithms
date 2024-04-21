n = int(input())
answer = 0
for a in range(1, n):
    for b in range(1, n):
        for c in range(1, n):
            if a % 2 == 0 and b >= c + 2 and a + b + c == n:
                answer += 1

print(answer)
