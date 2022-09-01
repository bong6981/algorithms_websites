package level3.kakao.kakao2020;

import java.util.*;

public class 보석쇼핑 {
    public static void main(String[] args) {

    }
    public int[] solution(String[] gems) {
        Map<String, Integer> info = new HashMap<>();
        int left = 0;
        int right = 0;
        Set<String> gemsSet = new HashSet<>(Arrays.asList(gems));
        int gemsKinds = gemsSet.size();
        int[] answer = null;
        int cnt = 100005;

        while(left <= (gems.length - gemsKinds)) {
            int kind  = info.size();
            if(kind == gemsKinds) {
                if((right-left+1) < cnt) {
                    answer = new int[]{left+1, right};
                    cnt = right - left + 1;
                }
                info.compute(gems[left], (k, v) -> v -= 1);
                if(info.get(gems[left]) == 0) {
                    info.remove(gems[left]);
                }
                left++;
                continue;
            }
            if(right == gems.length) {
                break;
            }
            info.compute(gems[right], (k, v) -> (v==null) ? 1 : v+1);
            right++;
        }


        return answer;
    }
}
