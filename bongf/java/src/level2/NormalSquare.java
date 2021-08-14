package level2;

public class NormalSquare {
    public static void main(String[] args) {
        System.out.println(solution(8, 12));
    }

    public static long solution(int w, int h) {
        long x = (long) w;
        long y = (long) h;
        return x * y - ( x + y - gcd(w, h));
    }

    private static int gcd(int w, int h){
        if(w%h == 0) {
            return h;
        }
        return gcd(h, w%h);
    }
}
