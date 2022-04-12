package bronze2;

import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Q17608_Stick {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        arr = new int[N];
        stack = new Stack<>();
        for (int i = 0; i < N; i++) {
            arr[i] = scan.nextInt();
        }
    }

    static int N;
    static int[] arr;
    static Stack<Integer> stack;

    static void sol() {
        for (int ele : arr) {
            while(!stack.isEmpty() && stack.peek() <= ele) {
                stack.pop();
            }
            stack.push(ele);
        }
    }

    public static void main(String[] args) {
        input();
        sol();
        System.out.println(stack.size());
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
