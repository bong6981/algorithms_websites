package bronze3;

import java.util.Scanner;

public class Q22864_Fatigue {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int m = sc.nextInt();

        int w = 0;
        int f = 0;
        if (a > m) {
            System.out.println(0);
            return;
        }
        for (int i = 0; i < 24; i++) {
            if (f + a <= m) {
                f += a;
                w += b;
            } else {
                if (f < c) {
                    f = 0;
                } else {
                    f -= c;
                }
            }
        }
        System.out.println(w);
    }
}
