package level1;

public class NumOfFactorsAndSum {
    public static void main(String[] args) {
        System.out.println(solution(24, 27));

    }
    public static int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i <= right ; i++) {
             if(Math.sqrt(i) == (int)Math.sqrt(i)) {
                 answer -= i;
             } else {
                 answer += i;
             }
        }
        return answer;
    }
}
