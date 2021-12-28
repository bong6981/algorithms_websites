package silver3;

import java.io.*;
import java.util.*;

// https://www.acmicpc.net/problem/21921
public class Q21921_Blog {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int prev = 0;
        int[] visitors = new int[n];
        for (int i = 0; i < n; i++) {
            int r = sc.nextInt();
            visitors[i] = r;
            if(i < x) {
                prev += r;
            }
        }

        int start = 0;
        int end = start + x - 1;

        List<Integer> record = new ArrayList<>();
        record.add(prev);
        start++;
        end++;
        while(end < n) {
            prev = prev - visitors[start-1] + visitors[end];
            record.add(prev);
            start++;
            end++;
        }
        record.sort(Collections.reverseOrder());
        if(record.get(0) == 0) {
            System.out.println("SAD");
            return;
        }
        System.out.println(record.get(0));
        int cnt = 0;
        for (int integer : record) {
            if(integer == record.get(0)) {
                cnt++;
                continue;
            }
            break;
        }
        System.out.println(cnt);
    }

    public static void fail() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        sc.nextLine();
        int[] visitors = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int start = 0;
        int end = start + x - 1;
        int prev = 0;
        for (int i = 0; i < x; i++) {
            prev += visitors[i];
        }

        List<Integer> record = new ArrayList<>();
        record.add(prev);
        start++;
        end++;
        while(end < n) {
            prev = prev - visitors[start-1] + visitors[end];
            record.add(prev);
            start++;
            end++;
        }
        record.sort(Collections.reverseOrder());
        if(record.get(0) == 0) {
            System.out.println("SAD");
            return;
        }
        System.out.println(record.get(0));
        //여기를 아래와 같이 filter를 걸면 틀리고, 직업 해당 개수를 count해주면 맞는다.
        System.out.println(record.stream().filter(r -> r.equals(record.get(0))).count());
    }

    // 백준 id : aeternussm, BufferedReader 학습용으로 작성해두었다
    // https://www.acmicpc.net/source/35151640
    public static void other() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        int[] visitors = new int[n];
        st = new StringTokenizer(br.readLine());
        int prev = 0;
        for (int i = 0; i < n; i++) {
            visitors[i] = Integer.parseInt(st.nextToken());
            if(i < x) prev += visitors[i];
        }

        int answer = prev;
        int cnt = 0;
        if( prev > 0) cnt++;

        for (int i = x; i < n; i++) {
            prev = prev - visitors[i-x] + visitors[i];
            if( answer < prev) {
                answer = prev;
                cnt = 1;
                continue;
            }
            if( answer == prev ) {
                cnt++;
            }
        }

        if (answer == 0) bw.write("SAD");
        else {
            bw.write(answer + "\n");
            bw.write(String.valueOf(cnt));
        }
        bw.flush();
        bw.close();
    }
}
