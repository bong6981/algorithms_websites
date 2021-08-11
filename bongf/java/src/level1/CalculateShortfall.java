package level1;

import java.util.stream.LongStream;

public class CalculateShortfall {
    public static void main(String[] args) {
        System.out.println(solution(3,20,4));
    }

    public static long solution(int price, int money, int count) {
        long sum = LongStream.range(1, count + 1)
                .map(x -> x * price)
                .sum();

        return Math.max(sum - money, 0);
    }
}
