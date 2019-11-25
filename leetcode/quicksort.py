#QuickSort Implementation -> no small enhancements
def swap(A, a, b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp


def partition(A, l, h) -> int:
    pivot = A[h]  # take rightmost element as pivot element
    i = l - 1

    for j in range(l, h+1):
        if A[j] < pivot:
            swap(A, i + 1, j)
            i += 1
    swap(A, i + 1, h)
    return i + 1


def quicksort(A, l, h):
    if l < h:
        p = partition(A, l, h)
        quicksort(A, l, p - 1)
        quicksort(A, p + 1, h)


if __name__ == "__main__":
    a = [-10,2,300,1000,-500,-700,2,0]
    quicksort(a, 0, len(a)- 1)
    print(a)
