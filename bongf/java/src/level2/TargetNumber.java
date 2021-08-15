package level2;

import java.util.Arrays;

public class TargetNumber {
    public static void main(String[] args) {
        int[] numbers = new int[]{1,1};
        System.out.println(solution(numbers, 0));
    }
    public static int solution(int[] numbers, int target) {
        if(numbers.length == 1) {
            if(numbers[0] == target || -numbers[0] == target) {
                return  1;
            }
            return 0;
        }
        return solution(Arrays.copyOfRange(numbers, 1, numbers.length), target + numbers[0]) + solution(Arrays.copyOfRange(numbers, 1, numbers.length), target - numbers[0]);
    }
}
