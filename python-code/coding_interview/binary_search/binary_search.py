def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while(left <= right):
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        
    # Replace this placeholder return statement with your code
    return -1


input1 = [1,6,8,10]
print(binary_search(input1, 6))