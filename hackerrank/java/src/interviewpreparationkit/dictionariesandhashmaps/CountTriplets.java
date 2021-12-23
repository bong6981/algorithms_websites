package interviewpreparationkit.dictionariesandhashmaps;

import static java.util.stream.Collectors.toList;

import java.io.*;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

// https://www.hackerrank.com/challenges/count-triplets-1/problem
// Medium
public class CountTriplets {

    // Complete the countTriplets function below.
    static long countTriplets(List<Long> arr, long r) {
        Map<Long, Long> map2 = new HashMap<>();
        Map<Long, Long> map3 = new HashMap<>();

        long result = 0L;
        for (Long num : arr) {
            result += map3.getOrDefault(num, 0L);
            map3.put(num * r, map3.getOrDefault(num * r, 0L) + map2.getOrDefault(num, 0L));
            map2.put(num * r, map2.getOrDefault(num*r, 0L) + 1);
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] nr = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(nr[0]);

        long r = Long.parseLong(nr[1]);

        List<Long> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Long::parseLong)
                .collect(toList());

        long ans = countTriplets(arr, r);

        bufferedReader.close();
    }
}
