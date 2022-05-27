package gold4;

import java.io.*;
import java.util.StringTokenizer;

public class Q1806_PartialSum {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        S = scan.nextInt();
        arr = new int[N+1];
        int num = 0;
        for(int i=1; i<=N; i++) {
            num += scan.nextInt();
            arr[i]  = num;
        }
    }

    static int N, S;
    static int[] arr;

    static int find(int start) {
        int from = start;
        int end = N;
        int ans = N+1;
        while(start <= end) {
            int mid = (start + end) / 2;
            if(arr[mid] - arr[from-1] >= S) {
                ans = mid - from + 1;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return ans;
    }

    static void sol() {
        int ans = N+1;
        int start = 1;
        for(int i=1; i<=N; i++) {
            int ret = find(Math.max(i, start));
            start = ret;
            ans = Math.min(ans, ret);
            if(ans==N+1) {
                break;
            }
        }
        if(ans == N+1) {
            System.out.println(0);
        } else {
            System.out.println(ans);
        }

    }

    public static void main(String[] args) {
        input();
//        sol();
        sol2();
    }

    static void input2() {
        N = scan.nextInt();
        S = scan.nextInt();
        arr = new int[N+1];
        for(int i=1; i<=N; i++) {
            arr[i] = scan.nextInt();
        }
    }


    private static void sol2() {
        input2();
        int r = 0, sum = 0, ans = N+1;
        for (int l = 1; l <= N; l++) {
            sum -= arr[l-1];

            while(r+1 <= N && sum < S) {
                sum += arr[r];
            }

            if(sum >= S) {
                ans = Math.min(ans, r-l+1);
            }

        }

        if(ans==N+1) {
            ans = 0;
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
            while(st==null || !st.hasMoreElements()) {
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
