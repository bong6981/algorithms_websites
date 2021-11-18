package level1;

import java.util.Arrays;

public class GetPrimeNumber {
    public static void main(String[] args) {
        System.out.println(solution(5));
    }

    public static int solution(int n) {
        int[] arr = new int[n + 1];
        Arrays.fill(arr, 2, n + 1, 1);
        for (int i = 0; i <= (int) Math.sqrt(n); i++) {
            if (arr[i] == 1) {
                for (int j = i * 2; j <= n; j += i) {
                    arr[j] = 0;
                }
            }
        }
        return (int) Arrays.stream(arr).filter(x -> x == 1).count();
    }
}
