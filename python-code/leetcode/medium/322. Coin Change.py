class Solution:
    def __init__(self):
        self.answer = 0

    def change(self, index, amount, coin_num, coins):
        if amount == 0:
            self.answer = min(self.answer, coin_num)
            return

        if index == len(coins):
            return

        count = 0
        coin = coins[index]

        while amount > coin * count:
            self.change(index + 1, amount - coin * count, coin_num + count, coins)
            self.change(index + 1, amount, coin_num, coins)
            count += 1

    def coinChange(self, coins, amount):
        sorted_coins = sorted(coins, reverse=True)
        self.change(0, amount, 0, sorted_coins)
        return self.answer


solution = Solution()
coins = [1, 2, 5]
amount = solution.coinChange(coins, 11)
print(amount)
