n = input("Nhập một dãy số: ").split()
num = [float(num) for num in n]

if len(num) == 0:
        print("Dãy số rỗng!")
else:
        so_lon_nhat = num[0]
        so_be_nhat = num[0]
        for num in num:
            if num > so_lon_nhat:
                so_lon_nhat = num
            if num < so_be_nhat:
                so_be_nhat = num

        print("Số lớn nhất trong dãy số là:", so_lon_nhat)
        print("Số nhỏ nhất trong dãy số là:", so_be_nhat)