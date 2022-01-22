package level3.heap;

import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/42627
public class DiskController {
    public static void main(String[] args) {
        String input = "[[0, 3], [1, 9], [2, 6]]";
        input = input.replaceAll("\\[", "{").replaceAll("]", "}");

        DiskController dc = new DiskController();
        System.out.println(input);
        System.out.println(dc.solution(new int[][]{{0, 3}, {1, 9}, {2, 6}}));
    }

    public int solution(int[][] jobs) {

        Arrays.sort(jobs, Comparator.comparing(x -> x[0]));
        Queue<Integer[]> queue = new LinkedList<>();

        for (int[] job : jobs) {
            queue.add(Arrays.stream(job).boxed().toArray(Integer[]::new));
        }

        PriorityQueue<Integer[]> pq = new PriorityQueue<>(new Comparator<Integer[]>() {
            @Override
            public int compare(Integer[] integers, Integer[] t1) {
                return integers[1] - t1[1];
            }
        });

        pq.offer(queue.poll());
        int now = 0;
        int wait = 0;

        while (!pq.isEmpty()) {
            Integer[] job = pq.poll();
            int dur = job[1];
            int start = job[0];
            now = Math.max(now + dur, start + dur);
            wait += now - start;
            while (!queue.isEmpty() && queue.peek()[0] <= now) {
                pq.offer(queue.poll());
            }
            if (!queue.isEmpty() && pq.isEmpty()) {
                pq.offer(queue.poll());
            }
        }

        return wait / jobs.length;


    }

    // https://programmers.co.kr/learn/courses/30/lessons/42627/solution_groups?language=java
    private int solution_other(int[][] jobs) {

        Arrays.sort(jobs, new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                if (o1[0] <= o2[0]) {
                    return -1;
                }
                return 1;
            }
        });

        PriorityQueue<int[]> queue = new PriorityQueue<int[]>(new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                if (o1[1] < o2[1]) {
                    return -1;
                }
                return 1;
            }
        });

        int time = 0;
        int index = 0;
        float answer = 0;

        while (true) {
            while (index < jobs.length && jobs[index][0] <= time) {
                queue.offer(jobs[index]);
                index++;
            }
            if (queue.size() == 0) {
                time = jobs[index][0];
                continue;
            }
            int[] job = queue.poll();
            time += job[1];
            answer += time - job[0];
            if (index == jobs.length && queue.size() == 0) {
                break;
            }
        }

        answer /= jobs.length;
        return (int) answer;
    }
}
