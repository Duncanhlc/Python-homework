a = 0

for i in range(5):
    list_1 = sorted([int(x) for x in input().split()])

    if list_1[0] + list_1[1] > list_1[2]:
        a = a +1

print(a)
