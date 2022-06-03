package gold5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q2470_TwoSolution {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        input();
        sol();
    }

    private static void input() {
        N = scan.nextInt();
        A = new int[N+1];
        for (int i = 1; i <= N; i++) {
            A[i] = scan.nextInt();
        }
    }

    private static void sol() {
        Arrays.sort(A, 1, N+1);

        int best_sum = Integer.MAX_VALUE;
        int v1 = 0, v2 = 0, L = 1, R = N;

        while(L < R) {
            int sum = A[L] + A[R];
            if(Math.abs(sum) < Math.abs(best_sum)) {
                best_sum = sum;
                v1 = A[L];
                v2 = A[R];
            }

            if( sum > 0) {
                R--;
            } else L++;
        }
        sb.append(v1).append(' ').append(v2);
        System.out.println(sb);
    }

    static int N;
    static int[] A;

    static class FastReader {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        String next() {
            while(st==null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();;
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

    }
}
