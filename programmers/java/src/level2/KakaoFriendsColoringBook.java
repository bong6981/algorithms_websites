package level2;

import java.util.Arrays;

/*
https://programmers.co.kr/questions/18934
테스트 케이스는 통과하지만 채점 하면 실패하시는 분들은 int[][] picture 배열을 복사해서 코딩해보세요.

배열에서 같은 색상을 찾고, 같은 곳을 다시 방문하지 않기 위해
picture[i][j] = 0을 쓰는 방법과 visited 배열을 이용하는 방법이 있는데
저는 picture[i][j] = 0; 하는 식으로 코드를 짰는데 테스트 케이스만 통과하고 계속 실패해서
여러가지 시도를 해보다가 picture 배열을 복사하여 사용했더니 통과했습니다.
자세한 이유는 모르겠지만 원본 배열이 훼손되면 안되는 것 같습니다.
 */
public class KakaoFriendsColoringBook {
    // 상, 하, 좌, 우
    int[][] move = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int m, n;
    int[][] picture;
    int[][] visited;


    public static void main(String[] args) {
        KakaoFriendsColoringBook kfcb = new KakaoFriendsColoringBook();
        System.out.println(Arrays.toString(kfcb.solution(6, 4, new int[][]{{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}})));
//        System.out.println(Arrays.toString(kfcb.solution(2, 2, new int[][]{{1, 0}, {0, 0}})));
//        System.out.println(Arrays.toString(kfcb.solution(3, 2, new int[][]{{1, 1}, {2, 2}, {0, 0}})));
    }

    public int[] solution(int m, int n, int[][] picture) {
        this.m = m;
        this.n = n;
        this.picture = picture;
        this.visited = new int[m][n];
        for(int[] v : visited){
            Arrays.fill(v,0);
        }


        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if(picture[i][j] != 0 && visited[i][j] == 0) {
                    numberOfArea++;
                    int newMax =  checkColor(i, j, picture[i][j]);
                    System.out.println("========");
                    System.out.println(i + "," + j + "," + newMax);
                    System.out.println(Arrays.deepToString(picture));
                    if(maxSizeOfOneArea < newMax) {
                        maxSizeOfOneArea = newMax;
                    }
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    private int checkColor(int i, int j, int color) {
        int count = 1;
        visited[i][j] = 1;
        for (int[] md : move ) {
            int tempx = i + md[0];
            int tempy = j + md[1];
            if( 0 <= tempx && tempx < m && 0 <= tempy && tempy < n && picture[tempx][tempy] == color && visited[tempx][tempy] == 0) {
                count += checkColor(tempx, tempy, color);
            }
        }
        return count;

    }
}
