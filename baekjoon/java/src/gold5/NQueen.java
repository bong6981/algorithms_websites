package gold5;

import java.io.*;
import java.util.StringTokenizer;
// https://www.acmicpc.net/problem/9663
public class NQueen {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        positions = new int[N + 1];
    }

    static int N, ans;
    static int[] positions;

    static boolean attackable(int r1, int c1, int r2, int c2) {
        if (c1 == c2) {
            return true;
        }
        if (r1 + c1 == r2 + c2) {
            return true;
        }
        if (r1 - c1 == r2 - c2) {
            return true;
        }
        return false;
    }

    static void recFunc(int row) {
        if (row == N + 1) {
            ans++;
            return;
        }
        for (int col = 1; col <= N; col++) {
            boolean possible = true;
            for (int i = 1; i < row; i++) {
                if (attackable(i, positions[i], row, col)) {
                    possible = false;
                    break;
                }
            }
            if (possible) {
                positions[row] = col;
                recFunc(row + 1);
                positions[row] = 0;
            }
        }
    }

    public static void main(String[] args) {
        input();
        recFunc(1);
        System.out.println(ans);
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
