package gold5;
//https://www.acmicpc.net/workbook/view/7942

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Q21922_2_UndergraduateStudentMinsang {
    static class Position {
        int x;
        int y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static int[][] lab;
    static List<Position> fans = new ArrayList<>();
    static boolean[][][] visitedWithDir;
    static int[][] moves = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static int ans = 0;

    static void input() {
        N = scan.nextInt();
        M = scan.nextInt();
        visitedWithDir = new boolean[N][M][5];
        lab = new int[N][M];
        fans = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int num = scan.nextInt();
                lab[i][j] = num;
                if( num == 9) {
                    fans.add(new Position(i, j));
                }
            }
        }
    }


    static int change_dir(int object, int dir) {
        if(object==1) {
            if(dir == 2) {
                return 3;
            }
            if(dir == 3) {
                return 2;
            }
        }

        if(object == 2) {
            if(dir==0) {
                return 1;
            }
            if(dir==1) {
                return 0;
            }
        }

        if(object==3) {
            if(dir==0) {
                return 3;
            }
            if(dir==1) {
                return 2;
            }
            if(dir==2) {
                return 1;
            }
            if(dir==3) {
                return 0;
            }
        }

        if(object==4) {
            if(dir==0) {
                return 2;
            }
            if(dir==1) {
                return 3;
            }
            if(dir==2) {
                return 0;
            }
            if(dir==3) {
                return 1;
            }
        }

        return dir;

    }

    static void blow(int x, int y, int dir) {
        while(true) {
            if(visitedWithDir[x][y][dir]) {
                    break;
            }
            visitedWithDir[x][y][dir] = true;
            if(!visitedWithDir[x][y][4]) {
                visitedWithDir[x][y][4] = true;
                ans++;
            }

            x += moves[dir][0]; y += moves[dir][1];
            if(!(0<= x && x < N && 0 <= y && y < M)) {
                break;
            }

            if(lab[x][y] == 9) {
                break;
            }
            if( lab[x][y] >= 1) {
                dir = change_dir(lab[x][y], dir);
            }
        }
    }

    static void sol() {
        for(Position fan : fans) {
            for (int i = 0; i < 4; i++) {
                blow(fan.x, fan.y, i);
            }
        }
    }

    static void print() {
        System.out.println(ans);
    }

    public static void main(String[] args) {
        input();
        sol();
        print();
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while ( st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextString() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
