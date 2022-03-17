package silver4;

import java.io.*;
import java.util.*;

// https://www.acmicpc.net/problem/1015
public class Q1015_SortSequence {
    static StringBuilder sb = new StringBuilder();
    static FastReader scan = new FastReader();

    static class Elem implements Comparable<Elem> {
        public int num, idx;

        @Override
        public int compareTo(Elem other) {
            // if (this.num == other.num) retrun this.idx = other.idx 안해도 되는 이유는 stable
            return num - other.num;
        }
    }

    // 호석님 풀이
    static int N;
    static int[] P;
    static Elem[] B;

    static void input_ho() {
        N = scan.nextInt();
        B = new Elem[N];
        P = new int[N];
        for (int i = 0; i < N; i++) {
            B[i] = new Elem();
            B[i].num = scan.nextInt();
            B[i].idx = i;
        }
    }

    static void pro_ho() {
        Arrays.sort(B);
        for (int i = 0; i < N; i++) {
            P[B[i].idx] = i;
        }
        for (int i = 0; i < N; i++) {
            sb.append(P[i]).append(' ');
        }
        System.out.println(sb.toString());
    }

    public static void main(String[] args) {
        input_ho();
        pro_ho();
    }

    //아래는 내가 풀었던 방식

    static void input() {
        N = scan.nextInt();
        a = new int[N];
        b = new int[N];
        for(int i=0; i<N; i++) {
            a[i] = scan.nextInt();
            b[i] = a[i];
        }
    }

    static void sol() {
        Arrays.sort(b);
        int before = 0;
        Map<Integer, Queue<Integer>> info = new HashMap<>();
        for(int i= 0; i<N; i++) {
            int num = b[i];
            if(num != before) {
                Queue<Integer> queue = new LinkedList<>();
                queue.add(i);
                info.put(num, queue);
            } else {
                info.get(num).add(i);
            }
            before = num;
        }

        for (int i = 0; i < N; i++) {
            Queue<Integer> queue = info.get(a[i]);
            sb.append(queue.poll()).append(' ');
        }
    }

//    static int N;
    static int[] a;
    static int[] b;

//    public static void main(String[] args) {
//        input();
//        sol();
//        System.out.println(sb.toString());
//    }

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
            while( st == null || !st.hasMoreElements()) {
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
