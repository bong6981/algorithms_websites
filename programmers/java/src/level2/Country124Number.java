package level2;

public class Country124Number {
    public static void main(String[] args) {
        Country124Number country124Number = new Country124Number();
        System.out.println(country124Number.solution(18)); //124
    }

    public String solution(int n) {
        int[] nums = new int[]{1, 2, 4};
        StringBuilder answer = new StringBuilder();

        while(n>0) {
            n -= 1;
            answer = answer.insert(0, nums[(n%3)]);
            n /= 3;
        }

        return answer.toString();
    }
}
