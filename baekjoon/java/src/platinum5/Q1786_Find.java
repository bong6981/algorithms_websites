package platinum5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

//https://www.acmicpc.net/problem/1786
public class Q1786_Find {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] text = br.readLine().toCharArray();
        char[] pattern = br.readLine().toCharArray();

        // make Fail Table;
        int pl = pattern.length;
        int[] fail = new int[pl];
        int j = 0;
        for (int i = 1; i < pl; i++) {
            while (j > 0 && pattern[i] != pattern[j]) {
                j = fail[j - 1];
            }
            if (pattern[i] == pattern[j]) {
                fail[i] = ++j;
            }
        }

        List<Integer> answer = new ArrayList<>();
        int tl = text.length;
        j = 0;
        for (int i = 0; i < tl; i++) {
            while (j > 0 && text[i] != pattern[j]) {
                j = fail[j - 1];
            }
            if (text[i] == pattern[j]) {
                if (j == pl - 1) {
                    answer.add(i - pl + 2);
                    j = fail[j];
                } else {
                    j++;
                }
            }
        }

        System.out.println(answer.size());
        for (Integer integer : answer) {
            System.out.print(integer + " ");
        }
    }

}
