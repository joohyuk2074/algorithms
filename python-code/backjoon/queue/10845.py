from sys import stdin

queue = []
n = int(stdin.readline())

for _ in range(n):
    command = stdin.readline().split()

    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            x = queue[0]
            queue.pop(0)
            print(x)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
