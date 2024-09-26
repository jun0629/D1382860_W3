number = input("請輸入一個三位數：")

num = int(number)

hundreds = num // 100
tens = (num % 100) // 10
ones = num % 10

sum = hundreds + tens + ones

print("每個位數的總和為：" + str(sum))