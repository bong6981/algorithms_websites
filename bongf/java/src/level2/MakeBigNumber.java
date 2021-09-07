package level2;

import java.util.Stack;
import java.util.stream.Collectors;

public class MakeBigNumber {
    public static void main(String[] args) {
        System.out.println(solution("1924", 2));
        System.out.println(solution("1231234", 3));
        System.out.println(solution("4177252841", 4));
    }

    public static String solution(String number, int k) {
        Stack<Character> answer = new Stack<>();
        char[] numbers = number.toCharArray();
        for (int i = 0; i < number.length(); i++) {
            while (!answer.isEmpty() && k > 0 && answer.peek() < numbers[i]) {
                answer.pop();
                k -= 1;
            }
            answer.push(numbers[i]);
        }

        //다른 분 풀이
        /*
        char[] result = new char[number.length() - k];
        for (int i=0; i<result.length; i++) {
            result[i] = stack.get(i);
        }
        return new String(result);
         */
        return answer.stream()
                .map(String::valueOf)
                .collect(Collectors.joining())
                .substring(0, answer.size() - k);
    }

    //StringBuilder 활용한 방법
    //for문 돌면서 그 기준점(sb.length)가 변할 때 인덱스 적절하게 바꾸는 법
    public String solution2(String number, int k) {
        StringBuilder sb = new StringBuilder(number);
        for (int i = 0; i+1 < sb.length() && k>0; i++) {
            if(sb.charAt(i) < sb.charAt(i+1)) {
                sb.deleteCharAt(i);
                i=-1;
                k--;
            }
        }
        if(k!=0)
            sb.delete(sb.length()-k, sb.length());
        return sb.toString();
    }
}
