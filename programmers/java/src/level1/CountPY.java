package level1;

public class CountPY {
    public static void main(String[] args) {
        System.out.println(solution("Pyy"));
    }

    public static boolean solution(String s) {
        int p = 0;
        int y = 0;

        for (char i : s.toLowerCase().toCharArray() ) {
            if(i == 'p') {
                p++;
            } else if(i == 'y') {
                y++;
            }
        }

        return p == y;
    }
}
