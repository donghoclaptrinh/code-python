N, M, X, T, D = map(int, input().split())

if M > X:
    ans = T
else :
    deff = X - M
    deff_height = D * deff
    ans = T - deff_height

print(ans)