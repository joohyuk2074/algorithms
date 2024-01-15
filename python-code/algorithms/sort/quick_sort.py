def partition(left, right, nums):
    pivot = nums[right]

    i = left - 1
    for j in range(left, right):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    pivot_pos = i + 1
    nums[pivot_pos], nums[right] = nums[right], nums[pivot_pos]
    return pivot_pos


def quick_sort_recursive(left, right, nums):
    if left >= right:
        return

    pivot_pos = partition(left, right, nums)

    quick_sort_recursive(left, pivot_pos - 1, nums)
    quick_sort_recursive(pivot_pos + 1, right, nums)


def quick_sort(nums):
    quick_sort_recursive(0, len(nums) - 1, nums)


nums = [5, 2, 7, 3, 8, 3, 4, 5, 6, 8, 2, 4]
quick_sort(nums)
