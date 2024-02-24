s = input()
# 0으로 통일하는 경우
answer = 0

arr = []
current = ""

zero = 0
one = 0
if s[0] == '0':
    zero += 1
else:
    one += 1

for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        if s[i] == '0':
            zero += 1
        else:
            one += 1

answer = min(zero, one)

print(answer)
