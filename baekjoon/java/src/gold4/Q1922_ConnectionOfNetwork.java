package gold4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;
import java.util.stream.Stream;

// https://www.acmicpc.net/problem/1922
public class Q1922_ConnectionOfNetwork {
    private static int[] parents;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        parents = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parents[i] = i;
        }
        List<List<Integer>> connections = new ArrayList<>();
        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            connections.add(Stream.of(c, a, b).collect(Collectors.toList()));
        }

        connections.sort(Comparator.comparingInt(conn -> conn.get(0)));
        int total = 0;
        for (List<Integer> connection : connections) {
            int x = connection.get(1);
            int y = connection.get(2);
            if (findParent(x) != findParent(y)) {
                union(x, y);
                total += connection.get(0);
            }
        }
        System.out.println(total);
    }

    private static int findParent(int x) {
        if (parents[x] != x) {
            parents[x] = findParent(parents[x]);
        }
        return parents[x];
    }

    private static void union(int x, int y) {
        x = findParent(x);
        y = findParent(y);
        if (x == y) {
            return;
        }
        if (x < y) {
            parents[y] = x;
            return;
        }
        parents[x] = y;
    }
}
