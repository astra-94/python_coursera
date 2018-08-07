def Smallest(A):
    i = 0
    for i in range(len(A)):
        i += 1
        if int(A[i]) % 2 != 0:
            n = A[i]
        break
    for i in range(len(A)):
        i += 1
        if int(A[i])%2 !=0 and int(A[i]) < n:
            n = int(A[i])

    return n


A = input().split(' ')
print(Smallest(A), end=' ')
