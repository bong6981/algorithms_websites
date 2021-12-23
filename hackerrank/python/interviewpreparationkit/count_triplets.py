# https://www.hackerrank.com/challenges/count-triplets-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Medium
def countTriplets(arr, r):
    result = 0
    ask_midde = {}
    ask_end = {}

    for num in arr :
        toAdd = ask_end.get(num)
        if toAdd != None :
            result += toAdd

        if ask_midde.get(num) != None :
            toAdd = 0
            if ask_end.get(num*r) != None:
                toAdd += ask_end[num*r]
            ask_end[num*r] = ask_midde[num] + toAdd
        
        toAdd = 0
        if ask_midde.get(num*r) != None :
            toAdd += ask_midde[num*r]
        ask_midde[num*r] = toAdd + 1
    return result


if __name__ == '__main__':
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)

# https://shareablecode.com/snippets/python-solution-for-hackerrank-problem-count-triplets-wX7k-vEUY
from collections import defaultdict

def count_triplets_other(arr, r):
    arr2 = defaultdict(int)
    arr3 = defaultdict(int)
    count = 0
    for i in arr:
        count += arr3[i]
        arr3[i*r] += arr2[i]
        arr2[i*r] += 1
    return count

n, r = map(int, input().split())
arr = list(map(int, input().split()))
print(count_triplets_other(arr, r))

