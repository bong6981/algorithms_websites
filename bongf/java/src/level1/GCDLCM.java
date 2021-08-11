package level1;

import java.util.Arrays;

public class GCDLCM {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution2(2, 5)));
    }

    public static int[] solution(int n, int m) {
        int x = Math.max(n,m);
        int y = Math.min(n,m);

        int t = 1;
        while(t>0) {
            t = x % y;
            x = y;
            y = t;
        }

        int[] answer = new int[]{x, n*m/x};
        return answer;
    }

    public static int[] solution2(int n, int m) {
        int gcd = gcd(Math.max(n,m), Math.min(n,m));
        return new int[]{gcd, n*m/gcd};
    }

    public static int gcd(int n, int m) {
        if(n<m) {
            gcd(m, n);
        }
        if(m==0) {
            return n;
        }
        return gcd(m, n%m);
    }
}
