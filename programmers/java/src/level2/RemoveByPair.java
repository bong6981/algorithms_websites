package level2;

import java.util.Stack;

public class RemoveByPair {
    public static void main(String[] args) {
        RemoveByPair removeByPair = new RemoveByPair();
        System.out.println(removeByPair.solution("baabaa"));

    }

    public int solution(String s) {
        char[] chars = s.toCharArray();
        Stack<Character> answer = new Stack<>();

        for (char c : chars) {
            if (answer.size() == 0) {
                answer.push(c);
            } else {
                if (answer.peek() == c) {
                    answer.pop();
                } else {
                    answer.push(c);
                }
            }
        }
        // return은 stack.isEmpty() ? 1 : 0 ;
        if (answer.isEmpty()) {
            return 1;
        }
        return 0;
    }
}
