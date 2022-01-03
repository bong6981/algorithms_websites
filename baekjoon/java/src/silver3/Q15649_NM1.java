package silver3;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// https://www.acmicpc.net/problem/15649
public class Q15649_NM1 {
    private static List<Integer[]> answer;
    private static int m;
    private static int n;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        answer = new ArrayList<>();
        back_tracking(new ArrayList<>());

        for (Integer[] integers : answer) {
            for (Integer integer : integers) {
                System.out.print(integer + " ");
            }
            System.out.println();
        }
    }

    public static void back_tracking(List<Integer> now) {
        if(now.size() == m) {
            Integer[] toAdd = new Integer[m];
            answer.add(now.toArray(toAdd));
            return;
        }
        for (int i = 1; i <= n; i++) {
             if(now.contains(i)) {
                 continue;
             }
             now.add(i);
             back_tracking(now);
             now.remove(now.size()-1);
        }
    }
}
