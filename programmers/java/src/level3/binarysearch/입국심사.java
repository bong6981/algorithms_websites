package level3.binarysearch;

import java.util.Arrays;

public class 입국심사 {

    public long solution(int n, int[] times) {
        Arrays.sort(times);

        long start = times[0];
        long end = (long) times[0] * n;
        long ans = -1;
        while( start <= end ) {
            long mid = (start + end) / 2;
            long covered = 0;
            for (int time : times) {
                if (time > mid) {
                    break;
                }
                covered += mid / time;
            }

            if (covered >= n) {
                ans = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return ans;
    }
}
