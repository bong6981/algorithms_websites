# ##bfs로 완탐하면서 하는 일 더하자. 중간에 만약에 시간 초과하면 멈추자

# from collections import deque
# import sys
# input = sys.stdin.readline

# N, M, T = map(int, input().split())
# graph = []
# time = []
# for _ in range(N):
#     graph.append(list(map(int, input().split())))
# for _ in range(N):
#     time.append(list(map(int, input().split())))

# q = deque([])
# ## 좌표 x, y와 남은 시간 t, 일의 수 
# q.append((0, 0, T, 0))


# moves = [(1, 0), (0, 1), (1, 1)]
# ans = 0
# while q:
#     r, c, t, w = q.popleft()
#     if(r==N-1 and c==M-1 and t >=0):
#         ans = max(ans, w)

#     ## case1
#     if(graph[r][c] > 0 and  time[r][c] < t):
#         nw = w + graph[r][c]
#         nt = t - time[r][c]
#         if nt > 0:
#             for move in moves:
#                 nr = r + move[0]
#                 nc = c + move[1]
#                 nnt = nt - 1
#                 if 0 <= nr < N and 0 <= nc < M:
#                     if nnt >= 0:
#                         q.append((nr, nc, nnt, nw))
#     ## case 2
#     for move in moves:
#         nr = r + move[0]
#         nc = c + move[1]
#         nt = t - 1
#         if 0 <= nr < N and 0 <= nc < M:
#             if nt >= 0:
#                 q.append((nr, nc, nt, w))




# print(ans)

s = 'a bc'
for i in range(len(s)):
    print(s[i])
    print(s[i] in s)

