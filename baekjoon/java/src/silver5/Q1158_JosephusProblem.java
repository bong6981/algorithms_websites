package silver5;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Q1158_JosephusProblem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        List<Integer> collect = IntStream.range(1, n+1).boxed().collect(Collectors.toList());
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int toDelete = (k-1) % collect.size();
            answer.add(collect.get(toDelete));
            List<Integer> newCollect = collect.subList(toDelete+1, collect.size());
            newCollect.addAll(collect.subList(0, toDelete));
            collect = newCollect;
        }
        String a = answer.toString();
        System.out.println("<" + a.substring(1, a.length()-1)+ ">");
    }
}
