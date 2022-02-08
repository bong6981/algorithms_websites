package gold5;

// https://www.youtube.com/watch?v=Xt2ouYSxWkw
// https://twpower.github.io/187-trie-concept-and-basic-problem
// https://www.baeldung.com/trie-java
// https://hongjw1938.tistory.com/24
public class TrieStructure {
    static final int ALPHABET_SIZE = 26;
    Trie[] children = new Trie[ALPHABET_SIZE];
    boolean isTerminal = false;
    char val = 0;

    void insert(char[] word, int idx) {
        if(idx == word.length) {
            this.isTerminal = true;
            return;
        }

        char letter = word[idx];
        int index = letter - 'a';

        if(this.children[index] == null) {
            this.children[index] = new Trie();
        }

        this.children[index].insert(word, idx+1);
    }

    boolean find(char[] word, int idx) {
        if(idx==word.length) {
            return this.isTerminal;
        }

        int index = word[idx] -'a';
        if(children[index] == null) {
            return false;
        }
        return children[index].find(word, idx+1);
    }
}
