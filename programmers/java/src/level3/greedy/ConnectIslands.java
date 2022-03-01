package level3.greedy;
// https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class ConnectIslands {
    static class Edge {
        int x;
        int y;
        int c;

        public Edge(int x, int y, int c) {
            this.x = x;
            this.y = y;
            this.c = c;
        }
    }

    private static int[] parents;

    public static void main(String[] args) {
        ConnectIslands connectIslands = new ConnectIslands();
        System.out.println(connectIslands.solution(4, new int[][]{{0, 1, 1}, {0, 2, 2}, {1, 2, 5}, {1, 3, 1}, {2, 3, 8}}));
    }

    public int findP(int c) {
        if (parents[c] != c) {
            parents[c] = findP(parents[c]);
        }
        return parents[c];
    }

    public void union(int x, int y) {
        x = findP(x);
        y = findP(y);
        if (x < y) {
            parents[y] = x;
        } else {
            parents[x] = y;
        }
    }

    public int solution(int n, int[][] costs) {
        parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }

        List<Edge> edges = new ArrayList<>();
        for (int[] cost : costs) {
            edges.add(new Edge(cost[0], cost[1], cost[2]));
        }
        edges.sort(Comparator.comparing(edge -> edge.c));
        int answer = 0;
        for (Edge edge : edges) {
            if (findP(edge.x) != findP(edge.y)) {
                union(edge.x, edge.y);
                answer += edge.c;
            }
        }
        return answer;
    }
}
