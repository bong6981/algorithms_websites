package level2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class StringCompression {
    public static void main(String[] args) {
        StringCompression sc = new StringCompression();
        System.out.println(sc.solution("aabbaccc"));
        System.out.println(sc.solution("ababcdcdababcdcd"));
        System.out.println(sc.solution("abcabcdede"));
        System.out.println(sc.solution("abcabcabcabcdededededede"));
        System.out.println(sc.solution("xababcdcdababcdcd"));
    }

    public int solution(String s) {
        List<Integer> strings = new ArrayList<>();
        for (int i = 1; i < s.length() / 2 + 1; i++) {
            strings.add(compression(i, s));
        }
        strings.add(compression(s.length(), s));
        Collections.sort(strings);
        return strings.get(0);
    }

    public int compression(int length, String s) {
        List<String> stringList = new ArrayList<>();
        for (int i = 0; i < s.length(); i += length) {
            if (i + length > s.length()) {
                stringList.add(s.substring(i));
            } else {
                stringList.add(s.substring(i, i + length));
            }
        }

        List<String> copyList = new ArrayList(stringList);
        copyList.remove(0);
        // 이거 안해주고 마지막 전의 것과 마지막 것만 비교하는 것에서 끝냈더니 add 안해주고 count 만 증가시키고 끝남
        copyList.add("");
        int curCount = 1;
        List<String> returnStringList = new ArrayList<>();
        for (int i = 0; i < stringList.size(); i++) {
            if (stringList.get(i).equals(copyList.get(i))) {
                curCount++;
            } else {
                if (curCount != 1) {
                    returnStringList.add(String.valueOf(curCount));
                }
                returnStringList.add(stringList.get(i));
                curCount = 1; 
            }
        }
        return String.join("", returnStringList).length();
    }

    public int solution2(String s) {
        int answer = 0;

        for(int i=1; i<=(s.length()/2)+1; i++){
            int result = getSplitedLength(s, i, 1).length();
            answer = i==1 ? result : (answer>result?result:answer);
        }

        return answer;
    }

    public String getSplitedLength(String s, int n, int repeat){
        if(s.length() < n) return s;
        String result = "";
        String preString = s.substring(0, n);
        String postString = s.substring(n, s.length());

        // 불일치 -> 현재까지 [반복횟수 + 반복문자] 조합
        if(!postString.startsWith(preString)){
            if(repeat ==1) return result += preString + getSplitedLength(postString, n, 1);
            return result += Integer.toString(repeat) + preString + getSplitedLength(postString, n, 1);
        }

        return result += getSplitedLength(postString, n, repeat+1);
    }
}
