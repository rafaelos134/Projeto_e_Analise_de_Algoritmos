def insertion_sort(A):
    n = len(A)
    for j in range(2, n):  # começa do índice 1 até n-1
        chave = A[j]
        i = j - 1
        while i >= 0 and A[i] >= chave:  # usa >= como no pseudocódigo
            A[i+1] = A[i]
            i -= 1
        A[i+1] = chave
    return A


def insertion_sort_cormen(A):
    n = len(A)
    for j in range(1, n):  # começa do índice 1 até n-1
        chave = A[j]
        i = j - 1
        while i >= 0 and A[i] > chave:  # estritamente >
            A[i+1] = A[i]
            i -= 1
        A[i+1] = chave
    return A



A = [5,2,3,4,9,8,6]


B = insertion_sort(A)
C = insertion_sort_cormen(A)

print(B)
print(C)