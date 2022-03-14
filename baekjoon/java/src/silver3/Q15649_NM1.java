package silver3;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/15649
public class Q15649_NM1 {
    static StringBuilder sb = new StringBuilder();

    static void input() {
        FastReader scan = new FastReader();
        N = scan.nextInt();
        M = scan.nextInt();
        selected = new int[M + 1];
        used = new int[N+1];
    }

    static int N, M;
    static int[] selected, used;

    static void recFunc(int k) {
        if (k == M + 1) {
            for (int i = 1; i <= M; i++) sb.append(selected[i]).append(' ');
            sb.append('\n');
            return;
        }

        for (int cand = 1; cand <= N; cand++) {
            if (used[cand] == 1) continue;
            selected[k] = cand;
            used[cand] = 1;
            recFunc(k + 1);
            selected[k] = 0;
            used[cand] = 0;
        }
    }

    static void recFunc_firstTry(int k) {
        if (k == M + 1) {
            for (int i = 1; i <= M; i++) sb.append(selected[i]).append(' ');
            sb.append('\n');
            return;
        }

        for (int cand = 1; cand <= N; cand++) {
            boolean isUsed = false;
            for (int i = 1; i < k; i++) {
                if (cand == selected[i]) {
                    isUsed = true;
                }
            }
            if (!isUsed) {
                selected[k] = cand;
                recFunc(k + 1);
                selected[k] = 0;
            }
        }
    }

    public static void main(String[] args) {
        input();
        recFunc(1);
        System.out.println(sb.toString());
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
            while (st == null || !st.hasMoreTokens()) {
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

    private static List<Integer[]> answer;
    private static int m;
    private static int n;


    public static void main_before(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        answer = new ArrayList<>();
        back_tracking(new ArrayList<>());

        for (Integer[] integers : answer) {
            for (Integer integer : integers) {
                System.out.print(integer + " ");
            }
            System.out.println();
        }
    }

    public static void back_tracking(List<Integer> now) {
        if (now.size() == m) {
            Integer[] toAdd = new Integer[m];
            answer.add(now.toArray(toAdd));
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (now.contains(i)) {
                continue;
            }
            now.add(i);
            back_tracking(now);
            now.remove(now.size() - 1);
        }
    }
}
