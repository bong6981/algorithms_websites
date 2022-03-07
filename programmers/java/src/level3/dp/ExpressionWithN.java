package level3.dp;

import java.util.*;

public class ExpressionWithN {
    public static void main(String[] args) {
        ExpressionWithN ewn = new ExpressionWithN();
        System.out.println(ewn.solution(5, 12));
        System.out.println(ewn.solution(2, 11));

    }
    public int solution(int N, int number) {
        if(N == number) {
            return 1;
        }
        String n = String.valueOf(N);
        List<Set<Integer>> dp = new ArrayList<>();
        dp.add(new HashSet<Integer>());
        for(int i=1; i <= 8; i++) {
            Set<Integer> s = new HashSet<>();
            int e = Integer.parseInt(String.join("", Collections.nCopies(i, n)));
            if( e == number) {
                return i;
            }
            s.add(e);
            for (int j = 1; j <= i-1; j++) {
                Set<Integer> s1 = dp.get(j);
                Set<Integer> s2 = dp.get(i - j);
                for (Integer integer1 : s1) {
                    for (Integer integer2 : s2) {
                        s.add(integer1 + integer2);
                        s.add(integer1 - integer2);
                        s.add(integer1 * integer2);
                        if(integer2!=0) {
                            s.add(integer1 / integer2);
                        }
                        if(s.contains(number)) {
                            return i;
                        }
                    }
                }
            }
            dp.add(s);
        }
        return -1;
    }
}
