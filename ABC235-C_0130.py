#ABC235-C
#titia

import sys
input = sys.stdin.readline
 
N,Q=map(int,input().split())
A=list(map(int,input().split()))
 
D=dict()
 
for i in range(N):
    if A[i] in D:
        D[A[i]].append(i)
    else:
        D[A[i]]=[i]

for i in range(Q):
    x,k=map(int,input().split())
 
    if not (x in D) or len(D[x])<k:
        print(-1)
    else:
        ans=D[x][k-1]
        print(ans+1)