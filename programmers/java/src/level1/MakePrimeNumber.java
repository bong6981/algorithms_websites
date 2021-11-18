package level1;

public class MakePrimeNumber {
    private int[] nums;
    private boolean[] selected;
    private int answer = 0;

    public int solution(int[] nums) {
        this.nums = nums;
        this.selected = new boolean[nums.length];
        select(0, 0);
        return answer;
    }

    private void select(int start, int cnt) {
        if (cnt == 3) {
            int sum = 0;
            for (int i = 0; i < selected.length; i++) {
                if (selected[i]) {
                    sum += nums[i];
                }
            }
            if (isPrime(sum)) {
                answer++;
            }
            return;
        }

        for (int i = start; i < selected.length; i++) {
            selected[i] = true;
            cnt += 1;
            select(i + 1, cnt);
            cnt -= 1;
            selected[i] = false;
        }

    }

    private boolean isPrime(int x) {
        if (x == 0) {
            return false;
        }
        if (x == 1) {
            return false;
        }
        for (int i = 2; i <= (int) Math.sqrt(x); i++) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }

    //I did with backtracking for combinations
    //But it's better to use tri-for? like bleow;
    public int solution2(int[] nums) {
        int ans = 0;

        for(int i = 0; i < nums.length - 2; i ++){
            for(int j = i + 1; j < nums.length - 1; j ++){
                for(int k = j + 1; k < nums.length; k ++ ){
                    if(isPrime(nums[i] + nums[j] + nums[k])){
                        ans += 1;
                    }
                }
            }
        }
        return ans;
    }
}
