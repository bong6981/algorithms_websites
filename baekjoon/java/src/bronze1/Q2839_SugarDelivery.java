package bronze1;

import java.util.Scanner;

// https://www.acmicpc.net/problem/2839
public class Q2839_SugarDelivery {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int q = n / 5;
        int r = n % 5;

        boolean possible = false;
        while (q >= 0) {
            if (r % 3 == 0) {
                possible = true;
                break;
            }
            q--;
            r += 5;
        }
        if (!possible) {
            System.out.println(-1);
            return;
        }
        System.out.println(q + r / 3);
    }
}
