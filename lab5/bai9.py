str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")
len_str1 = len(str1)
len_str2 = len(str2)
if len_str1 != len_str2:
    print("Không thể thay đổi chuỗi '{}' thành chuỗi '{}'.".format(str1, str2))
else:
    bien_thay_doi = 0
    for i in range(len_str1):
        if str1[i] != str2[i]:
            bien_thay_doi += 1
    if bien_thay_doi <= 2:
        print("Có thể thay đổi chuỗi '{}' thành chuỗi '{}'.".format(str1, str2))
    else:
        print("Không thể thay đổi chuỗi '{}' thành chuỗi '{}'.".format(str1, str2))