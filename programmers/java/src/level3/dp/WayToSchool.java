package level3.dp;

//https://programmers.co.kr/learn/courses/30/lessons/42898
public class WayToSchool {
    public static void main(String[] args) {
        WayToSchool wts = new WayToSchool();
        System.out.println(wts.solution(4, 3, new int[][]{{2,2}}));
    }

    public int solution(int m, int n, int[][] puddles) {
        int[][] graph = new int[n+1][m+1];
        for(int[] p : puddles) {
            graph[p[1]][p[0]] = -1;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <=m; j++) {
                if(i==1 && j==1) {
                    graph[i][j] = 1;
                    continue;
                }
                if(graph[i][j] == -1) {
                    graph[i][j] = 0;
                    continue;
                }
                graph[i][j] = (graph[i-1][j] + graph[i][j-1]) % 1000000007;
            }
        }

        return graph[n][m];
    }
}
