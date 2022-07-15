import sys
input = sys.stdin.readline

n, q = map(int, input().split())

result = [0] * (n+2)
print(result)

max_v = 0
sum = 0

for _ in range(q):
    q, x, y =  map(int, input().split())
    if q == 1:
        result[y] += x
        if y != n+1:
            max_v = max(max_v, result[y])
            sum += x
    
    else:
        print(result, max_v, sum)
        if result[n+1] + x <= max(result[1:n+1]):
            print("NO")
        else:
            if 
            # 더해야 할 것이 y 
            print("@@@")
            to_add = max_v * n - sum

            if to_add <= y:
                print("YES")
            else:
                to_add -= y
                res = to_add // n
                if to_add % n > 0:
                    res += 1
                if max_v + res < result[n+1]+x:
                    print("YES")
                else:
                    print("NO")

