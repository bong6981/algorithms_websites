// https://www.acmicpc.net/problem/10000
package platinum4;

import java.io.*;
import java.util.*;

public class CircleArea {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        points = new PointInfo[N*2];
        for (int i = 0; i < N; i++) {
            int x = scan.nextInt();
            int r = scan.nextInt();
            points[i*2] = new PointInfo(-1, x-r);
            points[i*2+1] = new PointInfo(1, x+r);
        }
    }

    static class PointInfo {
        //왼쪽 -1, 오른쪽 1
        int part;
        int position;

        public PointInfo(int part, int position) {
            this.part = part;
            this.position = position;
        }
    }

    static int N;
    static PointInfo[] points;
    static Comparator<PointInfo> comparator = new Comparator<PointInfo>() {
        @Override
        public int compare(PointInfo o1, PointInfo o2) {
            if(o1.position == o2.position) {
                return o2.part - o1.part;
            }
            return o1.position - o2.position;
        }
    };

    static void sol() {
        Arrays.sort(points, comparator);
        Stack<PointInfo> stack = new Stack<>();
        int ans = 1;
        for (PointInfo point : points) {
            if(point.part == -1) {
                stack.add(point);
                continue;
            }

            int lengthSum = 0;
            while(!stack.isEmpty()) {
                PointInfo prev = stack.pop();
                if(prev.part == 0) {
                    lengthSum += prev.position;
                } else {
                    int length =  point.position - prev.position;
                    if(lengthSum == length) {
                        ans += 2;
                    } else {
                        ans++;
                    }
                    stack.add(new PointInfo(0, length));
                    break;
                }
            }
        }
        System.out.println(ans);
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
