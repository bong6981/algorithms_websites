package silver5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q11728_ConcatenateArrays {
    // stream으로 input 받으면 시간초과
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);
        int[] a = new int[n];
        int[] b = new int[m];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int aIdx = 0;
        while (st.hasMoreTokens()) {
            a[aIdx++] = Integer.parseInt(st.nextToken());
        }
        aIdx = 0;
        st = new StringTokenizer(br.readLine(), " ");
        int bIdx = 0;
        while (st.hasMoreTokens()) {
            b[bIdx++] = Integer.parseInt(st.nextToken());
        }
        bIdx = 0;
        int idx = 0;
        int[] answer = new int[n + m];
        while (true) {
            if (n <= aIdx) {
                System.arraycopy(b, bIdx, answer, idx, answer.length - idx);
                break;
            }
            if (m <= bIdx) {
                System.arraycopy(a, aIdx, answer, idx, answer.length - idx);
                break;
            }

            if (a[aIdx] < b[bIdx]) {
                answer[idx++] = a[aIdx++];
            } else {
                answer[idx++] = b[bIdx++];
            }
        }
        // 이렇게 하면 시간 초과, StringBuilder로 묶어준 후에 해줘야한다. 
//        for (int i : answer) {
//            System.out.print(String.valueOf(i) + " ");
//        }

        StringBuilder answerString = new StringBuilder();
        for (int i : answer) {
            answerString.append(i + " ");
        }
        System.out.print(answerString);
    }
}
