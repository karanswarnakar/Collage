# Breadth First Search (love it 💖) 
def bfs(start, goal):
    q = [start]
    visited = []
    while(q):
        y = q.pop(0)
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

bfs(start, goal)