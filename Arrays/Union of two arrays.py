# -*- coding: utf-8 -*-

def union(A, B):
    count = 0
    for i in range(N):
        for j in range(M):
            if B[j] == A[i]:
                count = count + 1
    ans.append(N + M - count)
    count = 0


def intersection(A, B):
    count = 0
    for i in range(N):
        for j in range(M):
            if B[j] == A[i]:
                count = count + 1
    ans.append(count)
    count = 0


ans = []
T = int(input())
for i in range(T):
    N, M = map(int, input().split(" "))
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))
    union(A, B)
for i in ans:
    print(i)
