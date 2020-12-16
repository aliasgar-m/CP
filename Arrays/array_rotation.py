# -*- coding: utf-8 -*-


def cycle(A, n):
    temp = A[n-1]
    while (n-1) != 0:
        A[n-1] = A[n-2]
        n = n-1
        if n-1 == 0:
            A[0] = temp
    for i in A:
        print(i, end=" ")
    print("")


T = input()
for i in range(int(T)):
    N = input()
    Arr = list(map(int, input().split()))
    cycle(Arr, int(N))
