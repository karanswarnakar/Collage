def hill_climbing(start, goal):
    current = start
    visited = [current]

    while True:
        if current == goal:
            print(visited); 
            return
        
        if not graph[current]:
            print("No path found"); 
            return
        
        next_node = min(graph[current], key=lambda x: h[x])
        
        if h[next_node] >= h[current]:
            print("Stuck at", current)
            print(visited); 
            return
        
        current = next_node
        visited.append(current)
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
    "A":10,
    "B":3,
    "C":2,
    "D":5,
    "E":3,
    "F":9,
    "G":6,
    "H":1,
    "I":99,
    "J":99,
    "K":99,
    "L":3
}   
    
    
hill_climbing("A","L")   
    
    