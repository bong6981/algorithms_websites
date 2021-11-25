package silver1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

//https://www.acmicpc.net/problem/21608
public class Q21608_SharksElementarySchool {
    // 파이썬 랭커 jh05013 풀이 응용
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];
        List<List<Integer>> likes = new ArrayList<>((int) (Math.pow(n, 2) + 1));
        for (int i = 0; i <= Math.pow(n, 2); i++) {
            likes.add(new ArrayList<>());
        }
        for (int k = 0; k < Math.pow(n, 2); k++) {
            List<Integer> data = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).collect(Collectors.toList());
            int num = data.get(0);
            data = data.subList(1, data.size());
            likes.set(num, data);
            Integer[] ans = {-1, -1, -1, -1};
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] != 0) {
                        continue;
                    }
                    int like = 0;
                    int empty = 0;
                    for (int[] move : new int[][]{{i - 1, j}, {i, j + 1}, {i + 1, j}, {i, j - 1}}) {
                        int nx = move[0];
                        int ny = move[1];
                        if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                            if (board[nx][ny] == 0) {
                                empty++;
                            }
                            if (data.contains(board[nx][ny])) {
                                like++;
                            }
                        }
                    }
                    Integer[] now = new Integer[]{like, empty, i, j};
                    List<Integer[]> temp = new ArrayList<>();
                    temp.add(ans);
                    temp.add(now);
                    temp.sort((a, b) -> {
                        if (a[0] == b[0]) {
                            if (a[1] == b[1]) {
                                if (a[2] == b[2]) {
                                    return a[3] - b[3];
                                }
                                return a[2] - b[2];
                            }
                            return b[1] - a[1];
                        }
                        return b[0] - a[0];
                    });
                    ans = temp.get(0);
                }
            }
            board[ans[2]][ans[3]] = num;
        }

        int answer = 0;
        int[] point = new int[]{0, 1, 10, 100, 1000};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                List<Integer> like = likes.get(board[i][j]);
                int lp = 0;
                for (int[] move : new int[][]{{i - 1, j}, {i, j + 1}, {i + 1, j}, {i, j - 1}}) {
                    int nx = move[0];
                    int ny = move[1];
                    if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                        if (like.contains(board[nx][ny])) {
                            lp++;
                        }
                    }
                }
                answer += point[lp];
            }
        }
        System.out.println(answer);
    }
}
