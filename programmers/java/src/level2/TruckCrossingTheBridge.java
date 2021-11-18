package level2;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.stream.Collectors;

public class TruckCrossingTheBridge {
    public static void main(String[] args) {
        System.out.println(solution(2, 10, new int[]{7,4,5,6}));
    }

    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> trucks = Arrays.stream(truck_weights).boxed().collect(Collectors.toCollection(LinkedList::new));
        Integer[] temp = new Integer[bridge_length];
        Arrays.fill(temp, 0);
        Queue<Integer> bridge = new LinkedList<>(Arrays.asList(temp));
        int time = 0;
        int weightOnTheBridge = 0;

        while (!trucks.isEmpty()) {
            weightOnTheBridge -= bridge.poll();
            if (weightOnTheBridge + trucks.peek() <= weight) {
                int truck = trucks.poll();
                bridge.offer(truck);
                weightOnTheBridge += truck;
            } else {
                bridge.offer(0);
            }
            time++;
        }

        time += bridge_length;
        return time;
    }

    // for문 돌면서 que에 elements 넣는 것이 더 간단해 보임
    //클래스로 구현한 친구
    public int solution2(int bridgeLength, int weight, int[] truckWeights) {
        Queue<Truck> waitQ = new LinkedList<>();
        Queue<Truck> moveQ = new LinkedList<>();

        for (int t : truckWeights) {
            waitQ.offer(new Truck(t));
        }

        int answer = 0;
        int curWeight = 0;

        while (!waitQ.isEmpty() || !moveQ.isEmpty()) {
            answer++;

            if (moveQ.isEmpty()) {
                Truck t = waitQ.poll();
                curWeight += t.weight;
                moveQ.offer(t);
                continue;
            }

            for (Truck t : moveQ) {
                t.moving();
            }

            if (moveQ.peek().move > bridgeLength) {
                Truck t = moveQ.poll();
                curWeight -= t.weight;
            }

            if (!waitQ.isEmpty() && curWeight + waitQ.peek().weight <= weight) {
                Truck t = waitQ.poll();
                curWeight += t.weight;
                moveQ.offer(t);
            }
        }

        return answer;
    }

    class Truck {
        int weight;
        int move;

        public Truck(int weight) {
            this.weight = weight;
            this.move = 1;
        }

        public void moving() {
            move++;
        }
    }
}
