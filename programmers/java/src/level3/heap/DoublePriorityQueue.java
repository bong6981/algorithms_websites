package level3.heap;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

// https://programmers.co.kr/learn/courses/30/lessons/42628
public class DoublePriorityQueue {
    public static void main(String[] args) {
        DoublePriorityQueue dpq = new DoublePriorityQueue();
        System.out.println(Arrays.toString(dpq.solution(new String[]{"I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"})));
    }

    public int[] solution(String[] operations) {
        PriorityQueue<Integer> minPq = new PriorityQueue<>();
        PriorityQueue<Integer> maxPq = new PriorityQueue<>();
        Map<Integer, Integer> nums = new HashMap<>();
        int cnt = 0;
        for (String operation : operations) {
            System.out.println("operation = " + operation);
            String[] opStrings = operation.split(" ");
            String op = opStrings[0];
            int num = Integer.parseInt(opStrings[1]);

            if (op.equals("I")) {
                minPq.add(num);
                maxPq.add(-num);
                cnt++;
                nums.compute(num, (k, v) -> (v == null) ? 1 : v + 1);
            } else {
                if (cnt == 0) {
                    continue;
                }
                if (num == 1) {
                    int n = -maxPq.poll();
                    while (nums.get(n) == 0) {
                        n = -maxPq.poll();
                    }
                    nums.put(n, nums.get(n) - 1);
                    cnt--;
                } else {
                    int n = minPq.poll();
                    while (nums.get(n) == 0) {
                        n = minPq.poll();
                    }
                    nums.put(n, nums.get(n) - 1);
                    cnt--;
                }
            }
        }

        if(cnt == 0) {
            return new int[]{0, 0};
        }
        int maxV = -maxPq.poll();
        while(nums.get(maxV) == 0) {
            maxV = -maxPq.poll();
        }
        int minV = minPq.poll();
        while(nums.get(minV) == 0) {
            minV = minPq.poll();
        }
        return new int[]{maxV, minV};
    }
}
