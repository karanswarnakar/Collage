def beam_search(start, goal, width):
    q = [start]
    visited = []
    
    while q:
        new = []
        
        for y in q:
            visited.append(y)
            
            if y == goal:
                print(visited)
                return
            
            for i in graph[y]:
                if i not in visited:
                    new.append(i)
        
        new.sort(key=lambda x: h[x])
        q = new[:width]
        print(q)
        
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
        
        
        
beam_search("A", "H", 2)