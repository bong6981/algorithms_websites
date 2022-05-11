package silver4;

import java.io.*;
import java.util.*;

public class Q1764_듣보잡 {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        M = scan.nextInt();
        didntlisten = new HashSet<>();
        didntsee = new HashSet<>();

        for (int i = 0; i < N; i++) {
            didntlisten.add(scan.nextString());
        }

        for (int i = 0; i < M; i++) {
            didntsee.add(scan.nextString());
        }
    }

    static int N, M;
    static Set<String> didntlisten, didntsee;

    static void sol() {
        didntlisten.retainAll(didntsee);
        ArrayList<String> strings = new ArrayList<>(didntlisten);
        Collections.sort(strings);
        sb.append(strings.size()).append("\n");
        for (String string : strings) {
            sb.append(string).append("\n");
        }
        System.out.println(sb.toString());
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
            while(st == null || !st.hasMoreElements()) {
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

        String nextString() {
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
