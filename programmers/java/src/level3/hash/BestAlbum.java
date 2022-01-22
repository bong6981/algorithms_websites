package level3.hash;

import java.util.*;
import java.util.stream.Collectors;

// https://programmers.co.kr/learn/courses/30/lessons/42579
public class BestAlbum {
    public static void main(String[] args) {
        BestAlbum ba = new BestAlbum();
        System.out.println(Arrays.toString(ba.solution(new String[]{"classic", "pop", "classic", "classic", "pop"}, new int[]{500, 600, 150, 800, 2500})));
    }

    public Integer[] solution(String[] genres, int[] plays) {
        Map<String, Genre> records = new HashMap<>();
        for (int i = 0; i < genres.length; i++) {
            records.computeIfAbsent(genres[i], v -> new Genre());
            Genre genre = records.get(genres[i]);
            genre.total += plays[i];
            genre.musics.add(new Genre.Music(i, plays[i]));
        }

        List<Integer> answer = new ArrayList<>();
        List<Genre> generesInOrder = records.values().stream().sorted(Comparator.comparing((Genre g) -> g.total).reversed()).collect(Collectors.toList());
        for (Genre genre : generesInOrder) {
            List<Genre.Music> musics = genre.musics;
            musics.sort(Comparator.comparing(m -> m.number));
            genre.musics.stream().sorted(Comparator.comparing((Genre.Music m) -> m.number).reversed()).limit(2L).forEach(m-> answer.add(m.index));
        }
        return answer.toArray(new Integer[0]);
    }

    static class Genre {
        int total = 0;
        List<Music> musics = new ArrayList<>();

        static class Music {
            int index;
            int number;

            public Music(int index, int number) {
                this.index = index;
                this.number = number;
            }
        }
    }
}
