def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    start = 1
    second = 1

    for i in range(3, n + 1):
        temp = start + second
        start = second
        second = temp

    print(second)


fibonacci(8)
