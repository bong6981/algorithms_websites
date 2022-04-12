// https://www.acmicpc.net/problem/1629
package silver1;

import java.io.*;
import java.util.StringTokenizer;

public class Q1629_Multiplication {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        A = scan.nextLong();
        B = scan.nextInt();
        C = scan.nextInt();
    }

    static long A;
    static int B, C;

    static long sol(long num, int exponent) {
        if(exponent == 1) {
            return num % C;
        }

        long half = sol(num, exponent/2);

        if(exponent % 2 == 1) {
            return ((half * half) % C) * num % C;
        }
        return half * half % C;
    }

    public static void main(String[] args) {
        input();
        System.out.println(sol(A, B));
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
