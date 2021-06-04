x = int(input())
a = 0

for i in range(x):
    y = int(input())
    a = a + y

print("總和：{}".format(a))
a = a / i
print("平均數：{}".format(a))