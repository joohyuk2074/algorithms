# 1. 입력 배열을 오름차순으로 정렬합니다.
# 2. 입력 배열을 순회합니다. 현재 숫자가 0보다 크면 더 이상 세 쌍의 숫자가 나올 수 없으므로 루프를 종료합니다.
# 3. 반복 중 현재 인덱스 값이 이전 인덱스 값과 같으면 해당 반복을 건너 뜁니다.
# 4. 두개의 포인터(low와 high)를 사용하여 현재 요소와 함께 합이 0이 되는 세 쌍의 요소를 찾습니다.
# 5. 합계가 0보다 작으면, low 포인터를 앞으로 이동시켜 합계를 증가시킵니다. 합계가 0보다 크면, high 포인터를 뒤로 이동시켜 합계를 감소시킵니다.
# 6. 그렇지 않으면 합이 0이 되므로, 세 값을 결과 배열에 추가한 다음 중복을 건너뛰기 위해 두 포인터를 다음 고유 값으로 이동합니다.
# 7. 결과 배열을 반환합니다.

def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n-2):
        if nums[i] > 0:
            break

        if i == 0 or nums[i] != nums[i - 1]:
            low, high = i + 1, n - 1

            while low < high:
                sum = nums[i] + nums[low] + nums[high]

                if sum < 0:
                    low += 1
                elif sum > 0:
                    high -= 1
                else:
                    result.append([nums[i], nums[low], nums[high]])

                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low -1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
    return result


nums = [-1,0,1,2,-1,-4]
result = three_sum(nums)
print(result)