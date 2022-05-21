package silver1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Q3885_GrayArea {
    static FastReader scan = new FastReader();
    static StringBuffer sb = new StringBuffer();

    private static boolean input() {
        valCnt = scan.nextInt();
        w = scan.nextInt();
        if (valCnt == 0 && w == 0) {
            return false;
        }
        vals = new ArrayList<>();
        maxVal = 0;
        for (int i = 0; i < valCnt; i++) {
            int val = scan.nextInt();
            vals.add(val);
            maxVal = Math.max(maxVal, val);
        }
        graph = new int[(maxVal / w) + 1];
        return true;
    }

    static int valCnt, w, maxVal;
    static List<Integer> vals;
    static int[] graph;


    private static void sol() {
        int maxHeight = 0;
        for (Integer val : vals) {
            maxHeight = Math.max(maxHeight, ++graph[val / w]);
        }

        double ans = 0.01;
//        System.out.println("Arrays.toString(graph) = " + Arrays.toString(graph));
        for (int i = 0; i < graph.length; i++) {
            int h = graph[i];
            if (h == 0) {
                continue;
            }
            int bunmo = graph.length-1;
//            System.out.println("h = " + h);
//            System.out.println("maxHeight = " + maxHeight);
//            System.out.println("(double)h/maxHeight = " + (double) h / maxHeight);
//            System.out.println("bunmo = " + bunmo);
//            System.out.println("i = " + i);
            double color = (bunmo - i) / ((double) bunmo );
//            System.out.println("color = " + color);

            ans += (h / (float) (maxHeight)) * color;
        }
        sb.append(ans).append("\n");
    }

    public static void main(String[] args) {
        while (true) {
            if (!input()) {
                break;
            }
            sol();
        }
        System.out.println(sb.toString());
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
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
