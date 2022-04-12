//https://www.acmicpc.net/problem/6549
package platinum5;

import java.io.*;
import java.util.StringTokenizer;

public class Q6549_BiggestSquare {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        if (N == 0) {
            return;
        }
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scan.nextInt();
        }
    }

    static int N;
    static int[] arr;

    static long sol(int start, int end) {
        if (start == end) {
            return arr[start];
        }

        int mid = (start + end) / 2;
        long ans = Math.max(sol(start, mid), sol(mid + 1, end));
        ans = Math.max(calMid(start, mid, end), ans);
        return ans;
    }

    static long calMid(int start, int mid, int end) {
        int toLeft = mid;
        int toRight = mid;

        int height = arr[mid];
        long maxArea = height;

        while (toLeft != start || toRight != end) {
            if (toLeft == start) {
                toRight++;
            } else if (toRight == end) {
                toLeft--;
            } else if (arr[toLeft - 1] > arr[toRight + 1]) {
                toLeft--;
            } else {
                toRight++;
            }
            height = Math.min(height, Math.min(arr[toRight], arr[toLeft]));
            maxArea = Math.max(maxArea, ((long) height) * (toRight - toLeft + 1));
        }
        return maxArea;
    }

    public static void main(String[] args) {
        while (true) {
            input();
            if (N == 0) {
                break;
            }
            sb.append(sol(0, N - 1)).append("\n");
        }
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
