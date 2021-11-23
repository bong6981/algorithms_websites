package bronze2;

import java.util.Scanner;

// https://www.acmicpc.net/problem/10870
public class Q10870_FibonacciNumber {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        if(n==0) {
            System.out.println(0);
            return;
        }
        int[] d = new int[n+1];
        d[0] = 0;
        d[1] = 1;
        for (int i = 2; i <= n; i++) {
            d[i] = d[i-1] + d[i-2];
        }
        System.out.println(d[n]);
    }
}
