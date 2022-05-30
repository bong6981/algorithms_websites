package level2;

import java.util.ArrayList;
import java.util.List;

// https://programmers.co.kr/learn/courses/30/lessons/86971?language=java
public class DividingPowerGridIntoTwo {
    public static void main(String[] args) {
        DividingPowerGridIntoTwo e = new DividingPowerGridIntoTwo();
        System.out.println(e.solution(4, new int[][]{{1,2},{2,3},{3,4}}));

    }
    public int search(List<List<Integer>> graph, int n1, int n2) {
        int cnt = 0;
        System.out.println(graph);
        System.out.println("n1 = " + n1);
        for(int des : graph.get(n1)) {
            if(des==n2) {
                continue;
            }
            else {
                cnt++;
                cnt += search(graph, des, n1);
            }
        }
        return cnt;
    }

    public int solution(int n, int[][] wires) {
        List<List<Integer>> graph = new ArrayList<>();
        for(int i=0; i<n+1; i++) {
            graph.add(new ArrayList<>());
        }

        for(int[] wire:wires) {
            int n1 = wire[0];
            int n2 = wire[1];
            graph.get(n1).add(n2);
            graph.get(n2).add(n1);
        }

        int answer = 200;
        for(int[] wire : wires) {
            answer = Math.min(answer, Math.abs(search(graph, wire[0], wire[1]) - search(graph, wire[1], wire[0])));
        }
        return answer;
    }
}
