x, y, c = map(float, input().split())

start = 0
end = min(x, y)
ans = 0

while start+0.0001 <= end:
    mid = (start + end) / 2
    
    h1 = (x**2 - mid**2)**0.5
    h2 = (y**2 - mid**2)**0.5
    tmp = (h1*h2)/(h1+h2)

    if tmp >= c :
        ans = mid
        start = mid
    else:
        end = mid
print(ans)


