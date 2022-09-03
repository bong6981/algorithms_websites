package level3.월간코드챌린지.시즌1;

import java.util.Arrays;

// https://school.programmers.co.kr/learn/courses/30/lessons/68646
public class 풍선터트리기 {
    public int solution(int[] a) {
        int answer = 1;
        int M = Arrays.stream(a).min().getAsInt();
        int m = 1000000001;
        int i = 0;
        while(a[i] != M) {
            if(a[i] < m) {
                answer++;
                m = a[i];
            }
            i++;
        }
        m = 1000000001;
        i = a.length-1;
        while(a[i] != M) {
            if(a[i] < m) {
                answer++;
                m = a[i];
            }
            i--;
        }

        return answer;
    }
}
