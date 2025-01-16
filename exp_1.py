import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import heapq
import time

class MazePathfinder:

    # define start,end and maze shape
    def __init__(self, maze):
        self.maze = maze
        self.rows, self.cols = maze.shape
        self.start = (0, 0)
        self.end = (self.rows-1, self.cols-1)
        
    def get_neighbors(self, pos):
        row, col = pos
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if (0 <= r < self.rows and 0 <= c < self.cols and 
                self.maze[r, c] == 0):
                neighbors.append((r, c))
        return neighbors
    
    # for A* algo
    def manhattan_distance(self, pos):
        return abs(pos[0] - self.end[0]) + abs(pos[1] - self.end[1])
    
    #Breadth first Search Algo
    def bfs(self):
        start_time = time.time()
        visited = set([self.start])
        queue = deque([(self.start, [self.start])])
        nodes_explored = 0
        
        while queue:
            current, path = queue.popleft()
            nodes_explored += 1
            
            if current == self.end:
                return {
                    'path': path,
                    'nodes_explored': nodes_explored,
                    'time': time.time() - start_time
                }
            
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None
    
    # Depth First Search Algo
    def dfs(self):
        start_time = time.time()
        visited = set([self.start])
        stack = [(self.start, [self.start])]
        nodes_explored = 0
        
        while stack:
            current, path = stack.pop()
            nodes_explored += 1
            
            if current == self.end:
                return {
                    'path': path,
                    'nodes_explored': nodes_explored,
                    'time': time.time() - start_time
                }
            
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor]))
        return None
    
    # A* algo
    def a_star(self):
        start_time = time.time()
        nodes_explored = 0
        frontier = [(0, self.start, [self.start])]
        visited = {self.start: 0}
        
        while frontier:
            f_score, current, path = heapq.heappop(frontier)
            nodes_explored += 1
            
            if current == self.end:
                return {
                    'path': path,
                    'nodes_explored': nodes_explored,
                    'time': time.time() - start_time
                }
            
            for neighbor in self.get_neighbors(current):
                g_score = len(path)
                h_score = self.manhattan_distance(neighbor)
                f_score = g_score + h_score
                
                if neighbor not in visited or f_score < visited[neighbor]:
                    visited[neighbor] = f_score
                    heapq.heappush(frontier, (f_score, neighbor, path + [neighbor]))
        return None
    
    # Dijkstra Algo
    def dijkstra(self):
        start_time = time.time()
        nodes_explored = 0
        pq = [(0, self.start, [self.start])]
        distances = {self.start: 0}
        
        while pq:
            current_dist, current, path = heapq.heappop(pq)
            nodes_explored += 1
            
            if current == self.end:
                return {
                    'path': path,
                    'nodes_explored': nodes_explored,
                    'time': time.time() - start_time
                }
            
            if current in distances and current_dist > distances[current]:
                continue
            
            for neighbor in self.get_neighbors(current):
                distance = current_dist + 1
                
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor, path + [neighbor]))
        return None

# mazes
mazes = {
    'Series 1': np.array([
        [0,0,0,1,0,1,0,0,0,0,0,0,0],
        [0,0,1,1,0,1,0,0,0,1,0,0,0],
        [0,1,1,0,0,1,0,0,1,1,0,0,1],
        [0,0,1,0,0,1,0,0,1,0,0,0,1],
        [0,0,0,0,0,1,0,0,1,0,0,1,1],
        [1,0,0,1,0,1,0,0,1,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,0,0,0,0,1,0]
    ]),
    'Series 2': np.array([
        [0,0,1,1,0,0,1,0,1,1,0],
        [0,1,1,0,0,0,0,0,0,1,0],
        [0,0,0,0,1,1,1,0,0,0,0],
        [1,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0],
        [1,0,1,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,1,0]
    ]),
    'Series 3': np.array([
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]
    ]),
    'Series 4': np.array([
        [0,0,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,1,1,1,0],
        [1,1,0,0,0,0,0,0,1,1,0],
        [1,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,1,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,1,0]
    ])
}


# visualise
def plot_all_results(mazes):
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(4, 4, figsize=(15, 15))
    fig.suptitle('', y=0.98, fontsize=14)
    
    algorithms = ['BFS', 'DFS', 'A*', "Dijkstra's"]
    
    for row, (maze_name, maze) in enumerate(mazes.items()):
        pathfinder = MazePathfinder(maze)
        results = [
            pathfinder.bfs(),
            pathfinder.dfs(),
            pathfinder.a_star(),
            pathfinder.dijkstra()
        ]
        
        axes[row, 0].text(-0.3, 0.5, maze_name, rotation=90, 
                         transform=axes[row, 0].transAxes, fontsize=10)
        
        for col, (algo_name, result) in enumerate(zip(algorithms, results)):
            ax = axes[row, col]
            ax.imshow(maze, cmap='binary')
            
            if result:
                path = result['path']
                path = np.array(path)
                ax.plot(path[:, 1], path[:, 0], 'r-', linewidth=1.5, alpha=0.7)
            
            ax.plot(0, 0, 'ro', markersize=6)
            ax.plot(maze.shape[1]-1, maze.shape[0]-1, 'go', markersize=6)
            
            if row == 0:
                ax.set_title(f'{algo_name}', pad=5, fontsize=10)
            
            if result:
                metrics = f'T: {result["time"]:.3f}s\nN: {result["nodes_explored"]}\nL: {len(result["path"])}'
            else:
                metrics = 'No path'
            ax.text(0.5, -0.15, metrics, ha='center', transform=ax.transAxes, fontsize=8)
            
            ax.axis('off')
    
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, 
                       wspace=0.2, hspace=0.3)
    return fig


fig = plot_all_results(mazes)
plt.show()