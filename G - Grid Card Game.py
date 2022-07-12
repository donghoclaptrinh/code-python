from collections import deque
from typing import List, Tuple


class Dinic:
    """
    Usage:
       mf = Dinic(n)
    -> mf.add_link(from, to, capacity)
    -> mf.max_flow(source, target)
    """

    def __init__(self, n: int):
        self.n = n
        self.links: List[List[List[int]]] = [[] for _ in range(n)]
        # if exists an edge (v→u, capacity)...
        #   links[v] = [ [ capacity, u, index of rev-edge in links[u], is_original_edge ], ]

    def add_link(self, from_: int, to: int, capacity: int) -> None:
        self.links[from_].append([capacity, to, len(self.links[to]), 1])
        self.links[to].append([0, from_, len(self.links[from_]) - 1, 0])

    def bfs(self, s: int) -> List[int]:
        depth = [-1] * self.n
        depth[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for cap, to, rev, _ in self.links[v]:
                if cap > 0 and depth[to] < 0:
                    depth[to] = depth[v] + 1
                    q.append(to)
        return depth

    def dfs(self, s: int, t: int, depth: List[int], progress: List[int], link_counts: List[int]) -> int:
        links = self.links
        stack = [s]

        while stack:
            v = stack[-1]
            if v == t:
                break
            for i in range(progress[v], link_counts[v]):
                progress[v] = i
                cap, to, rev, _ = links[v][i]
                if cap == 0 or depth[v] >= depth[to] or progress[to] >= link_counts[to]:
                    continue
                stack.append(to)
                break
            else:
                progress[v] += 1
                stack.pop()
        else:
            return 0

        f = 1 << 60
        fwd_links = []
        bwd_links = []
        for v in stack[:-1]:
            cap, to, rev, _ = link = links[v][progress[v]]
            f = min(f, cap)
            fwd_links.append(link)
            bwd_links.append(links[to][rev])

        for link in fwd_links:
            link[0] -= f

        for link in bwd_links:
            link[0] += f

        return f

    def max_flow(self, s: int, t: int) -> int:
        link_counts = list(map(len, self.links))
        flow = 0
        while True:
            depth = self.bfs(s)
            if depth[t] < 0:
                break
            progress = [0] * self.n
            current_flow = self.dfs(s, t, depth, progress, link_counts)
            while current_flow > 0:
                flow += current_flow
                current_flow = self.dfs(s, t, depth, progress, link_counts)
        return flow

    def cut_edges(self, s: int) -> List[Tuple[int, int]]:
        """ max_flowしたあと、最小カットにおいてカットすべき辺を復元する """
        q = [s]
        reachable = [0] * self.n
        reachable[s] = 1
        while q:
            v = q.pop()
            for cap, u, li, _ in self.links[v]:
                if cap == 0 or reachable[u]:
                    continue
                reachable[u] = 1
                q.append(u)
        edges = []
        for v in range(self.n):
            if reachable[v] == 0:
                continue
            for cap, u, li, orig in self.links[v]:
                if orig == 1 and reachable[u] == 0:
                    edges.append((v, u))
        return edges


h, w = map(int, input().split())
aaa = [list(map(int, input().split())) for _ in range(h)]

rows_sum = list(map(sum, aaa))
cols_sum = list(map(sum, zip(*aaa)))
available_rows = [i for i, s in enumerate(rows_sum) if s > 0]
available_cols = [i for i, s in enumerate(cols_sum) if s > 0]

nr = len(available_rows)
nc = len(available_cols)

dnc = Dinic(nr + nc + 2)
s = nr + nc
t = s + 1
INF = 1 << 40
ans = 0

for ri, i in enumerate(available_rows):
    dnc.add_link(s, ri, rows_sum[i])
    dnc.add_link(ri, t, 0)
    ans += rows_sum[i]

for cj, j in enumerate(available_cols, start=nr):
    dnc.add_link(s, cj, 0)
    dnc.add_link(cj, t, cols_sum[j])
    ans += cols_sum[j]

for ri, i in enumerate(available_rows):
    for cj, j in enumerate(available_cols, start=nr):
        if aaa[i][j] < 0:
            dnc.add_link(ri, cj, INF)
        elif aaa[i][j] > 0:
            dnc.add_link(ri, cj, aaa[i][j])

res = dnc.max_flow(s, t)
ans -= res
print(ans)
