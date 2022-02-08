package platinum2.study;

import java.io.IOException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

class Trie {
    Trie[] children = new Trie[26];
    boolean isTerminal = false;
    Trie fail = null;
    String p; // 출력을 위한

    void insert(char[] pattern, int idx) {
        if (idx == pattern.length) {
            isTerminal = true;
            p = String.copyValueOf(pattern); // 출력을 위한
            return;
        }
        int index = pattern[idx] - 'a';
        if (this.children[index] == null) {
            this.children[index] = new Trie();
        }
        this.children[index].insert(pattern, idx + 1);
    }

}

public class AhoCorasick {
    private static Trie root;

    static void fail() {
        Queue<Trie> q = new LinkedList<>();
        root.fail = root;
        q.offer(root);

        while (!q.isEmpty()) {
            Trie cur = q.poll();
            for (int i = 0; i < 26; i++) {
                Trie next = cur.children[i];
                if (next == null) {
                    continue;
                }
                if (cur == root) {
                    next.fail = root;
                } else {
                    Trie dest = cur.fail;
                    while (dest != root && dest.children[i] == null) {
                        dest = dest.fail;
                    }

                    if (dest.children[i] != null) {
                        dest = dest.children[i];
                    }
                    next.fail = dest;
                }
                if (next.fail.isTerminal) {
                    next.isTerminal = true;
                }
                q.add(next);
            }
        }
    }

    static Map<String, Integer> kmp(char[] text) {
        Trie cur = root;
        int n = text.length;
        Map<String, Integer> answer = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int index = text[i] - 'a';
            while (cur != root && cur.children[index] == null) {
                cur = cur.fail;
            }
            if (cur.children[index] != null) {
                cur = cur.children[index];
            }
            if (cur.isTerminal) {
                answer.put(cur.p, i);
            }
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        String[] patterens = new String[]{"cache", "he", "chef", "achy"};
        root = new Trie();
        for (String patteren : patterens) {
            root.insert(patteren.toCharArray(), 0);
        }
        fail();
        String text = "cacachefcachy";
        System.out.println(kmp(text.toCharArray()));
    }
}
