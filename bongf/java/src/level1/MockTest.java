package level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MockTest {
    public static void main(String[] args) {
        int[] answers = {1,2,3,4,5};
        solution(answers);
    }

    public static int[] solution(int[] answers) {
        int[] p1 = {1, 2, 3, 4, 5};
        int[] p2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] correct = {0, 0, 0};

        for( int i=0; i < answers.length; i++) {
            if( answers[i] == p1[i%5] ) {
                correct[0]++;
            }
            if( answers[i] == p2[i%8] ) {
                correct[1]++;
            }
            if( answers[i] == p3[i%10] ) {
                correct[2]++;
            }
        }

        int max = Arrays.stream(correct).max().getAsInt();
        List<Integer> answerL = new ArrayList();
        for ( int i = 0; i < 3; i++ ) {
            if(correct[i] == max ) {
                answerL.add(i+1);
            }
        }
        return answerL.stream().mapToInt(x-> x).toArray();
    }
}
