package level2;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class FindPrimeNumber {
    private static Set<Integer> pm = new HashSet<>();

    public static void main(String[] args) {
        System.out.println(solution2("17"));
//        System.out.println(solution("011"));
    }

    public static int solution(String numbers) {
        Integer[] arr = Arrays.stream(numbers.split("")).map(Integer::valueOf).toArray(Integer[]::new);

        for (int i = 1; i < numbers.length() + 1; i++) {
            permutation(arr, 0, numbers.length(), i);
        }
        pm.remove(0);
        pm.remove(1);

        int max = pm.stream().mapToInt(x -> x).max().orElseThrow();
        for (int i = 2; i < ((int) Math.sqrt(max) + 1); i++) {
            for (int j = i * 2; j < max + 1; j += i) {
                pm.remove(j);
            }
        }

        return pm.size();
    }

    private static void permutation(Integer[] arr, int depth, int n, int r) {
        if (depth == r) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < r; i++) {
                sb.append(arr[i]);
            }
            pm.add(Integer.valueOf(sb.toString()));
        }

        for (int i = depth; i < n; i++) {
            swap(arr, depth, i);
            permutation(arr, depth + 1, n, r);
            swap(arr, depth, i);
        }
    }

    private static void swap(Integer[] arr, int depth, int i) {
        int temp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = temp;
    }

    public static int solution2(String numbers) {
        Set<Integer> set = new HashSet<>();
        permutation("", numbers, set);
        int count = 0;
        while(set.iterator().hasNext()) {
            int a = set.iterator().next(); //index 0부터 순차대로 빼준다
            set.remove(a);
            if(isPrime(a)) {
                count++;
            }
        }
        return count;
    }

    private static void permutation(String prefix, String str, Set<Integer> set) {
        int n = str.length();
        if(!prefix.equals("")) {
            set.add(Integer.valueOf(prefix));
        }
        for (int i = 0; i < n; i++) {
             permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i+1, n), set);
        }
    }

    // 2,3,4 체크하지 않고 애초에 2로 나눠지지 않는 n을 구분하여 3, 5, 7,...만 체크 (더 빠름)
    public static boolean isPrime(int n) {
        if(n==0 || n == 1) return false;
        if(n%2==0) {
            return n == 2;
        }
        for(int i=3; i<(int)Math.sqrt(n) + 1; i+=2) {
            if(n%i==0) {
                return false;
            }
        }
        return true;
    }
}
