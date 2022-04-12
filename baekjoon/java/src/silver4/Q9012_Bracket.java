package silver4;

import java.io.*;
import java.util.StringTokenizer;

public class Q9012_Bracket {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        s = scan.nextLine();
    }

    static String s;

    static boolean sol() {
        int cnt = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                cnt++;
            } else {
                cnt--;
            }

            if (cnt < 0) {
                return false;
            }
        }
        if (cnt != 0) {
            return false;
        }
        return true;
    }

    static void print(boolean result) {
        if (result) {
            System.out.println("YES");
            return;
        }
        System.out.println("NO");
    }

    public static void main(String[] args) {
        int t = scan.nextInt();
        for (int i = 0; i < t; i++) {
            input();
            print(sol());
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

