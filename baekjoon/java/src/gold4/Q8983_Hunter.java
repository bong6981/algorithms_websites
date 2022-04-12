package gold4;


import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q8983_Hunter  {
    static class Position {
        int x, y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        M = scan.nextInt();
        N = scan.nextInt();
        L = scan.nextInt();
        shots = new int[M];
        for (int i = 0; i < M; i++) {
            shots[i] = scan.nextInt();
        }
        animals = new Position[N];
        for (int i = 0; i < N; i++) {
            int x = scan.nextInt();
            int y = scan.nextInt();
            animals[i] = new Position(x, y);
        }
    }

    static int M, N, L;
    static int[] shots;
    static Position[] animals;

    static void sol() {
        int ans = 0;
        Arrays.sort(shots);
        for (Position animal : animals) {
            if(animal.y > L) {
                continue;
            }
            int start = 0;
            int end = shots.length -1;
            int minLength = L + 1;
            int pos = -1;
            while(start <= end) {
                int mid = (start + end) / 2;
                int dis = shots[mid] - animal.x;

                if(Math.abs(dis) < minLength) {
                    minLength = Math.abs(dis);
                    pos = mid;
                }

                if(dis < 0) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }

            if(pos != -1 && Math.abs(shots[pos]-animal.x) + animal.y <= L) {
                ans += 1;
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
