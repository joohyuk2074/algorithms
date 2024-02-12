def solution(n):
    answer = []

    def hanoi(n, start, via, dst):
        if n == 1:
            answer.append([start, dst])
            return

        hanoi(n - 1, start, dst, via)
        answer.append([start, dst])
        hanoi(n - 1, via, start, dst)

    hanoi(n, 1, 2, 3)

    return answer


result = solution(2)
print(result)
