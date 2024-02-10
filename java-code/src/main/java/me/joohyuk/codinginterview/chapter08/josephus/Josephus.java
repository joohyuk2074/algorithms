package me.joohyuk.codinginterview.chapter08.josephus;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

public class Josephus {

    public static void josephusWithQueue(int n, int k) {

        Queue<Integer> circle = new ArrayDeque<>();

        for (int i = 1; i <= n; i++) {
            circle.add(i);
        }

        while (circle.size() != 1) {
            for (int i = 1; i <= k; i++) {
                int eliminated = circle.poll();
                if (i == k) {
                    System.out.println("Eliminated: " + eliminated);
                    break;
                }
                circle.add(eliminated);
            }
        }

        System.out.println("Using queue! Survivor: " + circle.peek());
    }

    public static void josephusWithCircularLinkedList(int n, int k) {
        List<Integer> q = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            q.add(i);
        }

        int j = 0;
        while (q.size() > 1) {
            j = (j + k - 1) % q.size();
            q.remove(j);
            System.out.println("Eliminated: " + (j + 1));
        }

        System.out.println("Using CircularLinkedList! Survivor: " + (q.get(0) + 1));
    }

    public static int josephusWithRecursion(int n, int k) {
        if (n == 1) {
            return 1;
        }

        System.out.println("n: " + n + " k: " + k);

        return (josephusWithRecursion(n - 1, k) + k - 1) % n + 1;
    }

    public static void main(String[] args) {
        josephusWithQueue(7, 3);

        System.out.println();

        josephusWithCircularLinkedList(7, 3);

        System.out.println();

        josephusWithRecursion(7, 3);
    }
}
