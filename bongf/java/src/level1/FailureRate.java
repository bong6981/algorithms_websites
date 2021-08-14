package level1;

import java.util.*;

public class FailureRate {
    public static void main(String[] args) {
        System.out.println(solution2(5, new int[]{2, 1, 2, 6, 2, 4, 3, 3}));
    }

    //이게 더 빨랐다
    public static Integer[] solution(int N, int[] stages) {
        int[] ing = new int[N+2];
        Map<Integer, Double> rate = new HashMap<>();
        for (int stage : stages) {
            ing[stage]++;
        }
        for (int i = 1; i <=N; i++) {
            int triedP = Arrays.stream(Arrays.copyOfRange(ing, i, ing.length)).sum();
            if( triedP == 0 ) {
                rate.put(i, 0.0);
            } else {
                rate.put(i, (double)ing[i] / triedP);
            }
        }
        return rate.entrySet().stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .map(Map.Entry::getKey)
                .toArray(Integer[]::new);
    }

    public static Integer[] solution2(int N, int[] stages) {
        Map<Integer, Double> rate = new HashMap<>();
        int p = stages.length;
        for (int i = 1; i <=N; i++) {
            int finalI = i;
            long c = Arrays.stream(stages)
                    .filter(x-> x== finalI)
                    .count();
            if(p==0) {
                rate.put(i, 0.0);
            } else {
                rate.put(i, (double)c / (p));
                p -= c;
            }
        }

        System.out.println(rate);

        return rate.entrySet().stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .map(Map.Entry::getKey)
                .toArray(Integer[]::new);
    }
}
