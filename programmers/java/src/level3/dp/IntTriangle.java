package level3.dp;

import java.util.Arrays;
// https://programmers.co.kr/learn/courses/30/lessons/43105?language=java
public class IntTriangle {
    public static void main(String[] args) {
        IntTriangle it = new IntTriangle();
//        String input = "[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]";
//        input = input.replaceAll("\\[", "{").replaceAll("]", "}");
//        System.out.println("input = " + input);
        System.out.println(it.solution(new int[][]{{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}}));
        System.out.println(it.solution(new int[][]{{0}}));

    }

    public int solution(int[][] triangle) {
        int[] prev = triangle[0];
        for (int i = 1; i < triangle.length; i++) {
            int[] t = triangle[i];
            for (int j = 0; j < t.length; j++) {
                if( j == 0) {
                    t[j] += prev[0];
                    continue;
                }
                if ( j == t.length -1 ) {
                    t[j] += prev[j-1];
                    continue;
                }
                t[j] += Math.max(prev[j-1], prev[j]);
            }
            prev = t;
        }
        return Arrays.stream(prev).max().getAsInt();
    }

}
