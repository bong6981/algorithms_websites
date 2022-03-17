package silver5;

import java.io.*;
import java.util.*;

public class Q15970_DrawingArrow {
    static FastReader scan = new FastReader();

    // 류호석님 풀이 //
    static int n;
    static ArrayList<Integer>[] a;

    static void input_ho() {
        n = scan.nextInt();
        a = new ArrayList[n+1];
        for (int color = 1; color <= n; color++) {
            a[color] = new ArrayList<Integer>();
        }
        for (int i = 1; i <= n; i++) {
            int coord = scan.nextInt();
            int color = scan.nextInt();
            a[color].add(coord);
        }
    }

    static int toLeft(int color, int idx) {
        if(idx==0) return Integer.MAX_VALUE;
        return a[color].get(idx) - a[color].get(idx-1);
    }

    static int toRight(int color, int idx) {
        if(idx==a[color].size()-1) return Integer.MAX_VALUE;
        return a[color].get(idx+1) - a[color].get(idx);
    }

    static void pro_ho() {
        for (int color = 1; color <= n; color++) {
            Collections.sort(a[color]);
        }

        int ans = 0;
        for (int color = 1; color <= n; color++) {
            for (int i = 0; i < a[color].size(); i++) {
                int left = toLeft(color, i);
                int right = toRight(color, i);
                ans += Math.min(left, right);
            }
        }

        System.out.println(ans);
    }


    //풀었던 것 (아래) //

    static class Elem {
        public int position, color;
    }

    static int N;
    static Elem[] points;
    static int MAX_POINT = 100000;
    static int[] color, answer;


    static void input() {
        N = scan.nextInt();
        color = new int[N + 1];
        Arrays.fill(color, -1);
        points = new Elem[N];
        for (int i = 0; i < N; i++) {
            points[i] = new Elem();
            points[i].position = scan.nextInt();
            points[i].color = scan.nextInt();
        }
        answer = new int[MAX_POINT];
    }

    static void sol() {
        Arrays.sort(points, Comparator.comparing(p -> p.position));
        for (Elem p : points) {
            if (color[p.color] != -1) {
                answer[p.position] = p.position - color[p.color];
            }
            color[p.color] = p.position;
        }

        Arrays.fill(color, -1);
        for (int i = N - 1; i >= 0; i--) {
            Elem p = points[i];
            if (color[p.color] != -1) {
                if (answer[p.position] == 0 || answer[p.position] > color[p.color] - p.position) {
                    answer[p.position] = color[p.color] - p.position;
                }
            }
            color[p.color] = p.position;
        }

        System.out.println(Arrays.stream(answer).sum());
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
