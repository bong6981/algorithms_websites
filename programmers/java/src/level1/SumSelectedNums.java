package level1;

import java.util.Arrays;

public class SumSelectedNums {
    public static void main(String[] args) {
        int[] numbers = {2,1,3,4,1};
        int[] solution = solution(numbers);
        for (int i = 0; i < solution.length; i++) {
            System.out.println(solution[i]);
        }
    }

    //다른 사람의 풀이중 애초에 set으로 담아서 그것을 배열로 바꿔서 출력하는 것이 더 간단해 보인다.
    public static int[] solution(int[] numbers) {
        int s = (numbers.length * (numbers.length - 1)) / 2;
        int[] r = new int[s];
        int k = 0;

        for (int i = 0; i < numbers.length -1; i++) {
            for (int j = i+1; j < numbers.length; j++) {
                r[k] = (numbers[i] + numbers[j]);
                k++;
            }
        }
        return Arrays.stream(r).distinct().sorted().toArray();
    }
}
