package silver3;

import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

// https://www.acmicpc.net/problem/15650
public class Q15650_NM2 {
    static StringBuilder sb = new StringBuilder();

    public static void input() {
        FastReader scan = new FastReader();
        N = scan.nextInt();
        M = scan.nextInt();
        selected = new int[M+1];
    }

    static int N;
    static int M;
    static int[] selected;

    static void recFunc(int k) {
        if( k==M+1) {
            for(int i=1; i<=M; i++) sb.append(selected[i]).append(' ');
            sb.append('\n');
            return;
        }

        for(int i=selected[k-1]+1; i<=N; i++) {
            selected[k] = i;
            recFunc(k+1);
            selected[k] = 0;
        }
    }

    public static void main(String[] args) {
        input();
        recFunc(1);
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

    public static int[] ints;
    public static int m;
    public static int n;

    public static void main_before(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        ints = IntStream.range(1, n + 1).toArray();
        dfs(new int[m], 0, 0);
    }

    public static void dfs(int[] numbers, int idx, int start) {
        if (idx == m) {
            for (int number : numbers) {
                System.out.print(number + " ");
            }
            System.out.println();
            return;
        }

        for (int i = start; i < n; i++) {
            numbers[idx] = ints[i];
            dfs(numbers, idx + 1, i + 1);
        }
    }
}
