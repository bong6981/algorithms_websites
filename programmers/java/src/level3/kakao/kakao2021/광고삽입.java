package level3.kakao.kakao2021;

import java.util.Arrays;

//https://school.programmers.co.kr/learn/courses/30/lessons/72414?language=java
public class 광고삽입 {
    private int toSeconds(String time) {
        String[] str_times = time.split(":");
        return Integer.parseInt(str_times[0]) * 3600
                + Integer.parseInt(str_times[1]) * 60
                + Integer.parseInt(str_times[2]);
    }

    private String toStringTime(int time) {
        String strTime = String.valueOf(time);
        if(strTime.length() == 1) {
            strTime = "0" + strTime;
        }
        return strTime;
    }

    public String solution(String play_time, String adv_time, String[] logs) {
        int playTime = toSeconds(play_time);
        int advTime = toSeconds(adv_time);
        long[] times = new long[playTime + 1];

        int firstStart = playTime+1;
        int lastEnd = 0;

        for(String log: logs) {
            String[] split = log.split("-");
            int start = toSeconds(split[0]);
            int end = toSeconds(split[1]);

            times[start] += 1;
            times[end] -= 1;

            if(firstStart > start) {
                firstStart = start;
            }
            if(lastEnd < end) {
                lastEnd = end;
            }
        }


        for(int i=firstStart; i<=lastEnd; i++) {
            if(i==0) {
                continue;
            }
            times[i] = times[i] + times[i-1];
        }


        int start = Math.max(0, firstStart-advTime);
        int end = Math.min(playTime, lastEnd+advTime);

        long sum = 0;
        for(int i=start; i<start+advTime; i++) {
            sum += times[i];
        }
        int left = start;
        int right = start+advTime-1;


        long ansCnt = sum;
        int ans = start;
        while(right < end) {
            sum -= times[left];
            left += 1;
            right += 1;
            sum += times[right];
            if(sum > ansCnt) {
                sum = ansCnt;
                ans = left;
            }
        }


        int intHour = ans / 3600;
        ans %= 3600;
        int intMin = ans / 60;
        ans %= 60;

        String h = toStringTime(intHour);
        String m = toStringTime(intMin);
        String s = toStringTime(ans);

        return h+":"+m+":"+s;

    }
}
