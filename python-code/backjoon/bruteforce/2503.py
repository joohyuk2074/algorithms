def check(number1, number2, strike, ball):
    strike_cnt = 0
    ball_cnt = 0

    str_number1 = str(number1)
    str_number2 = str(number2)

    for i in range(0, 3):
        for j in range(0, 3):
            if str_number1[i] == str_number2[j]:
                if i == j:
                    strike_cnt += 1
                else:
                    ball_cnt += 1

    if strike == strike_cnt and ball_cnt == ball:
        return True
    else:
        return False


n = int(input())

hint = []
for _ in range(n):
    score, strike, ball = map(int, input().split())
    hint.append([score, strike, ball])

answer = 0
for number in range(123, 999):
    num_str = str(number)
    if '0' in num_str:
        continue

    flag = True
    for score, strike, ball in hint:
        if not check(number, score, strike, ball):
            flag = False
            break
    if flag:
        answer += 1

print(answer)
