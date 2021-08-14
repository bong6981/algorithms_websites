package level1;

public class CaesarCipher {
    public static void main(String[] args) {
        System.out.println(solution("z a", 1));
    }

    public static String solution(String s, int n) {
        char[] arr = s.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            //Character.isLowerCase(ch) 로 해도 무방
            if ('a' <= arr[i] && arr[i] <= 'z') {
                arr[i] = (char) ((arr[i] - 'a' + n) % 26 + 'a');
            } else if ('A' <= arr[i] && arr[i] <= 'Z') {
                arr[i] = (char) ((arr[i] - 'A' + n) % 26 + 'A');
            }
        }
        return String.valueOf(arr);
    }
}
