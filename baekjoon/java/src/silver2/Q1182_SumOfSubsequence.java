package silver2;

import java.io.*;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/1182
public class Q1182_SumOfSubsequence {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        S = scan.nextInt();
        nums = new int[N+1];
        for (int i=1; i<= N; i++) nums[i] = scan.nextInt();
    }

    static int N, S, ans;
    static int[] nums;

    static void sol(int k, int val) {
        if(k == N+1) {
            if(val == S) {
                ans++;
            }
            return;
        }
        sol(k+1, val+nums[k]);
        sol(k+1, val);
    }


    public static void main(String[] args) {
        input();
        sol(1, 0);
        if( S == 0) {
            ans--;
        }
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
            while(st == null || !st.hasMoreElements()) {
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
