package level1;

import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StringDesc {
    public static void main(String[] args) {
        System.out.println(solution("Zbcdefg"));
    }

    public static String solution(String s) {
        return Stream.of(s.split("")).sorted(Comparator.reverseOrder()).collect(Collectors.joining());
    }

    public static String solution2(String s) {
        char[] sor = s.toCharArray();
        Arrays.sort(sor);
        // Arrays.sort(array, Collections.reverseOrder());으로 정렬하기 위해서는 char가 아닌 Character가 필요해서 StringBuilder로 역순 정렬한다.
        return new StringBuilder(new String(sor)).reverse().toString();
    }
}
