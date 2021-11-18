package bronze3;

import java.util.*;

//https://www.acmicpc.net/problem/5618
public class Q5816_CommonDivisor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = sc.nextInt();
        }

        int g = gcd(numbers[0], numbers[1]);
        if(n==3){
            g = gcd(g, numbers[2]);
        }

        List<Integer> answer = new ArrayList<>();
        for (int i = 1; i <= (int) Math.sqrt(g); i++) {
            if(g % i == 0) {
                answer.add(i);
                int x = g / i;
                if(x != i) {
                    answer.add(x);
                }
            }
        }

        Collections.sort(answer);
        for (Integer integer : answer) {
            System.out.println(integer);
        }
    }

    public static int gcd(int x, int y) {
        int i = Math.max(x,y);
        int j = Math.min(x,y);
        int t = 1;
        while(t > 0) {
            t = i % j;
            i = j;
            j = t;
        }
        return i;

    }
}
