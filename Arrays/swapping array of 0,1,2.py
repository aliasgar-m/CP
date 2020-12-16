def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def sorting(A, end):
    start = mid = 0
    check = 1
    while mid <= end:
        if A[mid] < check:
            swap(A, mid, start)
            start = start + 1
            mid = mid + 1
        elif A[mid] > check:
            swap(A, mid, end)
            end = end - 1
        else:
            mid = mid + 1


if __name__ == '__main__':
    A = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
    sorting(A, len(A) - 1)
    print(A)
