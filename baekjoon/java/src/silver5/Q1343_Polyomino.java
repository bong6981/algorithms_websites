package silver5;

import java.util.Scanner;

// https://www.acmicpc.net/problem/1343
public class Q1343_Polyomino {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        input = input.replaceAll("XXXX", "AAAA").replaceAll("XX", "BB");
        if( input.contains("X") ) {
            System.out.println(-1);
        } else {
            System.out.println(input);
        }
    }
}
