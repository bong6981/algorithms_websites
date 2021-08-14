package level1;

import java.util.Arrays;
import java.util.List;
import java.util.Locale;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class CreateStrangeString {
    public static void main(String[] args) {
//        System.out.println(solution("try hello world"));

        System.out.println(Arrays.toString("hello world".split(" ", -1)));
        System.out.println(Arrays.toString("hello world".split(" ")));
    }


    //split에 limit 으로 -1을 준 것은 "hello world  " 이렇게 뒤에 공백이 들어갈 경우 최종 출력도 공백을 주기 위해서
    //   System.out.println(Arrays.toString("hello world   ".split(" ", -1))); 결과값 [hello, world, , , ]
    //   System.out.println(Arrays.toString("hello world   ".split(" "))); 결과값 [hello, world]
    public static String solution(String s) {
        String[] arr = s.split(" ", -1);
        for (int i = 0; i < arr.length; i++) {
            String [] chars = arr[i].split("");
            for (int j = 0; j < chars.length; j++) {
                if ( j % 2 == 0 ) {
                    chars[j] = chars[j].toUpperCase();
                } else {
                    chars[j] = chars[j].toLowerCase();
                }
            }
            arr[i] = String.join("", chars);
        }
        return String.join(" ", arr);
    }
}
