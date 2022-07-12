from collections import defaultdict
n = int(input())
d = defaultdict(list)
a = defaultdict(list)
for i in range(n):
  m = int(input())
  for j in range(m):
    p,e = map(int, input().split())
    d[p].append((e,i))
    
for k,v in d.items():
  v.sort(reverse=True)
  if len(v) > 1 and v[0][0] != v[1][0]:
    a[v[0][1]].append(k)
  if len(v) == 1:
    a[v[0][1]].append(k)
    
ans = len(a)
if ans != n:
  ans += 1
print(ans)
    
  
