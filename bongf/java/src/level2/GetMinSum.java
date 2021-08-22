package level2;

import java.util.Arrays;
import java.util.Comparator;

public class GetMinSum {
    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 4, 2}, new int[]{4, 4, 5}));
    }

    //자바는 시간초과 4개 전부
    public static int try1(int[] A, int[] B) {
        A = Arrays.stream(A).sorted().toArray();
        B = Arrays.stream(B).boxed().sorted(Comparator.reverseOrder()).mapToInt(x -> x).toArray();
        int answer = 0;
        for (int i = 0; i < A.length; i++) {
            answer += A[i] * B[i];
        }
        return answer;
    }

    // 한 개만 시간초과
    public static int try2(int[] A, int[] B) {
        A = Arrays.stream(A).sorted().toArray();
        B = Arrays.stream(B).sorted().toArray();
        int answer = 0;
        int length = A.length;
        for (int i = 0; i < length; i++) {
            answer += A[i] * B[length - 1 - i];
        }
        return answer;
    }

    public static int solution(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);

        int length = A.length;
        int answer = 0;
        for (int i = 0; i < length; i++) {
            answer += A[i] * B[length - 1 - i];
        }
        return answer;
    }

}
