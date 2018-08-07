def merge(A, B):
    C=[]
    k = 0
    n = 0
    while k+n <= len(A)+len(B)-1:
        if k<len(A) and n<len(B):
            if A[k]>B[n]:
                C.append(B[n])
                n += 1
            else:
                C.append(A[k])
                k += 1
        else:
            if k==len(A):
                C.append(B[n])
                n+=1
            else:
                C.append(A[k])
                k+=1

    return C

A = input().split(' ')
A = list(map(int, A))
B = input().split(' ')
B = list(map(int, B))
print(merge(A, B), end=' ')