list_1 = [int(x) for x in input().split()]
a = 0

for i in range(list_1[0],list_1[1]+1):
  if(i%2 == 0):
    a = a+1

print(a)