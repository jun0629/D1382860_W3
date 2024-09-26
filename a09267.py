a = int(input("輸入一個十進制數字："))

b = bin(a)[2:] 
o = oct(a)[2:]   
h = hex(a)[2:].upper() 

print("二進制：" + b)
print("八進制：" + o)
print("十六進制：" + h)
