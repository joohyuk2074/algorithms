
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort() # O(nlogn)

        max_count = 0

        count = 1
        cur_num = nums[0]

        for i in range(1, len(nums)):
            if cur_num + 1 == nums[i]:
                count += 1
                cur_num = nums[i]
            elif cur_num == nums[i]:
                continue
            else:
                if max_count < count:
                    max_count = count
                
                count = 1
                cur_num = nums[i]
        
        if max_count < count:
            max_count = count
        
        return max_count


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        
        return longest
                
    
       




solution = Solution()
nums = [100,4,200,1,3,2]
result = solution.longestConsecutive(nums)
print(result)

nums2 = [0,3,7,2,5,8,4,6,0,1]
result2 = solution.longestConsecutive(nums2)
print(result2)