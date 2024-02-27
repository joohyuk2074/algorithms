def recursion(index, dwarf_num, sum, result):
    if dwarf_num == 7 and sum == 100:
        for i in range(len(result)):
            print(dwarf[result[i]])
        return

    if index >= len(dwarf):
        return

    result.append(index)
    recursion(index + 1, dwarf_num + 1, sum + dwarf[index], result)
    result.remove(index)
    recursion(index + 1, dwarf_num, sum, result)


dwarf = [int(input()) for _ in range(9)]

recursion(0, 0, 0, [])