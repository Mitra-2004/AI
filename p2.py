#Implement a model-based intelligent agent that navigates a grid environment with obstacles using an internal state representation.

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

position = (0, 0)
goal = (2, 2)
visited = set()

while position != goal:
    visited.add(position)
    print("Current position:", position)

    r, c = position

    if c < 2 and grid[r][c + 1] == 0 and (r, c + 1) not in visited:
        position = (r, c + 1)
    elif r < 2 and grid[r + 1][c] == 0 and (r + 1, c) not in visited:
        position = (r + 1, c)
    elif c > 0 and grid[r][c - 1] == 0 and (r, c - 1) not in visited:
        position = (r, c - 1)
    elif r > 0 and grid[r - 1][c] == 0 and (r - 1, c) not in visited:
        position = (r - 1, c)
    else:
        print("No path found")
        break

if position == goal:
    print("Goal reached:", goal)
