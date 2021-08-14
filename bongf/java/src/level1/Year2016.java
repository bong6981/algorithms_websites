package level1;

import java.time.LocalDate;

public class Year2016 {
    public static void main(String[] args) {
        System.out.println(solution2(5, 24));
    }

    public static String solution(int a, int b) {
        String[] split = "FRI,SAT,SUN,MON,TUE,WED,THU".split(",");
        int days = b;

        if (a != 1) {
            for (int i = 1; i < a; i++) {
                if(i==2) {
                    days += 29;
                } else if (i == 4 || i == 6 || i == 9 | i == 11) {
                    days += 30;
                } else  {
                    days += 31;
                }
            }
        }
        return split[( days - 1 ) % 7];
    }

    public static String solution2(int a, int b) {
       return LocalDate.of(2016, a, b).getDayOfWeek().toString().substring(0,3);
    }
}
