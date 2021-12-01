package gold5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// https://www.acmicpc.net/submit/16234
// 파이썬과 똑같은 방식으로 풀었지만 실패
public class Q16234_PopulationMovement_Fail {
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
        search = new LinkedList<>();
        visited = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                countries[i][j] = Integer.parseInt(input[j]);
                search.offer(new Integer[]{i, j});
                visited[i][j] = -1;
            }
        }

        int t = 0;
        while(true) {
            int cnt = 0;
            for (int i = 0; i < search.size(); i++) {
                Integer[] poll = search.poll();
                int x = poll[0];
                int y = poll[1];
                if(visited[x][y] != t) {
                    cnt += move(x, y, t);
                }
            }
            if(cnt == 0) {
                break;
            }
            t++;
        }
        System.out.println(t);
    }

    public static int move(int x, int y, int t) {
        Queue<Integer[]> q = new LinkedList<>();
        Integer[] in = new Integer[]{x, y};
        q.add(in);
        List<Integer[]> union = new ArrayList<>();
        union.add(in);
        int sum = countries[x][y];
        visited[x][y] = t;
        while(!q.isEmpty()) {
            Integer[] poll = q.poll();
            int i = poll[0];
            int j = poll[1];
            for (int[] m : moves) {
                int ni = i + m[0];
                int nj = j + m[1];
                if( 0<= ni && ni < n && 0 <= nj && nj < n) {
                    if(visited[ni][nj] != t) {
                        int diff = Math.abs(countries[i][j] - countries[ni][nj]);
                        if(l<= diff && diff <= r) {
                            sum += countries[ni][nj];
                            visited[ni][nj] = t;
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
                search.offer(new Integer[]{nowx, nowy});
            }
            return 1;
        }
        return 0;
    }
}
