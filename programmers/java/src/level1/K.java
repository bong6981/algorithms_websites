package level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class K {
    public static void main(String[] args) {
        int[] array = {1, 5, 2, 6, 3, 7, 4};
        int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
        System.out.println(Arrays.toString(solution(array, commands)));
    }

    public static int[] solution(int[] array, int[][] commands) {

        List<Integer> answerList = new ArrayList();
        for (int[] command : commands) {
            int start = command[0];
            int end = command[1];
            List<Integer> temp = new ArrayList();
            for (int i = (start-1); i <= (end-1); i++) {
                temp.add(array[i]);
            }
            temp.sort(null);
            answerList.add(temp.get(command[2]-1));
        }
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }
        return answer;
    }
}
