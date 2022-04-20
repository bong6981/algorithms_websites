package silver1;

import java.io.*;
import java.util.*;

public class Q2292_Coin2_BFS {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        K = scan.nextInt();
        for (int i = 0; i < N; i++) {
            int coin = scan.nextInt();
            if(coin <= K) {
                coins.add(coin);
            }
        }
        dp = new int[10001];
        Arrays.fill(dp, -1);
    }

    static int N, K;
    static List<Integer> coins = new ArrayList<>();
    static int[] dp;

    static void sol() {
        Collections.sort(coins);
        Queue<Integer> q = new LinkedList<>();
        dp[0] = 0;
        q.add(0);
        while(!q.isEmpty()) {
            int now = q.poll();
            for(int coin : coins) {
                if( now + coin <= K && dp[now+coin] == -1) {
                    dp[now+coin] = dp[now] + 1;
                    q.add(now+coin);
                }
            }
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
