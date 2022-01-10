package silver2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

// https://www.acmicpc.net/problem/17829
public class Q17829_222Pooling {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] data = br.readLine().split(" ");
            for (int j = 0; j < data.length; j++) {
                board[i][j] = Integer.parseInt(data[j]);
            }
        }

        while (n > 1) {
            n /= 2;
            int[][] newBoard = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    Integer[] toCompare = {board[i * 2][j * 2], board[i * 2][j * 2 + 1], board[i * 2 + 1][j * 2], board[i * 2 + 1][j * 2 + 1]};
                    Arrays.sort(toCompare, Comparator.reverseOrder());
                    newBoard[i][j] = toCompare[2];
                }
            }
            board = newBoard;
        }

        System.out.println(board[0][0]);
    }
}
