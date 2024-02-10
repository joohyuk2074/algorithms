package me.joohyuk.codinginterview.chapter08.biggestcolorspots;

public class BiggestColorSpots {

    private int currentColorSpots;

    void determineBiggestColorSpot(int cols, int rows, int[][] a) {
        if (a == null) {
            throw new IllegalArgumentException("The matrix a cannot be null");
        }

        if (cols <= 0 || rows <= 0) {
            throw new IllegalArgumentException("The matrix a cannot be null");
        }

        int biggestColorSpot = 0;
        int color = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (a[i][j] > 0) {
                    currentColorSpots = 0;
                    computeColorSpot(i, j, cols, rows, a, a[i][j]);

                    if (currentColorSpots > biggestColorSpot) {
                        biggestColorSpot = currentColorSpots;
                        color = a[i][j] * (-1);
                    }
                }
            }
        }
        System.out.println("\nColor: " + color + " Bigest spot: " + biggestColorSpot);
    }

    private void computeColorSpot(int i, int j, int cols, int rows, int[][] a, int color) {
        a[i][j] = -a[i][j];     // 방문
        currentColorSpots++;

        if (i > 1 && a[i - 1][j] == color) {
            computeColorSpot(i - 1, j, cols, rows, a, color);
        }

        if ((i + 1) < rows && a[i + 1][j] == color) {
            computeColorSpot(i + 1, j, cols, rows, a, color);
        }

        if (j > 1 && a[i][j - 1] == color) {
            computeColorSpot(i, j - 1, cols, rows, a, color);
        }

        if ((j + 1) < cols && a[i][j + 1] == color) {
            computeColorSpot(i, j + 1, cols, rows, a, color);
        }
    }
}
