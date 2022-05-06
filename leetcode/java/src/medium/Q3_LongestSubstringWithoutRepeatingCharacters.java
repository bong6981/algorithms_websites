package medium;

import java.util.LinkedList;
import java.util.Queue;

public class Q3_LongestSubstringWithoutRepeatingCharacters {
    public static int lengthOfLongestSubstring(String s) {
        Queue<Character> sub = new LinkedList<>();
        int ans = 0;
        for(char c : s.toCharArray()) {
            System.out.println("sub = " + sub);
            System.out.println("c = " + c);
            if(sub.contains(c)) {
                while(!sub.isEmpty()) {
                    Character poll = sub.poll();
                    if(poll == c) {
                        break;
                    }
                }
            }
            sub.add(c);
            ans = Math.max(ans, sub.size());
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("aab"));
    }
}
