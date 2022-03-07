package level3.kakao.kakao2018;

import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/17676
public class ChuseokTraffic {
    public static void main(String[] args) {
        ChuseokTraffic ct = new ChuseokTraffic();
        System.out.println(ct.solution(new String[]{
                "2016-09-15 20:59:57.421 0.351s",
                "2016-09-15 20:59:58.233 1.181s",
                "2016-09-15 20:59:58.299 0.8s",
                "2016-09-15 20:59:58.688 1.041s",
                "2016-09-15 20:59:59.591 1.412s",
                "2016-09-15 21:00:00.464 1.466s",
                "2016-09-15 21:00:00.741 1.581s",
                "2016-09-15 21:00:00.748 2.31s",
                "2016-09-15 21:00:00.966 0.381s",
                "2016-09-15 21:00:02.066 2.62s"
        }));
    }

    public int solution(String[] lines) {
        Integer[][] times = new Integer[lines.length][2];
        for (int i = 0; i < times.length; i++) {
            String line = lines[i];
            String[] lineStrings = line.split(" ");

            String[] endTimeStrings = lineStrings[1].split(":");
            String[] endSecondStrings = endTimeStrings[2].split("\\.");
            int endTime = Integer.parseInt(endSecondStrings[1])
                    + 1000 * (Integer.parseInt(endSecondStrings[0])
                    + Integer.parseInt(endTimeStrings[1]) * 60
                    + Integer.parseInt(endTimeStrings[0]) * 3600);

            String[] leadTimeStrings = lineStrings[2].substring(0, lineStrings[2].length() -1).split("\\.");
            String leadTimeMsString = "";
            if(leadTimeStrings.length == 1) {
                leadTimeMsString = "000";
            } else {
                leadTimeMsString = String.format("%03d", Integer.parseInt(leadTimeStrings[1]));
            }
            Integer leadTime = Integer.parseInt(leadTimeMsString) + 1000 * Integer.parseInt(leadTimeStrings[0]);

            int startTime = endTime - leadTime + 1;
            times[i] = new Integer[]{startTime, endTime+999};
        }
        Arrays.sort(times, Comparator.comparing(x-> x[0]));
        List<Integer[]> temp = new ArrayList<>();
        int answer = 0;
        for(Integer[] time: times) {
            int s = time[0];
            int idx = 0;
            temp.add(time);
            temp.sort(Comparator.comparing(x-> x[1]));
            while(idx < temp.size()) {
                int endTime = temp.get(idx)[1];
                if(endTime < s) {
                    idx++;
                    continue;
                }
                break;
            }
            temp = temp.subList(idx, temp.size());
            answer = Math.max(answer, temp.size());
        }
        return answer;
    }
}
