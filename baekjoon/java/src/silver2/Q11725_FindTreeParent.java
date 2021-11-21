package silver2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Q11725_FindTreeParent {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<List<Integer>> board = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            board.add(new ArrayList<>());
        }
        for (int i = 0; i < n-1; i++) {
            Integer[] input = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);
            int x = input[0];
            int y = input[1];
            board.get(x).add(y);
            board.get(y).add(x);
        }

        Queue<Integer> q = new LinkedList<>();
        int[] parent = new int[n+1];
        for (Integer integer : board.get(1)) {
            q.add(integer);
            parent[integer] = 1;
        }
        while(!q.isEmpty()) {
            int x = q.poll();
            for (Integer integer : board.get(x)) {
                if(parent[x] != integer) {
                    parent[integer] = x;
                    q.offer(integer);
                }
            }
        }
        for (int i = 2; i <= n; i++) {
            System.out.println(parent[i]);
        }
    }
}
