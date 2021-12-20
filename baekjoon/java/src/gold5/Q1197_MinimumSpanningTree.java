package gold5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

//https://www.acmicpc.net/problem/1197
public class Q1197_MinimumSpanningTree {
    private static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int v = Integer.parseInt(s[0]);
        int e = Integer.parseInt(s[1]);

        parent = new int[v + 1];
        for (int i = 0; i < v + 1; i++) {
            parent[i] = i;
        }

        List<List<Integer>> edges = new ArrayList<>();

        for (int i = 0; i < e; i++) {
            String[] x = br.readLine().split(" ");
            int a = Integer.parseInt(x[0]);
            int b = Integer.parseInt(x[1]);
            int c = Integer.parseInt(x[2]);
            edges.add(Arrays.asList(c, a, b));
        }

        edges.sort(Comparator.comparingInt(x -> x.get(0)));

        int result = 0;
        for (List<Integer> edge : edges) {
            int c = edge.get(0);
            int a = edge.get(1);
            int b = edge.get(2);
            if (findParent(a) != findParent((b))) {
                union(a, b);
                result += c;
            }
        }
        System.out.println(result);
    }

    private static int findParent(int x) {
        if (parent[x] != x) {
            parent[x] = findParent(parent[x]);
        }
        return parent[x];
    }

    private static void union(int x, int y) {
        x = findParent(x);
        y = findParent(y);
        if (x < y) {
            parent[y] = x;
            return;
        }
        parent[x] = y;
    }
}
