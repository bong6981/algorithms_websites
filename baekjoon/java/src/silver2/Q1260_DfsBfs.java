package silver2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

// https://www.acmicpc.net/problem/126
public class Q1260_DfsBfs {
    private static List<List<Integer>> board;
    private static int[] visited1;
    private static int[] visited2;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] meta = br.readLine().split(" ");
        int n  = Integer.parseInt(meta[0]);
        int m  = Integer.parseInt(meta[1]);
        int v  = Integer.parseInt(meta[2]);

        board = new ArrayList<>();
        for (int i = 0; i < n+1; i++) {
            board.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            String[] nodes = br.readLine().split(" ");
            Integer node1 = Integer.parseInt(nodes[0]);
            Integer node2 = Integer.parseInt(nodes[1]);
            board.get(node1).add(node2);
            board.get(node2).add(node1);
        }

        for (List<Integer> list : board) {
            Collections.sort(list);
        }

        visited1 = new int[n+1];
        visited2 = new int[n+1];
        visited1[v] = 1;
        visited2[v] = 1;

        List<Integer> answerForDfs = new ArrayList<>();
        answerForDfs.add(v);
        System.out.println(dfs(answerForDfs, v).stream().map(x-> x + "").collect(Collectors.joining(" ")));
        System.out.println(bfs(v).stream().map(x -> x + "").collect(Collectors.joining(" ")));
    }

    private static List<Integer> bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        List<Integer> answer = new ArrayList<>();

        while(!q.isEmpty()) {
            Integer now = q.poll();
            answer.add(now);
            for (Integer item : board.get(now)) {
                if( visited1[item] == 0) {
                    q.offer(item);
                    visited1[item] = 1;
                }
            }
        }
        return answer;
    }

    private static List<Integer> dfs(List<Integer> answer, int idx) {
        for (Integer item : board.get(idx)) {
            if(visited2[item] == 0) {
                visited2[item] = 1;
                answer.add(item);
                dfs(answer, item);
            }
        }
        return answer;
    }
}
