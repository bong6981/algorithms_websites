package level2;

import java.util.Arrays;

public class HIndex {
    public static void main(String[] args) {
        System.out.println(solution(new int[]{3, 0, 6, 1, 5}));
    }

    public static int solution(int[] citations) {
        Arrays.sort(citations);
        int l = citations.length;

        for (int i = 0; i < l; i++) {
           if(citations[i] >= l - i) {
               return l-i;
           }
        }
        return 0;
    }
}
