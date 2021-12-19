package gold5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//https://www.acmicpc.net/problem/15681
public class Q15681_TreeAndQuery {
    private static List<List<Integer>> graph;
    private static int[] numberOfPoint;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] initial = br.readLine().split(" ");
        int n = Integer.parseInt(initial[0]);
        int r = Integer.parseInt(initial[1]);
        int q = Integer.parseInt(initial[2]);

        graph = new ArrayList<>(n+1);
        for (int i = 0; i < n+1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < n-1; i++) {
            String[] s = br.readLine().split(" ");
            int x = Integer.parseInt(s[0]);
            int y = Integer.parseInt(s[1]);

            graph.get(x).add(y);
            graph.get(y).add(x);
        }

        numberOfPoint = new int[n+1];
        countPoint(r);

        for (int i = 0; i < q; i++) {
            System.out.println(numberOfPoint[Integer.parseInt(br.readLine())]);
        }
    }

    private static void countPoint(int root) {
        numberOfPoint[root] = 1; //부모를 일단 더이상 탐색하지 않게 0이 아니게 만들어줘야함
        for (Integer connectedNode : graph.get(root)) {
            if(numberOfPoint[connectedNode] == 0) {
                countPoint(connectedNode);
                numberOfPoint[root] += numberOfPoint[connectedNode];
            }
        }
    }
}
