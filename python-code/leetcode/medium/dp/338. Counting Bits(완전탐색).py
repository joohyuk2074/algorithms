class Solution:
    def countOne(self, binary):
        count = 0
        for c in binary:
            if c == "1":
                count += 1
        return count

    def getBinary(self, number):
        binary = ""

        while number != 0:
            q = number % 2
            number = number // 2
            binary += str(q)

        return binary

    def countBits(self, n):
        answer = []
        for num in range(n + 1):
            binary = self.getBinary(num)
            count = self.countOne(binary)
            answer.append(count)
        return answer


solution = Solution()
n = 5
bits = solution.countBits(5)
print(bits)
