package level2.kakao.kakao2018;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.omg.CORBA.NO_IMPLEMENT;

// https://programmers.co.kr/learn/courses/30/lessons/17679
// 카카오 블라인드 2018
public class Friends4Block {
    public static void main(String[] args) {
        Friends4Block friends4Block = new Friends4Block();
        System.out.println(friends4Block.solution(4, 5, 	new String[]{"CCBDE", "AAADE", "AAABF", "CCBBF"}));
    }
    public int solution(int m, int n, String[] board) {
        char[][] graph = new char[m][n];
        for (int i = 0; i < m; i++) {
            char[] chars = board[i].toCharArray();
            for (int j = 0; j < n; j++) {
                graph[i][j] = chars[j];
            }
        }
        int cnt = 0;
        int[][] moves = new int[][]{{0,1}, {1,0}, {1,1}};
        while(true) {
            List<Integer[]> toDelete = new ArrayList<>();
            for (int i = 0; i < m-1; i++) {
                for (int j = 0; j < n-1; j++) {
                    if(graph[i][j] != '팡') {
                        char c = graph[i][j];
                        boolean square = true;
                        for (int[] move : moves) {
                            int ni = i + move[0];
                            int nj = j + move[1];
                            if(graph[ni][nj] != c) {
                                square = false;
                                break;
                            }
                        }
                        if(square) {
                            toDelete.add(new Integer[]{i, j});
                        }
                    }
                }
            }

            if(toDelete.size() == 0) {
                break;
            }

            for (Integer[] deleteStart : toDelete) {
                int x = deleteStart[0];
                int y = deleteStart[1];
                if(graph[x][y] != '팡') {
                    graph[x][y] = '팡';
                    cnt++;
                }
                for (int[] move : moves) {
                    int nx = x + move[0];
                    int ny = y + move[1];
                    if(graph[nx][ny] != '팡') {
                        cnt++;
                        graph[nx][ny] = '팡';
                    };
                }
            }

            List<Integer> onlyPangLeft = new ArrayList<>();
            for (int i = m-1; i >= 0; i--) {
                for (int j = 0; j < n; j++) {
                    if(!onlyPangLeft.contains(j)) {
                        if(graph[i][j] == '팡') {
                            boolean empty = true;
                            for (int k = i-1; k >= 0; k--) {
                                if(graph[k][j] != '팡') {
                                    graph[i][j] = graph[k][j];
                                    graph[k][j] = '팡';
                                    empty = false;
                                    break;
                                }
                            }
                            if(empty) {
                                onlyPangLeft.add(j);
                            }
                        }
                    }
                }
            }
        }
        return cnt;
    }
}
