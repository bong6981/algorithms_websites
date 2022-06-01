package silver2;
// https://www.acmicpc.net/problem/24913

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q24913_Vote {
    static FastReader scan = new FastReader();
    static StringBuffer sb = new StringBuffer();

    static void input() {
        N = scan.nextInt();
        Q = scan.nextInt();
        res = new long[N + 1];
    }

    static int N, Q;
    static long jh = 0;
    static long maxV = 0;
    static long sum = 0;
    static long[] res;

    static void sol() {
        for (int i = 0; i < Q; i++) {
            int op = scan.nextInt();
            if (op == 1) {
                int cnt = scan.nextInt();
                int cand = scan.nextInt();
                if (cand != N + 1) {
                    res[cand] += cnt;
                    maxV = Math.max(maxV, res[cand]);
                    sum += cnt;
                } else {
                    jh += cnt;
                }
            } else if (op == 2) {
                int me = scan.nextInt();
                int other = scan.nextInt();

                if (jh + me <= maxV) {
                    sb.append("NO").append("\n");
                } else {
                    long toCompare = Math.max(maxV, (long)Math.ceil((sum + other) / (double)N));
                    if(jh+me > toCompare) {
                        sb.append("YES").append("\n");
                    } else {
                        sb.append("NO").append("\n");
                    }
                }
            }
        }

    }

    public static void main(String[] args) {
        input();
        sol();
        System.out.println(sb.toString());
    }

    static class FastReader {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

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
    }
}
