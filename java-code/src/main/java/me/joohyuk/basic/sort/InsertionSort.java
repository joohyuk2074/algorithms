package me.joohyuk.basic.sort;

public class InsertionSort {

    public static void insertionSort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            int target = nums[i];
            int j = i - 1;

            while (j >= 0 && target < nums[j]) {
                nums[j + 1] = nums[j];
                j -= 1;
            }

            nums[j + 1] = target;
        }
    }

    public static void main(String[] args) {
        int[] nums = {5, 2, 3, 4, 65, 6, 45, 3, 657, 456, 7, 456, 7};
        insertionSort(nums);
        for (int num : nums) {
            System.out.print(num + " ");
        }
    }
}
