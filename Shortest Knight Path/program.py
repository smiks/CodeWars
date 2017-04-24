def knight(p1, p2):
    from collections import deque

    mapper = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}
    mapper_inv = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    visited = set()
    que = deque()

    start_pos = tuple(p1)
    start_pos = (int(mapper_inv[start_pos[0]]), int(start_pos[1]))

    que.appendleft((start_pos, 1))

    def _gen_move(spos):
        """
        Generate next moves
        eg. spos = (a, 1) == (1, 1) == (x, y)
        """
        dx = [-2, -1, 1, 2, 2, 1, -1, -2]  # relative directions x
        dy = [1, 2, 2, 1, -1, -2, -2, -1]  # relative directions y
        for d in range(8):
            nx = spos[0] + dx[d]
            ny = spos[1] + dy[d]
            if not 0 < nx < 9 or not 0 < ny < 9 and (nx, ny) not in visited:
                continue
            npos = (nx, ny)
            visited.add(npos)
            yield npos

    while len(que) > 0:

        # generate next positions and put them in que
        sp, step = que.pop()
        for nm in _gen_move(sp):
            # check if next move is last
            nm_ = mapper[nm[0]]+str(nm[1])
            if nm_ == p2:
                return step
            que.appendleft((nm, step+1))
