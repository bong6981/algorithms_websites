package silver3.Q2805;

import java.io.*;
import java.util.StringTokenizer;

public class CuttingTrees {
    static FastReader scan = new FastReader();

    static void input() {
        N = scan.nextInt();
        M = scan.nextLong();
        trees = new long[N];
        max_tree = 0;
        for (int i = 0; i < N; i++) {
            trees[i] = scan.nextLong();
            max_tree = Math.max(max_tree, trees[i]);
        }
    }

    static int N;
    static long M;
    static long[] trees;
    static long max_tree;

    static void sol() {
        long start = 0L;
        long end = max_tree;
        long ans = 0L;

        while(start <= end) {
            long mid = (start + end) / 2;

            long total = 0;
            for(long tree : trees) {
                long left = tree - mid;
                if(left < 0) {
                    continue;
                }
                total += left;
            }

            if(total >= M) {
                ans = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        System.out.println(ans);
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
