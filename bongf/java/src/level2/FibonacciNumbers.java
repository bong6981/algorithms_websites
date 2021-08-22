package level2;

public class FibonacciNumbers {
    public static void main(String[] args) {
        System.out.println(solution(100));
        System.out.println(solution2(100));
    }

    //JAVA는 피보나치를 계산하다 보면 Long의 범위 까지 초과해서 답이 다르게 나온다.
    // (N) % 1234567 = F(N - 1) % 1234567 + F(N - 2) % 1234567를 이용해야 한다.
    public static long solution(int n) {
        long cnt = 1;
        long[] arr = {0L, 1L};
        while ( cnt != n) {
            long temp = arr[1];
            arr[1] = arr[0] % 1234567 + arr[1] % 1234567;
            arr[0] = temp;
            cnt++;
        }
        return arr[1] % 1234567;
    }

    public static int solution2(int n) {
        int answer = 0;
        long[] pib=new long[n+1];
        pib[0]=0L;
        pib[1]=1L;
        int times=1;
        for(int i=2; i<=n; i++){
            pib[i]=(pib[i-1]+pib[i-2])%1234567L;
        }
        //answer=(int)(pib[n]%1234567L);
        answer=(int)(pib[n]);
        return answer;
    }

}
