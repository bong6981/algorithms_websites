package level1;

public class SumTwoIntegers {
    public static void main(String[] args) {
        System.out.println(solution(5,3));
    }

    public static long solution(int a, int b) {
        return (long) (Math.abs(a - b) + 1) * (a + b) / 2;
    }
}
