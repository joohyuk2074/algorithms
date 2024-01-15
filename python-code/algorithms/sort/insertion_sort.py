def insertion_sort(nums):
    for i in range(1, len(nums)):
        target = nums[i]
        j = i - 1
        while target < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = target


nums = [5, 2, 7, 3, 8, 3, 4, 5, 6, 8, 2, 4]
insertion_sort(nums)
