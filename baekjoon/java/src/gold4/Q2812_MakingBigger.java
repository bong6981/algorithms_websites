package gold4;

import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Q2812_MakingBigger {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        K = scan.nextInt();
        arr = new int[N];
        char[] charArr = scan.next().toCharArray();
        for (int i = 0; i < N; i++) {
            arr[i] = charArr[i] - '0';
        }
    }

    static int N, K;
    static int[] arr;

    static void sol() {
        Stack<Integer> stack = new Stack<>();
        int left = K;
        for (int ele : arr) {
            while (!stack.isEmpty() && stack.peek() < ele && left > 0) {
                stack.pop();
                left--;
            }
            stack.push(ele);
        }

        int end = stack.size() - 1;
        if (left > 0) {
            end -= left;
        }
        for (int i = 0; i <= end; i++) {
            sb.append(stack.get(i));
        }
    }

    public static void main(String[] args) {
        input();
        sol();
        if(sb.length() == 0) {
            System.out.println("");
        } else {
            System.out.println(sb.toString());
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
