# câu a
a = 0
so = []
while a <= 1000:
    n = int(input("Nhập số nguyên dương: "))
    if n > 0:
        a += n
        if n % 2 != 0:
           so.append(n)  
print("Các số lẻ đã nhập:",so)
#câu b
a = 0
so = []
while a <= 1000:
    n = int(input("Nhập số nguyên dương: "))
    if n > 0:
        a += n
        if n % 2 == 0:
           so.append(n)  
print("Các số chẵn đã nhập:",so)
#Câu c
a=0
b=0
while a <= 1000:
    n = int(input("Nhập số nguyên dương: "))
    if n > 0:
        a += n
        b +=1
           
print("SỐ lượng số nguyên đã nhập là:",b)