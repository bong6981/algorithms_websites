def trap(height) -> int:
    graph = []
    ans = 0
    for i, h in enumerate(height):
        while graph and height[graph[-1]] < h:
            now = graph.pop()
            if(not graph):
                break
            ans += (min(height[graph[-1]], h) - height[now]) * (i-graph[-1]-1)  
        graph.append(i)
    return ans


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
