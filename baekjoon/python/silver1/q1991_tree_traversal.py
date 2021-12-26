def solution():
    n = int(input())
    graph = {}
    for _ in range(n):
        node, left, right = input().split()
        graph[node] = [left, right]
    print(preorder(graph, 'A'))
    print(inorder(graph, 'A'))
    print(postorder(graph, 'A'))

def preorder(graph, v):
    string = v
    left = graph[v][0]
    right = graph[v][1]
    if left != '.':
        string += preorder(graph, left)
    if right != '.':
        string += preorder(graph, right)
    return string

def inorder(graph, v):
    string = v
    left = graph[v][0]
    right = graph[v][1]
    if left != '.':
        string = inorder(graph, left) + string
    if right != '.':
        string += inorder(graph, right)
    return string

def postorder(graph, v):
    string = ''
    left = graph[v][0]
    right = graph[v][1]
    if left != '.':
        string = postorder(graph, left)
    if right != '.':
        string += postorder(graph, right)
    return string + v








solution()
