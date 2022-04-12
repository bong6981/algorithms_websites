package gold5;

import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Q2493_Tower {
    static class Tower {
        int idx, height;

        public Tower(int idx, int height) {
            this.idx = idx;
            this.height = height;
        }
    }
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        arr = new int[N+1];
        for (int i = 1; i <= N; i++) {
            arr[i] = scan.nextInt();
        }
        stack = new Stack<>();
    }

    static int N;
    static int[] arr;
    static Stack<Tower> stack;

    static void sol() {
        for (int i = 1; i <= N; i++) {
            int ele = arr[i];
            while(!stack.isEmpty() && stack.peek().height < ele) {
                stack.pop();
            }
            if(stack.isEmpty()) {
                sb.append(0).append(" ");
            } else {
                sb.append(stack.peek().idx).append(" ");
            }
            stack.push(new Tower(i, ele));
        }
    }

    public static void main(String[] args) {
        input();
        sol();
        System.out.println(sb.toString());
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
