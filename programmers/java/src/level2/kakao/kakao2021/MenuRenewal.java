package level2.kakao.kakao2021;

import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/72411
public class MenuRenewal {
    private static Map<List<String>, Integer> combs;

    public static void main(String[] args) {
        MenuRenewal mr = new MenuRenewal();
        System.out.println(Arrays.toString(mr.solution(new String[]{"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"}, new int[]{2, 3, 4})));
        System.out.println(Arrays.toString(mr.solution(new String[]{"ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"}, new int[]{2, 3, 5})));
        System.out.println(Arrays.toString(mr.solution(new String[]{"XYZ", "XWY", "WXA"}, new int[]{2, 3, 4})));
    }

    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();

        for (int c : course) {
            combs = new HashMap<>();
            for (String order : orders) {
                String[] split = order.split("");
                Arrays.sort(split);
                getComb(split, 0, c, new ArrayList<>());
            }

            Integer integer = combs.values().stream().max(Comparator.comparing(x -> x)).orElse(0);
            if (integer > 1) {
                for (List<String> string : combs.keySet()) {
                    if (combs.get(string).equals(integer)) {
                        answer.add(String.join("", string));
                    }
                }
            }
        }

        Collections.sort(answer);
        return answer.toArray(new String[0]);
    }

    private void getComb(String[] order, int start, int target_size, List<String> string) {
        if (string.size() == target_size) {
            if (combs.get(string) == null) {
                combs.put(new ArrayList<>(string), 1);
                return;
            }
            ;
            combs.put(string, combs.get(string) + 1);
            return;
        }

        for (int i = start; i < order.length; i++) {
            string.add(order[i]);
            getComb(order, i + 1, target_size, string);
            string.remove(order[i]);
        }
    }
}
