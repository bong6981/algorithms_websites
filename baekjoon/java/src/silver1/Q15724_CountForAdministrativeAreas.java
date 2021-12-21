package silver1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// https://www.acmicpc.net/problem/15724
public class Q15724_CountForAdministrativeAreas {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);

        int[][] graph = new int[n+1][m+1];
        for (int i = 1; i <= n; i++) {
            String[] s1 = br.readLine().split(" ");
            for (int j = 1; j <= m; j++) {
                graph[i][j] = graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1] + Integer.parseInt(s1[j-1]);
            }
        }

        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            String[] s1 = br.readLine().split(" ");
            int x1 = Integer.parseInt(s1[0]);
            int y1 = Integer.parseInt(s1[1]);
            int x2 = Integer.parseInt(s1[2]);
            int y2 = Integer.parseInt(s1[3]);
            System.out.println(graph[x2][y2] - graph[x1-1][y2] - graph[x2][y1-1] + graph[x1-1][y1-1]);
        }
    }
}
