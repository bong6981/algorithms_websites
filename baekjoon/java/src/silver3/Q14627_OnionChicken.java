package silver3;

import java.io.*;
import java.util.StringTokenizer;

public class Q14627_OnionChicken {
    static FastReader scan = new FastReader();

    static void input() {
        S = scan.nextInt();
        C = scan.nextInt();
        onions = new int[S];
        onionSum = 0;
        maxVal = 0;
        for (int i = 0; i < S; i++) {
            onions[i] = scan.nextInt();
            onionSum += onions[i];
            if (onions[i] > maxVal) {
                maxVal = onions[i];
            }
        }
    }

    static void sol() {
        long start = 0;
        long end = maxVal;
        long ans = 0;
        while (start <= end) {
//            long tmp = 0;
            long cnt = 0;
            long mid = (start + end) / 2;
            if(mid==0) {
                break;
            }
            for (int onion : onions) {
                long countToAdd = onion / mid;
                cnt += countToAdd;
//                tmp += countToAdd * mid;
            }
            if (cnt < C) {
                end = mid - 1;
            } else {
//                ans = onionSum - tmp;
                start = mid + 1;
            }
        }
        System.out.println(onionSum - end * C);
    }

    static int S, C, maxVal;
    static int[] onions;
    static long onionSum;

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
