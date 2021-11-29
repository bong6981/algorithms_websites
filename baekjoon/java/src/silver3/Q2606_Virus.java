package silver3;

import java.util.*;

public class Q2606_Virus {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
        int m = sc.nextInt();
        List<List<Integer>> board = new ArrayList<>(c+1);
        for (int i = 0; i <= c; i++) {
            board.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            board.get(x).add(y);
            board.get(y).add(x);
        }

        int[] visited = new int[c+1];
        visited[1] = 1;
        Queue<Integer> q = new LinkedList<>();
        q.offer(1);
        int cnt = 0;

        while(!q.isEmpty()) {
            Integer poll = q.poll();
            cnt++;
            for (Integer integer : board.get(poll)) {
                if(visited[integer] == 0) {
                    visited[integer] = 1;
                    q.offer(integer);
                }
            }
        }
        System.out.println(cnt-1);
    }
}
