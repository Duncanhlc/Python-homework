list_1 = []

for i in range(1000):
    if i%6 == 0:
        if i%8 == 0:
            list_1.append(i)

print(len(list_1))