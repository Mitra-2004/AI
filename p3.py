# Implement A* Search for the 8 Puzzle Problem
#To implement the A* search algorithm to solve the 8 Puzzle problem.


import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)

    return distance

queue = [(heuristic(start), 0, start)]
visited = set()
parent = {start: None}
cost = {start: 0}

while queue:
    f, g, state = heapq.heappop(queue)

    if state == goal:
        break

    if state in visited:
        continue

    visited.add(state)
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

        new_cost = g + 1

        if new_state not in cost or new_cost < cost[new_state]:
            cost[new_state] = new_cost
            parent[new_state] = state
            h = heuristic(new_state)
            heapq.heappush(queue, (new_cost + h, new_cost, new_state))

if state == goal:
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    for state in path:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution found")
