package level3.kakao.kakao2019;

import java.util.ArrayDeque;
import java.util.Arrays;

//https://school.programmers.co.kr/learn/courses/30/lessons/64062
public class 징검다리건너기 {

    // soultion1 : 이분탐색 이용
    public int solution1(int[] stones, int k) {
        int start = 1;
        int end = Math.max(stones.length, Arrays.stream(stones).max().getAsInt());
        int answer = 1;

        while(start <= end) {
            int mid = (start + end) / 2;
            if(check(stones, mid, k)) {
                answer = Math.max(answer, mid);
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return answer;
    }

    private boolean check(int[] stones, int m, int k) {
        int cnt = 0;
        for(int stone : stones) {
            if(stone < m) {
                cnt += 1;
            } else {
                cnt = 0;
            }

            if(cnt == k) {
                return false;
            }
        }
        return true;
    }

    // soultion2 : 슬라이딩 윈도우, deque 사용
    public int solution2(int[] stones, int k) {
        ArrayDeque<Integer> q = new ArrayDeque<>();
        int answer = 200000000;

        for(int i=0; i<stones.length; i++) {
            if( (!q.isEmpty()) && (q.peekFirst() == (i - k))) {
                q.pollFirst();
            }

            while(!q.isEmpty()) {
                if(stones[q.peekLast()] < stones[i]) {
                    q.pollLast();
                } else {
                    break;
                }
            }

            q.offerLast(i);
            if(i >= (k-1)) {
                answer = Math.min(answer, stones[q.peekFirst()]);
            }
        }
        return answer;
    }


}
