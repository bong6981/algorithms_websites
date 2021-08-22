package level2;

import java.util.*;
import java.util.stream.Collectors;

public class Printers {
    public static void main(String[] args) {
        System.out.println(solution(new int[]{2, 1, 3, 2},2));
        System.out.println(solution(new int[]{1, 1, 9, 1, 1, 1},0));

    }

    //파이썬 풀이보고 구현함
    public static int solution(int[] priorities, int location) {
        Queue<Integer> queue = new LinkedList<>(Arrays.stream(priorities).boxed().collect(Collectors.toList()));

        List<Integer> max = Arrays.stream(priorities)
                .boxed()
                .sorted(Comparator.reverseOrder())
                .collect(Collectors.toList());

        int answer = 0;
        while (true) {
            int c = queue.poll();
            if (c == max.get(0)) {
                answer++;
                if (location == 0) {
                    break;
                } else {
                    location--;
                }
                max.remove(0);
            } else {
                queue.offer(c);
                if (location == 0) {
                    location = queue.size() - 1;
                } else {
                    location--;
                }
            }
        }
        return answer;
    }
}
