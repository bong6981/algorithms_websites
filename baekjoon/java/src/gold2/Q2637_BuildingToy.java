//https://www.acmicpc.net/problem/2637
package gold2;

import java.io.*;
import java.util.*;

public class Q2637_BuildingToy {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        M = scan.nextInt();

        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<Info>();
        }

        indegree = new int[N + 1];
        while (M-- > 0) {
            int X = scan.nextInt();
            int Y = scan.nextInt();
            int K = scan.nextInt();
            indegree[Y]++;
            graph[X].add(new Info(Y, K));
        }

        cnt = new int[N+1];
    }

    static int N, M;
    static List<Info>[] graph;
    static int[] indegree, cnt;
    static List<Integer> basic = new ArrayList<>();

    static class Info {
        int part;
        int cnt;

        public Info(int part, int cnt) {
            this.part = part;
            this.cnt = cnt;
        }
    }

    static void sol() {
        cnt[N] = 1;
        Queue<Integer> q = new LinkedList<>();
        q.add(N);

        while(!q.isEmpty()) {
            int now = q.poll();
            if(graph[now].size() == 0) {
                basic.add(now);
            }
            for(Info info : graph[now]) {
                cnt[info.part] += cnt[now] * info.cnt;
                indegree[info.part]--;
                if(indegree[info.part] == 0) {
                    q.add(info.part);
                }
            }
        }

        Collections.sort(basic);
        for(int p: basic) {
            sb.append(p).append(" ").append(cnt[p]).append("\n");
        }
    }

    public static void main(String[] args) {
        input();
        sol();
        System.out.println(sb.toString());
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
