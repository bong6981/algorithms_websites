package level1;

import java.util.*;
import java.util.stream.Collectors;

public class GymClothes {
    public static void main(String[] args) {
        int n = 5;
        int[] lost = {1, 2, 4, 5};
        int[] reserve = {2, 3, 4};
        System.out.println(solution(n, lost, reserve));
    }

    public static int solution(int n, int[] lost, int[] reserve) {
        Set<Integer> lostS = Arrays.stream(lost).boxed().collect(Collectors.toSet());
        Set<Integer> collectS = Arrays.stream(reserve).boxed().collect(Collectors.toSet());

        Set<Integer> intersection = lostS.stream().filter(collectS::contains).collect(Collectors.toSet());

        lostS.removeAll(intersection);
        collectS.removeAll(intersection);

        for( Integer x : collectS) {
            if(lostS.contains(x-1)) {
                lostS.remove(x-1);
            } else if (lostS.contains(x+1)) {
                lostS.remove(x+1);
            }
        }
        return  n - lostS.size();
    }

    public static int solution_2(int n, int[] lost, int[] reserve) {
        int[] people = new int[n];
        int answer = n;

        for(int l : lost) {
            people[l-1]--;
        }
        for(int r : reserve) {
            people[r-1]++;
        }

        for (int i = 0; i < people.length; i++) {
            if(people[i] == -1) {
                if(i-1 >= 0 && people[i-1] == 1) {
                    people[i-1]--;
                    people[i]++;
                } else if(i+1< people.length && people[i+1] ==1) {
                    people[i+1]--;
                    people[i]++;
                } else {
                    answer--;
                }
            };
        }
        return answer;
    }
}
