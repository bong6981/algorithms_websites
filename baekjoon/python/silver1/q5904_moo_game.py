## https://www.acmicpc.net/problem/5904
n = int(input())

def moo(length, center, n):
  prev = (length-center)//2

  if n < prev:
    moo(prev,center-1,n)
  elif n > prev + center:
    moo(prev,center-1, n-(prev + center))
  else:
    if n-prev == 1:
      print('m')
    else:
      print('o')

length = 3
k = 0
while length < n:
  k+=1
  length = 2*length+ k+3

moo(length, k+3, n)
