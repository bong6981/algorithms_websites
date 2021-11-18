package level2;

import java.util.Arrays;

public class LifeBoat {
    public static void main(String[] args) {
        System.out.println(solution(new int[]{70, 50, 80, 50}, 100));
        System.out.println(solution(new int[]{70, 80, 50}, 100));
    }

    //파이썬의 다른 분 풀이 보고 함
    public static int solution(int[] people, int limit) {
        Arrays.sort(people);
        int mini = 0;
        int maxi = people.length -1;
        int answer = 0;

        while ( mini < maxi ) {
            if (people[mini] + people[maxi] <= limit) {
                answer++;
                mini++;
            }
            maxi--;
        }
        return people.length - answer;
    }

    public int solution2(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, j = people.length - 1;
        for (; i < j; --j) {
            if (people[i] + people[j] <= limit)
                ++i;
        }
        return people.length - i;
    }
}
