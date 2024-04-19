n = int(input("Nhập số phần tử của mảng: "))
arr = []
print("Nhập các phần tử của mảng:")
for i in range(n):
        arr.append(int(input()))
so_hoan_hao=[]
so_nguyen_to=[]
for num in arr:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                so_nguyen_to.append(num)

        # Kiểm tra số hoàn hảo
        tong_uoc = 0
        for i in range(1, num):
            if num % i == 0:
                tong_uoc += i
        if tong_uoc == num:
            so_hoan_hao.append(num)

print("Các số nguyên tố trong mảng là:", so_nguyen_to)
print("Các số hoàn hảo trong mảng là:", so_hoan_hao)
                
                
                


