package level1;

import java.util.Arrays;

public class FindMrKim {
    public static void main(String[] args) {
        String [] seoul = {"Jane", "Kim"};
        System.out.println(solution(seoul));
    }

    public static String solution(String[] seoul) {
       return "김서방은 " + Arrays.asList(seoul).indexOf("Kim")+"에 있다";
    }
}
