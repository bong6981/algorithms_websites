package gold5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

// https://www.acmicpc.net/submit/16234
public class Q16234_PopulationMovement {
    public static int[][] moves = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    public static int n;
    public static int l;
    public static int r;
    public static Queue<Integer[]> search;
    public static int[][] visited;
    public static int[][] countries;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] info = br.readLine().split(" ");
        n = Integer.parseInt(info[0]);
        l = Integer.parseInt(info[1]);
        r = Integer.parseInt(info[2]);

        countries = new int[n][n];
        visited = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                countries[i][j] = Integer.parseInt(input[j]);
            }
        }

        int t = 0;
        while(true) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    visited[i][j] = -1;
                }
            }

            int cnt = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if(visited[i][j] == -1) {
                        cnt += move(i, j);
                    }
                }
            }
            if(cnt == 0) {
                break;
            }
            t++;
        }
        System.out.println(t);
    }

    public static int move(int x, int y) {
        Queue<Integer[]> q = new LinkedList<>();
        Integer[] in = new Integer[]{x, y};
        q.add(new Integer[]{x, y});
        List<Integer[]> union = new ArrayList<>();
        union.add(new Integer[]{x, y});
        int sum = countries[x][y];
        visited[x][y] = 1;
        while(!q.isEmpty()) {
            Integer[] poll = q.poll();
            int i = poll[0];
            int j = poll[1];
            for (int[] m : moves) {
                int ni = i + m[0];
                int nj = j + m[1];
                if( 0<= ni && ni < n && 0 <= nj && nj < n) {
                    if(visited[ni][nj] == -1) {
                        int diff = Math.abs(countries[i][j] - countries[ni][nj]);
                        if(l<= diff && diff <= r) {
                            sum += countries[ni][nj];
                            visited[ni][nj] = 1;
                            q.add(new Integer[]{ni, nj});
                            union.add(new Integer[]{ni, nj});
                        }
                    }
                }
            }
        }

        if(union.size() > 1) {
            int average = sum / union.size();
            for (Integer[] unit : union) {
                int nowx = unit[0];
                int nowy = unit[1];
                countries[nowx][nowy] = average;
            }
            return 1;
        }
        return 0;
    }
}
