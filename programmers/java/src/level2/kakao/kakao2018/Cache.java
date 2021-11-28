package level2.kakao.kakao2018;

import java.util.*;

//https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3
// 카카오 블라인드 1차
public class Cache {
    public static void main(String[] args) {
        Cache cache = new Cache();
        System.out.println(cache.solution(3, new String[]{"Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"}));
    }

    public int solution(int cacheSize, String[] cities) {
        int time = 0;
        List<String> cache = new ArrayList<>(cacheSize);
        for(String c : cities) {
            c = c.toUpperCase();
            if(cache.contains(c)) {
                cache.remove(c);
                cache.add(c);
                time++;
                continue;
            }
            time += 5;
            if(cacheSize!=0) {
                if(cache.size() == cacheSize) {
                    cache.remove(0);
                }
                cache.add(c);
            }
        }
        return time;
    }
}
