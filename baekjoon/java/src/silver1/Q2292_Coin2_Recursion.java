package silver1;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q2292_Coin2_Recursion {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        K = scan.nextInt();
        coins = new int[N+1];
        for (int i = 0; i < N; i++) {
            coins[i] = scan.nextInt();
        }
        dp = new int[10001];
        Arrays.fill(dp, 10001);
    }

    static int N, K;
    static int[] coins, dp;

    static void sol() {
        dp[0] = 0;
        for (int i = 0; i < N; i++) {
            int coin = coins[i];
            for (int j = coin; j <= K; j++) {
                dp[j] = Math.min(dp[j], dp[j-coin]+ 1);
            }
        }

        if (dp[K] == 10001) {
            System.out.println(-1);
            return;
        }
        System.out.println(dp[K]);
    }


    public static void main(String[] args) {
        input();
        sol();
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
