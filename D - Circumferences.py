import math
import sys
import copy

def zeros(*shape):
    def _zeros(i):
        if i >= len(shape):
            return 0
        z = []
        for j in range(shape[i]):
            elem = _zeros(i+1)
            z.append(elem)
        return z
    return _zeros(0)

n, = list(map(lambda i: int(i), input().split()))
s_x, s_y, t_x, t_y, = list(map(lambda i: int(i), input().split()))
x = zeros(n)
y = zeros(n)
r = zeros(n)
for i in range(n):
    x[i], y[i], r[i] = list(map(lambda i: int(i), input().split()))

sys.setrecursionlimit(n+1000)

def is_contiguous(i,j):
    if i==j:
        return True
    d = (x[i]-x[j])**2+(y[i]-y[j])**2
    return (r[i]+r[j])**2 >= d and (r[i]-r[j])**2 <= d

vis = zeros(n)

def dfs(i):
    vis[i] = 1
    # print(vis)
    d = (x[i]-t_x)**2+(y[i]-t_y)**2
    if d == r[i]**2:
        return True
    res = False
    for j in range(n):
        if i==j:
            continue
        if vis[j]==0 and is_contiguous(i,j):
            res = res or dfs(j)
            if res:
                break
    return res

fres = False
for i in range(n):
    d = (x[i]-s_x)**2+(y[i]-s_y)**2
    if d == r[i]**2:
        fres = dfs(i)
        break

print("Yes" if fres else "No")
