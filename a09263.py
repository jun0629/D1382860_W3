n = int(input("請輸入一個整數："))

result = (n % 2 == 0) * "是偶數" + (n % 2 != 0) * "是奇數"

print(f"{n} {result}")

