//https://www.acmicpc.net/problem/2470
package gold5;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q2470_TwoSolutions {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scan.nextInt();
        }
    }

    static int N;
    static int[] arr;

    static void sol() {
        Arrays.sort(arr);

        int start = 0;
        int end = N-1;
        int ans = Integer.MAX_VALUE;
        int ans_S = -1;
        int ans_E = -1;
        while(start <= end) {
            int mix = arr[start] + arr[end];
            if(ans > Math.abs(mix)) {
                ans = Math.abs(mix);
                ans_S = arr[start];
                ans_E = arr[end];
            }
            if( mix < 0) {
                start++;
            } else {
                end--;
            }
        }
        System.out.println(ans_S + " " + ans_E);
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
