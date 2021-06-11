list_1 = [int(x) for x in input().split()]

s = (list_1[0] + list_1[1] + list_1[2]) / 2
area = int(s * (s - list_1[0]) * (s - list_1[1]) * (s - list_1[2]))

print(area)