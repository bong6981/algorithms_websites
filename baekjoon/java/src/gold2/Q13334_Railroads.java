package gold2;

import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Q13334_Railroads {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class Route {
        int start, end;

        public Route(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    static void input() {
        N = scan.nextInt();
        routes = new Route[N];
        for (int i = 0; i < N; i++) {
            int x = scan.nextInt();
            int y = scan.nextInt();
            if (x < y) {
                routes[i] = new Route(x, y);
            } else {
                routes[i] = new Route(y, x);
            }
        }
        pq = new PriorityQueue<>(startComp);
        D = scan.nextInt();
    }

    static int N, D;
    static Route[] routes;
    static PriorityQueue<Route> pq;
    static Comparator<Route> startComp = new Comparator<Route>() {
        @Override
        public int compare(Route o1, Route o2) {
            return o1.start - o2.start;
        }
    };

    static int sol() {
        Arrays.sort(routes, Comparator.comparing(x -> x.end));
        int ans = 0;
        int cnt = 0;
        for (Route route : routes) {
            if (route.end - route.start > D) {
                continue;
            }

            while (!pq.isEmpty() && route.end - pq.peek().start > D) {
                pq.poll();
                cnt--;
            }

            pq.add(route);
            cnt++;
            ans = Math.max(ans, cnt);
        }
        return ans;
    }

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
