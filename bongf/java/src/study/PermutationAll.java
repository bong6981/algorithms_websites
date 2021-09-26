package study;

import java.util.HashSet;

public class PermutationAll {
    public static void main(String[] args) {
        String numbers = "011";
        HashSet<Integer> set = new HashSet<>();
        permutation("", numbers, set);
    }

    public static void permutation(String prefix, String str, HashSet<Integer> set) {
        int n = str.length();
        //if (n == 0) System.out.println(prefix);
        if(!prefix.equals("")) {
            set.add(Integer.valueOf(prefix));
        }
        System.out.println("set은" + set);
        for (int i = 0; i < n; i++) {
            permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i + 1, n), set);
        }
    }
}
