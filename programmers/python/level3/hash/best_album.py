# https://programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic.keys():
            dic[genres[i]][0] += plays[i]
            dic[genres[i]].append((plays[i], i))
        else:
            dic[genres[i]] = [plays[i], (plays[i], i)]
    

    in_order = sorted([k for k in dic.keys()], key=lambda x : dic[x][0], reverse=True)
    answer = []
    for k in in_order:
        in_order_musics = sorted(dic[k][1:], key=lambda x: x[0], reverse=True)
        for m in in_order_musics[:2]:
            answer.append(m[1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

# 프로그래머스 다른 사람 풀이 : 파이썬으로 클래스 만들어서 비교하기 
def solution_other(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)



    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play


