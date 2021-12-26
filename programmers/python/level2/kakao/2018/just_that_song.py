# https://programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    answer = []
    m = replace_sharp(m)
    for idx, info in enumerate(musicinfos):
        start, end, title, info = info.split(",")
        sth, stm = map(int, start.split(":"))
        endh, endm = map(int, end.split(":"))
        time = (endh * 60 + endm) - (sth * 60 + stm)

        info = replace_sharp(info)
        mock, rest = divmod(time, len(info))
        info = info * mock + info[:rest]

        if m in info:
            answer.append((-time, idx, title))
    if answer == [] :
        return "(None)"
    answer.sort()
    return answer[0][2]

def replace_sharp(string):
    string = string.replace('A#', 'a')
    string = string.replace('C#', 'c')
    string = string.replace('D#', 'd')
    string = string.replace('F#', 'f')
    string = string.replace('G#', 'g')
    return string

def solution_fail_eight(m, musicinfos):
    answer = []
    for idx, info in enumerate(musicinfos):
        start, end, title, info = info.split(",")
        sth, stm = map(int, start.split(":"))
        endh, endm = map(int, end.split(":"))
        time = (endh * 60 + endm) - (sth * 60 + stm)

        cnt = info.count("#")
        cnt_music = len(info) - cnt

        mock, rest = divmod(time, cnt_music)
        temp = ''
        if rest != 0 :
            cnt = info[:rest].count("#")
            temp = info[:rest+cnt]
        info = info * mock + temp
    
        found = False
        while True:
            idx = info.find(m)
            if idx == -1 :
                break
            if len(info) - 1 >= idx + len(m) :
                if info[idx + len(m)] == "#" :
                    if len(info) == idx + len(m) + 1:
                        break
                    info = info[idx+len(m)+1:]
                    continue
            found = True
            break

        if not found:
            continue
        answer.append((-time, idx, title))
    if answer == [] :
        return "(None)"
    answer.sort()
    return answer[0][2]
      

# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CDCDF", ["12:00,12:14,HELLO,CDCDCDF"]))
# print(solution("CDCDF", ["12:00,12:07,HELLO,CDCDCDF"]))
# print(solution("DF", ["6:20,6:50,TEST,DDF"]))
# print(solution("CCB", ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]))
# print(solution("A#", ["13:00,13:02,HAPPY,B#A#"]))
# print(solution("A#", ["12:00,12:01,HELLO,A#"]))

