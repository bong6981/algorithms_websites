package platinum2;

import java.io.*;
import java.util.*;

public class Q2261_ClosestTwoPoints {
    static FastReader scan = new FastReader();

    static void input() {
        N = scan.nextInt();
        points = new Position[N];
        for (int i = 0; i < N; i++) {
            int r = scan.nextInt();
            int c = scan.nextInt();
            points[i] = new Position(r, c);
        }
        minDis = MAX_DIS;
    }

    static class Position {
        int x;
        int y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int N;
    static Position[] points;
    static int minDis;
    static int MAX_DIS = (int) Math.pow(40000, 2);

    static void sol() {
        Arrays.sort(points, Comparator.comparing(p -> p.x));
        System.out.println(findMinDis(0, N-1));
    }

    private static int findMinDis(int start, int end) {
        if (start == end) {
            return MAX_DIS;
        }
        if (end - start == 1) {
            return (int) (Math.pow((points[start].x - points[end].x), 2) +
                    Math.pow((points[start].y - points[end].y), 2));
        }

        int mid = (start + end) / 2;
        int ans = Math.min(findMinDis(start, mid), findMinDis(mid + 1, end));

        List<Position> candidates = new ArrayList<>();
        int midX = points[mid].x;
        for (int i = start; i <= end; i++) {
            int xDis = midX - points[i].x;
            if (xDis * xDis < ans) {
                candidates.add(points[i]);
            }
        }

        candidates.sort(Comparator.comparing(p -> p.y));
        for (int i = 0; i < candidates.size() - 1; i++) {
            Position p1 = candidates.get(i);
            for (int j = i + 1; j < candidates.size(); j++) {
                Position p2 = candidates.get(j);
                int dis = p2.y - p1.y;
                if(dis * dis >= ans) {
                    break;
                }
                ans = Math.min(ans, (int) (Math.pow((p1.x - p2.x), 2) + dis * dis));
            }
        }
        return ans;
    }

    public static void main(String[] args) throws IOException{
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
