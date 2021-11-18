package level1;

public class IntRootDetermination {
    public static void main(String[] args) {
        System.out.println(solution(12));
        System.out.println(solution(121));
    }
    public static long solution(long n) {
        if (Math.sqrt(n) == (int) Math.sqrt(n)) {
            return (long) Math.pow(Math.sqrt(n) + 1, 2);
        }
        return -1;
    }
}
