package level1;

public class ReverseTernary {
    public static void main(String[] args) {
        System.out.println(solution2(125));
    }

    public static int solution(int n) {
        String result = "";
        while(n > 0) {
            result += n % 3;
            n = n / 3;
        }

        int answer = 0;
        for(int i=0; i<result.length(); i++) {
            answer += (Integer.parseInt(String.valueOf(result.charAt(i)))) * Math.pow(3, result.length() - 1 - i);

        }
        return answer;
    }

    public static int solution2(int n) {
        String result = "";
        while(n > 0) {
            result += n % 3;
            n = n / 3;
        }
        return Integer.parseInt(result, 3);
    }
}
