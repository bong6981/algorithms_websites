package level1;

import java.util.stream.IntStream;

public class SumOfDivisor {
    public static void main(String[] args) {
        System.out.println(solution(12));
        System.out.println(solution(5));
        System.out.println(solution(4));
    }

    public static int solution(int n) {
        int answer = IntStream.range(1, (int) Math.sqrt(n) + 1)
                .filter(x -> n % x == 0)
                .reduce(0, (sum, x) -> sum + (x + n / x));

        if ((int) Math.sqrt(n) == Math.sqrt(n)) {
            answer -= Math.sqrt(n);
        }
        return answer;
    }
}
