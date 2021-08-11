package level1;

import java.util.Arrays;

public class RemoveTheSmallestNum {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{1, 5, 2, 3, 4})));


    }

    public static int[] solution(int[] arr) {
        if (arr.length == 1) {
            return new int[]{-1};
        }

        return Arrays.stream(arr).filter(x -> x != Arrays.stream(arr).min().orElse(0)).toArray();
    }
}
