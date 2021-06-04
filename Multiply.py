import numpy

list_1 = []

for i in range(int(input())):
    list_1.append(i+1)

print(numpy.prod(list_1))