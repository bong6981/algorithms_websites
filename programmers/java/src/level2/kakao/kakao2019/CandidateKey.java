package level2.kakao.kakao2019;

import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/42890
public class CandidateKey {
    public List<List<Integer>> coms = new ArrayList<>();
    public int relationLength;
    public int dataLength;

    public static void main(String[] args) {
        CandidateKey ck = new CandidateKey();
        String s = "[['a', 'aa'], ['aa', 'a'], ['a', 'a']]";
//        System.out.println(s.replace("[", "{").replace("]", "}"));
        System.out.println(ck.solution3(new String[][]{{"100", "ryan", "music", "2"}, {"200", "apeach", "math", "2"}, {"300", "tube", "computer", "3"}, {"400", "con", "computer", "4"}, {"500", "muzi", "music", "3"}, {"600", "apeach", "music", "2"}}));
//        System.out.println(ck.solution3(new String[][]{{"a", "aa"}, {"aa", "a"}, {"a", "a"}}));
    }

    public int solution3(String[][] relations) {
        relationLength = relations.length;
        dataLength = relations[0].length;
        List<Integer> cands = new ArrayList<>();
        for (int bit = 0; bit < (1 << (dataLength + 1)); bit++) {
            Set<List<String>> midData = new HashSet<>();
            for (String[] rel : relations) {
                List<String> d = new ArrayList<>();
                for (int j = 0; j < dataLength; j++) {
                    if ((bit & (1 << j)) > 0) {
                        d.add(rel[j]);
                    }
                }
                midData.add(d);
            }
            if (midData.size() == relationLength) {
                cands.add(bit);
            }
        }

        boolean[] result = new boolean[cands.size()];
        Arrays.fill(result, true);
        for (int i = 0; i < result.length - 1; i++) {
            if (result[i]) {
                for (int j = i + 1; j < result.length; j++) {
                    if ((cands.get(i) & cands.get(j)) == cands.get(i)) {
                        result[j] = false;
                    }
                }
            }
        }

        int cnt = 0;
        for (boolean r : result) {
            if (r) {
                cnt++;
            }
        }
        return cnt;

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
            if (idxs.size() == 0) {
                continue;
            }
            Set<List<String>> set1 = new HashSet<>();
            for (String[] r : relation) {
                List<String> s2 = new ArrayList<>();
                for (Integer idx : idxs) {
                    s2.add(r[idx]);
                }
                if (set1.contains(s2)) {
                    break;
                }
                set1.add(s2);
            }
            if (set1.size() < relationLength) {
                continue;
            }
            answer++;
            for (int j = i + 1; j < coms.size(); j++) {
                boolean containAll = true;
                for (Integer idx : idxs) {
                    if (!coms.get(j).contains(idx)) {
                        containAll = false;
                        break;
                    }
                }
                if (containAll) {
                    coms.set(j, new ArrayList<>());
                }
            }
        }
        return answer;
    }

    public void combination(int toPick, int start, Stack<Integer> output) {
        if (toPick == 0) {
            coms.add(new ArrayList<>(output));
            return;
        }

        for (int i = start; i < dataLength; i++) {
            output.push(i);
            combination(toPick - 1, i + 1, output);
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
