package level1;

import java.util.Arrays;
import java.util.stream.IntStream;

public class GetAverage {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4};
        int[] arr1 = {5,5};
        System.out.println(solution2(arr));
        System.out.println(solution2(arr1));
    }

    public static double solution(int[] arr) {
        return (double) IntStream.of(arr).sum() / arr.length;
    }

    // Array라면 평균값을 구하는 함수 average()가 있다.
    // average()의 리턴 값이 OptionalDouble이기 때문에 orElse를 넣어줘야 한다.
    public static double solution2(int[] array) {
        return Arrays.stream(array).average().orElse(0);
    }
}
