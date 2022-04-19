// https://www.acmicpc.net/problem/5639
package gold5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Q5639_BinarySearchTree {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static void input() throws IOException {
        String str;
        while ((str = br.readLine()) != null && !str.equals("")) {
            numbers.add(Integer.parseInt(str));
        }
    }

    static List<Integer> numbers = new ArrayList<>();

    static void sol() {
        search(0, numbers.size() - 1);
    }

    static void search(int start, int end) {
        if (start > end) {
            return;
        }
        if (start == end) {
            sb.append(numbers.get(start)).append("\n");
            return;
        }

        int point = numbers.get(start++);
        int left = start, right = end;
        int mid = lowerbound(left, right, point);
        if (mid > end) {
            search(start, end);
        } else {
            search(start, mid - 1);
            search(mid, end);
        }
        sb.append(point).append("\n");
    }

    static int lowerbound(int start, int end, int point) {
        int ans = end + 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (numbers.get(mid) >= point) {
                ans = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return ans;
    }

    public static void main(String[] args) throws IOException {
        input();
        sol();
        System.out.println(sb.toString());
    }
}
