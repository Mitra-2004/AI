#Blocks worlds problem

from collections import deque

start = (("A",), ("B",), ("C",))
goal = (("C", "B", "A"),)

queue = deque([start])
visited = {start}
parent = {}

while queue:
    state = queue.popleft()

    if state == goal:
        break

    for i in range(len(state)):
        if not state[i]:
            continue

        block = state[i][-1]
        new_stacks = [list(s) for s in state]
        new_stacks[i].pop()

        for j in range(len(state) + 1):
            if i == j:
                continue

            temp = [s[:] for s in new_stacks]

            if j < len(state):
                temp[j].append(block)
            else:
                temp.append([block])

            new_state = tuple(tuple(s) for s in temp if s)

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

    for step in path:
        print(step)
else:
    print("Goal not found")
