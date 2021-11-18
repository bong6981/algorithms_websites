package level2;

import java.util.Arrays;
import java.util.stream.Collectors;

public class JadenCase {
    public static void main(String[] args) {
        System.out.println(solution(" 3people   unFollowed me "));
        System.out.println(solution("  "));
    }

    public static String solution(String s) {
        return Arrays.stream(s.split(" ", -1))
                .map(x -> x.equals("") ? x : x.substring(0, 1).toUpperCase() + x.substring(1).toLowerCase())
                .collect(Collectors.joining(" "));
    }
}
