package level3.bfsdfs;
//https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=java
public class 네트워크 {
    private int[][] computers;
    private int n;
    private boolean[] visited;
    public void dfs(int start) {
        visited[start] = true;
        for(int i=0; i<n; i++) {
            if(!visited[i] && computers[start][i] == 1) {
                dfs(i);
            }
        }

    }

    public int solution(int n, int[][] computers) {
        this.computers = computers;
        this.n = n;
        int answer = 0;
        visited = new boolean[n];
        for(int i=0; i<n; i++) {
            if(!visited[i]) {
                dfs(i);
                answer++;
            }
        }
        return answer;
    }
}
