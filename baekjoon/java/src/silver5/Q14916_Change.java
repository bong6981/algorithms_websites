package silver5;

import java.util.Scanner;

// https://www.acmicpc.net/problem/14916
public class Q14916_Change {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int maxFive = n / 5;
        int cnt = 0;
        while (maxFive >= 0) {
            int temp = n - maxFive * 5;
            if (temp % 2 == 0) {
                cnt += (maxFive + temp / 2);
                break;
            }
            maxFive--;
        }
        if (maxFive < 0) {
            System.out.println(-1);
        } else {
            System.out.println(cnt);
        }
    }
}
