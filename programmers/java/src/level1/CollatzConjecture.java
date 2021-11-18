package level1;

public class CollatzConjecture {
    public static void main(String[] args) {
        System.out.println(solution(626331));
    }

    //연산 안에서 int의 범위 넘어가는지 주의!
    public static int solution(int num) {
        long answer = 0;
        long n = num;
        while( answer!= 500 && n != 1) {
            if(n%2==0) {
                n /= 2;
            } else {
                n = n*3 + 1;
            }
            answer++;
        }
        return n == 1 ? (int) answer : -1;
    }
}
