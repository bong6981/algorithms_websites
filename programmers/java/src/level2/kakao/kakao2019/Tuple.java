package level2.kakao.kakao2019;

import java.util.*;
import java.util.stream.Collectors;

// https://programmers.co.kr/learn/courses/30/lessons/64065
public class Tuple {
    public static void main(String[] args) {
        Tuple t = new Tuple();
        System.out.println(t.solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"));
        System.out.println(t.solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"));
        System.out.println(t.solution("{{20,111},{111}}"));
        System.out.println(t.solution("{{123}}"));
        System.out.println(t.solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"));
        System.out.println(t.other("{{4,2,3},{3},{2,3,4,1},{2,3}}"));
    }

    private List<Integer> solution(String s) {
        s = s.substring(2, s.length()-2);
        String[] split = s.split("},\\{");
        List<List<Integer>> tuple = new ArrayList<>();
        for (String s1 : split) {
            List<Integer> numbers = new ArrayList<>();
            String[] split1 = s1.split(",");
            for (String s2 : split1) {
                numbers.add(Integer.parseInt(s2));
            }
            tuple.add(numbers);
        }
        tuple.sort(Comparator.comparingInt(List::size));
        List<Integer> answer = new ArrayList<>();
        for (List<Integer> t : tuple) {
            for (Integer integer : t) {
                if(answer.contains(integer)) {
                    continue;
                }
                answer.add(integer);
            }
        }
        return answer;
    }

    public List<Integer> solution_old(String s) {
        s = s.substring(1, s.length() - 2);
        List<Set<Integer>> list = new ArrayList<>();
        Arrays.stream(s.split("},"))
                .map(x -> x.substring(1))
                .map(x -> Arrays.stream(x.split(",")).map(Integer::parseInt).collect(Collectors.toSet()))
                .forEach(list::add);
        list.sort(Comparator.comparingInt(Set::size));
        Set<Integer> now = new HashSet<>();
        List<Integer> answer = new ArrayList<>();
        for (Set<Integer> integers : list) {
            integers.removeAll(now);
            Integer integer = integers.stream().findFirst().get();
            answer.add(integer);
            now.add(integer);
        }
        return answer;
    }

    public int[] other(String s) {
        Set<String> set = new HashSet<>();
        String[] arr = s.replaceAll("[{]", " ").replaceAll("[}]", " ").trim().split(" , ");
        Arrays.sort(arr, (a, b) -> {
            return a.length() - b.length();
        });
        int[] answer = new int[arr.length];
        int idx = 0;
        for (String s1 : arr) {
            for (String s2 : s1.split(",")) {
                if (set.add(s2)) answer[idx++] = Integer.parseInt(s2);
            }
        }
        return answer;
    }
}
