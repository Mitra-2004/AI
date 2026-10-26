# Blocks world using DFS


def dfs(state, visited):
    state = tuple(state)

    if state in visited:
        return False

    visited.add(state)
    print(state)

    if state == ("C", "B", "A"):
        print("Goal reached!")
        return True

    for i in range(len(state)):
        new_state = list(state)
        block = new_state.pop(i)
        new_state.append(block)

        if dfs(new_state, visited):
            return True

    return False

dfs(["A", "B", "C"], set())
