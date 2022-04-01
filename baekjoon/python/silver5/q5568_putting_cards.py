import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

cards = []
for _ in range(n):
    cards.append(input().rstrip())

numbers = set()

def put_cards_proc(arr, visited):
    if len(arr) == k:
        str = ''
        for s in arr:
            str += s
        numbers.add(int(str))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(cards[i])
            put_cards_proc(arr, visited)
            arr.pop()
            visited[i] = False

put_cards_proc([], [False for _ in range(n)])
print(len(numbers))

