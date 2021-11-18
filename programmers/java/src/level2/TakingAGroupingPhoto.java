package level2;

import javax.print.DocFlavor;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class TakingAGroupingPhoto {
    public List<String> ps = new ArrayList<>();

    public static void main(String[] args) {
        TakingAGroupingPhoto takingAGroupingPhoto = new TakingAGroupingPhoto();
        System.out.println(takingAGroupingPhoto.solution(2, new String[]{"N~F=0", "R~T>2"}));
        System.out.println(takingAGroupingPhoto.solution(2, new String[]{"M~C<2", "C~M>1"}));
    }

    public int solution(int n, String[] data) {
        String[] people = new String[]{"A", "C", "F", "J", "M", "N", "R", "T"};
        permutation(people, 0, people.length, people.length);

        int answer = ps.size();
        for (String p : ps) {
            List<String> position = List.of(p.split(""));
            for (String d : data) {
                if (!checkDistance(position, d.substring(0, 1), d.substring(2, 3), d.substring(3, 4), Integer.parseInt(d.substring(4, 5)))) {
                    answer--;
                    break;
                }
            }
        }
        return answer;
    }

    public boolean checkDistance(List<String> position, String p1, String p2, String sign, int requiredD) {
        int distance = Math.abs(position.indexOf(p1) - position.indexOf(p2)) - 1;
        if (sign.equals(">")) {
            return distance > requiredD;
        }
        if (sign.equals("<")) {
            return distance < requiredD;
        }
        return distance == requiredD;
    }

    public void permutation(String[] arr, int depth, int n, int r) {
        if (depth == r) {
            ps.add(String.join("", arr));
        }

        for (int i = depth; i < arr.length; i++) {
            swap(arr, depth, i);
            permutation(arr, depth + 1, n, r);
            swap(arr, depth, i);
        }
    }

    private void swap(String[] arr, int depth, int i) {
        String temp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = temp;
    }
}
