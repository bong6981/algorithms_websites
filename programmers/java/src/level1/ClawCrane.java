package level1;

import java.util.ArrayList;
import java.util.List;

public class ClawCrane {
    public static void main(String[] args) {
        int[][] board = {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
        int[] moves = {1,5,3,5,1,2,1,4};
        System.out.println(solution(board, moves));
    }

    public static int solution(int[][] board, int[] moves) {
        List<Integer> resultList = new ArrayList<Integer>();
        int count = 0;
        for( int column : moves) {
            int index = column -1;
            for(int j=0; j<board.length; j++) {
                if(board[j][index] != 0) {
                    if(resultList.size() != 0 && resultList.get(resultList.size()-1) == board[j][index]) {
                        count += 2;
                        resultList.remove(resultList.size() -1);
                        board[j][index] = 0;
                        break;
                    } else {
                        resultList.add(board[j][index]);
                        board[j][index] = 0;
                        break;
                    }
                }
            }
        }

        int answer = count;
        return answer;
    }
}
