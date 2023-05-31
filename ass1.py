# DFS implementation
visited = set()
def dfs(visited, graph, root):
    if root not in visited:
        print(root, end=' ')
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)

# BFS implementation
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Call the DFS & BFS function with the starting vertex
print("The DFS is : ")
dfs(visited, graph, root="A")
print("\nThe BFS is : ")
bfs(graph, 'A')
