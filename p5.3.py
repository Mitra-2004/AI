# 8 puzzle problem

from collections import deque

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

queue = deque([start])
visited = {start}
parent = {}

while queue:
    state = queue.popleft()

    if state == goal:
        break

    pos = state.index(0)
    moves = []

    if pos >= 3:
        moves.append(pos - 3)
    if pos < 6:
        moves.append(pos + 3)
    if pos % 3 != 0:
        moves.append(pos - 1)
    if pos % 3 != 2:
        moves.append(pos + 1)

    for new_pos in moves:
        new_state = list(state)
        new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
        new_state = tuple(new_state)

        if new_state not in visited:
            visited.add(new_state)
            parent[new_state] = state
            queue.append(new_state)

if goal in visited:
    path = []
    state = goal

    while state != start:
        path.append(state)
        state = parent[state]

    path.append(start)
    path.reverse()

    for state in path:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution found")
