package level2;

import java.math.BigInteger;
import java.util.Arrays;

public class NLcd {
    public static void main(String[] args) {

    }

    public int solution(int[] arr) {
        return Arrays.stream(arr)
                .reduce(1, (x, y) -> x * y / gcd(x, y));
    }

    private int gcd(int x, int y) {
        return x % y == 0 ? y : gcd(y, x % y);
    }

    public long solution2(int[] arr) {
       return Arrays.stream(arr)
                .mapToLong(x -> Long.valueOf(x))
                .reduce(1, (x, y) -> x * y / BigInteger.valueOf(x).gcd(BigInteger.valueOf(y)).longValue());
    }
}
