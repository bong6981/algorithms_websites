//https://www.acmicpc.net/problem/2630
package silver3;

import java.io.*;
import java.util.StringTokenizer;

public class Q2630_MakingColoredPaper {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class Result {
        int white;
        int blue;

        public Result(int white, int blue) {
            this.white = white;
            this.blue = blue;
        }
    }

    static void input() {
        N = scan.nextInt();
        paper = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                paper[i][j] = scan.nextInt();
            }
        }
    }

    static int N;
    static int[][] paper;

    static Result sol(int size, int r, int c) {
        if(size == 1) {
            return paper[r][c] == 0? new Result(1, 0) : new Result(0, 1);
        }

        int half = size / 2;

        Result r1 = sol(half, r, c);
        Result r2 = sol(half, r+half, c);
        Result r3 = sol(half, r, c+half);
        Result r4 = sol(half, r+half, c+half);

        int white = r1.white + r2.white + r3.white + r4.white;
        int blue = r1.blue + r2.blue + r3.blue + r4.blue;

        if (white == 0) {
            return new Result(0, 1);
        }
        if (blue == 0) {
            return new Result(1, 0);
        }
        return new Result(white, blue);
    }

    public static void main(String[] args) {
        input();
        Result rs = sol(N, 0, 0);
        System.out.println(rs.white);
        System.out.println(rs.blue);
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
