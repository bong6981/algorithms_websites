package level1;

import java.util.Arrays;
import java.util.stream.Collectors;

public class Phoneketmon {
    public static void main(String[] args) {
        int[] nums = {3,3,3,2,2,2};
        System.out.println(solution(nums));
    }

    public static int solution(int[] nums) {
        return Math.min( nums.length /2 ,  Arrays.stream(nums).boxed().collect(Collectors.toSet()).size());
    }

    public static int solution_2(int[] nums) {
        return Arrays.stream(nums)
                .boxed()
                .collect(Collectors.collectingAndThen(Collectors.toSet(),
                        x -> Integer.min(x.size(), nums.length / 2)));
    }
}
