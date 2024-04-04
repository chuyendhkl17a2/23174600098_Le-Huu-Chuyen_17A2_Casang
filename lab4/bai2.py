#câu c
a  = 0
b=1
print("Các số Fibonacci nhỏ hơn 1000:")
while a < 1000:
    print(a)
    a, b = b, a + b
#câu b
num = 1
print("Các số chính phương nhỏ hơn 100:")
while num < 100:
    so = int(num ** 0.5)
    if so * so == num:
        print(num)
    num += 1
#câu a
num = 2
print("Các số nguyên tố nhỏ hơn 100:")
while num < 100:
    a = 2
    while a * a <= num:
        if num % a == 0:
            break
        a += 1
        print(num)
    num += 1
       
        
    

       
