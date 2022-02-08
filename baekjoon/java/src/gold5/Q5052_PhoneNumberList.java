package gold5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
// https://www.acmicpc.net/problem/5052
class Trie {
    Trie[] children = new Trie[10];
    boolean isTerminal = false;

    public void insert(char[] word, int idx) {
        if(idx == word.length) {
            this.isTerminal = true;
            return;
        }

        int index = Integer.parseInt(String.valueOf(word[idx]));
        if(this.children[index] == null) {
            this.children[index] = new Trie();
        }
        
        this.children[index].insert(word, idx+1);
    }

    boolean find(char[] word, int idx) {
        if(idx==word.length) {
            return true;
        }

        if(isTerminal) {
            return false;
        }
        int index =  Integer.parseInt(String.valueOf(word[idx]));
        return children[index].find(word, idx+1);
    }
}

public class Q5052_PhoneNumberList {
    static char[][] phoneNumbers = new char[10000][10];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
        for (int i = 0; i < testCase; i++) {
            int phoneNumberCnt = 0;
            int n = Integer.parseInt(br.readLine());
            Trie root = new Trie();
            boolean isPossible = true;
            for (int j = 0; j < n; j++) {
                char[] phoneNumber = br.readLine().toCharArray();
                phoneNumbers[phoneNumberCnt++] = phoneNumber;
                root.insert(phoneNumber, 0);
            }

            for (int j = 0; j < n; j++) {
                if(!root.find(phoneNumbers[j], 0)) {
                    isPossible = false;
                    break;
                }
            }

            System.out.println(isPossible? "YES":"NO");
        }
    }
}
