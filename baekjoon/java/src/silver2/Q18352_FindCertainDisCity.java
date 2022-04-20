// https://www.acmicpc.net/problem/18352
package silver2;

import java.io.*;
import java.util.*;

public class Q18352_FindCertainDisCity {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        M = scan.nextInt();
        K = scan.nextInt();
        X = scan.nextInt();
        graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        distance = new int[N+1];
        Arrays.fill(distance, -1);

        for (int i = 0; i < M; i++) {
            int A = scan.nextInt();
            int B = scan.nextInt();
            graph.get(A).add(B);
        }
    }

    static class Info {
        int point;
        int cost;

        public Info(int point, int cost) {
            this.point = point;
            this.cost = cost;
        }
    }

    static int N, M, K, X;
    static List<List<Integer>> graph;
    static int[] distance;

    static void sol() {
        Queue<Info> q = new LinkedList<>();
        q.add(new Info(X, 0));
        distance[X] = 0;
        while (!q.isEmpty()) {
            Info now = q.poll();
            for(int dest : graph.get(now.point)) {
                if(distance[dest] == -1) {
                    distance[dest] = now.cost + 1;
                    q.add(new Info(dest, distance[dest]));
                }
            }
        }

        boolean found = false;
        for (int i = 1; i < distance.length; i++) {
            if(K == distance[i]) {
                sb.append(i).append("\n");
                found = true;
            }
        }
        if(!found) {
            sb.append(-1);
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



