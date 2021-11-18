package level2;

import java.util.ArrayList;
import java.util.List;

public class Joystick {
    public int lastidx;
    public static void main(String[] args) {
        Joystick js = new Joystick();
        System.out.println(js.solution("ABC"));
    }

    public int solution(String name) {
        List<Integer> aidx = new ArrayList<>();

        int answer = 0;
        for (int i = 0; i < name.length(); i++) {
            char c = name.charAt(i);
            if(c != 'A') {
                 aidx.add(i);
                answer += Math.min( c - 'A', 91 - c);
             }
        }

        lastidx = name.length() - 1;

        int p = 0;
        if(aidx.contains(p)){
            aidx.remove(p);
        }

        while (aidx.size() > 0) {
            int len1 = getDistance(p, aidx.get(0));
            int len2 = getDistance(p, aidx.get(aidx.size()-1));

            if(len1 <= len2) {
                answer += len1;
                p = aidx.get(0);
            } else {
                answer += len2;
                p = aidx.get(aidx.size()-1);
            }

            aidx.remove(Integer.valueOf(p));
        }
        return answer;
    }

    public int getDistance(int p, int to) {
        if( p <= to) {
            return Math.min( to-p, p +1 + lastidx - to);
        }
        return Math.min(p-to, lastidx - p + 1 + to);
    }
}
