list_1 = [int(x) for x in input().split()]
list_2 = []
a = 0

for i in range(len(list_1)):
    if list_1[i] <= 60:
        list_2.append(list_1[i])
        a = a + 1

print(list_2)
print(a)