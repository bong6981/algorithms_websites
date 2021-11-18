def solution(n):
    return (n ** 0.5 + 1)**2  if n ** 0.5 == float(int(n ** 0.5)) else -1

print(solution(10))
