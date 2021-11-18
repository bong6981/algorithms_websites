package level1;

import java.util.Scanner;
import java.util.stream.IntStream;

public class RectangularStar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        for ( int i = 1; i<= b; i++) {
            for (int j = 1; j <= a; j++) {
                if (j == a ) {
                    System.out.println("*");
                }else {
                    System.out.print("*");
                }
            }
        }
    }

    //for문 대신 횟수만큼 돌리는 방법. 그리고 한줄의 string을 만들어주고 반복
    public static void main2(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        StringBuilder sb = new StringBuilder();
        IntStream.range(0, a).forEach(s -> sb.append("*"));
        IntStream.range(0, b).forEach(s -> System.out.println(sb.toString()));
    }

    //이런식으로 개행 추가하는 방법도 있습니다
    public static void main3(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        for (int i = 0; i < b; i++) {
            for (int j = 0; j < a; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
