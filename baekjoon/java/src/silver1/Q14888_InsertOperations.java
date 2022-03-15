package silver1;

import java.io.*;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/14888
public class Q14888_InsertOperations {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        nums = new int[N + 1];
        operators = new int[5];
        order = new int[N + 1];

        for (int i = 1; i <= N; i++) nums[i] = scan.nextInt();
        for (int i = 1; i <= 4; i++) operators[i] = scan.nextInt();

        max = Integer.MIN_VALUE;
        min = Integer.MAX_VALUE;
    }

    static int N, max, min;
    static int[] nums, operators, order;

    static int calculate(int operand1, int operator, int operand2) {
        if (operator == 1) {
            return operand1 + operand2;
        }
        else if (operator == 2) {
            return operand1 - operand2;
        }
        else if (operator == 3) {
            return operand1 * operand2;
        }
        else {
            return operand1 / operand2;
        }
    }

    static void rec_func(int k, int val) {
        if (k == N) {
            max = Math.max(max, val);
            min = Math.min(min, val);
            return;
        }
        for (int cand = 1; cand <= 4; cand++) {
            if (operators[cand] >= 1) {
                operators[cand]--;
                rec_func(k+1, calculate(val, cand, nums[k+1]));
                operators[cand]++;
            }
        }
    }

    //// === 이전 버전 (아래) === ///

    static int calculate() {
        int value = nums[1];
        for (int i = 1; i <= N - 1; i++) {
            if (order[i] == 1) {
                value += nums[i + 1];
            }
            if (order[i] == 2) {
                value -= nums[i + 1];
            }
            if (order[i] == 3) {
                value *= nums[i + 1];
            }
            if (order[i] == 4) {
                value /= nums[i + 1];
            }
        }
        return value;
    }

    static void rec_func(int k) {
        if (k == N) {
            int value = calculate();
            max = Math.max(max, value);
            min = Math.min(min, value);
            return;
        }

        for (int cand = 1; cand <= 4; cand++) {
            if (operators[cand] >= 1) {
                operators[cand]--;
                order[k] = cand;
                rec_func(k + 1);
                operators[cand]++;
                order[k] = 0;
            }
        }
    }

    public static void main(String[] args) {
        input();
        rec_func(1, nums[1]);
        sb.append(max).append('\n').append(min);
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
