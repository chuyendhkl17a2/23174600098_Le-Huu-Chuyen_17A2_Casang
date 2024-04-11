str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")
string = ""
dem_chuoi_nho = min(len(str1), len(str2))
for i in range(dem_chuoi_nho):
    string += str1[i] + '-' + str2[i]+'-'
if len(str1) > len(str2):
    string += '-' + str1[dem_chuoi_nho:]
elif len(str2) > dem_chuoi_nho:
    string += '-' + str2[dem_chuoi_nho:]
print("Chuỗi kết quả sau khi trộn:",string)
