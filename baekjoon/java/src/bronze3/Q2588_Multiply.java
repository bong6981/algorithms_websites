package bronze3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// https://www.acmicpc.net/problem/2588
public class Q2588_Multiply {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int input1 = Integer.parseInt(br.readLine());
        int input2 = Integer.parseInt(br.readLine());

        System.out.println(input2 % 10 * input1);
        System.out.println(input2 / 10 % 10 * input1);
        System.out.println(input2 / 100 * input1);
        System.out.println(input2 * input1);
    }
}
