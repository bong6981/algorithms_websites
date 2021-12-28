package level2.kakao.kakao2021;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

// https://programmers.co.kr/learn/courses/30/lessons/81302
public class CheckDistancing {
    public static void main(String[] args) {
        CheckDistancing checkDistancing = new CheckDistancing();
//        String input = "[[\"POOOP\", \"OXXOX\", \"OPXPX\", \"OOXOX\", \"POXXP\"], [\"POOPX\", \"OXPXP\", \"PXXXO\", \"OXXXO\", \"OOOPP\"], [\"PXOPX\", \"OXOXP\", \"OXPOX\", \"OXXOP\", \"PXPOX\"], [\"OOOXX\", \"XOOOX\", \"OOOXX\", \"OXOOX\", \"OOOOO\"], [\"PXPXP\", \"XPXPX\", \"PXPXP\", \"XPXPX\", \"PXPXP\"]]";
//        input = input.replaceAll("\\[", "{").replaceAll("]", "}");
//        System.out.println(input);
        System.out.println(Arrays.toString(checkDistancing.solution(new String[][]{{"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"}, {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"}, {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"}, {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"}, {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}})));
    }

    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        Arrays.fill(answer, -1);
        for (int i = 0; i < 5; i++) {
            String[] placeString = places[i];
            String[][] place = new String[5][5];
            for (int j = 0; j < 5; j++) {
                String string = placeString[j];
                String[] room = string.split("");
                place[j] = room;
            }

            loop1 :for (int j = 0; j < 5; j++) {
                for (int k = 0; k < 5; k++) {
                    if(place[j][k].equals("P")) {
                        if(!check(j, k, place)) {
                            answer[i] = 0;
                            break  loop1;
                        };
                    }
                }
            }
            if(answer[i] == -1) {
                answer[i] = 1;
            }
        }
        return answer;
    }

    private boolean check(int i, int j, String[][] place) {
        int[][] moves = new int[][]{{-1, 0}, {1, 0}, {0,-1}, {0, 1}};
        Queue<Integer[]> queue = new LinkedList<>();
        queue.add(new Integer[]{i, j, 0});
        boolean[][] visited = new boolean[5][5];

        while(!queue.isEmpty()) {
            Integer[] poll = queue.poll();
            int x = poll[0];
            int y = poll[1];
            int d = poll[2];
            visited[x][y] = true;
            for (int[] move : moves) {
                int nx = x + move[0];
                int ny = y + move[1];
                int nd = d + 1;
                if( 0<= nx && nx < 5 && 0 <= ny && ny < 5) {
                    if(!visited[nx][ny]) {
                        visited[nx][ny] = true;
                        if(place[nx][ny].equals("P")) {
                            return false;
                        }
                        if(place[nx][ny].equals("O")) {
                            if(nd == 1) {
                                queue.offer(new Integer[]{nx, ny, nd});
                            }
                        }
                    }
                }
            }

        }
        return true;
    }
}

// 프로그래머스에서 가져온 답, DFS를 이용
// https://programmers.co.kr/learn/courses/30/lessons/81302/solution_groups?language=java
 class SolutionProgrammers {
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static boolean[][] visit;

    static int[] answer;

    public void dfs(int num, int x, int y, int count, String[] places){
        if (count > 2) return;
        if (count > 0 && count <= 2 && places[x].charAt(y) == 'P'){
            //2칸 범위내에 다른 응시자가 있을 경우 거리두기 미준수로 0처리
            answer[num] = 0;
            return;
        }
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            //배열 범위 밖으로 초과하는지 여부 검사, 파티션으로 분리되어 있는 경우 상관 없음.
            if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && places[nx].charAt(ny) != 'X') {
                if (visit[nx][ny]) continue; //이미 방문한 곳일 경우 생략
                visit[nx][ny] = true;
                dfs(num, nx, ny, count + 1, places);
                visit[nx][ny] = false;
            }
        }
    }

    public int[] solution(String[][] places) {
        answer = new int[places.length];
        for (int i = 0; i < places.length; i++) {
            answer[i] = 1;
        }

        for (int i = 0; i < places.length; i++) {
            visit = new boolean[5][5];
            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < 5; k++) {
                    if (places[i][j].charAt(k) == 'P'){
                        visit[j][k] = true;
                        dfs(i, j, k, 0, places[i]);
                        visit[j][k] = false;
                    }
                }
            }
        }
        return answer;
    }
}
