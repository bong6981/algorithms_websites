package level1;

import java.util.Arrays;
import java.util.stream.IntStream;

public class XIntervalNNumber {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(2,5)));
        System.out.println(Arrays.toString(solution(4,3)));
        System.out.println(Arrays.toString(solution(-4, 2)));
    }

    public static long[] solution(int x, int n) {
        long[] answer = new long[n];
        IntStream.range(1, n+1).forEach( i -> answer[i-1] = (long) x * i);
        return answer;
    }
}
