import sys
input = sys.stdin.readline

w, h = map(int, input().split())
cnt = int(input())

horiz_cut_point = []
verti_cut_point = []

for i in range(cnt):
    op, line_num = map(int, input().split())
    if op == 1:
        horiz_cut_point.append(line_num)
    else:
        verti_cut_point.append(line_num)

horiz_cut_point.append(w)
verti_cut_point.append(h)

max_horiz_gap = 0
max_vertical_gap = 0
prev_horiz = 0
prev_vertical = 0

for h_p in sorted(horiz_cut_point):
    max_horiz_gap = max(max_horiz_gap, h_p-prev_horiz)
    prev_horiz = h_p

for v_p in sorted(verti_cut_point) :
    max_vertical_gap = max(max_vertical_gap, v_p - prev_vertical)
    prev_vertical = v_p

print(max_horiz_gap * max_vertical_gap)
