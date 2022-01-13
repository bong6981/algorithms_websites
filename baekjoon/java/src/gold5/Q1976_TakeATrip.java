package gold5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// https://www.acmicpc.net/problem/1976
public class Q1976_TakeATrip {
    private static int[] parents;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }

        for (int i = 0; i < n; i++) {
            String[] inputString = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                if (inputString[j].equals("1")) {
                    union(i, j);
                }
            }
        }

        int[] trips = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int root = findParent(trips[0]-1);
        for (int i = 1; i < m; i++) {
            if(findParent(trips[i]-1) != root) {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }

    private static int findParent(int x) {
        if (parents[x] != x) {
            parents[x] = findParent(parents[x]);
        }
        return parents[x];
    }

    private static void union(int x, int y) {
        x = findParent(x);
        y = findParent(y);
        if (x < y) {
            parents[y] = x;
            return;
        }
        parents[x] = y;
    }
}
