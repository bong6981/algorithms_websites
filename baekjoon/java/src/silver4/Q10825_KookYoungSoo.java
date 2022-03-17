package silver4;

import java.io.*;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q10825_KookYoungSoo {
    static StringBuilder sb = new StringBuilder();
    static FastReader scan = new FastReader();

    static class Data implements Comparable<Data> {
        String name;
        int kook, young, soo;

        public Data(String name, int kook, int young, int soo) {
            this.name = name;
            this.kook = kook;
            this.young = young;
            this.soo = soo;
        }

        @Override
        public int compareTo(Data other) {
            if (this.kook == other.kook) {
                if (this.young == other.young) {
                    if (this.soo == other.soo) {
                        return this.name.compareTo(other.name);
                    }
                    return other.soo - this.soo;
                }
                return this.young - other.young;
            }
            return other.kook - this.kook;
        }
    }

    static void input() {
        N = scan.nextInt();
        data = new Data[N];
        for (int i = 0; i < N; i++) {
            data[i] = new Data(scan.next(), scan.nextInt(), scan.nextInt(), scan.nextInt());
        }
    }

    static void sol() {
        Arrays.sort(data);
        for(Data d : data) {
            sb.append(d.name).append('\n');
        }
    }

    static int N;
    static Data[] data;

    public static void main(String[] args) {
        input();
        sol();
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
