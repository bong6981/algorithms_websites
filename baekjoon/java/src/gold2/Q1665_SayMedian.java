package gold2;

import java.io.*;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Q1665_SayMedian {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scan.nextInt();
        }
        maxHeap = new PriorityQueue<>(N, Collections.reverseOrder());
        minHeap = new PriorityQueue<>(N);
    }

    static int N;
    static int[] arr;
    static PriorityQueue<Integer> maxHeap;
    static PriorityQueue<Integer> minHeap;


    static void solve() {
        for(int e : arr) {
            if(maxHeap.size() == minHeap.size()) {
                if(minHeap.size() > 0 && minHeap.peek() < e) {
                    maxHeap.add(minHeap.poll());
                    minHeap.add(e);
                } else {
                    maxHeap.add(e);
                }
            } else {
                if(maxHeap.size() > 0 && maxHeap.peek() > e) {
                    minHeap.add(maxHeap.poll());
                    maxHeap.add(e);
                } else {
                    minHeap.add(e);
                }
            }
            sb.append(maxHeap.peek()).append("\n");
        }
    }

    public static void print() {
        System.out.println(sb.toString());
    }


    public static void main(String[] args) {
        input();
        solve();
        print();
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
