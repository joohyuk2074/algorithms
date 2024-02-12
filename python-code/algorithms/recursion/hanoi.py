def hanoi(n, src, dst, via):
    if n == 1:
        print(f"{src} -> {dst}")
        return

    hanoi(n - 1, src, via, dst)
    print(f"{src} -> {dst}")
    hanoi(n - 1, via, dst, src)


hanoi(3, "src", "dst", "via")
