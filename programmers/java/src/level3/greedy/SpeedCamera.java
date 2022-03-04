package level3.greedy;

import java.util.*;
//https://programmers.co.kr/learn/courses/30/lessons/42884?language=java
public class SpeedCamera {

    public static void main(String[] args) {
        SpeedCamera sc = new SpeedCamera();
        System.out.println(sc.solution(new int[][]{{-20, -15}, {-14, -5}, {-18, -13}, {-5, -3}}));
    }

    public int solution(int[][] routes) {
        Arrays.sort(routes, Comparator.comparing(route -> route[1]));
        int end = routes[0][1];
        int cnt = 1;
        for(int[] route : routes) {
            if(route[0] > end) {
                cnt++;
                end = route[1];
            }
        }
        return cnt;
    }
}
