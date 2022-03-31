x, y, w, h = map(int, input().split(" "))

print(min(min(abs(w-x), abs(w-0)), min(abs(h-y), abs(y-0))))

