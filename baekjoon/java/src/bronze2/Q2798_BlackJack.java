package bronze2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

// https://www.acmicpc.net/problem/2798
public class Q2798_BlackJack {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();
        String[] input = sc.nextLine().split(" ");
        List<Integer> numbers = new ArrayList<>();
        for (String s : input) {
            numbers.add(Integer.parseInt(s));
        }
        Collections.sort(numbers);
        int answer = 0;
        for (int i = 0; i < n - 2; i++) {
            int x = numbers.get(i);
            if (x >= m) {
                break;
            }
            for (int j = i + 1; j < n - 1; j++) {
                int y = x + numbers.get(j);
                if (y >= m) {
                    break;
                }
                for (int k = j + 1; k < n; k++) {
                    int z = y + numbers.get(k);
                    if (z > m) {
                        break;
                    }
                    answer = Math.max(answer, z);
                }
            }
        }
        System.out.println(answer);
    }
}
