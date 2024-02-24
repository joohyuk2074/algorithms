n = int(input())
for _ in range(n):
    s = input()
    arr = []
    flag = True
    for c in s:
        if c == '(':
            arr.append(c)
        else:
            if len(arr) == 0:
                flag = False
                break
            else:
                arr.pop()

    if len(arr) != 0 or flag is False:
        flag = False

    if flag:
        print("YES")
    else:
        print("NO")
