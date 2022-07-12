def stacked_dfs():
    no_select, selectable = [0]*N, [0]*N
    stack = [(0, -1, True)]  # (u, par, to_child})

    while stack:
        u, par, to_child = stack.pop()

        if to_child:
            stack.append((u, par, False))  # to parent
            for v, _ in adj[u]:
                if v != par:
                    stack.append((v, u, True))

        else:  # to parent
            base = 0
            diff = [0]
            for v, w in adj[u]:
                if v == par:
                    continue
                base += no_select[v]
                diff.append(max(0, max(0, w) + selectable[v] - no_select[v]))
            diff.sort(reverse=True)
            no_select[u] = selectable[u] = base
            if deg_limit[u] == 0:
                selectable[u] = -INF
            else:
                sum_diff = sum(diff[:deg_limit[u] - 1])
                selectable[u] += sum_diff
                no_select[u] += sum_diff + diff[deg_limit[u] - 1]

    return no_select[0]
# stacked_dfs end


INF = float('inf')
N = int(input())
deg_limit = [*map(int, input().split())]

adj = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append((v, w))
    adj[v].append((u, w))

print(stacked_dfs())
