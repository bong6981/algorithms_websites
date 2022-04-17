package gold4;

import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Q1715_SortingCards {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        pq = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            pq.add(scan.nextInt());
        }
    }

    static int sol() {
        int ans = 0;
        while(pq.size() >= 2) {
            int p1 = pq.poll();
            int p2 = pq.poll();
            ans += (p1 + p2);
            pq.add(p1+p2);
        }
        return ans;
    }

    static int N;
    static PriorityQueue<Integer> pq;

    public static void main(String[] args) {
        input();
        System.out.println(sol());
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
