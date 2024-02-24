class Solution:
    def fib(self, n):
        first = 0
        second = 1
        for _ in range(1, n):
            temp = first + second
            first = second
            second = temp

        return second


solution = Solution()
fib = solution.fib(5)
print(fib)
