package silver3;

import java.io.*;
import java.util.*;

//https://www.acmicpc.net/problem/15651
public class Q15651_NM3 {
    static StringBuilder sb = new StringBuilder();

    static void input() {
        FastReader scan = new FastReader();
        N = scan.nextInt();
        M = scan.nextInt();
        selected = new int[M+1];
    }

    private static int N, M;
    private static int[] selected;

    static void recFunc(int k) {
        if ( k == M + 1) {
            for (int i=1; i<=M; i++) sb.append(selected[i]).append(' ');
            sb.append('\n');
            return;
        }
        for(int cand = 1; cand <= N; cand++) {
            selected[k] = cand;
            recFunc(k+1);
        }

    }

    public static void main(String[] args) {
        input();
        recFunc(1);
        System.out.println(sb.toString());
    }

//    public static void sol(Stack<Integer> numbers) {
//        if(numbers.size() == m) {
//            for(int n : numbers) {
//                System.out.print(n + " ");
//            }
//            System.out.println();
//            return;
//        }
//
//        for (int i = 1; i <= n; i++) {
//            numbers.add(i);
//            sol(numbers);
//            numbers.pop();
//        }
//    }

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
