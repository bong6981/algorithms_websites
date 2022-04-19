// https://www.acmicpc.net/problem/21606
package gold3;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Q21606_MorningWalk {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        inOut = new int[N+1];
        String next = scan.next();
        for (int i = 0; i < N; i++) {
            if(next.charAt(i) == '1') {
                inOut[i+1] = 1;
            }
        }
        graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < N-1; i++) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        visited = new boolean[N+1];
    }

    static int N;
    static int[] inOut;
    static List<List<Integer>> graph;
    static boolean[] visited;

    static void sol() {
        int ans = 0;
        for (int i = 1; i <= N; i++) {
            if(inOut[i] == 1) {
                for(int des:graph.get(i)) {
                    if(inOut[des] == 1) {
                        ans++;
                    }
                }
            } else {
                if(!visited[i]) {
                    int reuslt = dfs(i);
                    ans += reuslt * (reuslt - 1);
                }
            }
        }
        System.out.println(ans);
    }

    static int dfs(int start) {
        visited[start] = true;
        int ret = 0;
        for(int des: graph.get(start)) {
            if(!visited[des]) {
                if(inOut[des] == 1) {
                    ret++;
                } else {
                    ret += dfs(des);
                }
            }
        }
        return ret;
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
