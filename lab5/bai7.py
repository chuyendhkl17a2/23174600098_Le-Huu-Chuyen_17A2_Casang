str = input("Nhập chuỗi: ")
chuoi_thuong = 0
chuoi_hoa = 0
chuoi_so = 0
chuoi_ki_tu = 0
for char in str:
    if char.islower():
        chuoi_thuong += 1 
    elif char.isupper():
        chuoi_hoa += 1
    elif char.isdigit():
        chuoi_so += 1
    else:
        chuoi_ki_tu += 1
print("Số lượng chữ thường:", chuoi_thuong)
print("Số lượng chữ hoa:", chuoi_hoa)
print("Số lượng chữ số:", chuoi_so)
print("Số lượng ký tự đặc biệt:", chuoi_ki_tu) 