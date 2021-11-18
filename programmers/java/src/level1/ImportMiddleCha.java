package level1;

public class ImportMiddleCha {
    public static void main(String[] args) {
        System.out.println(solution("abcd"));

    }

    public static String solution(String s) {
        int i = s.length() % 2;
        if( i == 0 ) {
            return s.split("")[s.length()/2 -1] +  s.split("")[s.length()/2];
        }
        return s.split("")[s.length()/2];
    }

    public static String solution2(String s) {
        return s.substring((s.length()-1) / 2, s.length()/2 + 1);
    }
}
