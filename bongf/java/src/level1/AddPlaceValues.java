package level1;

import java.util.Arrays;

public class AddPlaceValues {
    public static void main(String[] args) {
        System.out.println(solution(123));
        System.out.println(solution(987));
    }

    public static int solution(int n) {
        return Arrays.stream(String.valueOf(n).split(""))
                .map(Integer::parseInt)
                .reduce(0, Integer::sum);
    }
}
