package me.joohyuk.codinginterview.chapter01;

public class Problem07 {

    boolean rotate(int[][] matrix) {
        if (matrix.length == 0 || matrix.length != matrix[0].length) {
            return false;
        }

        int n = matrix.length;
        for (int layer = 0; layer < n; layer++) {
            int first = layer;
            int last = n - 1 - layer;
            for (int i = first; i < last; i++) {
                int offset = i - first;
                int top = matrix[first][i];     // 윗 부분을 저장해 놓는다.

                // 왼쪽 -> 위쪽
                matrix[first][i] = matrix[last - offset][first];

                // 아래쪽 -> 왼쪽
                matrix[last - offset][first] = matrix[last][last - offset];

                // 오른쪽 -> 아래쪽
                matrix[last][last - offset] = matrix[i][last];

                // 위쪽 -> 오른쪽
                matrix[i][last] = top;
            }
        }

        return true;
    }

}
