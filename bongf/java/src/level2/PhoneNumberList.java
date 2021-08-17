package level2;

import java.util.*;

public class PhoneNumberList {
    public static void main(String[] args) {
        System.out.println(solution(new String[]{"97674223", "1195524421", "119"}));
        System.out.println(solution(new String[]{"1195524421", "97674223", "1"}));
        System.out.println(solution(new String[]{"010", "011", "0112", "112"}));
        System.out.println(solution2(new String[]{"119", "97674223", "1195524421"}));
    }

    public static boolean solution(String[] phone_book) {
        Map<Character, List<String>> dic = new HashMap<>();
        dic.put('0', new ArrayList<>());
        dic.put('1', new ArrayList<>());
        dic.put('2', new ArrayList<>());
        dic.put('3', new ArrayList<>());
        dic.put('4', new ArrayList<>());
        dic.put('5', new ArrayList<>());
        dic.put('6', new ArrayList<>());
        dic.put('7', new ArrayList<>());
        dic.put('8', new ArrayList<>());
        dic.put('9', new ArrayList<>());

        for( String num : phone_book) {
            dic.get(num.charAt(0)).add(num);
        }

        for (Character character : dic.keySet()) {
            List<String> ns = dic.get(character);
            if(ns.size() >= 2) {
                Collections.sort(ns);
                for (int i = 0; i < ns.size() - 1; i++) {
                    if(ns.get(i+1).startsWith(ns.get(i))) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public static boolean solution2(String[] phone_book) {
        Arrays.sort(phone_book);
        if(phone_book.length >= 2) {
            for (int i = 0; i < phone_book.length-1; i++) {
                if (phone_book[i+1].startsWith(phone_book[i])) {
                    return false;
                }
            }
        }
        return true;
    }
}
