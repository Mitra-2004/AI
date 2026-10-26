# Design a Python program using BFS to find a path for a robot from a starting position to a goal position in a grid containing obstacles.

from collections import deque

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

start = (0, 0)
goal = (2, 2)

queue = deque([start])
visited = [start]
parent = {}

while queue:
    current = queue.popleft()

    if current == goal:
        break

    r, c = current

    for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
        if (0 <= nr < 3 and 0 <= nc < 3
            and grid[nr][nc] == 0
            and (nr, nc) not in visited):

            visited.append((nr, nc))
            parent[(nr, nc)] = current
            queue.append((nr, nc))

if goal in visited:
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    print("Path:", path)
else:
    print("No path found")
