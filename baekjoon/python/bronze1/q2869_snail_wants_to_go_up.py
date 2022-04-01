import sys
input = sys.stdin.readline

import math

a, b, v = map(int, input().split())
print(math.ceil((v-b) / (a-b)))

print(math.ceil((v-a)/(a-b))+1)

