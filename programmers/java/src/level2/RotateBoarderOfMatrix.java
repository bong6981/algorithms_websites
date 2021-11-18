package level2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class RotateBoarderOfMatrix {
    public static void main(String[] args) {
        RotateBoarderOfMatrix rotateBoarderOfMatrix = new RotateBoarderOfMatrix();
//        String a = "[[2,2,5,4],[3,3,6,6],[5,1,6,3]]";
//        a = a.replace("[", "{");
//        a = a.replace("]", "}");
//        System.out.println(a);
        System.out.println(Arrays.toString(rotateBoarderOfMatrix.solution(6, 6, new int[][]{{2,2,5,4},{3,3,6,6},{5,1,6,3}})));

    }

    public int[] solution(int rows, int columns, int[][] queries) {
        int[][] graph = new int[rows][columns];
        for(int i=0; i<rows; i++) {
            for(int j=0; j<columns; j++) {
                graph[i][j] = i * columns + j + 1;
            }
        }

        int[] answer = new int[queries.length];

        for (int k =0; k< queries.length; k++) {
            int[] query = queries[k];
            int x1 = query[0] -1;
            int y1 = query[1] -1;
            int x2 = query[2] -1;
            int y2 = query[3] -1;

            List<Integer> stack = new ArrayList<>();
            stack.add(graph[x1][y1]);
            for (int i = y1+1; i < y2+1; i++) {
                stack.add(graph[x1][i]);
                graph[x1][i] = stack.get(stack.size()-2);
            }

            for(int i=x1+1; i<x2+1; i++) {
                stack.add(graph[i][y2]);
                graph[i][y2] = stack.get(stack.size()-2);
            }

            for(int i=y2-1; i>y1-1; i--) {
                stack.add(graph[x2][i]);
                graph[x2][i] = stack.get(stack.size()-2);
            }

            for(int j=x2-1; j>x1-1; j--) {
                stack.add(graph[j][y1]);
                graph[j][y1] = stack.get(stack.size()-2);
            }

            answer[k] = Collections.min(stack);
        }
        return answer;
    }
}
