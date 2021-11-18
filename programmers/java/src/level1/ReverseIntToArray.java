package level1;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ReverseIntToArray {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(123)));
        System.out.println(Arrays.toString(solution2(123)));
    }

    //StringBuilder에도 reverse() 있다
    public static int[] solution(long n) {
        List<String> strings = Arrays.asList(String.valueOf(n).split(""));
        Collections.reverse(strings);
        return strings.stream()
                .mapToInt(Integer::parseInt)
                .toArray();
    }

    public static int[] solution2(long n) {
        // String s = ""+n; 로도 string으로 변환 가능
        int[] answer = new int[String.valueOf(n).length()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = (int) (n % 10);
            n /= 10;
        }
        return answer;
    }
}

