package silver3;

import java.util.Scanner;
import java.util.stream.IntStream;

// https://www.acmicpc.net/problem/15650
public class Q15650_NM2 {
    public static int[] ints;
    public static int m;
    public static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        ints = IntStream.range(1, n + 1).toArray();
        dfs(new int[m], 0, 0);
    }

    public static void dfs(int[] numbers, int idx, int start) {
        if (idx == m) {
            for (int number : numbers) {
                System.out.print(number + " ");
            }
            System.out.println();
            return;
        }

        for (int i = start; i < n; i++) {
            numbers[idx] = ints[i];
            dfs(numbers, idx + 1, i + 1);
        }
    }
}
