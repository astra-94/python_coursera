numbers = list(map(int, input().split()))
k = int(input())
numbers.pop(k)
print(' '.join(map(str, numbers)))
