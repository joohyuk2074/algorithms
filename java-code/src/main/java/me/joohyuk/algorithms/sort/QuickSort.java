package me.joohyuk.algorithms.sort;

public class QuickSort {

    public static int partition(int left, int right, int[] numbers) {
        int pivot = numbers[right];
        int i = left - 1;
        int j = 0;

        for (j = left; j < right; j++) {
            if (pivot > numbers[j]) {
                i++;
                int temp = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = temp;
            }
        }

        int temp = numbers[i + 1];
        numbers[i + 1] = numbers[j];
        numbers[j] = temp;

        return i + 1;
    }

    public static void quickSortRecursion(int left, int right, int[] numbers) {
        if (left >= right) {
            return;
        }

        int pivotIndex = partition(left, right, numbers);

        quickSortRecursion(left, pivotIndex - 1, numbers);
        quickSortRecursion(pivotIndex + 1, right, numbers);
    }

    public static void quickSort(int[] numbers) {
        quickSortRecursion(0, numbers.length - 1, numbers);
    }

    public static void main(String[] args) {
        int[] numbers = {7, 2, 5, 1, 3, 8, 7, 4, 9, 6};

        quickSort(numbers);

        for (int number : numbers) {
            System.out.print(number + " ");
        }
    }
}
