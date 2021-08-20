package level2;

import java.util.Arrays;
import java.util.Stack;

public class FunctionDevelopment {
    public static void main(String[] args) {
        int[] progresses = {93, 30, 55};
        int[] speeds = {1, 30, 5};
        System.out.println(Arrays.toString(solution2(progresses, speeds)));
    }

    public static int[] solution(int[] progresses, int[] speeds) {
        Stack<Integer> answer = new Stack<>();
        Stack<Integer> stack = new Stack<>();
        stack.push(0);

        for (int i = 0; i < progresses.length; i++) {
            int p = progresses[i];
            int s = speeds[i];
            int d = (100 - p) % s == 0 ? (100 - p) / s : (int) ((100 - p) / s) + 1;

            if (stack.peek() < d) {
                stack.pop();
                stack.push(d);
                answer.push(1);
            } else {
                answer.push(answer.pop() + 1);
            }
        }
        return answer.stream().mapToInt(Integer::valueOf).toArray();
    }

    public static int[] solution2(int[] progresses, int[] speeds) {
        int[] dayOfEnd = new int[100];
        int day = -1;
        for(int i=0; i<progresses.length; i++) {
            while(progresses[i] + (day*speeds[i]) < 100) {
                day++;
            }
            dayOfEnd[day]++;
        }
        return Arrays.stream(dayOfEnd).filter(i -> i!=0).toArray();
    }
}
