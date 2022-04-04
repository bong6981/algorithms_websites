package silver3;

import java.io.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Q7795_EatOrEaten {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static Integer[] A, B;

    static void input() {
        N = scan.nextInt();
        M = scan.nextInt();
        A = new Integer[N];
        B = new Integer[M];
        for (int i = 0; i < N; i++) {
            A[i] = scan.nextInt();
        }
        for (int i = 0; i < M; i++) {
            B[i] = scan.nextInt();
        }
    }

    static int lower_bound(Integer refer, Integer end) {
        Integer start = 0;
        Integer ans = -1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (B[mid] >= refer) {
                end = mid - 1;
            } else {
                ans = mid;
                start = mid + 1;
            }
        }
        return ans;
    }

    static void sol() {
        Arrays.sort(B);
        Arrays.sort(A, Collections.reverseOrder());
        int ans = 0;
        int lastIdx = M - 1;
        for (Integer e : A) {
            lastIdx = lower_bound(e, lastIdx);
            if (lastIdx == -1) {
                break;
            }
            ans += lastIdx + 1;
        }
        System.out.println(ans);
    }


    public static void main(String[] args) {
        int T = scan.nextInt();
        for (int t = 1; t <= T; t++) {
            input();
            sol();
        }
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

        Integer nextInt() {
            return Integer.parseInt(next());
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
