def binomial(n, k):
    if k == 0 or k == n:
        return 1

    return binomial(n - 1, k - 1) + binomial(n - 1, k)
