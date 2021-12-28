package level2.kakao.kakao2019;

import java.util.*;

public class CandidateKey {
    public List<List<Integer>> coms = new ArrayList<>();
    public int relationLength;
    public int dataLength;
    public static void main(String[] args) {
        CandidateKey ck = new CandidateKey();
        String s = "[['a', 'aa'], ['aa', 'a'], ['a', 'a']]";
        System.out.println(s.replace("[", "{").replace("]", "}"));
        System.out.println(ck.solution2(new String[][]{{"100","ryan","music","2"},{"200","apeach","math","2"},{"300","tube","computer","3"},{"400","con","computer","4"},{"500","muzi","music","3"},{"600","apeach","music","2"}}));
        System.out.println(ck.solution2(new String[][]{{"a", "aa"}, {"aa", "a"}, {"a", "a"}}));
    }

    public int solution(String[][] relation) {
        relationLength = relation.length;
        dataLength = relation[0].length;
        for (int i = 1; i <= dataLength; i++) {
           combination(i, 0, new Stack<Integer>());
        }
        System.out.println(coms);
        int answer = 0;
        for (int i = 0; i < coms.size(); i++) {
            List<Integer> idxs = coms.get(i);
            System.out.println(idxs);
            if(idxs.size() == 0) {
                continue;
            }
            Set<List<String>> set1 = new HashSet<>();
            for(String[] r : relation) {
                List<String> s2 = new ArrayList<>();
                for(Integer idx : idxs) {
                    s2.add(r[idx]);
                }
                if(set1.contains(s2)) {
                    break;
                }
                set1.add(s2);
            }
            if(set1.size() < relationLength) {
                continue;
            }
            answer++;
            for (int j = i+1; j < coms.size(); j++) {
                boolean containAll = true;
                for(Integer idx : idxs) {
                    if (!coms.get(j).contains(idx)) {
                        containAll = false;
                        break;
                    }
                }
                if(containAll) {
                    coms.set(j, new ArrayList<>());
                }
            }
        }
        return answer;
    }

    public void combination(int toPick, int start, Stack<Integer> output) {
        if(toPick == 0) {
            coms.add(new ArrayList<>(output));
            return;
        }

        for (int i = start; i < dataLength;  i++) {
             output.push(i);
             combination(toPick-1, i+1, output);
             output.pop();
        }
    }

    public int solution2(String[][] relation) {
        List<Integer> answers = new ArrayList<>();
        for (int i = 1; i < (1 << relation[0].length); i++) {
            Set<List<String>> set1 = new HashSet<>();
            for (int j = 0; j < relation.length; j++) {
                List<String> s2 = new ArrayList<>();
                for (int k = 0; k < relation[0].length; k++) {
                    if ((i & (1 << k)) != 0) {
                        s2.add(relation[j][k]);
                    }
                }
                set1.add(s2);
            }

            if (set1.size() == relation.length) {
                boolean toRemove = false;
                for (Integer answer : answers) {
                    if ((answer & i) == answer) {
                        toRemove = true;
                        break;
                    }
                }
                if (!toRemove) {
                    answers.add(i);
                }
            }
        }
        return answers.size();
    }
}
