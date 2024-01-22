package me.joohyuk.sort;

public class QuickSort {
    private static int partition(int left, int right, int[] nums) {

        int pivotNum = nums[right];
        int j = left - 1;

        for (int i = left; i < nums.length; i++) {
            if (nums[i] < pivotNum) {
                j += 1;

                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
            }
        }

        int temp = nums[j + 1];
        nums[j + 1] = nums[right];
        nums[right] = temp;
        return j + 1;
    }

    private static void sort(int left, int right, int[] nums) {
        if (left >= right) {
            return;
        }

        int pivot = partition(left, right, nums);

        sort(left, pivot - 1, nums);
        sort(pivot + 1, right, nums);
    }

    private static void quickSort(int[] nums) {
        sort(0, nums.length - 1, nums);
    }

    public static void main(String[] args) {
        int[] nums = {5, 2, 3, 4, 65, 6, 45, 3, 657, 456, 7, 456, 7};
        quickSort(nums);
        for (int num : nums) {
            System.out.print(num + " ");
        }
    }
}
