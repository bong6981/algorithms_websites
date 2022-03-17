package silver5;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

//https://www.acmicpc.net/problem/11652
public class Q11652_Card {
    static StringBuilder sb = new StringBuilder();
    static FastReader scan = new FastReader();

    static int N;
    static long[] nums;


    // == 류호석님 풀이 == //

    static void input_ho() {
        N = scan.nextInt();
        nums = new long[N + 1];
        for (int i = 1; i <= N; i++) nums[i] = scan.nextLong();
    }

    static void pro_ho() {
        Arrays.sort(nums, 1, N + 1);

        long mode = nums[1];
        int modeCnt = 1, curCnt = 1;

        for (int i = 2; i <= N; i++) {
            if (nums[i] == nums[i - 1]) {
                curCnt++;
            } else {
                curCnt = 1;
            }

            if (modeCnt < curCnt) {
                modeCnt = curCnt;
                mode = nums[i];
            }
        }

        System.out.println(mode);
    }

    // == 내가 푼 풀이 == //

    static void input() {
        N = scan.nextInt();
        nums = new long[N];
        for (int i = 0; i < nums.length; i++) nums[i] = scan.nextLong();
    }

    static void sol() {
        Arrays.sort(nums);
        int ansCnt = 0;
        long ans = 0;
        int cnt = 0;
        long before = -(long) Math.pow(2, 62) - 1;
        for (long num : nums) {
            if (num == before) {
                cnt++;
            } else {
                if (cnt > ansCnt) {
                    ansCnt = cnt;
                    ans = before;
                }
                cnt = 1;
                before = num;
            }
        }
        if (cnt > ansCnt) {
            ansCnt = cnt;
            ans = before;
        }
        System.out.println(ans);
    }

    public static void main(String[] args) {
//        input();
//        sol();
        input_ho();
        pro_ho();
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
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

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
