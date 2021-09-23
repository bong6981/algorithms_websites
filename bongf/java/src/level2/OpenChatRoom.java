package level2;

import java.util.*;

public class OpenChatRoom {
    public static void main(String[] args) {
        OpenChatRoom openChatRoom = new OpenChatRoom();
        System.out.println(Arrays.toString(openChatRoom.solution(new String[]{"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"})));
    }

    public String[] solution(String[] record) {
        Map<String, String> dic = new HashMap<>();

        for(String r : record) {
            String[] s = r.split(" ");
            if(!s[0].equals("Leave")) {
                dic.put(s[1], s[2]);
            }
        }

        List<String> answer = new ArrayList<>();

        String[] printer = new String[]{"님이 들어왔습니다.", "님이 나갔습니다."};

        for(String r : record) {
            String[] s = r.split(" ");
            if(s[0].equals("Enter")) {
                answer.add(dic.get(s[1]) + printer[0]);
            } else if (s[0].equals("Leave")) {
                answer.add(dic.get(s[1]) + printer[1]);
            }
        }
        return answer.toArray(new String[0]);
    }
}
