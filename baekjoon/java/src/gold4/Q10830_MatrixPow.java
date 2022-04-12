// https://www.acmicpc.net/problem/10830
package gold4;

import java.io.*;
import java.util.StringTokenizer;

public class Q10830_MatrixPow  {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        B = scan.nextLong();
        matrix = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                matrix[i][j] = scan.nextInt() % 1000;
            }
        }
    }

    static int N;
    static long B;
    static int[][] matrix;

    static int[][] sol(long exponent, int[][] m) {
        if(exponent == 1) {
            return m;
        }
        if(exponent == 2) {
            return mul(m, m);
        }

        int[][] half = sol(exponent / 2, m);
        int[][] result = mul(half, half);
        if(exponent % 2 == 1) {
            result = mul(result, m);
        }
        return result;
    }

    static int[][] mul(int[][] x, int[][] y) {
        int[][] result = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int val = 0;
                for (int k = 0; k < N; k++) {
                    val += (x[i][k] * y[k][j]) % 1000;
                }
                result[i][j] = val % 1000;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        input();
        int[][] ans = sol(B, matrix);
        for (int[] row : ans) {
            for (int ele : row) {
                System.out.print(ele % 1000+" ");
            }
            System.out.println();
        }
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
