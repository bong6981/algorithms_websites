package level2.kakao.kakao2018;

import java.util.*;

public class NewsClustering {
    public static void main(String[] args) {
        NewsClustering nc = new NewsClustering();
        System.out.println(nc.solution("FRANCE", "french"));
        System.out.println(nc.solution_other("FRANCE", "french"));
    }
    public int solution(String str1, String str2) {
        List<String> str1List = new ArrayList<>();
        for (int i = 0; i < str1.length() -1; i++) {
            char c1 = str1.charAt(i);
            char c2 = str1.charAt(i+1);
            if(Character.isLetter(c1) && Character.isLetter(c2)) {
                str1List.add(str1.substring(i, i+2).toLowerCase());
            }
        }

        List<String> str2List = new ArrayList<>();
        for (int i = 0; i < str2.length() -1; i++) {
            char c1 = str2.charAt(i);
            char c2 = str2.charAt(i+1);
            if(Character.isLetter(c1) && Character.isLetter(c2)) {
                str2List.add(str2.substring(i, i+2).toLowerCase());
            }
        }

        int total = str1List.size() + str2List.size();
        int bunza = 0;
        if(total == 0) {
            return 65536;
        }
        int st2Idx =0;
        Collections.sort(str1List);
        Collections.sort(str2List);
        for (String s : str1List) {
            for (int i = st2Idx; i < str2List.size(); i++) {
                 if(str2List.get(i).equals(s)) {
                     st2Idx = i + 1;
                     bunza += 1;
                     total -= 1;
                     break;
                 }
            }
            if(st2Idx == str2List.size()) {
                break;
            }
        }
        return (int) (((float) bunza)/total * 65536);
    }
    public int solution_other(String str1, String str2) {
        List<String> str1List = new ArrayList<>();
        for (int i = 0; i < str1.length()-1; i++) {
            char c1 = str1.charAt(i);
            char c2 = str1.charAt(i+1);
            if(Character.isLetter(c1) && Character.isLetter(c2)) {
                str1List.add(str1.substring(i, i+2).toLowerCase());
            }
        }

        List<String> str2List = new ArrayList<>();
        for (int i = 0; i < str2.length()-1; i++) {
            char c1 = str2.charAt(i);
            char c2 = str2.charAt(i+1);
            if(Character.isLetter(c1) && Character.isLetter(c2)) {
                str2List.add(str2.substring(i, i+2).toLowerCase());
            }
        }
        Set<String> gyo = new HashSet<>();
        Set<String> hap = new HashSet<>();

        hap.addAll(str1List);
        hap.addAll(str2List);

        gyo.addAll(str1List);
        gyo.retainAll(str2List);

        if(hap.size() == 0) {
            return 65536;
        }

        int bunza = 0;
        int bunmo = 0;
        for(String g : gyo) {
            bunza += Math.min(Collections.frequency(str1List, g), Collections.frequency(str2List, g));
        }
        for(String h : hap) {
            bunmo += Math.max(Collections.frequency(str1List, h), Collections.frequency(str2List, h));
        }

        float float_bunza = (float) bunza;
        return (int) ((float_bunza / bunmo) * 65536);
    }
}
