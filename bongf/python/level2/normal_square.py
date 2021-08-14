
## 시간초과되서 특이 케이스 연산 안하게 처리해줬더니 통과 
def solution(w,h):
    if(w==h) :
        return w * w - w
    elif(w==1 or h==1):
        return 0
    return sum(int(-(h/w)*i + h)  for i in range(1, w)) * 2

def gcd(a,b) : 
    return b if a%b == 0 else gcd(b, a%b)
def solution2(w, h):
    return w*h - (w+h-gcd(w,h))
    ## 둘의 최대공약수가 1이 아니면 가장 작은(정수)닮은 사각형의 꼭지점에서 대각선과 만나고, 그것이 반복된다 
    ## w와 h의 최대공약수가 1이면 가로길이만큼 한줄 세로길이 만큼 한번씩 쫙 지나는데 세로 가로 한번씩 반복되니까 뺴줘야함 w + h - 1
    ## 선이 지나가는 사각형 개수 : 최대공약수 * 반복되는블럭에서 선이랑 겹치는 수 
    ## 최대공약수 = g
    ## = g * (( w//g) + (h//g) - 1) = w + h - g
print(solution2(12, 8))
