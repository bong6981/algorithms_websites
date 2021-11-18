package level1;

import java.util.Arrays;

public class DivisibleNumArray {
    public static void main(String[] args) {
        int[] arr = {3, 2, 6};
        int divisor = 10;
        System.out.println(Arrays.toString(solution(arr, divisor)));
    }

    public static int[] solution(int[] arr, int divisor) {
        int[] ints = Arrays.stream(arr).filter(x -> x % divisor == 0).sorted().toArray();
        if (ints.length == 0) {
            return new int[]{-1};
        }
        return ints;
    }
}
