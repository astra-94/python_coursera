# N = int(input())
# numbers = list(map(int, input().split()))
# x = int(input())

# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 != 0:
#         numbers.pop(i)
#     else:
#         i += 1
# print(min(numbers, key=lambda a:abs(a-x)))


# a = [input() for i in range(int(input()))]

# numbers = [input() for i in range(list(map(int, input().split()))]

n = int(input())
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)

