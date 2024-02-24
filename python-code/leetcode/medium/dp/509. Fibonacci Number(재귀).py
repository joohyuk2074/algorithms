class Solution:
    def fib(self, n):
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)


solution = Solution()
fib = solution.fib(5)
print(fib)
