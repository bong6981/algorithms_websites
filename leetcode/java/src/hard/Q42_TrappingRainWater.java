package hard;

import java.util.Stack;

public class Q42_TrappingRainWater {
    public static int trap(int[] height) {
        Stack<Integer> stack = new Stack<>();
        int ans = 0;
        for (int i = 0; i < height.length; i++) {
            int h = height[i];
            while(!stack.isEmpty() && height[stack.peek()] < h) {
                int now = stack.pop();
                if(stack.isEmpty()) {
                    break;
                }
                ans += (Math.min(height[stack.peek()], h) - height[now]) * (i-stack.peek() -1);
            }
            stack.push(i);
        }
        return ans;
    }



    public static void main(String[] args) {
//        System.out.println(trap(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}));
        System.out.println(trap(new int[]{4,2,0,3,2,5}));
    }
}
