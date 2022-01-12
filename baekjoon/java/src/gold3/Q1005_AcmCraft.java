package gold3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// https://www.acmicpc.net/problem/1005
public class Q1005_AcmCraft {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCnt = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCnt; i++) {
            List<Integer> time = new ArrayList<>();
            time.add(0);
            String[] meta = br.readLine().split(" ");
            int n = Integer.parseInt(meta[0]);
            int k = Integer.parseInt(meta[1]);
            String[] timeStrings = br.readLine().split(" ");
            for (String timeString : timeStrings) {
                time.add(Integer.parseInt(timeString));
            }

            List<List<Integer>> board = new ArrayList<>();
            int[] indegree = new int[n+1];
            for (int j = 0; j <= n; j++) {
                board.add(new ArrayList<>());
            }
            for (int j = 0; j < k; j++) {
                String[] order = br.readLine().split(" ");
                int later = Integer.parseInt(order[1]);
                board.get(Integer.parseInt(order[0])).add(later);
                indegree[later]++;
            }

            Integer[] result = time.toArray(new Integer[n+1]);
            int w = Integer.parseInt(br.readLine());
            Queue<Integer> queue = new LinkedList<>();
            for (int j = 1; j <= n; j++) {
                if(indegree[j] == 0) {
                    queue.add(j);
                }
            }
            while(!queue.isEmpty()) {
                int now = queue.poll();
                for (int to : board.get(now)) {
                    result[to] = Math.max(result[to], result[now] + time.get(to));
                    indegree[to]--;
                    if(indegree[to] == 0) {
                        queue.add(to);
                    }
                }
            }

            System.out.println(result[w]);
        }
    }
}
