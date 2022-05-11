package easy;

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
public class Q121_BestTimeToBuyAndSellStock {
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
//        System.out.println(maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
//        System.out.println(maxProfit(new int[]{7, 6, 4, 3, 1}));
        System.out.println(maxProfit(new int[]{1, 2}));
    }

    public static int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }
        int max_v = prices[prices.length - 1];
        int ans = 0;
        for (int i = prices.length - 2; i >= 0; i--) {
            ans = Math.max(max_v - prices[i], ans);
            max_v = Math.max(max_v, prices[i]);
        }
        return ans;
    }
}
