#câu b
for i in range(1, 1001):
    num = int(i ** 0.5)  
    if num * num == i:  
        print(i,end=",")    


#câu e
sum = 0
for i in range(1, 201):
    tong = i * (3 * i - 1) // 2
    sum += tong             
print(sum)



#câu a
for j in range(100, 1001):
    if j > 1:  # Kiểm tra số nguyên tố phải lớn hơn 1
        check = True
        for i in range(2, int(j ** 0.5) + 1):
            if j % i == 0:
                check = False
                break
        if check:
            print(j, end=", ")


# câu d
for j in range(2, 500):
    sum = 0
    for i in range(1, j):
        if j % i == 0:
            sum += i
    if sum == j:
        print(j, end=", ")  

