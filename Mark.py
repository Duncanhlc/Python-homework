list_1 = []

for i in range(10):
    x = int(input())
    list_1.append(x)

list_1.pop(0)
list_1.pop()

y = sum(list_1)/len(list_1)
