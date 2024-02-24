s = input()
# 0으로 통일하는 경우
answer = 0

arr = []
current = ""
for i in range(len(s)):
    if i == 0 and s[i] == '1':
        current += '1'
        continue

    if s[i] == '1':
        current += '1'
    else:
        if len(current) != 0:
            arr.append(current)
            current = ""

if current:
    arr.append(current)
    current = ""

answer = len(arr)
arr = []

for i in range(len(s)):
    if i == 0 and s[i] == '0':
        current += '0'
        continue

    if s[i] == '0':
        current += '0'
    else:
        if len(current) != 0:
            arr.append(current)
            current = ""

if current:
    arr.append(current)

answer = min(answer, len(arr))

print(answer)
