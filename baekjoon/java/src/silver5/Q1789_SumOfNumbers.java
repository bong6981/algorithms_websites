package silver5;

import java.util.Scanner;

// https://www.acmicpc.net/problem/1789
public class Q1789_SumOfNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long start = 1;
        long end = n;
        long answer = 0;
        while(start <= end) {
            long mid = (start+end) / 2;
            if (mid * (mid+1) / 2 <= n) {
                answer = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        System.out.println(answer);
    }

    public static void solution(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long total = 0;
        long now = 0;
        while (total < n) {
            now++;
            total += now;
        }
        if (total != n) {
            now--;
        }
        System.out.println(now);
    }
}
