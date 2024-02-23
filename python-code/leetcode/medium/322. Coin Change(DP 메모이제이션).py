import sys


class Solution:
    def coinChange(self, coins, amount):
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        def findLowestCoins(coins, cur, amount):
            if cur == len(coins) or amount <= 0:
                return 0 if amount == 0 else sys.maxsize - 1

            if dp[cur][amount] != -1:
                return dp[cur][amount]

            if coins[cur] > amount:
                dp[cur][amount] = findLowestCoins(coins, cur + 1, amount)
            else:
                dp[cur][amount] = min(1 + findLowestCoins(coins, cur, amount - coins[cur]),
                                      findLowestCoins(coins, cur + 1, amount))
            return dp[cur][amount]

        result = findLowestCoins(coins, 0, amount)
        return -1 if result == sys.maxsize - 1 else result


solution = Solution()
coins = [1, 2, 5]
amount = 11
change = solution.coinChange(coins, amount)
print(change)
