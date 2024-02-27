dwarfs = [int(input()) for _ in range(9)]
total_height = sum(dwarfs)

exclusive_arr = []
for i in range(9):
    for j in range(i + 1, 9):
        if total_height - (dwarfs[i] + dwarfs[j]) == 100:
            exclusive_arr.append(i)
            exclusive_arr.append(j)

for i in range(9):
    if i not in exclusive_arr:
        print(dwarfs[i])
