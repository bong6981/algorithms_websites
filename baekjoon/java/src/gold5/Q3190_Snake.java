package gold5;

import java.io.*;
import java.util.*;

public class Q3190_Snake {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class Position {
        int x, y;
        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    // 뱀 : 2, 사과 :1, 벽 : -1
    static void input() {
        N = scan.nextInt();
        K = scan.nextInt();
        board = new int[N+2][N+2];
        for (int i : new int[]{0, N+1}) {
            for (int j = 0; j <= N; j++) {
                board[i][j] = -1;
                board[j][i] = -1;
            }
        }
        for (int i = 0; i < K; i++) {
            int r = scan.nextInt();
            int c = scan.nextInt();
            board[r][c] = 1;
        }
        L = scan.nextInt();
        changeDirInfo = new int[(int) Math.pow(10, 4) + 1];
        for (int i = 0; i < L; i++) {
            int time = scan.nextInt();
            String dir = scan.next();
            if(dir.equals("D")) {
                changeDirInfo[time] = 1;
            } else {
                changeDirInfo[time] = -1;
            }
        }
        board[1][1] = 2;
        head = new Position(1, 1);
        snake.add(new Position(1, 1));
    }

    static int N, K, L;
    static int[][] board;
    static int[] changeDirInfo;
    static Position head;
    static int[][] moves = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    static Queue<Position> snake = new LinkedList<>();

    static int sol() {
        int time = 0;
        int dir = 0;
        while(!snake.isEmpty()) {
            time += 1;
            int next_x = head.x + moves[dir][0];
            int next_y = head.y + moves[dir][1];
            if(board[next_x][next_y] == 2 || board[next_x][next_y] == -1) {
                break;
            }

            if(board[next_x][next_y] != 1) {
                Position deleted = snake.poll();
                board[deleted.x][deleted.y] = 0;
            }

            snake.add(new Position(next_x, next_y));
            board[next_x][next_y] = 2;

            dir += changeDirInfo[time];
            if(dir==4) {
                dir = 0;
            } else if(dir == -1) {
                dir = 3;
            }
            head = new Position(next_x, next_y);
        }
        return time;
    }

    public static void main(String[] args) {
        input();
        System.out.println(sol());
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
