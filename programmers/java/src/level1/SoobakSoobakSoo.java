package level1;

import java.util.Collections;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class SoobakSoobakSoo {
    public static void main(String[] args) {
        System.out.println(solution4(5));
    }

    public static String solution(int n) {
        return IntStream.range(1, n+1)
                .mapToObj(x -> x%2 == 0 ? "박" : "수")
                .collect(Collectors.joining());
    }

    public static String solution2(int n){
        return new String(new char [n/2+1]).replace("\0", "수박").substring(0,n);
    }

    //자바 11부터 repeat() 가능
    public static String solution3(int n) {
        String str = "수박";
        return str.repeat(n/2+1).substring(0,n);
    }

    public static String solution4(int n) {
        // create a string made up of n copies of string s
        return String.join("", Collections.nCopies(n/2+1, "수박")).substring(0,n);
    }

}
