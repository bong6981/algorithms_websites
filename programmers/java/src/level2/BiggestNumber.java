package level2;

import java.util.*;

public class BiggestNumber {
    public static void main(String[] args) {
        System.out.println(solution(new int[]{6, 10, 2}));
    }

    public static String solution(int[] numbers) {

        String[] strings = Arrays.stream(numbers)
                .boxed()
                .map(String::valueOf)
                .toArray(String[]::new);


        Arrays.sort(strings, new Comparator<String>() {
                    @Override
                    public int compare(String s1, String s2) {
                       String newS1 = s1 + s1 + s1;
                       String newS2 = s2 + s2 + s2;

                       return -(newS1.compareTo(newS2));
                    }
                });

        String answer = String.join("", strings);
        if (answer.startsWith("0")) {
            return String.valueOf(0);
        }
        return answer;
    }

    //깔끔 : compare 구현방식, 정수를 string으로 바꾸는 방식 , 마지막 0으로 시작할 때 삼항연산자로 return하는 방식
    public String solution2(int[] numbers) {
        String[] nums = new String[numbers.length];

        for (int i=0; i<nums.length; i++)
            nums[i] = numbers[i] + "";

        Arrays.sort(nums, new Comparator<String>() {
            public int compare(String o1, String o2) {
                return (o2 + o1).compareTo(o1 + o2);
            }
        });

        String ans = "";
        for (int i=0; i<numbers.length; i++)
            ans += nums[i];

        return ans.charAt(0) == '0' ? "0" : ans;
    }

    public String solution3(int[] numbers) {
        String answer = "";

        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < numbers.length; i++) {
            list.add(numbers[i]);
        }
        Collections.sort(list, (a, b) -> {
            String as = String.valueOf(a), bs = String.valueOf(b);
            return -Integer.compare(Integer.parseInt(as + bs), Integer.parseInt(bs + as));
        });
        StringBuilder sb = new StringBuilder();
        for(Integer i : list) {
            sb.append(i);
        }
        answer = sb.toString();
        if(answer.charAt(0) == '0') {
            return "0";
        }else {
            return answer;
        }
    }
}
