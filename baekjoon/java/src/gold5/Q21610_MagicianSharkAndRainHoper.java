package gold5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/21610
public class Q21610_MagicianSharkAndRainHoper {
    private static int[][] board;
    private static int[][] clouds;
    private static int[][] moves = new int[][]{{0, 0}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        board = new int[n][n];
        clouds = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        clouds[n - 1][0] = 1;
        clouds[n - 1][1] = 1;
        clouds[n - 2][0] = 1;
        clouds[n - 2][1] = 1;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int moveX = moves[d][0] * s + s * n;
            int moveY = moves[d][1] * s + s * n;
            int[][] disappearedClouds = new int[n][n];
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (clouds[j][k] == 1) {
                        int nx = (j + moveX) % n;
                        int ny = (k + moveY) % n;
                        disappearedClouds[nx][ny] = 1;
                        board[nx][ny] += 1;
                    }
                }
            }

            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (disappearedClouds[j][k] == 1) {
                        for (int[] move : new int[][]{moves[2], moves[4], moves[6], moves[8]}) {
                            int nx = j + move[0];
                            int ny = k + move[1];
                            if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                                if (board[nx][ny] >= 1) {
                                    board[j][k] += 1;
                                }
                            }
                        }
                    }
                }
            }

            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (disappearedClouds[j][k] == 1) {
                        disappearedClouds[j][k] = 0;
                        continue;
                    }
                    if (board[j][k] >= 2) {
                        board[j][k] -= 2;
                        disappearedClouds[j][k] = 1;
                    }
                }
            }
            clouds = disappearedClouds;
        }

        int sum = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sum += board[i][j];
            }
        }
        System.out.println(sum);
    }
}
