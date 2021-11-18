package level1;

import java.util.*;

public class SortStringSuitMyself {
    public static void main(String[] args) {
        String[] strings = {"abce", "abcd", "cdx"};
        int n = 2;
        System.out.println(Arrays.toString(solution(strings, n)));
    }

    public static String[] solution(String[] strings, int n) {
        String[] answer = {};
        Arrays.sort(strings, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                char ch1 = s1.charAt(n);
                char ch2 = s2.charAt(n);

                if(ch1 == ch2) {
                    return s1.compareTo(s2);
                } else if(ch1 > ch2) {
                    return 1;
                } else {
                    return -1;
                }
            }
        });
        return strings;
    }

    //어차피 그 n번째 문자만 비교하고 뒤에는 알파벳 순이니까 n번째 문자를 안빼도 된다.
    public static String[] solution2(String[] strings, int n) {
        String[] answer = {};
        ArrayList<String> arr = new ArrayList<>();
        for (int i = 0; i < strings.length; i++) {
            arr.add("" + strings[i].charAt(n) + strings[i]);
        }
        Collections.sort(arr);
        answer = new String[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            answer[i] = arr.get(i).substring(1, arr.get(i).length());
        }
        return answer;
    }

    // 람다식 sort 구현
    public String[] solution3(String[] strings, int n) {
        List<String> list = Arrays.asList(strings);
        list.sort((a, b) -> {
            int result = (a.split(""))[n].compareTo((b.split(""))[n]);
            if(result == 0)
                return a.compareTo(b);
            return result;
        });
        return list.toArray(new String[0]);
    }
}
