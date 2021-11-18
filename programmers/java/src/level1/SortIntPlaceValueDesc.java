package level1;

import java.util.Arrays;
import java.util.Collections;

public class SortIntPlaceValueDesc {
    public static void main(String[] args) {
        System.out.println(solution(8000000000L));
    }

    public static long solution(long n) {
        String[] split = ("" + n).split("");
        Arrays.sort(split, Collections.reverseOrder());
        return (long) Long.parseLong(String.join("", split));
    }
}
