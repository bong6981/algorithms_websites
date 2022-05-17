package silver1;

//https://www.acmicpc.net/problem/16987
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q16987_HitEggWithEgg {
    static FastReader scan = new FastReader();

    static void input() {
        N = scan.nextInt();
        eggs = new int[N][2];
        for (int i = 0; i < N; i++) {
            eggs[i][0] = scan.nextInt();
            eggs[i][1] = scan.nextInt();
        }
    }

    static int N;
    static int answer = 0;
    static int[][] eggs;

    static void hit(int now, int cnt) {
        answer = Math.max(cnt, answer);

        System.out.println("--------------");
        System.out.println("now = " + now);
        System.out.println("cnt = " + cnt);
        System.out.println("Arrays.deepToString(eggs) = " + Arrays.deepToString(eggs));
        
        if(now == N) {
            return;
        }

        System.out.println("eggs[now][0] = " + eggs[now][0]);
        if((eggs[now][0] <= 0) || N-cnt == 1) {
            hit(now+1, cnt);
        } else {

            for (int i = 0; i < N; i++) {
                if(i==now) {
                    continue;
                }

                if(eggs[i][0] <= 0) {
                    continue;
                }

                int originNowW = eggs[now][0];
                int originObjW = eggs[i][0];

                eggs[now][0] = originNowW - eggs[i][1];
                eggs[i][0] = originObjW - eggs[now][1];
                int toAdd = 0;

                if(eggs[now][0] <= 0) {
                    toAdd++;
                }
                if(eggs[i][0] <= 0) {
                    toAdd++;
                }
//            System.out.println("hi!! " + i);
                hit(now+1, cnt+toAdd);

                eggs[now][0] = originNowW;
                eggs[i][0] = originObjW;
            }
        }


    }

    static void sol() {
        int cnt = 0;
        hit(0, 0);
        System.out.println(answer);
    }

    public static void main(String[] args) {
        input();
        sol();
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while(st == null ||!st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

    }
}
