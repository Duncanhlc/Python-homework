list_1 = [int(x) for x in input().split()]
a = 0

for i in range(list_1[0],list_1[1]+1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        a = a+1

print(a)