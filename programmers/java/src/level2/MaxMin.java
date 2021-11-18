package level2;

import java.util.Arrays;

public class MaxMin {
    public static void main(String[] args) {
        System.out.println(solution("1 2 3 4"));
    }

    public static String solution(String s) {
        Integer[] ints = Arrays.stream(s.split(" "))
                .map(Integer::valueOf)
                .sorted()
                .toArray(Integer[]::new);

        StringBuilder sb = new StringBuilder();
        sb.append(ints[0]);
        sb.append(" ");
        sb.append(ints[ints.length - 1]);
        return sb.toString();
    }
}
