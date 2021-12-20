package silver3;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

// https://www.acmicpc.net/problem/14425
public class Q14425_SetOfStrings {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        Set<String> strings = new HashSet<>();

        sc.nextLine();
        for (int i = 0; i < n; i++) {
            strings.add(sc.nextLine());
        }

        int cnt = 0;
        for (int i = 0; i < m; i++) {
            if(strings.contains(sc.nextLine())) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
