package level3.kakao.kakao2019;

import java.util.*;
import java.util.stream.IntStream;

//https://school.programmers.co.kr/learn/courses/30/lessons/64064
public class 불량사용자 {
    public static void main(String[] args) {
        System.out.println(solution(new String[]{"frodo", "fradi", "crodo", "abc123", "frodoc"}, new String[]{"*rodo", "*rodo", "******"}));
    }
    private static List<List<Integer>> info;
    private static String[] banned_id;
    private static Set<String> ans;


    private static void sol(int turn, int[] arr) {
        if(turn == banned_id.length) {
            StringJoiner sj = new StringJoiner("");
            IntStream.of(arr).forEach(c->sj.add(String.valueOf(c)));
            ans.add(sj.toString());
            return;
        }

        for(int i=0; i<info.get(turn).size(); i++) {
            int j = info.get(turn).get(i);
            if(arr[j] == 0) {
                arr[j] = 1;
                sol(turn+1, arr);
                arr[j] = 0;
            }
        }
    }

    public static int solution(String[] user_id, String[] banned_id) {
        ans = new HashSet<>();
        info = new ArrayList<>();
        불량사용자.banned_id = banned_id;

        for(int i=0; i < banned_id.length; i++) {
            info.add(new ArrayList<>());
            for(int j=0; j< user_id.length; j++) {
                if(banned_id[i].length() != user_id[j].length()) {
                    continue;
                }
                boolean possible = true;

                for(int k=0; k<banned_id[i].length(); k++) {
                    if(banned_id[i].charAt(k) == '*') {
                        continue;
                    }
                    if(banned_id[i].charAt(k) != user_id[j].charAt(k)) {
                        possible = false;
                        break;
                    }
                }
                if(possible) {
                    info.get(i).add(j);
                }
            }
        }

        System.out.println(info);
        sol(0, new int[user_id.length]);
        System.out.println(ans);
        return ans.size();
    }


    static Set<Integer> set;

    public static int solution_from_other(String[] user_id, String[] banned_id) {
        set = new HashSet<>();

        go(0, user_id, banned_id, 0);

        return set.size();
    }

    public static void go(int index, String[] user_id, String[] banned_id, int bit) {

        if(index == banned_id.length) {
            set.add(bit);
            return;
        }

        String reg = banned_id[index].replace("*", "[\\w\\d]");
        System.out.println("reg = " + reg);
        for(int i=0; i<user_id.length; ++i) {
            if((((bit>>i) & 1) == 1) || !user_id[i].matches(reg)) continue;
            go(index + 1, user_id, banned_id, (bit | 1<<i));
        }

    }
}
