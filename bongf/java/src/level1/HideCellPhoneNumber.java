package level1;

import java.util.stream.IntStream;

public class HideCellPhoneNumber {
    public static void main(String[] args) {
        System.out.println(solution3("01033334444"));
    }

    public static String solution(String phone_number) {
        String answer = "";
        for (int i = 0; i < phone_number.length() - 4; i++) {
             answer += "*";
        }
        answer += phone_number.substring(phone_number.length()-4);
        return answer;
    }

    public static String solution2(String phone_number) {
        char[] ch = phone_number.toCharArray();
        for(int i = 0; i < ch.length - 4; i ++){
            ch[i] = '*';
        }
        return String.valueOf(ch);
    }

    //. -> 임의의 문자 한 개
    // (?=.) -> 뒷쪽에 임의의 문자 한 개를 제외하고 선택
    // {숫자} -> 숫자 만큼의 자릿수
    // .(?=.{4}) ==> 뒤쪽에서 임의의 문자 4개를 제외한 임의의 문자 한 개 선택
    public static String solution3(String phone_number) {
        return phone_number.replaceAll(".(?=.{4})", "*");
    }
}
