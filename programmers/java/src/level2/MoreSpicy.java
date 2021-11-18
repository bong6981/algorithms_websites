package level2;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class MoreSpicy {
    public static void main(String[] args) {
        System.out.println(solution2(new int[]{2,3,7,10,15}, 11));
    }

    public static int solution2(int[] s, int K) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        for (int i : s) {
            priorityQueue.offer(i);
        }

        int c = 0;
        while(priorityQueue.peek() < K) {
            if(priorityQueue.size() == 1) {
                return -1;
            }
            int n = priorityQueue.poll();
            int m = priorityQueue.poll();
            priorityQueue.add(n+m*2);
            c++;
        }
        return c;
    }

    // 파이썬의 heap 원리 보고 구현해 봤으나 효율성 실패
    public static int solution(int[] s, int K) {
        List<Integer> scoville = heapify(s);
        int c = 0;
        while (scoville.get(0) < K) {
            if(scoville.size() == 1) {
                return -1;
            }
            int n =  scoville.get(0);
            scoville = heappop(scoville);
            int m = scoville.get(0);
            scoville = heappop(scoville);
            heappush(scoville, n + m*2);
            c++;
        }
        return c;
    }

    private static List<Integer> heapify(int[] arr) {
        List<Integer> result = new ArrayList<>();
        for(int i : arr) {
            result = heappush(result, i);
        }
        return result;
    }

    private static List<Integer> heappush(List<Integer> list, int i) {
        list.add(i);
        int newNumIdx = list.indexOf(i);

        while(true) {
            if(newNumIdx == 0) {
                break;
            }
            int parentIdx = (newNumIdx - 1) / 2;

            int parentNum = list.get(parentIdx);
            if( i > parentNum) {
                break;
            }
            list.set(parentIdx, i);
            list.set(newNumIdx, parentNum);
            newNumIdx = parentIdx;
        }
        return list;
    }

    private static List<Integer> heappop(List<Integer> scoville) {
        if(scoville.size() == 0) {
            return scoville;
        }
        if(scoville.size() == 1) {
            return new ArrayList<>();
        }
        int last = scoville.get(scoville.size()-1);
        scoville.set(0, last);
        scoville = scoville.subList(0, scoville.size()-1);
        return heappopsort(scoville, 0);
    }

    private static List<Integer> heappopsort(List<Integer> scoville, int newNumIdx) {
        int childNumIdxL = newNumIdx * 2 + 1;
        int newNum = scoville.get(newNumIdx);

        if(scoville.size() > childNumIdxL && scoville.get(childNumIdxL) < newNum) {
            scoville.set(newNumIdx, scoville.get(childNumIdxL));
            scoville.set(childNumIdxL, newNum);
            scoville = heappopsort(scoville, childNumIdxL);
        }

        int childNumIdxR = newNumIdx * 2 + 2;
        newNum = scoville.get(newNumIdx);

        if(scoville.size() > childNumIdxR && scoville.get(childNumIdxR) < newNum) {
            scoville.set(newNumIdx, scoville.get(childNumIdxR));
            scoville.set(childNumIdxR, newNum);
            scoville = heappopsort(scoville, childNumIdxR);
        }
        return scoville;
    }
}
