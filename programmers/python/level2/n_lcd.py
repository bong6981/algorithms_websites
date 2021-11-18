from functools import reduce
def solution(arr):
    gcd = lambda x,y : y if x%y == 0 else gcd(y, x%y)
    lcm = lambda x,y : x*y // gcd(x,y)
    return reduce(lambda x,y: lcm(x,y), arr, 1)

from math import gcd
def solution2(arr) :
    return reduce(lambda x,y: x*y//gcd(x,y), arr, 1)

print(solution2([2,6,8,14]))
print(solution2([1,2,3]))

