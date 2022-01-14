package level1;

public class Id_Recommendation {

    public static void main(String[] args) {
        System.out.println(solution("-_.~!@#$%^&*()=+[{]}:?,<>/._-"));
    }

    private static String solution(String new_id) {
        new_id = new_id.toLowerCase();
        new_id = new_id.replaceAll("[~!@#$%^&*()=+\\[{\\]}:?,<>/]", "");
        while(new_id.contains("..")) {
           new_id = new_id.replace("..", ".");
        }
        if( new_id.length() > 0 && new_id.startsWith(".")) {
            new_id = new_id.replaceFirst(".", "");
        }
        if( new_id.length() >0 && new_id.endsWith(".")) {
            new_id = new_id.substring(0, new_id.length()-1);
        }
        if( new_id.length() == 0) {
            new_id = "a";
        } else if ( new_id.length() >= 16) {
            new_id = new_id.substring(0, 15);
            if(new_id.endsWith(".")) {
                new_id = new_id.substring(0, 14);
            }
        }
        while (new_id.length() <= 2) {
            new_id = new_id + new_id.charAt(new_id.length()-1);
        }
        return new_id;
    }
}
