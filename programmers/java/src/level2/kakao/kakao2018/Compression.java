package level2.kakao.kakao2018;

import java.util.*;
import java.util.stream.Collectors;

public class Compression {
    public static void main(String[] args) {
        Compression c = new Compression();
        System.out.println(c.solution("KAKAO"));
    }
    public List<Integer> solution(String msg) {
        Map<String, Integer> dic = new HashMap<>();
        for (int i = 1; i < 27; i++) {
             dic.put((char)(64+i) + "", i);
        }

        int last = 26;
        Queue<String> queue = Arrays.stream(msg.split("")).collect(Collectors.toCollection(LinkedList::new));
        List<Integer> answer = new ArrayList<>();

        while(!queue.isEmpty()) {
            String now = "";
            String temp = "";
            while(true) {
                now += queue.poll();
                if(queue.isEmpty()) {
                    break;
                }
                temp = now + queue.peek();
                if (! dic.containsKey(temp)) {
                    break;
                }
            }
            answer.add(dic.get(now));
            last++;
            if(temp != "") {
                dic.put(temp, last);
            }
        }
        return answer;
    }
}
