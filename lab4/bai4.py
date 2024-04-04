#câu a
n=int(input("Nhập vào một số nguyên và số nguyên đó phải lớn hơn 10:"))
a = 1
s1 = 0
while a <= n:
    s1 += 6 ** a
    a += 1

print("Tổng s1 =", s1)
#câu b
n=int(input("Nhập vào một số nguyên và số nguyên đó phải lớn hơn 10:"))
a = 1
s2 = 0
while a <= n:
    s2 =s2+1/3**(2*a+1)
    a += 1

print("Tổng s2 =", s2)
#Câu c
n=int(input("Nhập vào một số nguyên và số nguyên đó phải lớn hơn 10:"))
a = 1
s3 = 0
while a <= n:
    s3 =s3+((-1)**a*a**2)
    a += 1

print("Tổng s3 =", s3)
#câu d
n=int(input("Nhập vào một số nguyên và số nguyên đó phải lớn hơn 10:"))
a = 1
s4 = 0
while a <= n:
    s4=s4+(a*(a+1)*(a+2))
    a += 1

print("Tổng s4 =", s4)