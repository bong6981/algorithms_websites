package level2.kakao.kakao2022;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// https://programmers.co.kr/learn/courses/30/lessons/92341
public class ParkingFeeCal {
    public static void main(String[] args) {
        ParkingFeeCal pfc = new ParkingFeeCal();
        System.out.println(Arrays.toString(pfc.solution(new int[]{180, 5000, 10, 600}, new String[]{"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"})));
    }

    public Integer[] solution(int[] fees, String[] records) {
        int minTime = fees[0];
        int minFee = fees[1];
        int unitTime = fees[2];
        int unitFee = fees[3];

        int[] inTime = new int[10000];
        Arrays.fill(inTime, -2);
        int[] total = new int[10000];
        for (String r : records) {
            String[] r1 = r.split(" ");
            String[] r2 = r1[0].split(":");
            int h = Integer.parseInt(r2[0]);
            int m = Integer.parseInt(r2[1]);
            int t = h * 60 + m;
            if (r1[2].equals("IN")) {
                inTime[Integer.parseInt(r1[1])] = t;
            } else {
                int num = Integer.parseInt(r1[1]);
                total[Integer.parseInt(r1[1])] += t - inTime[num];
                inTime[num] = -1;
            }
        }

        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < 10000; i++) {
            if (inTime[i] != -2) {
                if (inTime[i] != -1) {
                    total[i] += 23 * 60 + 59 - inTime[i];
                }
                if (total[i] <= minTime) {
                    answer.add(minFee);
                } else {
                    answer.add(minFee + (int) (Math.ceil((total[i] - minTime) / (double)unitTime) * unitFee));
                }
            }
        }
        return answer.toArray(new Integer[0]);
    }
}
