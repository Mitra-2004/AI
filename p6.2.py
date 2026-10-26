# MIssionaries and cannibals problem statement
def dfs(m, c, boat, visited):
    state = (m, c, boat)

    if state in visited:
        return False

    visited.add(state)
    print(state)

    if state == (0, 0, 0):
        print("All crossed safely!")
        return True

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for a, b in moves:
        if boat == 1:
            nm, nc, nb = m-a, c-b, 0
        else:
            nm, nc, nb = m+a, c+b, 1

        if not (0 <= nm <= 3 and 0 <= nc <= 3):
            continue

        if (nm > 0 and nc > nm) or (3-nm > 0 and 3-nc > 3-nm):
            continue

        if dfs(nm, nc, nb, visited):
            return True

    return False

dfs(3, 3, 1, set())
