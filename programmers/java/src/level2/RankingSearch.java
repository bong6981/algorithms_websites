package level2;

import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/72412?language=java
public class RankingSearch {
    public static void main(String[] args) {
        String[] info = new String[]{"java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"};
        String[] query = new String[]{"java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"};
        RankingSearch rs = new RankingSearch();
        System.out.println(Arrays.toString(rs.solution(info, query)));
    }

    public int[] solution(String[] info, String[] query) {
        Map<String, List<Integer>> dic = new HashMap<>();
        for(String a : new String[]{"cpp", "java", "python", "-"}) {
            for(String b : new String[]{"backend", "frontend", "-"}) {
                for(String c : new String[]{"junior", "senior", "-"}) {
                    for(String  d: new String[]{"chicken", "pizza", "-"}) {
                        StringBuilder sb = new StringBuilder();
                        sb.append(a);
                        sb.append(" ");
                        sb.append(b);
                        sb.append(" ");
                        sb.append(c);
                        sb.append(" ");
                        sb.append(d);
                        dic.put(sb.toString(), new ArrayList<>());
                    }
                }
            }
        }

        for(String i : info) {
            String[] data = i.split(" ");
            for(String a : new String[]{data[0], "-"}) {
                for(String b : new String[]{data[1], "-"}) {
                    for(String c : new String[]{data[2], "-"}) {
                        for(String d : new String[]{data[3], "-"}) {
                            StringBuilder sb = new StringBuilder();
                            sb.append(a);
                            sb.append(" ");
                            sb.append(b);
                            sb.append(" ");
                            sb.append(c);
                            sb.append(" ");
                            sb.append(d);
                            dic.get(sb.toString()).add(Integer.valueOf(data[4]));
                        }
                    }
                }
            }
        }

        for(List<Integer> v : dic.values()) {
            Collections.sort(v);
        }

        int[] answer = new int[query.length];
        for(int i =0; i< query.length; i++) {
            String q = query[i];
            String[] s = q.split(" ");
            String toFind = s[0] + " " + s[2] + " " + s[4] + " " + s[6];
            List<Integer> integers = dic.get(toFind);
            int target = Integer.parseInt(s[7]);
            int start = 0;
            int end = integers.size();
            int mid = 0;
            while(start < end)  {
                mid = (start + end) / 2;
                if(integers.get(mid) >= target) {
                    end = mid;
                } else {
                    start = mid + 1;
                }
            }
            answer[i] = integers.size() - end;
        }
        return answer;
    }
}
