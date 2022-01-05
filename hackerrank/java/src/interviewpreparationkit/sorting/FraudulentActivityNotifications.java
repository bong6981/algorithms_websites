package interviewpreparationkit.sorting;

// https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
import static java.util.stream.Collectors.toList;

import java.io.*;
import java.util.List;
import java.util.stream.Stream;

class Result {

    // fail
    public static int activityNotifications(List<Integer> expenditure, int d) {
        int midIdx1 = d / 2;
        int midIdx2;
        if(d % 2 == 0) {
            midIdx2 = midIdx1 - 1;
        } else {
            midIdx2 = midIdx1;
        }

        int[] count = new int[201];
        for (Integer integer : expenditure) {
            count[integer] += 1;
        }

        int cnt = 0;
        for (int i = d; i < expenditure.size(); i++) {
            int before = expenditure.get(i-d);
            int toAdd = expenditure.get(i);
            if( toAdd >= getMedians(count, midIdx1, midIdx2)) {
                cnt++;
            };

            count[before]--;
            count[toAdd]++;
        }

        return cnt;
    }

    private static int getMedians(int[]count, int midIdx1, int midIdx2) {
        long acc = 0L;
        long ansIdx2 = -1L;
        for (int i = 0; i < count.length; i++) {
            acc += count[i];
            if( ansIdx2 == -1L && acc > midIdx2) {
                if( acc > midIdx1) {
                    return i * 2;
                }
                ansIdx2 = i + 0L;
            }
            if( acc > midIdx1) {
                return (int) ansIdx2 + i;
            }
        }
        return -1;
    }
}

public class FraudulentActivityNotifications {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);
        int d = Integer.parseInt(firstMultipleInput[1]);

        List<Integer> expenditure = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int result = Result.activityNotifications(expenditure, d);
        bufferedReader.close();

        System.out.println(result);
    }
}
