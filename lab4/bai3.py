num = int(input("Nhập một số nguyên: "))

b = 0
while num != 0:
    b += 1
    num //= 10

print("Số chữ số của số nguyên:", b)