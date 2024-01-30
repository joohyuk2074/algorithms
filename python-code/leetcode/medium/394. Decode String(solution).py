class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = ''

        for c in s:
            if c == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif c == ']':
                num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + cur_str * num
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_str += c

        return cur_str


s1 = "2[abc]3[cd]ef"
s2 = "3[a2[c]]"
solution = Solution()
result = solution.decodeString(s2)
print(result)
