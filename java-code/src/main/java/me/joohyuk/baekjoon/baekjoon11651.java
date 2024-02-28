package me.joohyuk.baekjoon;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class baekjoon11651 {

    static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            points[i] = new Point(x, y);
        }
//
//        Comparator<Point> comparator = (Point p1, Point p2) -> {
//            if (p1.y > p2.y) {
//                return 1;
//            } else if (p1.y < p2.y) {
//                return -1;
//            } else {
//                return Integer.compare(p1.x, p2.x);
//            }
//        };
//
//        Arrays.sort(points, comparator);

        Arrays.sort(points, Comparator.comparingInt((Point p) -> p.y).thenComparingInt(p -> p.x));

        for (int i = 0; i < n; i++) {
            System.out.println(points[i].x + " " + points[i].y);
        }

        scanner.close();
    }
}
