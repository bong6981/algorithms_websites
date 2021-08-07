package level1;

import java.util.stream.Stream;

public class HarshadNumber {
    public static void main(String[] args) {
        System.out.println(solution(10));
        System.out.println(solution(12));
        System.out.println(solution(11));
        System.out.println(solution(13));

    }

    public static boolean solution(int x) {
        return x % Stream.of(String.valueOf(x)
                .split("")).map(Integer::valueOf)
                .reduce(0, Integer::sum) == 0;
    }
}
