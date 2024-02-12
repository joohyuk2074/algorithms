def solution(n):
    answer = [[]]

    def hanoi(n, start, inter, to):
        if n == 1:
            answer.append([start, to])
            return

        hanoi(n - 1, start, to, inter)
        print(str(start) + " to " + str(to))
        hanoi(n - 1, inter, to, inter)

    hanoi(n, 1, 2, 3)

    return answer


solution(3)

