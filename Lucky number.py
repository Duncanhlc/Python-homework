import random

name = input("請輸入你的名字：")

print("Hello！{}".format(name))

guard = ord(name[0])%100

print("你的幸運數字是"+str(random.choice(range(guard))))