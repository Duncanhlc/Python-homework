a = 0

for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
            if i + 2*j + 5*k == 100:
                   print("1分的枚數："+str(i), "2分的枚數："+str(j), "5分的枚數："+str(k))
                   a = a + 1

print("總次數："+str(a))

