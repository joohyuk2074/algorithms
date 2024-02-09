package me.joohyuk.codinginterview.chapter08.hanoi;

public class Hanoi {

    public static void moveDisks(int n, char origin, char target, char intermediate) {
        if (n <= 0) {
            return;
        }

        if (n == 1) {
            System.out.println("Move disk 1 from rod " + origin + " to rod " + target);
            return;
        }

        moveDisks(n - 1, origin, intermediate, target);

        System.out.println("Move disk " + n + " from rod " + origin + " to rod " + target);

        moveDisks(n - 1, intermediate, target, origin);
    }
}
