n = int(input())
for i in range(n):
    number = int(input())
    flag = True
    for k in range(2, 1000000):
        if number % k == 0:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
