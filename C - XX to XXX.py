S = list(input())
T = list(input())

i = 0
j = 0
while True:
    if S[i] == T[j]:
        i += 1
        j += 1
    else:
        if T[j-2] == T[j-1] == T[j]:
            j += 1
        else:
            print('No')
            exit()

    if i == len(S):
        break

for k in range(j, len(T)-1):
    if T[k] != T[k+1]:
        print('No')
        exit()

print('Yes')