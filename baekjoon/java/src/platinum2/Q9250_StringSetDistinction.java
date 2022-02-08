package platinum2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

//https://www.acmicpc.net/problem/9250
class Trie {
    Trie[] children = new Trie[26];
    boolean isEnd = false;
    Trie fail = null;

    void insert(char[] patteren, int idx) {
        if(idx==patteren.length) {
            this.isEnd = true;
            return;
        }
        int index = patteren[idx] - 'a';
        if(this.children[index] == null) {
            this.children[index] = new Trie();
        }
        this.children[index].insert(patteren, idx+1);
    }

}

public class Q9250_StringSetDistinction {
    private static Trie root;
    private static void fail() {
        Queue<Trie> q = new LinkedList<>();
        root.fail = root;
        q.offer(root);

        while(!q.isEmpty()) {
            Trie cur = q.poll();
            for (int i = 0; i < 26; i++) {
                Trie next = cur.children[i];
                if(next == null) {
                    continue;
                }
                if(cur == root) {
                    next.fail = root;
                } else {
                    Trie dest = cur.fail;
                    while(dest != root && dest.children[i] == null) {
                        dest = dest.fail;
                    }
                    if(dest.children[i] != null) {
                        dest = dest.children[i];
                    }
                    next.fail = dest;
                }
                if(next.fail.isEnd){
                    next.isEnd = true;
                }
                q.add(next);
            }
        }
    }

    private static boolean kmp(char[] text) {
        Trie cur = root;
        int n = text.length;
        for (int i = 0; i < n; i++) {
            int index = text[i] - 'a';
            while (cur != root && cur.children[index] == null) {
                cur = cur.fail;
            }
            if(cur.children[index] != null) {
                cur = cur.children[index];
            }
            if(cur.isEnd) {
                return true;
            }
        }
        return false;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        root = new Trie();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            root.insert(br.readLine().toCharArray(), 0);
        }
        fail();
        int q = Integer.parseInt(br.readLine());
        for (int i = 0; i < q; i++) {
            if(kmp(br.readLine().toCharArray())) {
                System.out.println("YES");
            }else {
                System.out.println("NO");
            }
        }
    }
}
