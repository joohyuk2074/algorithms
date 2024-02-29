t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    new_arr = [0] * n
    for i in range(n):
        if i % 2 == 0:
            new_arr[i // 2] = numbers[i]
        else:
            new_arr[n - 1 - (i // 2)] = numbers[i]

    answer = 0
    for i in range(n - 1):
        answer = max(answer, abs(new_arr[i] - new_arr[i + 1]))

    answer = max(answer, abs(new_arr[n - 1] - new_arr[0]))

    print(answer)
