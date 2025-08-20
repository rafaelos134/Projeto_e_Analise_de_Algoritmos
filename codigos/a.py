A = [5,1,2,3,4]

n = len(A)

for i in range(1,n):
    print(f"i: {i}")
    for j in range(n-1,i-1, -1):
        print(f"j: {j}")
        if A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]

print(A)