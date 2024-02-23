class Solution:
    def countBits(self, n):
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i >> 1] + (i & 1)
        return f


solution = Solution()
n = 5
bits = solution.countBits(5)
print(bits)
