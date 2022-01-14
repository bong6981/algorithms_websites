package level2.kakao.kakao2020;

import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/67257
public class MaximizeTheFormula {
    public static void main(String[] args) {
        MaximizeTheFormula mtf = new MaximizeTheFormula();
        System.out.println(mtf.solution("100-200*300-500+20"));
    }

    public long solution(String expression) {
        Character[][] operations = new Character[][]{{'+', '-', '*'}, {'+', '*', '-'}, {'-', '+', '*'}, {'-', '*', '+'}, {'*', '+', '-'}, {'*', '-', '+'}};
        String[] splitStrings = expression.split("\\+|-|\\*");
        Long[] numbers = new Long[splitStrings.length];
        for (int i = 0; i < splitStrings.length; i++) {
            numbers[i] = Long.parseLong(splitStrings[i]);
        }
        int idx = 0;
        Map<Character, List<Integer>> usedOperations = new HashMap<>();
        for (Character c : expression.toCharArray()) {
            if (Character.isDigit(c)) {
                continue;
            }
            usedOperations.computeIfAbsent(c, v -> new ArrayList<>()).add(idx);
            idx++;
        }

        long answer = 0;

        for (Character[] operation : operations) {
            boolean[] used = new boolean[numbers.length];
            List<Long> temp_numbers = new ArrayList<>(Arrays.asList(numbers));
            for (Character op : operation) {
                if (usedOperations.containsKey(op)) {
                    List<Integer> operationsIdxs = usedOperations.get(op);
                    Collections.sort(operationsIdxs);
                    for (Integer operationsIdx : operationsIdxs) {
                        int prev = -1;
                        int next = -1;
                        for (int i = operationsIdx; i >= 0; i--) {
                            if (!used[i]) {
                                prev = i;
                                break;
                            }
                        }
                        for (int i = operationsIdx + 1; i < numbers.length; i++) {
                            if (!used[i]) {
                                next = i;
                                break;
                            }
                        }
                        if (op == '+') {
                            temp_numbers.set(prev, temp_numbers.get(prev) + temp_numbers.get(next));
                        } else if (op == '-') {
                            temp_numbers.set(prev, temp_numbers.get(prev) - temp_numbers.get(next));
                        } else {
                            temp_numbers.set(prev, temp_numbers.get(prev) * temp_numbers.get(next));
                        }
                        temp_numbers.set(next, 0L);
                        used[next] = true;
                    }
                }
            }
            answer = Math.max(answer, Math.abs(temp_numbers.get(0)));
        }
        return answer;
    }
}
