package level3.kakao.kakao2022;

import java.util.Arrays;

public class UndestroyedBuilding {
    public static void main(String[] args) {
//        String s = "[[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]";
//        String s1 = "[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]";
//        s = s.replaceAll("\\[", "{").replaceAll("]", "}");
//        s1 = s1.replaceAll("\\[", "{").replaceAll("]", "}");
//        System.out.println(s); // {{5,5,5,5,5},{5,5,5,5,5},{5,5,5,5,5},{5,5,5,5,5}}
//        System.out.println(s1); // {{1,0,0,3,4,4},{1,2,0,2,3,2},{2,1,0,3,1,2},{1,0,1,3,3,1}}
        UndestroyedBuilding ub = new UndestroyedBuilding();
        System.out.println(ub.solution(new int[][]{{5, 5, 5, 5, 5}, {5, 5, 5, 5, 5}, {5, 5, 5, 5, 5}, {5, 5, 5, 5, 5}}, new int[][]{{1, 0, 0, 3, 4, 4}, {1, 2, 0, 2, 3, 2}, {2, 1, 0, 3, 1, 2}, {1, 0, 1, 3, 3, 1}}));
    }

    public int solution(int[][] board, int[][] skill) {
        int[][] acc = new int[board.length + 1][board[0].length + 1];
        for (int[] s : skill) {
            int op = 1;
            if (s[0] == 1) {
                op = -1;
            }

            acc[s[1]][s[2]] += op * s[5];
            acc[s[1]][s[4]+1] -= op * s[5];
            acc[s[3]+1][s[2]] -= op * s[5];
            acc[s[3]+1][s[4]+1] += op * s[5];
        }
        int ans = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 1; j < board[0].length; j++) {
                acc[i][j] += acc[i][j - 1];
            }
        }

        for (int i = 1; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                acc[i][j] += acc[i - 1][j];
            }
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] + acc[i][j] > 0) {
                    ans += 1;
                }
                board[i][j] = acc[i][j];
            }
        }
        return ans;
    }
}
