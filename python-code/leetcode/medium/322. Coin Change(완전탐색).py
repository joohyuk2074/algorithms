import sys


class Solution:
    def coinChange(self, coins, amount):
        def findLowestCoins(coins, cur, amount):
            if cur >= len(coins) or amount <= 0:
                return 0 if amount == 0 else sys.maxsize - 1

            if coins[cur] > amount:
                return findLowestCoins(coins, cur + 1, amount)
            else:
                return min(1 + findLowestCoins(coins, cur, amount - coins[cur]), findLowestCoins(coins, cur + 1, amount))

        res = findLowestCoins(coins, 0, amount)
        return -1 if res == sys.maxsize - 1 else res


solution = Solution()
coins = [1, 2, 5]
amount = 11
change = solution.coinChange(coins, amount)
print(change)
