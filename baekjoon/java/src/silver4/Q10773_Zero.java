// https://www.acmicpc.net/problem/10773
package silver4;

import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Q10773_Zero {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void inputAndSolve() {
        K = scan.nextInt();
        stack = new Stack<>();
        for (int i = 0; i < K; i++) {
            int n = scan.nextInt();
            if( n == 0) {
                stack.pop();
            } else {
                stack.push(n);
            }
        }
        System.out.println(stack.stream().reduce(0, Integer::sum));
    }

    static int K;
    static Stack<Integer> stack;

    public static void main(String[] args) {
        inputAndSolve();
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
