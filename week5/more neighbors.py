def neighbors(A):
    i = 0
    k = 0
    for i in range(0, len(A) - 2):
        i += 1
        if (A[i]) > (A[i - 1]) and A[i] > A[i + 1]:
            k += 1
    if k > 0:
        return k
    else:
        return ''


A = input("Введите последовательность через пробел: ").split(' ')
print(neighbors(A), end=' ')
