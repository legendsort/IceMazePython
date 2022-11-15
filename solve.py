
# for file input
with open('./test3.txt') as f:
    # input
    lines = f.readlines()
    n, m, t = list(map(int, lines[0].split()))
    grid = []
    queue = []
    target = (t, m)
    m += 1
    ans = {}
    for i in range(n):    
        squares = list(lines[i + 1].split())
        grid.append(squares)
        if i == t: grid[i].append('.')
        else: grid[i].append('*')
        pass

    # init for graph and dfs search
    inf = 1000000000
    dst = [[inf for x in range(m)]  for _ in range(n)]
    graph = [[[] for x in range(m)] for _ in range(n)]
    bgraph = [[[] for x in range(m)] for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0 ,1, 0, -1]
    # find next position starting from (x, y) towards kth direction.
    def findNext(x, y, k):
        while grid[x][y] != '*':
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= n or ny >= m or nx < 0 or ny < 0 or grid[nx][ny] == '*':
                break
            x, y = nx, ny
            pass
        return x, y

    # build graph
    def buildGraph():
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '*':
                    for k in range(4):
                        ni, nj = findNext(i, j, k)
                        if ni != i or nj != j:
                            graph[i][j].append((ni, nj))
                            bgraph[ni][nj].append((i, j))
                pass
            pass
        pass
    buildGraph()
    # bfs
    queue.append((t, m-1))
    dst[t][m-1] = 0
    while queue:
        x, y = queue.pop(0)
        d = dst[x][y]
        if d in ans:
            ans[d].append((x, y))
            pass
        elif d > 0:
            ans[d] = [(x, y)]
            pass
        for i in range(len(bgraph[x][y])):
            nx, ny = bgraph[x][y][i]
            if nx != x or ny != y:
                if dst[nx][ny] == inf:
                    dst[nx][ny] = d + 1
                    queue.append((nx, ny))
                    pass
                pass
            pass
        pass
    
    cant = []
    for i in range(n):
        for j in range(m-1):
            if dst[i][j] == inf:
                cant.append((i, j))
    
    # output
    for key in ans:
        print(key, ": [", end="")
        print(", ".join(map(lambda x: "({}, {})".format(x[0], x[1]), ans[key])), end='')
        print("]")

    print("No path: [", end="")
    print(", ".join(map(lambda x: "({}, {})".format(x[0], x[1]), cant)), end='')
    print("]")


