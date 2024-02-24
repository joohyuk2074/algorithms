def recursive(n):
    if n == 1:
        return ['*']

    stars = recursive(n // 3)
    answer = []

    # 1 line
    for i in stars:
        answer.append(i * 3)
    # 2 line
    for i in stars:
        answer.append(i + ' ' * (n // 3) + i)
    # 3 line
    for i in stars:
        answer.append(i * 3)

    return answer


n = int(input())
print(recursive(n))
# print('\n'.join(recursive(n)))
