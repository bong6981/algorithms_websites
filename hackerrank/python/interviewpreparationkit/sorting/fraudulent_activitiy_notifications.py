## https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

## CountingSort를 쓰는 방식
def activityNotifications(expenditure, d):
    mididx1 = d // 2
    mididx2 = mididx1 if d % 2 else mididx1 -1 
    count = [0] * 201
    for e in expenditure[:d] :
        count[e] += 1
    
    cnt = 0
    for i, value in enumerate(expenditure[d:], d):
        before = expenditure[i-d]
        if value >= get_medains(count, mididx1, mididx2) :
            cnt += 1
        
        count[before] -= 1
        count[value] += 1 
    
    return cnt

def get_medains(counter, mididx1, mididx2):
    count = 0
    ans_mididx2 = -1
    for i, v  in enumerate(counter) :
        count += v
        if ans_mididx2 == -1 and count > mididx2 :
            if count > mididx1:
                return i * 2
            else :
                ans_mididx2 = i
        if count > mididx1 :
            return ans_mididx2 + i

## bisect를 쓰는 방식 
import bisect
def activityNotifications(expenditure, d):
    traling = sorted(expenditure[:d])
    mididx1 = d // 2
    mididx2 = mididx1 if d % 2 else mididx1 -1 
    cnt = 0

    for i, value in enumerate(expenditure[d:], d):
        before = expenditure[i-d]
        if value >= (traling[mididx1] + traling[mididx2])  :
            cnt += 1
        to_remove = bisect.bisect_left(traling, before)
        traling.pop(to_remove)
        bisect.insort(traling, value)
    return cnt

def pick_middle(traling):
    temp = sorted(traling)
    if len(temp) % 2 == 1:
        return temp[len(temp) // 2]
    x = len(temp) // 2
    return (temp[x] + temp[x-1]) / 2 
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print("result : " + str(result))


'''
5 4
1 2 3 4 4
답 : 0
'''

'''
9 5
2 3 4 2 3 6 8 4 5
답 : 2
'''

'''
5 3
10 20 30 40 50
답 1
'''
