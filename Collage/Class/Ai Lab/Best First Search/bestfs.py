def bestfs(start, goal):
    q = [start]
    visited = []
    
    while(q):
        q.sort(key=lambda x: h[x])
        y = q.pop(0)
        
        visited.append(y)  
        
        if y == goal:
            print(visited)
            return
        
        for i in graph[y]:
            if i not in q and i not in visited:
                q.append(i)
graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":["H"],
    "E":["I"],
    "F":["J"],
    "G":["K","L"],
    "H":[],
    "I":[],
    "J":[],
    "K":[],
    "L":[]
}
h = {
    "A":0,
    "B":3,
    "C":2,
    "D":2,
    "E":3,
    "F":2,
    "G":4,
    "H":1,
    "I":99,
    "J":99,
    "K":99,
    "L":3
}
     
bestfs("A", "H")