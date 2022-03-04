# https://programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    routes.sort(key=lambda x : (x[0], x[1]))
    cnt = 1
    end = routes[0][1]
    for route in routes:
        print(f'route : {route}')
        if route[0] > end:
            cnt += 1
            end = route[1] 
        elif route[1] < end :
            end = route[1]
        print(f'cnt = {cnt}')
        print(f'end = {end}')
    return cnt

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
