package level1;

public class BasicString {
    public static void main(String[] args) {
        System.out.println(solution("a1234"));

        int x = Integer.parseInt("1234a");
        System.out.println(x);
    }

    public static boolean solution(String s) {
        if (!(s.length() == 4 || s.length() == 6)) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
             if(!Character.isDigit(s.charAt(i))) {
                 return false;
            }
        }
        return true;
    }

    //Integer.parseInt(문자열) 하면 해당 문자열 그대로 숫자로, 아니면 (NumberFormatException e 발생
    public static boolean solution2(String s) {
        if(s.length() == 4 || s.length() == 6){
            try{
                int x = Integer.parseInt(s);
                return true;
            } catch(NumberFormatException e){
                return false;
            }
        }
        else return false;
    }


}
