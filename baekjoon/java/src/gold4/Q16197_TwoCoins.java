package gold4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//https://www.acmicpc.net/problem/16197
public class Q16197_TwoCoins {
    static FastReader scan = new FastReader();

    static class Info {
        int x1, y1, x2, y2, turn;

        public Info(int x1, int y1, int x2, int y2, int turn) {
            this.x1 = x1;
            this.y1 = y1;
            this.x2 = x2;
            this.y2 = y2;
            this.turn = turn;
        }
    }

    static void input() {
        N = scan.nextInt();
        M = scan.nextInt();

        graph = new char[N][M];
        for (int i = 0; i < N; i++) {
            String s = scan.nextLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = s.charAt(j);
                if (graph[i][j] == 'o') {
                    graph[i][j] = '.';
                    start.add(i);
                    start.add(j);
                }
            }
        }
    }

    static int N, M;
    static List<Integer> start = new ArrayList<>();
    static char[][] graph;
    //왼, 오, 위, 아래
    static int[][] moves = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
    static int ans = 11;

    static void sol() {
        //모든 조합 구하기
        if (!search()) {
            System.out.println(-1);
            return;
        }
        ;
        if (ans > 10) {
            System.out.println(-1);
        } else {
            System.out.println(ans);
        }
    }

    static boolean isOut(int r, int c) {
        if (r < 0 || r >= N || c < 0 || c >= M) {
            return true;
        }
        return false;
    }

    static boolean search() {
        Queue<Info> q = new LinkedList<>();
        q.add(new Info(start.get(0), start.get(1), start.get(2), start.get(3), 0));

        while (!q.isEmpty()) {
            Info poll = q.poll();

            for (int i = 0; i < 4; i++) {
                int npx1 = poll.x1 + moves[i][0];
                int npy1 = poll.y1 + moves[i][1];
                int npx2 = poll.x2 + moves[i][0];
                int npy2 = poll.y2 + moves[i][1];
                boolean out1 = isOut(npx1, npy1);
                boolean out2 = isOut(npx2, npy2);

                if (poll.turn + 1 > 10) {
                    return false;
                }


                if (out1 && out2) {
                    continue;
                }
                if (out1 && !out2) {
                    ans = poll.turn + 1;
                    return true;
                }

                if (!out1 && out2) {
                    ans = poll.turn + 1;
                    return true;
                }

                if (graph[npx1][npy1] == '#') {
                    npx1 = poll.x1;
                    npy1 = poll.y1;
                }
                if (!isOut(npx2, npy2) && graph[npx2][npy2] == '#') {
                    npx2 = poll.x2;
                    npy2 = poll.y2;
                }

                q.add(new Info(npx1, npy1, npx2, npy2, poll.turn + 1));
            }
        }
        return true;
    }

    public static void main(String[] args) {
        input();
        sol();
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
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

        String nextLine() {
            String s = "";
            try {
                s = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return s;
        }
    }
}
