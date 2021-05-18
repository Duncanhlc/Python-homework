hobbies = " "

for i in range(3):
    s = input("請輸入你的小愛好（最多三個，按Q或q結束）：")
    if s.upper() == "Q":
        break
    hobbies += s + " "

print("你的小愛好是："+hobbies)