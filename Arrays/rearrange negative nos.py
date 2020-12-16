# -*- coding: utf-8 -*-

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def rearrange(A):
    start = 0
    end = len(A) - 1
    while start <= end:
        if A[start] < 0:
            start = start + 1
        else:
            swap(A, start, end)
            end = end - 1


if __name__ == "__main__":

    A = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    rearrange(A)
    print(A)
