package silver5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// https://www.acmicpc.net/problem/1620
public class Q1629_ImAMasterOfPocketmon {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);

        List<String> stringList = new ArrayList<>();
        stringList.add("");
        Map<String, Integer> stringIntegerMap = new HashMap<>();

        for (int i = 1; i <= n; i++) {
            String s1 = br.readLine();
            stringList.add(s1);
            stringIntegerMap.put(s1, i);
        }

        for (int i = 0; i < m; i++) {
            String s1 = br.readLine();
            try {
                int i1 = Integer.parseInt(s1);
                System.out.println(stringList.get(i1));
            } catch (NumberFormatException exception) {
                System.out.println(stringIntegerMap.get(s1));
            }
        }
    }
}
