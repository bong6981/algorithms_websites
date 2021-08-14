package level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class practice {
    public static void main(String[] args) {
        Integer[] array = {1, 5, 2, 6, 3, 7, 4};
        List<Integer> temp = Arrays.asList(array);
        System.out.println(temp.size());
        System.out.println(temp.get(1));
        System.out.println(temp.toString());

    }
}
