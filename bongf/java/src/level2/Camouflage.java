package level2;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import static java.util.stream.Collectors.*;

public class Camouflage {
    public static void main(String[] args) {
        String[][] clothes = new String[][]{{"1"}, {"2"}};
        System.out.println(Arrays.toString(clothes));
    }

    public static int solution(String[][] clothes) {
        Map<String, Integer> organize = new HashMap<>();
        for (String[] item : clothes) {
            if (organize.containsKey(item[1])) {
                organize.put(item[1], organize.get(item[1]) + 1);
            } else {
                organize.put(item[1], 2);
            }
        }
        return organize.values().stream()
                .reduce(1, (x, y) -> x * y) - 1;
    }

    public static int solutionEdit(String[][] clothes) {
        Map<String, Integer> organize = new HashMap<>();
        for (String[] item : clothes) {
            organize.computeIfAbsent(item[1], v -> 1);
            organize.computeIfPresent(item[1], (k, v) -> v + 1);
        }
        return organize.values().stream()
                .reduce(1, (x, y) -> x * y) - 1;
    }

    public static int solution2(String[][] clothes) {
        return Arrays.stream(clothes)
                .collect(groupingBy(p -> p[1], mapping(p -> p[0], counting())))
                .values()
                .stream()
                .reduce(1L, (x, y) -> x * (y + 1)).intValue() - 1;
    }
}
