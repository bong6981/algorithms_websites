package level1;

import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class DartGame {
    public static void main(String[] args) {
        System.out.println(solution("1S2D*3T"));
        System.out.println(solution("1D2S#10S"));
        System.out.println(solution("1D2S0T"));
        System.out.println(solution("1S*2T*3S"));
        System.out.println(solution("1D#2S*3S"));
        System.out.println(solution("1T2D3D#"));
        System.out.println(solution("1D2S3T*"));
    }

    public static int solution(String dartResult) {
        dartResult = dartResult.replace("10", "k");
        int[] score_arr = new int[3];
        List<String> area = Arrays.asList("S", "D", "T");
        int i = -1;
        for ( String s : dartResult.split("")) {
            if ( area.contains(s) ) {
                score_arr[i] = (int) Math.pow(score_arr[i], area.indexOf(s)+1);
            } else if ( s.equals("*")) {
                score_arr[i] *= 2;
                if (i != 0) {
                    score_arr[i - 1] *= 2;
                }
            } else if (s.equals("#")) {
                score_arr[i] *= -1;
            } else {
                if( s.equals("k")) {
                    s = "10";
                }
                i++;
                score_arr[i] = Integer.parseInt(s);
            }
        }
        return IntStream.of(score_arr).sum();
    }
}
