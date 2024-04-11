n = int(input("Nhập số nguyên dương (số thập phân): "))

if n <= 0:
    print("mơif nhập một số dương.")
else:
    m = ""
    while n > 0:
        m = str(n % 2) + m
        n //= 2
    
    print("Số nhị phân là:", m)


