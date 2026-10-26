#River crossing using DFS 

def dfs(state, visited):
    if state in visited:
        return False

    visited.add(state)
    print(state)

    if state == (1, 1, 1, 1):
        print("Everyone crossed safely!")
        return True

    f, w, g, c = state

    for item in [-1, 0, 1, 2]:
        if item == -1:
            new = (1-f, w, g, c)
        elif item == 0 and w == f:
            new = (1-f, 1-w, g, c)
        elif item == 1 and g == f:
            new = (1-f, w, 1-g, c)
        elif item == 2 and c == f:
            new = (1-f, w, g, 1-c)
        else:
            continue

        nf, nw, ng, nc = new

        if nw == ng and nf != nw:
            continue
        if ng == nc and nf != ng:
            continue

        if dfs(new, visited):
            return True

    return False

dfs((0, 0, 0, 0), set())
