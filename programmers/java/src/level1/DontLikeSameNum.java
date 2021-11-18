package level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class DontLikeSameNum {
    public static void main(String[] args) {
        int[] arr = {1, 1, 3, 3, 0, 1, 1};
        System.out.println(Arrays.toString(solution(arr)));
    }

    public static int[] solution(int[] arr) {
        List<Integer> l = new ArrayList();
        l.add(arr[0]);
        for (int n : arr) {
            if (n != l.get(l.size() - 1)) {
                l.add(n);
            }
        }
        return l.stream().mapToInt(Integer::intValue).toArray();
    }
}
