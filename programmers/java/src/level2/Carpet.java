package level2;

import java.util.Arrays;

public class Carpet {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(10,2)));
    }

    public static int[] solution(int brown, int yellow) {
        for(int i=1; i< (int)Math.sqrt(yellow) + 1; i++) {
            if( yellow % i == 0 ) {
                if( 2 * ( i + yellow / i ) == brown - 4 ) {
                    return new int[]{yellow/i + 2, i+2};
                }
            }
        }
        return null;
    }

    // https://cjlee38.github.io/problem-solving/problem_solving_9
    public static int[] solution2(int brown, int red) {
        int a = (brown+4)/2;
        int b = red+2*a-4;
        int[] answer = {(int)(a+Math.sqrt(a*a-4*b))/2,(int)(a-Math.sqrt(a*a-4*b))/2};
        return answer;
    }
}
