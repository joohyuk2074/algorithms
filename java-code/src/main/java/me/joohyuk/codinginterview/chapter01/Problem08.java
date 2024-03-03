package me.joohyuk.codinginterview.chapter01;

public class Problem08 {

    void setZeros(int[][] matrix) {
        boolean[] row = new boolean[matrix.length];
        boolean[] column = new boolean[matrix[0].length];

        // 값이 0인 행과 열의 인덱스를 저장한다.
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    row[i] = true;
                    column[j] = true;
                }
            }
        }

        // 행의 원소를 전부 0으로 바꾼다.
        for (int i = 0; i < row.length; i++) {
            if (row[i]) {
                nullifyRow(matrix, i);
            }
        }

        // 열의 원소를 전부 0으로 바꾼다.
        for (int j = 0; j < column.length; j++) {
            if (column[j]) {
                nullifyColumn(matrix, j);
            }
        }
    }

    private void nullifyRow(int[][] matrix, int row) {
        for (int j = 0; j < matrix[0].length; j++) {
            matrix[row][j] = 0;
        }
    }

    private void nullifyColumn(int[][] matrix, int col) {
        for (int i = 0; i < matrix[0].length; i++) {
            matrix[i][col] = 0;
        }
    }

}
