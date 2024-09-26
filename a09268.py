number = input("請輸入一個五位數：")

num = int(number)

a = num // 10000
b = (num % 10000) // 1000
c = (num % 1000) // 100
d = (num % 100) // 10
e = num % 10

print(a)
print(b)
print(c)
print(d)
print(e)
