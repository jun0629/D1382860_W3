number = input("請輸入三位數字：")

num = int(number)

hundreds = num // 100
tens = (num % 100) // 10
ones = num % 10

r = ones * 100 + tens * 10 + hundreds

print("結果：" + str(r))
