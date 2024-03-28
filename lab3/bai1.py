#câu a
n=int(input("Nhập vào một số nguyên:"))
if n<0:
    print("Xin mời bạn nhập lại một só nguyên dương")
else:
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print(sum)    
# Câu b
n = int(input("Nhập số nguyên dương n: "))
if n<0:
    print("Xin mời bạn nhập lại số nguyên dương")    
else:    
    sum = 0
    for i in range(1, n + 1):
        sum=sum+ 1/i
    print(sum)    
# Câu c
import math
n = int(input("Nhập số nguyên dương n: "))
if n<0:
    print("Xin mời bạn nhập lại số nguyên dương")    
else: 
    sum=0
    for i in range(1,n+1):
        sum=sum+1/math.sqrt(2*i)    
    print(sum)
# câu d
n = int(input("Nhập số nguyên dương n: "))
if n<0:
    print("Xin mời bạn nhập lại số nguyên dương")    
else: 
    sum=0
    for i in range(1,n+1):
        sum=sum+(-1**i)/i
    print(sum)       
            

    

    