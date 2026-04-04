# Depth First Search (like it more )
def dfs(start, goal):
    q = [start]
    visited = []
    while(q):
        y = q.pop()
        print(y)
        if y == goal: 
            visited.append(y)
            print(visited)
            return
        visited.append(y)
        q.extend(graph[y])
    
 
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':['H','I'],
    'E':['J','K'],
    'F':['L'],
    'G':[],
    'H':[],
    'I':[],
    'J':[],
    'K':[],
    'L':[]
}
start = input("Enter Start point: ")
goal = input("Enter Goal: ")

dfs(start, goal)        